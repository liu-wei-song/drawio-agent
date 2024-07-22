import json

from metagpt.actions import Action
from metagpt.schema import Message, Plan
from metagpt.utils.common import CodeParser

from prompts.refine_need import (REFINE_NEED_PROMPT, REFINE_NEED_DOCUMENTS)
# import prompts.agent_prompt 

OUTPUT_TEMPLATE = """
"""

class RefineNeed(Action):
    desc: str = "breaking down user requirements into sub-requirements that align with flowchart nodes"

    def preproccess_msg(self, msg: list[Message]) -> Message:
        
        requirement = msg[0]
        history = msg[1:]


        return requirement, history  


    async def run(self, msg: list[Message]) -> Message: 

        requirement, history = self.preproccess_msg(msg)
        
        refine_need_prompt = REFINE_NEED_PROMPT.format(
            action_desc = self.desc,
            requirement = requirement.content,
            history = "\n".join([f"{m.role}: {m.content}" for m in history]),
            document = REFINE_NEED_DOCUMENTS
        )
        rsp = await self.llm.aask(refine_need_prompt)

        rsp_msg = Message(role="assistant", content=rsp, cause_by = RefineNeed)

        return rsp_msg 
