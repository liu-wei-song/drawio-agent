
GENERATE_NODES_PROMPT = """
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
example output: 
```json
[
{{
  "id": "0",
  "dependency": ["-1"],
  "value": "Start process",
  "vertex": "1",
  "x": "100",
  "y": "50",
  "shape": "ellipse",
  "fillColor": "#32CD32",  // Lime Green for visibility
  "rounded": "true",
  "fontColor": "#FFFFFF",
  "fontSize": "16",
  "fontStyle": "bold",
  "strokeColor": "#000000",
  "strokeWidth": "2",
  "dashed": "false"
}},
{{
  "id": "1",
  "dependency": ["0"],
  "value": "Check if human",
  "vertex": "1",
  "x": "300",
  "y": "150",
  "shape": "rhombus",
  "fillColor": "#FFD700",  // Gold for decision points
  "rounded": "false",
  "fontColor": "#000000",
  "fontSize": "14",
  "fontStyle": "italic",
  "strokeColor": "#000000",
  "strokeWidth": "2",
  "dashed": "true"
}},
{{
  "id": "2",
  "dependency": ["1"],
  "value": "Initialize HumanProvider",
  "vertex": "1",
  "x": "500",
  "y": "250",
  "shape": "rectangle",
  "fillColor": "#FFA07A",  // Light Salmon for steps
  "rounded": "true",
  "fontColor": "#FFFFFF",
  "fontSize": "14",
  "fontStyle": "normal",
  "strokeColor": "#000000",
  "strokeWidth": "2",
  "dashed": "false"
}},
{{
  "id": "3",
  "dependency": ["1", "2"],
  "value": "end decision",
  "vertex": "1",
  "x": "300",
  "y": "350",
  "shape": "ellipse",
  "fillColor": "#6A5ACD",  // Slate Blue for end decisions
  "rounded": "true",
  "fontColor": "#FFFFFF",
  "fontSize": "14",
  "fontStyle": "bold",
  "strokeColor": "#000000",
  "strokeWidth": "3",
  "dashed": "false"
}},
{{
  "id": "4",
  "dependency": ["3"],
  "value": "Check actions",
  "vertex": "1",
  "x": "300",
  "y": "450",
  "shape": "rectangle",
  "fillColor": "#20B2AA",  // Light Sea Green for action checks
  "rounded": "false",
  "fontColor": "#000000",
  "fontSize": "14",
  "fontStyle": "normal",
  "strokeColor": "#000000",
  "strokeWidth": "2",
  "dashed": "true"
}},
{{
  "id": "5",
  "dependency": ["4"],
  "value": "Set system prompt",
  "vertex": "1",
  "x": "300",
  "y": "550",
  "shape": "rectangle",
  "fillColor": "#FF6347",  // Tomato for system settings
  "rounded": "false",
  "fontColor": "#FFFFFF",
  "fontSize": "14",
  "fontStyle": "italic",
  "strokeColor": "#000000",
  "strokeWidth": "2",
  "dashed": "false"
}},
{{
  "id": "6",
  "dependency": ["5"],
  "value": "Set cost manager",
  "vertex": "1",
  "x": "300",
  "y": "650",
  "shape": "rectangle",
  "fillColor": "#4682B4",  // Steel Blue for management settings
  "rounded": "true",
  "fontColor": "#FFFFFF",
  "fontSize": "16",
  "fontStyle": "bold",
  "strokeColor": "#000000",
  "strokeWidth": "3",
  "dashed": "false"
}},
{{
  "id": "7",
  "dependency": ["6"],
  "value": "Watch UserRequirement",
  "vertex": "1",
  "x": "300",
  "y": "750",
  "shape": "rectangle",
  "fillColor": "#008080",  // Teal for monitoring activities
  "rounded": "true",
  "fontColor": "#FFFFFF",
  "fontSize": "14",
  "fontStyle": "normal",
  "strokeColor": "#FFFFFF",
  "strokeWidth": "2",
  "dashed": "true"
}},
{{
  "id": "8",
  "dependency": ["7"],
  "value": "End process",
  "vertex": "1",
  "x": "300",
  "y": "850",
  "shape": "ellipse",
  "fillColor": "#B22222",  // Firebrick for end process
  "rounded": "true",
  "fontColor": "#FFFFFF",
  "fontSize": "16",
  "fontStyle": "bold",
  "strokeColor": "#FFFFFF",
  "strokeWidth": "2",
  "dashed": "false"
}}
]
```

## Output Requirement
Output a json following the format:
```json
[
    {{
            "id":  str = "unique identifier for a node in diagram, can be an ordinal",
            "dependency": str = "The node's dependency, which is a list of node ids",
            "value": str = "The text content of the node",
            "vertex": str = "1(Identifies this as a node)",
            "x": str = "The node's x position coordinates on the canvas.",
            "y": str = "The node's y position coordinates on the canvas.",
            "shape" : str = "The basic shape of the node.",
            "fillColor": str = "Background color of the node.",
            "rounded" : str = "Whether the corners are rounded.",
            "fontColor": str = "The color of the text inside the node.",
            "fontSize": str = "The size of the font of the text inside the node, typically in points.",
            "fontStyle": str = "The style of the font (e.g., normal, bold, italic).",
            "strokeColor": str = "The color of the border line of the node.",
            "strokeWidth": str = "The thickness of the border line of the node, measured in pixels.",
            "dashed": str = "Indicates if the border line of the node is dashed (True) or solid (False).",
    }},
    ...
]
```

## Action Role
You are an action executor, completing actions based on action description, history, documents, and examples. Organize output in strict accordance with output requirements.

## start to complete the action
"""


