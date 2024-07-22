import json

from metagpt.actions import Action
from metagpt.schema import Message, Plan
from metagpt.utils.common import CodeParser

from prompts.exec_and_reflect import (
    GENERATE_XML_PROMPT,
    GENERATE_XML_DOCUMENTS    
)

class ExecAndReflect(Action):
    desc: str = "At this stage, you generate the contents of an xml file that describes the flowchart based on node and edge information. Then get the flow chart through drawio, then check the flow chart as required and finally get feedback."
    generate_xml_desc: str = "Generate the contents of an xml file that describes the flowchart based on node and edge information."

    def preproccess_msg(self, msg: list[Message]) -> Message:
        
        requirement = msg[-1]
        history = msg[:-1]

        return requirement, history  

    def parse_xml(self, xml_code: str):

        return  CodeParser.parse_code(text=xml_code,lang="xml")

    async def run(self, msg: list[Message]) -> Message:

        requirement, history = self.preproccess_msg(msg)

        ## get xml and check xml code 
        generate_xml_prompt = GENERATE_XML_PROMPT.format(
            action_desc = self.generate_xml_desc,
            requirement = requirement.content,
            history = "\n".join([f"{m.role}: {m.content}" for m in history]),
            document = GENERATE_XML_DOCUMENTS
        )

        xml_rsp = await self.llm.aask(generate_xml_prompt)

        xml_code = self.parse_xml(xml_rsp)

        ## get .png image
        

        ## check

        rsp_msg = xml_code

        
        return rsp_msg