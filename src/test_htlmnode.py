import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode


class TestHTMLNode(unittest.TestCase):
    def test_to_html(self):
        self.assertRaises(NotImplementedError)

    def test_props_to_html(self):
        node = HTMLNode(props={"href": "https://www.google.com", "target": "_blank"})
        self.assertEqual(" href=\"https://www.google.com\" target=\"_blank\"", node.props_to_html())

    def test_none_props_to_html(self):
        node = HTMLNode()
        self.assertEqual("", node.props_to_html())

    def test_repr(self):
        child_node1 = HTMLNode("span")
        child_node2 = HTMLNode()
        node = HTMLNode(tag="p",
                        value="This is HTMLNode",
                        props={"class": "some-class", "other_prop": "some-prop"},
                        children=[child_node1, child_node2]
                        )
        self.assertEqual((f"HTMLNode: {id(node)}\n" +
                          "     Tag: <p>\n" +
                          "   Value: \"This is HTMLNode\"\n" +
                          "   Props: {'class': 'some-class', 'other_prop': 'some-prop'}\n" +
                          "Children:\n 0: tag <span>\n 1: has no tag"),
                         repr(node))

    def test_repr_empty_node(self):
        node = HTMLNode()
        test_expectation = f"HTMLNode: {id(node)}"
        self.assertEqual(test_expectation, repr(node))


class TestLeafNode(unittest.TestCase):
    def test_leaf_node_to_html_without_props(self):
        node = LeafNode("p", "This is a paragraph of text.")
        self.assertEqual("<p>This is a paragraph of text.</p>", node.to_html())

    def test_leaf_node_to_html_with_props(self):
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        self.assertEqual("<a href=\"https://www.google.com\">Click me!</a>", node.to_html())

    def test_leaf_node_to_html_none_tag(self):
        node = LeafNode(tag=None, value="Some test node")
        self.assertEqual("Some test node", node.to_html())


class TestParentNode(unittest.TestCase):
    def test_parent_node_to_html(self):
        node = ParentNode(
            tag="p",
            children=[
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        print("")
        print(node.to_html())
        self.assertEqual("<p>\n" +
                         "    <b>Bold text</b>\n" +
                         "    Normal text\n" +
                         "    <i>italic text</i>\n" +
                         "    Normal text\n" +
                         "</p>",
                         node.to_html())


if __name__ == "__main__":
    unittest.main()