GENERATE_NODES_DOCUMENTS = """
### The following is the introduction of the filling content for your reference
{{
  "id": {{
    "description": "Unique identifier for each node within a diagram, essential for linking and referencing.",
    "commonValues": ["1", "2", "node1", "step1"]
  }},
  "dependency": {{
    "description": "Lists the identifiers of nodes that this node depends on, defining the flow or sequence in the diagram.",
    "commonValues": [["1", "2"], ["start", "mid"]]
  }},
  "value": {{
    "description": "Holds the text content displayed inside the node, typically describing the function or name of the node.",
    "commonValues": ["Start Process", "Approve Document", "Check Inventory"]
  }},
  "vertex": {{
    "description": "Identifies the element as a node, differentiating it from edges or other diagram elements.",
    "commonValues": ["1"]
  }},
  "x": {{
    "description": "Specifies the node's horizontal position on the canvas, essential for layout.",
    "commonValues": ["100", "200", "300"]
  }},
  "y": {{
    "description": "Specifies the node's vertical position on the canvas, essential for layout.",
    "commonValues": ["100", "200", "300"]
  }},
  "shape": {{
    "description": "Defines the node's geometric shape, which can visually differentiate node types.",
    "commonValues": ["rectangle", "ellipse", "rhombus"]
  }},
  "fillColor": {{
    "description": "Sets the background color of the node, used for thematic grouping or visual differentiation.",
    "commonValues": ["#FFFFFF", "#FF5733", "#0000FF"]
  }},
  "rounded": {{
    "description": "Determines if the node has rounded corners, adding a stylistic touch.",
    "commonValues": ["true", "false"]
  }},
  "fontColor": {{
    "description": "Specifies the color of the text inside the node, affecting readability and style.",
    "commonValues": ["#000000", "#FFFFFF"]
  }},
  "fontSize": {{
    "description": "Sets the text size within the node, impacting visibility and emphasis.",
    "commonValues": ["12", "14", "16"]
  }},
  "fontStyle": {{
    "description": "Defines the style of the font used within the node, useful for emphasizing different parts of the information.",
    "commonValues": ["normal", "bold", "italic"]
  }},
  "strokeColor": {{
    "description": "Determines the color of the node's border, which can highlight or differentiate nodes.",
    "commonValues": ["#000000", "#FF0000"]
  }},
  "strokeWidth": {{
    "description": "Specifies the thickness of the node's border, enhancing visual impact.",
    "commonValues": ["1", "2", "3"]
  }},
  "dashed": {{
    "description": "Indicates if the border of the node is dashed, which can suggest a provisional or special status.",
    "commonValues": ["true", "false"]
  }}
}}

### Examples of some nodes
开始/结束节点：
    形状：通常是圆形或椭圆形，表示流程的开始和结束。
<mxCell value="开始" style="shape=ellipse;fillColor=#0000FF;strokeColor=#000000;fontColor=#FFFFFF" vertex="1" parent="1">
  <mxGeometry x="100" y="100" width="60" height="60" as="geometry"/>
</mxCell>
过程节点：
形状：矩形，用于表示一个步骤或操作。
示例：
<mxCell value="过程" style="shape=rectangle;fillColor=#FFFFFF;strokeColor=#000000" vertex="1" parent="1">
  <mxGeometry x="200" y="200" width="80" height="40" as="geometry"/>
</mxCell>
决策节点：
	•	形状：菱形，用于表示决策点。
	•	示例：
    <mxCell value="决策" style="shape=rhombus;fillColor=#FFFF00;strokeColor=#000000" vertex="1" parent="1">
  <mxGeometry x="300" y="300" width="80" height="80" as="geometry"/>
</mxCell>
数据/输入输出节点：
	•	形状：平行四边形，表示数据的输入或输出。
	•	示例：
<mxCell value="输入/输出" style="shape=parallelogram;fillColor=#00FF00;strokeColor=#000000" vertex="1" parent="1">
  <mxGeometry x="400" y="400" width="100" height="60" as="geometry"/>
</mxCell>

### Additional attention needs to be paid
1. The generated nodes can not be completely compared with the requirements, and can be further divided according to the flow chart
2. The generated nodes should be laid out as neatly, neatly, and clearly as possible

"""


