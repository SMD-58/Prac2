from plantuml import PlantUML

DEFAULT_SERVER = "https://www.plantuml.com/plantuml/svg/"

def to_plantuml(graph, title):
    lines = ["@startuml"]
    lines.append(f"title {title}")
    lines += ["left to right direction", "skinparam componentStyle rectangle"]
    for src, dsts in graph.items():
        dsts = list(dsts)
        if not dsts:
            lines.append(f'[{src}]')
        else:
            for dst in sorted(dsts):
                lines.append(f'[{src}] --> [{dst}]')
    lines.append("@enduml")
    return "\n".join(lines)


def text_to_plantuml(puml_text, svg_path, server_url=DEFAULT_SERVER):
    client = PlantUML(url=server_url)
    svg_bytes = client.processes(puml_text)
    svg_path.write_bytes(svg_bytes)