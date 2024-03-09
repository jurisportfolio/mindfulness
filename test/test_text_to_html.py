from src.htmlnode import LeafNode
from src.text_to_html import leaf_node_from
from src.textnode import TextNode, TextType
import unittest


class TestTextNodeToLeafNode(unittest.TestCase):

    def test_node_text_type(self):
        self.assertEqual(LeafNode(None, "some text"),
                         leaf_node_from(TextNode("some text", TextType.TEXT)))

    def test_node_bold_type(self):
        self.assertEqual(LeafNode("b", "some bold text"),
                         leaf_node_from(TextNode("some bold text", TextType.BOLD)))

    def test_node_italic_type(self):
        self.assertEqual(LeafNode("i", "some italic text"),
                         leaf_node_from(TextNode("some italic text", TextType.ITALIC)))

    def test_node_code_type(self):
        self.assertEqual(LeafNode("code", "some code text"),
                         leaf_node_from(TextNode("some code text", TextType.CODE)))

    def test_node_link_type(self):
        self.assertEqual(LeafNode("a", "some link text", {"href": "http://google.com"}),
                         leaf_node_from(TextNode("some link text", TextType.LINK, "http://google.com")))

    def test_node_image_type(self):
        self.assertEqual(LeafNode("img", "", {"src": "/src/img/test.jpeg", "alt": "some alt text"}),
                         leaf_node_from(TextNode("some alt text", TextType.IMAGE, "/src/img/test.jpeg")))