GENERATE_EDGES_PROMPT = """
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
```json
[
{{
  "id": "0",
  "dependency": ["-1"],
  "value": "Start process",
  "vertex": "1",
  "x": "100",
  "y": "50",
  "shape": "ellipse",
  "fillColor": "#32CD32",  // Lime Green for visibility
  "rounded": "true",
  "fontColor": "#FFFFFF",
  "fontSize": "16",
  "fontStyle": "bold",
  "strokeColor": "#000000",
  "strokeWidth": "2",
  "dashed": "false"
}},
{{
  "id": "1",
  "dependency": ["0"],
  "value": "Check if human",
  "vertex": "1",
  "x": "300",
  "y": "150",
  "shape": "rhombus",
  "fillColor": "#FFD700",  // Gold for decision points
  "rounded": "false",
  "fontColor": "#000000",
  "fontSize": "14",
  "fontStyle": "italic",
  "strokeColor": "#000000",
  "strokeWidth": "2",
  "dashed": "true"
}},
{{
  "id": "2",
  "dependency": ["1"],
  "value": "Initialize HumanProvider",
  "vertex": "1",
  "x": "500",
  "y": "250",
  "shape": "rectangle",
  "fillColor": "#FFA07A",  // Light Salmon for steps
  "rounded": "true",
  "fontColor": "#FFFFFF",
  "fontSize": "14",
  "fontStyle": "normal",
  "strokeColor": "#000000",
  "strokeWidth": "2",
  "dashed": "false"
}},
{{
  "id": "3",
  "dependency": ["1", "2"],
  "value": "end decision",
  "vertex": "1",
  "x": "300",
  "y": "350",
  "shape": "ellipse",
  "fillColor": "#6A5ACD",  // Slate Blue for end decisions
  "rounded": "true",
  "fontColor": "#FFFFFF",
  "fontSize": "14",
  "fontStyle": "bold",
  "strokeColor": "#000000",
  "strokeWidth": "3",
  "dashed": "false"
}},
{{
  "id": "4",
  "dependency": ["3"],
  "value": "Check actions",
  "vertex": "1",
  "x": "300",
  "y": "450",
  "shape": "rectangle",
  "fillColor": "#20B2AA",  // Light Sea Green for action checks
  "rounded": "false",
  "fontColor": "#000000",
  "fontSize": "14",
  "fontStyle": "normal",
  "strokeColor": "#000000",
  "strokeWidth": "2",
  "dashed": "true"
}},
{{
  "id": "5",
  "dependency": ["4"],
  "value": "Set system prompt",
  "vertex": "1",
  "x": "300",
  "y": "550",
  "shape": "rectangle",
  "fillColor": "#FF6347",  // Tomato for system settings
  "rounded": "false",
  "fontColor": "#FFFFFF",
  "fontSize": "14",
  "fontStyle": "italic",
  "strokeColor": "#000000",
  "strokeWidth": "2",
  "dashed": "false"
}},
{{
  "id": "6",
  "dependency": ["5"],
  "value": "Set cost manager",
  "vertex": "1",
  "x": "300",
  "y": "650",
  "shape": "rectangle",
  "fillColor": "#4682B4",  // Steel Blue for management settings
  "rounded": "true",
  "fontColor": "#FFFFFF",
  "fontSize": "16",
  "fontStyle": "bold",
  "strokeColor": "#000000",
  "strokeWidth": "3",
  "dashed": "false"
}},
{{
  "id": "7",
  "dependency": ["6"],
  "value": "Watch UserRequirement",
  "vertex": "1",
  "x": "300",
  "y": "750",
  "shape": "rectangle",
  "fillColor": "#008080",  // Teal for monitoring activities
  "rounded": "true",
  "fontColor": "#FFFFFF",
  "fontSize": "14",
  "fontStyle": "normal",
  "strokeColor": "#FFFFFF",
  "strokeWidth": "2",
  "dashed": "true"
}},
{{
  "id": "8",
  "dependency": ["7"],
  "value": "End process",
  "vertex": "1",
  "x": "300",
  "y": "850",
  "shape": "ellipse",
  "fillColor": "#B22222",  // Firebrick for end process
  "rounded": "true",
  "fontColor": "#FFFFFF",
  "fontSize": "16",
  "fontStyle": "bold",
  "strokeColor": "#FFFFFF",
  "strokeWidth": "2",
  "dashed": "false"
}}
]
```
example output:
```json
[
    {{
        "id": "9",
        "value": "",
        "source": "0",
        "target": "1",
        "style": "edgeStyle=orthogonalEdgeStyle;endArrow=block;strokeColor=#000000;'",
        "mxPoints": [
            {{
                "x": "200",
                "y": "100",
                "as": "waypoint"
            }}
            ...
        ]
    }},
    {{
        "id": "10",
        "value": "yes",
        "source": "1",
        "target": "2",
        "style": "edgeStyle=elbowEdgeStyle;endArrow=open;strokeColor=#ff0000;",
        "mxPoints": [
            {{
                "x": "400",
                "y": "200",
                "as": "waypoint'"
            }}
            ...
        ]
    }},
    ...
]
```

## Output Requirement
Output a json following the format:
```json
[
        {{
  "id": str = "unique identifier for an edge or node in diagram, can be an ordinal, Do not repeat with nodes",
  "value": str = "The text content of the edge, yes or no or noting",
  "source": str = "Identifier of the source node from which the edge originates'",
  "target": str = "Identifier of the target node to which the edge points'",
  "style": str = "Defines the appearance of the edge including line type, color, and arrow style'",
  "mxPoints": [
    {{
      "x": str = "The x-coordinate for the point, used in defining path waypoints or absolute start/end positions'",
      "y": str = "The y-coordinate for the point, used in defining path waypoints or absolute start/end positions'",
      "as": str = "Defines the role of the point in the geometry of the edge, such as a source point, target point, or waypoint'"
    }},
    ...
    // Add more points as necessary
  ]
}}
...
]
```

## Action Role
You are an action executor, completing actions based on action description, history, documents, and examples. Organize output in strict accordance with output requirements.

## start to complete the action
"""


