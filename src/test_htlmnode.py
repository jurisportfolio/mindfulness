import unittest

from htmlnode import HTMLNode


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
        node = HTMLNode("p",
                        "This is HTMLNode",
                        {"class": "some-class", "other_prop": "some-prop"},
                        [child_node1, child_node2]
                        )
        self.assertEqual((f"HTMLNode: {id(node)}\n" +
                          f"     Tag: <p>\n" +
                          f"   Value: \"This is HTMLNode\"\n" +
                          f"   Props: class=\"some-class\" other_prop=\"some-prop\"\n" +
                          f"Children:\n 0: tag <span>\n 1: has no tag"),
                         repr(node))

    def test_repr_empty_node(self):
        node = HTMLNode()
        test_expectation = f"HTMLNode: {id(node)}"
        self.assertEqual(test_expectation, repr(node))


if __name__ == "__main__":
    unittest.main()
