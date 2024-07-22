
GENERATE_XML_PROMPT = """
## Action Description
{action_desc}

## History
{history}

## Requirement 
{requirement}

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
...
]
```
```json
[
    {{
        "id": "9",
        "value": "",
        "source": "0",
        "target": "1",
        "style": "edgeStyle=orthogonalEdgeStyle;endArrow=block;strokeColor=#000000;",
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
        "style": "edgeStyle=elbowEdgeStyle;endArrow=open;strokeColor=#ff0000;'",
        "mxPoints": [
            {{
                "x": "400",
                "y": "200'",
                "as": "waypoint"
            }}
            ...
        ]
    }},
    ...
]
```
example output: 
```xml
<mxfile host="Electron" modified="2024-07-19T23:59:43.420Z" agent="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) draw.io/24.6.4 Chrome/124.0.6367.207 Electron/30.0.6 Safari/537.36" version="24.6.4" etag="btvJdfSu-Ib8PiGPSB4P" type="device">
  <diagram id="8sEYoDRRnTibXLsbt6C7" name="第 1 页">
    <mxGraphModel dx="1114" dy="800" grid="1" gridSize="10" guides="1" tooltips="1" connect="1" arrows="1" fold="1" page="1" pageScale="1" pageWidth="827" pageHeight="1169" math="0" shadow="0">
      <root>
        <mxCell id="0" />
        <mxCell id="1" parent="0" />
        <mxCell id="2" value="Start process" style="ellipse;fontSize=16;fontStyle=bold;strokeWidth=2;" parent="1" vertex="1">
          <mxGeometry x="100" y="50" width="80" height="40" as="geometry" />
        </mxCell>
        <mxCell id="3" value="Check if human" style="rhombus;fontSize=14;fontStyle=italic;strokeWidth=2;dashed=1;" parent="1" vertex="1">
          <mxGeometry x="300" y="200" width="100" height="60" as="geometry" />
        </mxCell>
        <mxCell id="J_xaAk_2bt4Iq0r9EQf_-10" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;entryX=1;entryY=0.5;entryDx=0;entryDy=0;" edge="1" parent="1" source="4" target="5">
          <mxGeometry relative="1" as="geometry">
            <Array as="points">
              <mxPoint x="590" y="520" />
            </Array>
          </mxGeometry>
        </mxCell>
        <mxCell id="4" value="Initialize HumanProvider" style="rectangle;fontSize=14;rounded=1;strokeWidth=2;" parent="1" vertex="1">
          <mxGeometry x="530" y="340" width="120" height="50" as="geometry" />
        </mxCell>
        <mxCell id="5" value="End decision" style="ellipse;fontSize=14;fontStyle=bold;strokeWidth=3;" parent="1" vertex="1">
          <mxGeometry x="300" y="500" width="80" height="40" as="geometry" />
        </mxCell>
        <mxCell id="6" value="Check actions" style="rectangle;fontSize=14;strokeWidth=2;" parent="1" vertex="1">
          <mxGeometry x="280" y="660" width="120" height="50" as="geometry" />
        </mxCell>
        <mxCell id="7" value="" style="edgeStyle=orthogonalEdgeStyle;endArrow=block;strokeColor=#000000;" parent="1" source="2" target="3" edge="1">
          <mxGeometry relative="1" as="geometry">
            <Array as="points">
              <mxPoint x="180" y="100" as="waypoint" />
            </Array>
          </mxGeometry>
        </mxCell>
        <mxCell id="8" value="yes" style="edgeStyle=elbowEdgeStyle;endArrow=open;strokeColor=#000000;" parent="1" source="3" target="4" edge="1">
          <mxGeometry relative="1" as="geometry">
            <Array as="points">
              <mxPoint x="400" y="275" as="waypoint" />
            </Array>
          </mxGeometry>
        </mxCell>
        <mxCell id="9" value="no" style="edgeStyle=elbowEdgeStyle;endArrow=open;strokeColor=#000000;" parent="1" source="3" target="5" edge="1">
          <mxGeometry relative="1" as="geometry">
            <Array as="points">
              <mxPoint x="400" y="375" as="waypoint" />
            </Array>
          </mxGeometry>
        </mxCell>
        <mxCell id="10" value="" style="edgeStyle=orthogonalEdgeStyle;endArrow=block;strokeColor=#000000;" parent="1" source="5" target="6" edge="1">
          <mxGeometry relative="1" as="geometry">
            <Array as="points">
              <mxPoint x="300" y="575" as="waypoint" />
            </Array>
          </mxGeometry>
        </mxCell>
      </root>
    </mxGraphModel>
  </diagram>
</mxfile>
```


## Output Requirement
Output a json following the format:
```xml
your code
```

## Documents
{document}

## Action Role
You are an action executor, completing actions based on action description, history, documents, and examples. Organize output in accordance with output format.

## start to complete the action
"""


