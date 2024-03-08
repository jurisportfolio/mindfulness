import unittest
from src.textnode import (
    TextNode,
    TextType
)


class TestTextNode(unittest.TestCase):
    def test_eq_true(self):
        node = TextNode("This is a TextNode", TextType.BOLD)
        node2 = TextNode("This is a TextNode", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_eq_false(self):
        node = TextNode("This is a TextNode", TextType.BOLD)
        node2 = TextNode("This is a TextNode", TextType.TEXT)
        self.assertNotEqual(node, node2)

    def test_repr(self):
        node = TextNode("This is a text node", TextType.TEXT.value, "https//new-node.com")
        self.assertEqual(
            "TextNode(This is a text node, text, https//new-node.com)", repr(node)
        )


if __name__ == "__main__":
    unittest.main()
