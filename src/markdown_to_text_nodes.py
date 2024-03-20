from src.link_extracter import split_nodes_link
from src.text_node_splitter import split_nodes
from src.textnode import TextNode, TextType
from src.image_extracter import split_nodes_image


def textnodes_from_markdown(text: str) -> [TextNode]:
    """Convert Markdown string into list of TextNodes"""
    if text == "":
        raise ValueError("Input string is empty")
    start_node = [TextNode(text, TextType.TEXT)]
    # TODO: Make funktion which do not relay on order
    # Attention: split_nodes_images should go before split_nodes_link
    markdown_nodes = split_nodes_image(start_node)
    markdown_nodes = split_nodes_link(markdown_nodes)
    # Attention: split_nodes on BOLD should go before split_nodes on ITALIC
    markdown_nodes = split_nodes(markdown_nodes, TextType.BOLD)
    markdown_nodes = split_nodes(markdown_nodes, TextType.ITALIC)
    markdown_nodes = split_nodes(markdown_nodes, TextType.CODE)

    return markdown_nodes