GENERATE_EDGES_DOCUMENTS = """
### The following is the introduction of the filling content for your reference
{{
  "id": {{
    "description": "Unique identifier for an edge in the diagram, ensuring that it doesn't conflict with identifiers used for nodes.",
    "commonValues": str = "id of edge eg '1', '10'..."
  }},
  "value": {{
    "description": "Text content or label that describes the relationship or flow represented by the edge, providing contextual information directly on the diagram.",
    "commonValues": str = "description of edge eg 'yes','no',''"
  }},
  "source": {{
    "description": "Identifier of the node from which the edge originates, linking the start of the edge to a specific node.",
    "commonValues": str = "source node id"
  }},
  "target": {{
    "description": "Identifier of the node to which the edge points, linking the end of the edge to a specific node.",
    "commonValues": str = "target node id"
  }},
  "style": {{
    "description": "Visual appearance settings for the edge, including line type, color, and arrow configurations, to enhance diagram readability and aesthetics.",
    "commonValues": str = "eg 'edgeStyle=orthogonalEdgeStyle;endArrow=block;strokeColor=#000000;','edgeStyle=elbowEdgeStyle;endArrow=open;strokeColor=#ff0000;edgeStyle=straight;','endArrow=classic;strokeColor=#00ff00;'"
  }},
  "mxPoints": [
    {{
      "description": "A list of points defining complex paths or specific start and end points for an edge. Each point can control a segment of the edge's path.",
      "commonValues": list = [
        {{
          "x": "100",
          "y": "100",
          "as": "sourcePoint"
        }},
        {{
          "x": "200",
          "y": "200",
          "as": "waypoint"
        }},
        {{
          "x": "300",
          "y": "300",
          "as": "targetPoint"
        }}
      ]
    }}
  ]
}}

### other notes
1. Create edges with predefined nodes to complete the flowchart
2. Focus on mxpoint so that the edges do not coincide
3. you need give all the mxPoints and edges 
4. generate edge valuse eg "yes" or "no" when source has branch edge
5. check if every dependency has edge
"""
