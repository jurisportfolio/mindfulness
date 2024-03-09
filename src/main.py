from src.textnode import TextNode


def main():
    new_node = TextNode("My new node", "bold", "https//new-node.com")
    print(new_node.__repr__())


main()
