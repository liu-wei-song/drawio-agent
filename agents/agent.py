from __future__ import annotations

import json
from typing import Literal, Union

from pydantic import Field, model_validator

from metagpt.actions import Action
from metagpt.logs import logger
from metagpt.roles import Role
from metagpt.schema import Message
from metagpt.utils.common import CodeParser

from prompts.agent_prompt import PREFIX_TEMPLATE, CONSTRAINT_TEMPLATE, STATE_TEMPLATE
from actions.refine_need import RefineNeed
from actions.generate_element import GenerateElements
from actions.exec_and_reflect import ExecAndReflect

import re
'''
            input: 
                requeriment
            
            llm + fromat

            output:
                edge and node

            edge + node -> 详细的edge + node + doc : use llm + format

            edge + node -> image : draw.io
            image + req -> ref : vllm 
            ref + req -> node + edge 

            node, edge = text 
            text -> xml
'''

def extract_state_value_from_output(content: str) -> str:
    """
    For openai models, they will always return state number. But for open llm models, the instruction result maybe a
    long text contain target number, so here add a extraction to improve success rate.

    Args:
        content (str): llm's output from `Role._think`
    """
    content = content.strip()  # deal the output cases like " 0", "0\n" and so on.
    pattern = (
        r"(?<!-)[0-9]"  # TODO find the number using a more proper method not just extract from content using pattern
    )
    matches = re.findall(pattern, content, re.DOTALL)
    matches = list(set(matches))
    state = matches[0] if len(matches) > 0 else "-1"
    return state


class Agent(Role):
    name: str = "ali"
    profile: str = "Agent"
    goal: str = """
    Your task is to create flowcharts using draw.io’s XML files based on user requirements. Here’s a refined version of the steps:

	1.	Break down the main requirement into sub-requirements.
	2.	Based on the sub-requirements, generate the flowchart nodes and edges.
	3.	Implement the generated elements to xml based on nodes and edges information and get reflect from .png.
	4.	Based on the reflection, edit the elements and re-implement them.
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.set_actions([RefineNeed,GenerateElements,ExecAndReflect])
        self._set_react_mode("react")
        self.rc.max_react_loop = len(self.actions) * 2
    def _actions_desc(self):
        actions_desc = []
        for action in self.actions:
            actions_desc.append(action.desc if hasattr(action, "desc") else action.__class__.__name__)

        return "\n".join(actions_desc)
    def _get_prefix(self):
        """Get the role prefix"""
        if self.desc:
            return self.desc

        prefix = PREFIX_TEMPLATE.format(**{"profile": self.profile, "name": self.name, "goal": self.goal})

        if self.constraints:
            prefix += CONSTRAINT_TEMPLATE.format(**{"constraints": self.constraints})

        if self.rc.env and self.rc.env.desc:
            all_roles = self.rc.env.role_names()
            other_role_names = ", ".join([r for r in all_roles if r != self.name])
            env_desc = f"You are in {self.rc.env.desc} with roles({other_role_names})."
            prefix += env_desc
        return prefix

    async def _think(self) -> bool:
        """Consider what to do and decide on the next course of action. Return false if nothing can be done."""
        if len(self.actions) == 1:
            # If there is only one action, then only this one can be performed
            self._set_state(0)

            return True

        if self.recovered and self.rc.state >= 0:
            self._set_state(self.rc.state)  # action to run from recovered state
            self.recovered = False  # avoid max_react_loop out of work
            return True

        prompt = self._get_prefix()
        prompt += STATE_TEMPLATE.format(
            history=self.rc.history,
            states="\n".join(self.states),
            n_states=len(self.states) - 1,
            previous_state=self.rc.state,
        )

        next_state = await self.llm.aask(prompt)
        next_state = extract_state_value_from_output(next_state)
        logger.debug(f"{prompt=}")

        if (not next_state.isdigit() and next_state != "-1") or int(next_state) not in range(-1, len(self.states)):
            logger.warning(f"Invalid answer of state, {next_state=}, will be set to -1")
            next_state = -1
        else:
            next_state = int(next_state)
            if next_state == -1:
                logger.info(f"End actions with {next_state=}")
        self._set_state(next_state)
        return True


    async def _act(self) -> Message:
        logger.info(f"{self._setting}: to do {self.rc.todo}({self.rc.todo.name})")
        
        msg = await self.rc.todo.run(self.rc.history)
        
        self.rc.memory.add(msg)
        
        return msg
    
    async def _react(self) -> Message:
        actions_taken = 0
        rsp = Message(content="No actions taken yet", cause_by=Action)  # will be overwritten after Role _act
        while actions_taken < self.rc.max_react_loop:
            # think
            await self._think()
            if self.rc.todo is None:
                break

            # act
            logger.debug(f"{self._setting}: {self.rc.state=}, will do {self.rc.todo}")
            rsp = await self._act()
            actions_taken += 1
        return rsp  # return output from the last action
    
        
async def main():
    a = Agent()
    rsp = await a.run()


if __name__ == "__main__":
    import asyncio
    import sys
    sys.path.append("..")
    asyncio.run(main())
