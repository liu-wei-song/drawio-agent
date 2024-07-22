
REFINE_NEED_PROMPT = """
## Action Description
{action_desc}

## History
{history}

## Requirement 
{requirement}

## Documents
{document}

## Examples
### example 1
example requirement:
        if self.tools:
            context = (
                self.working_memory.get()[-1].content if self.working_memory.get() else ""
            )  # thoughts from _think stage in 'react' mode
            plan = self.planner.plan if self.use_plan else None
            tool_info = await self.tool_recommender.get_recommended_tool_info(context=context, plan=plan)
        else:
            tool_info = ""

        # data info
        await self._check_data()

        while not success and counter < max_retry:
            ### write code ###
            code, cause_by = await self._write_code(counter, plan_status, tool_info)

            self.working_memory.add(Message(content=code, role="assistant", cause_by=cause_by))
            
            ### execute code ###
            result, success = await self.execute_code.run(code)
            print(result)

            self.working_memory.add(Message(content=result, role="user", cause_by=ExecuteNbCode))

            ### process execution result ###
            counter += 1

            if not success and counter >= max_retry:
                logger.info("coding failed!")
                review, _ = await self.planner.ask_review(auto_run=False, trigger=ReviewConst.CODE_REVIEW_TRIGGER)
                if ReviewConst.CHANGE_WORDS[0] in review:
                    counter = 0  # redo the task again with help of human suggestions
example output:
```json
[
    {{ "id": "0", "value": "Start process", "type": "step", "dependency": ["-1"] }},
    {{ "id": "1", "value": "Check tools", "type": "decision", "dependency": ["0"] }},
    {{ "id": "2", "value": "Get the last content from working memory", "type": "step", "dependency": ["1"] }},
    {{ "id": "3", "value": "Get the plan", "type": "step", "dependency": ["2"] }},
    {{ "id": "4", "value": "Get recommended tool info", "type": "step", "dependency": ["3"] }},
    {{ "id": "5", "value": "Tool info is empty", "type": "step", "dependency": ["1"] }},
    {{ "id": "6", "value": "End tool info check", "type": "end decision", "dependency": ["4", "5"] }},
    {{ "id": "7", "value": "Check data", "type": "step", "dependency": ["6"] }},
    ...
]
```
### example 2
if self.is_human:
            self.llm = HumanProvider(None)

        self._check_actions()
        self.llm.system_prompt = self._get_prefix()
        self.llm.cost_manager = self.context.cost_manager
        self._watch(kwargs.pop("watch", [UserRequirement]))
```json
[
    {{ "id": "0", "value": "Start process", "type": "step", "dependency": ["-1"] }},
    {{ "id": "1", "value": "Check if human", "type": "decision", "dependency": ["0"] }},
    {{ "id": "2", "value": "Initialize HumanProvider", "type": "step", "dependency": ["1"] }},
    {{ "id": "3", "value": "end decision", "type": "end decision", "dependency": ["1","2"] }},
    {{ "id": "4", "value": "Check actions", "type": "step", "dependency": ["3"] }},
    {{ "id": "5", "value": "Set system prompt", "type": "step", "dependency": ["4"] }},
    {{ "id": "6", "value": "Set cost manager", "type": "step", "dependency": ["5"] }},
    {{ "id": "7", "value": "Watch UserRequirement", "type": "step", "dependency": ["6"] }},
    {{ "id": "8", "value": "End process", "type": "step", "dependency": ["7"] }}
] 
```

## Output Requirement
Output a json following the format:
```json
[
    {{ "id": "{{unique ID}}", "value": "{{node name}}", "type": "{{node type}}", "dependency": [{{dependency IDs}}] }},
    ...
]
```
"id": "{{unique ID}}": A unique identifier for each node, starting from 0.
"value": "{{node name}}": The name of the node derived from the decomposition.
"type": "{{node type}}": The type of the node, which can be “step”, "decision", "end decision". "end decision" means the end of "decision". after "decision" process end  you should add "start"
"dependency": [{{dependency IDs}}]: The IDs of the nodes this node depends on. If there are multiple dependencies, separate them with commas.
not others output.  

## Action Role
You are an action executor, completing actions based on action description, history, documents, and examples.

"""

REFINE_NEED_DOCUMENTS = """
1. you could add new node when decision end, this node could dependency two nodes which let flowchart fluency.
"""