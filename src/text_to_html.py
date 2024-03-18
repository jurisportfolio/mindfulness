from src.htmlnode import LeafNode
from src.textnode import TextNode, TextType


def leaf_node_from(node: TextNode) -> LeafNode:
    if node.text_type not in TextType:
        raise TypeError("TextNode type expected to be TextType member")
    leaf_nodes = {
        TextType.TEXT: LeafNode(None, node.text),
        TextType.BOLD: LeafNode("b", node.text),
        TextType.ITALIC: LeafNode("i", node.text),
        TextType.CODE: LeafNode("code", node.text),
        TextType.LINK: LeafNode("a", node.text, {"href": node.url}),
        TextType.IMAGE: LeafNode("img", "", {"src": node.url, "alt": node.text})
    }
    return leaf_nodes.get(node.text_type)
