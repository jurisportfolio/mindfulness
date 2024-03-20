from src.textnode import TextNode, TextType

DELIMITERS = {TextType.CODE: "`",
              TextType.BOLD: "**",
              TextType.ITALIC: "*"}


def split_text_node(node_to_split: TextNode, type_to_split: TextType = TextType.BOLD) -> [TextNode]:
    text_to_split = node_to_split.text
    if not text_to_split:
        return [node_to_split]
    delimiter = DELIMITERS[type_to_split]
    sections = text_to_split.split(delimiter)

    if len(sections) == 1:
        return [node_to_split]
    if len(sections) % 2 == 0:
        raise ValueError(f"\nExpected to contain \"{type_to_split.value}\" with open/close delimiters \"{delimiter}\""
                         f"\nInvalid Markdown text: {text_to_split}")

    result = []
    for idx, string in enumerate(sections):
        #TODO: Decide what to do with spaces on left/right side of text
        if string == "":
            continue
        if idx % 2 == 0:
            result.append(TextNode(string, node_to_split.text_type, None))
        else:
            result.append(TextNode(string, type_to_split, None))
    return result


def split_nodes(nodes: list, type_to_split: TextType):
    new_nodes = []
    for node in nodes:
        # TODO: Add splitting other inline types.
        if node.text_type == TextType.TEXT:
            new_nodes.extend(split_text_node(node, type_to_split))
        else:
            new_nodes.append(node)
    return new_nodes
