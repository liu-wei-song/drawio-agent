import json

from metagpt.actions import Action
from metagpt.schema import Message, Plan
from metagpt.utils.common import CodeParser

from prompts.generate_element import (
    GENERATE_NODES_PROMPT,
    GENERATE_EDGES_DOCUMENTS,
    GENERATE_EDGES_PROMPT,
    GENERATE_NODES_DOCUMENTS
)

class GenerateElements(Action):
    desc: str = "Creating flowchart nodes and edges based on user requirement decomposition"
    generate_nodes_desc: str = "Creating flowchart nodes based on user requirement decomposition, In the process of generating flowchart nodes, the properties of the generated current node should refer to the previous node, so that the flowchart is clean and beautiful"
    generate_edges_desc: str = "Creating flowchart edges based on user requirement decomposition and nodes"

    def preproccess_msg(self, msg: list[Message]) -> Message:
        
        requirement = msg[-1]
        history = msg[:-1]

        return requirement, history  

    async def run(self, msg: list[Message]) -> Message:

        requirement, history = self.preproccess_msg(msg)

        generate_nodes_prompt = GENERATE_NODES_PROMPT.format(
            action_desc = self.generate_nodes_desc,
            requirement = requirement.content,
            history = "\n".join([f"{m.role}: {m.content}" for m in history]),
            document = GENERATE_NODES_DOCUMENTS
        )

        node_rsp = await self.llm.aask(generate_nodes_prompt)

        generate_edges_prompt = GENERATE_EDGES_PROMPT.format(
            action_desc = self.generate_edges_desc,
            requirement = node_rsp,
            history = "\n".join([f"{m.role}: {m.content}" for m in history]),
            document = GENERATE_EDGES_DOCUMENTS
        )

        edge_rsp = await self.llm.aask(generate_edges_prompt)

        rsp_msg = Message(
            role = "assistant",
            content = node_rsp + "\n" + edge_rsp,
            cause_by = GenerateElements
        )

        return rsp_msg