GENERATE_XML_DOCUMENTS = """
### The following is a drawio xml file examlpe
<mxfile host="Electron" modified="2024-07-10T06:26:40.097Z" agent="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) draw.io/24.6.4 Chrome/124.0.6367.207 Electron/30.0.6 Safari/537.36" etag="2n953u5diPrpASoHhpBY" version="24.6.4" type="device">
  <diagram id="C5RBs43oDa-KdzZeNtuy" name="Page-1">
    <mxGraphModel dx="1114" dy="800" grid="1" gridSize="10" guides="1" tooltips="1" connect="1" arrows="1" fold="1" page="1" pageScale="1" pageWidth="827" pageHeight="1169" math="0" shadow="0">
      <root>
        <mxCell id="WIyWlLk6GJQsqaUBKTNV-0" />
        <mxCell id="WIyWlLk6GJQsqaUBKTNV-1" parent="WIyWlLk6GJQsqaUBKTNV-0" />
        <mxCell id="WIyWlLk6GJQsqaUBKTNV-2" value="" style="rounded=0;html=1;jettySize=auto;orthogonalLoop=1;fontSize=11;endArrow=block;endFill=0;endSize=8;strokeWidth=1;shadow=0;labelBackgroundColor=none;edgeStyle=orthogonalEdgeStyle;entryX=0.5;entryY=0;entryDx=0;entryDy=0;" parent="WIyWlLk6GJQsqaUBKTNV-1" source="WIyWlLk6GJQsqaUBKTNV-3" target="WIyWlLk6GJQsqaUBKTNV-11" edge="1">


          <mxGeometry relative="1" as="geometry">
            <mxPoint x="220" y="170" as="targetPoint" />
          </mxGeometry>
        </mxCell>
        <mxCell id="WIyWlLk6GJQsqaUBKTNV-3" value="Lamp doesn&#39;t work" style="rounded=1;whiteSpace=wrap;html=1;fontSize=12;glass=0;strokeWidth=1;shadow=0;" parent="WIyWlLk6GJQsqaUBKTNV-1" vertex="1">
          <mxGeometry x="160" y="80" width="120" height="40" as="geometry" />
        </mxCell>
        <mxCell id="WIyWlLk6GJQsqaUBKTNV-11" value="Repair Lamp" style="rounded=1;whiteSpace=wrap;html=1;fontSize=12;glass=0;strokeWidth=1;shadow=0;" parent="WIyWlLk6GJQsqaUBKTNV-1" vertex="1">
          <mxGeometry x="200" y="220" width="120" height="40" as="geometry" />
        </mxCell>
      </root>
    </mxGraphModel>
  </diagram>
</mxfile>

### Additional attention needs to be paid
1. The color should be uniform, and the distance between nodes should be large
"""


CHECK_FLOWCHART_PROMPT = """
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
        "value": "Transition from start to decision",
        "source": "0",
        "target": "1",
        "style": "edgeStyle=orthogonalEdgeStyle;endArrow=block;strokeColor=#000000;",
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
        "value": "Decision to Initialize Provider",
        "source": "1",
        "target": "2",
        "style": "edgeStyle=elbowEdgeStyle;endArrow=open;strokeColor=#ff0000;'",
        "mxPoints": [
            {{
                "x": "400",
                "y": "200'",
                "as": "waypoint"
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
  "id": "str = 'unique identifier for an edge or node in diagram, can be an ordinal, Do not repeat with nodes'",
  "value": "str = 'The text content of the edge, describe the edge'",
  "source": "str = 'Identifier of the source node from which the edge originates'",
  "target": "str = 'Identifier of the target node to which the edge points'",
  "style": "str = 'Defines the appearance of the edge including line type, color, and arrow style'",
  "mxPoints": [
    {{
      "x": "str = 'The x-coordinate for the point, used in defining path waypoints or absolute start/end positions'",
      "y": "str = 'The y-coordinate for the point, used in defining path waypoints or absolute start/end positions'",
      "as": "str = 'Defines the role of the point in the geometry of the edge, such as a source point, target point, or waypoint'"
    }},
    {{
      "x": "str = 'Another x-coordinate for an additional point along the edge'",
      "y": "str = 'Another y-coordinate for an additional point along the edge'",
      "as": "str = 'Additional role of another point, if needed for complex paths'"
    }}
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


CHECK_FLOWCHART_DOCUMENTS = """
### The following is the introduction of the filling content for your reference
{{
  "id": {{
    "description": "Unique identifier for an edge in the diagram, ensuring that it doesn't conflict with identifiers used for nodes.",
    "commonValues": str = "id of edge eg '1', '10'..."
  }},
  "value": {{
    "description": "Text content or label that describes the relationship or flow represented by the edge, providing contextual information directly on the diagram.",
    "commonValues": str = "description of edge eg 'yes','no','transfer'..."
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
"""
