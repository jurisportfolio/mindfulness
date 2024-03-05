import unittest
from textnode import (
    TextNode,
    text_type_bold,
    text_type_text
)


class TestTextNode(unittest.TestCase):
    def test_eq_true(self):
        node = TextNode("This is a TextNode", text_type_bold)
        node2 = TextNode("This is a TextNode", text_type_bold)
        self.assertEqual(node, node2)

    def test_eq_false(self):
        node = TextNode("This is a TextNode", text_type_bold)
        node2 = TextNode("This is a TextNode", text_type_text)
        self.assertNotEqual(node, node2)

    def test_repr(self):
        node = TextNode("This is a text node", text_type_text, "https//new-node.com")
        self.assertEqual(
            "TextNode(This is a text node, text, https//new-node.com)", repr(node)
        )




if __name__ == "__main__":
    unittest.main()
