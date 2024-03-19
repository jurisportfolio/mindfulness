import re
from src.textnode import TextNode, TextType


def images_from_markdown(text: str) -> list:
    return re.findall(r"!\[(.*?)\]\((\S*?)\)", text)


def split_by_image(node: TextNode, image: tuple) -> [TextNode]:
    sections = node.text.split(f"![{image[0]}]({image[1]})", 1)
    new_nodes = []
    if sections[0] != "":
        new_nodes.append((TextNode(sections[0], TextType.TEXT)))
    new_nodes.append((TextNode(image[0], TextType.IMAGE, image[1])))
    if sections[1] != "":
        new_nodes.append((TextNode(sections[1], TextType.TEXT)))
    return new_nodes


def images_extracted(node: TextNode) -> [TextNode]:
    images = images_from_markdown(node.text)
    new_nodes = [node]
    for image in images:
        splited_nodes = split_by_image(new_nodes[-1], image)
        del new_nodes[-1]
        new_nodes.extend(splited_nodes)
    return new_nodes


def split_nodes_image(old_nodes: [TextNode]) -> [TextNode]:
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
        else:
            new_nodes.extend(images_extracted(node))
    return new_nodes
