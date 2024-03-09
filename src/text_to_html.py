from src.htmlnode import LeafNode
from src.textnode import TextNode, TextType


def leaf_node_from(text_node: TextNode) -> LeafNode:
    node_type = text_node.text_type
    text = text_node.text
    if node_type not in TextType:
        raise TypeError("TextNode type expected to be TextType member")
    if node_type == TextType.TEXT:
        return LeafNode(None, text)
    if node_type == TextType.BOLD:
        return LeafNode("b", text)
    if node_type == TextType.ITALIC:
        return LeafNode("i", text)
    if node_type == TextType.CODE:
        return LeafNode("code", text)
    if node_type == TextType.LINK:
        return LeafNode("a", text, {"href": text_node.url})
    if node_type == TextType.IMAGE:
        return LeafNode("img", "", {"src": text_node.url, "alt": text_node.text})
