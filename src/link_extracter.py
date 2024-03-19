import re

from src.textnode import TextNode, TextType


# regex https://regexr.com/


def links_from_markdown(text: str) -> list:
    return re.findall(r"\[(.*?)\]\((\S*?)\)", text)


def split_by_link(node: TextNode, link: tuple) -> [TextNode]:
    sections = node.text.split(f"[{link[0]}]({link[1]})", 1)
    new_nodes = []
    if sections[0] != "":
        new_nodes.append((TextNode(sections[0], TextType.TEXT)))
    new_nodes.append((TextNode(link[0], TextType.LINK, link[1])))
    if sections[1] != "":
        new_nodes.append((TextNode(sections[1], TextType.TEXT)))
    return new_nodes


def links_extracted(node: TextNode) -> [TextNode]:
    links = links_from_markdown(node.text)
    new_nodes = [node]
    for link in links:
        splited_nodes = split_by_link(new_nodes[-1], link)
        del new_nodes[-1]
        new_nodes.extend(splited_nodes)
    return new_nodes


def split_nodes_link(old_nodes: [TextNode]) -> [TextNode]:
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
        else:
            new_nodes.extend(links_extracted(node))
    return new_nodes
