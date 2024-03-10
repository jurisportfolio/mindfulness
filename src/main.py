from src.textnode import TextNode, TextType


def main():
    new_node = TextNode("My new node", TextType.BOLD, "https//new-node.com")
    print(new_node.__repr__())


main()
