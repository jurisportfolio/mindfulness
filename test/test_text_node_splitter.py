import unittest
from src.textnode import TextType, TextNode
from src.text_node_splitter import split_text_node, split_nodes


class TestSplitTextNode(unittest.TestCase):

    def test_split_code(self):
        text_node_with_code = TextNode("Some text `some code` more text", TextType.TEXT, None)

        self.assertEqual([
            TextNode("Some text ", TextType.TEXT, None),
            TextNode("some code", TextType.CODE, None),
            TextNode(" more text", TextType.TEXT, None)
        ], split_text_node(text_node_with_code, TextType.CODE))

    def test_split_bold(self):
        text_node_with_bold = TextNode("Some text *some bold text* more text", TextType.TEXT, None)

        self.assertEqual([
            TextNode("Some text ", TextType.TEXT, None),
            TextNode("some bold text", TextType.BOLD, None),
            TextNode(" more text", TextType.TEXT, None)
        ], split_text_node(text_node_with_bold, TextType.BOLD))

    def test_split_italic(self):
        text_node_with_italic = TextNode("Some text **some italic text** more text", TextType.TEXT, None)

        self.assertEqual([
            TextNode("Some text ", TextType.TEXT, None),
            TextNode("some italic text", TextType.ITALIC, None),
            TextNode(" more text", TextType.TEXT, None)
        ], split_text_node(text_node_with_italic, TextType.ITALIC))

    def test_no_split(self):
        text_node_plain_text = TextNode("Some text more text", TextType.TEXT, None)
        self.assertEqual([text_node_plain_text], split_text_node(text_node_plain_text, TextType.CODE))

    def test_empty_text_split(self):
        text_node_plain_text = TextNode("", TextType.TEXT, None)
        self.assertEqual([text_node_plain_text], split_text_node(text_node_plain_text, TextType.CODE))

    def test_nodo_with_none_text(self):
        text_node_none_text = TextNode(None, TextType.TEXT, None)
        self.assertEqual([text_node_none_text], split_text_node(text_node_none_text, TextType.CODE))

    # TODO: Learn how to test errors
    # def test_with_missing_delimiter(self):
    #     text_node_missing_italic = TextNode("Some text **some italic text more text", TextType.TEXT, None)
    #     self.assertRaises(ValueError, split_text_node(text_node_missing_italic, TextType.ITALIC))

    def test_split_two_bold_texts(self):
        text_node_with_bold = TextNode("Some text *some bold text* more text *more bold text* end of text", TextType.TEXT, None)

        self.assertEqual([
            TextNode("Some text ", TextType.TEXT, None),
            TextNode("some bold text", TextType.BOLD, None),
            TextNode(" more text ", TextType.TEXT, None),
            TextNode("more bold text", TextType.BOLD, None),
            TextNode(" end of text", TextType.TEXT, None)
        ], split_text_node(text_node_with_bold, TextType.BOLD))

    def test_split_when_strats_from_bold(self):
        text_node_with_bold = TextNode("*some bold text* more text *more bold text* end of text", TextType.TEXT, None)

        self.assertEqual([
            TextNode("some bold text", TextType.BOLD, None),
            TextNode(" more text ", TextType.TEXT, None),
            TextNode("more bold text", TextType.BOLD, None),
            TextNode(" end of text", TextType.TEXT, None)
        ], split_text_node(text_node_with_bold, TextType.BOLD))

    def test_split_when_just_bold_texts(self):
        text_node_with_bold = TextNode("*some bold text* *more bold text*", TextType.TEXT, None)

        self.assertEqual([
            TextNode("some bold text", TextType.BOLD, None),
            TextNode(" ", TextType.TEXT, None),
            TextNode("more bold text", TextType.BOLD, None)
        ], split_text_node(text_node_with_bold, TextType.BOLD))


class TestSplitNodes(unittest.TestCase):
    def test_split_italic_nodes_input(self):
        text_node_with_italic = TextNode("Some text **some italic text** more text", TextType.TEXT, None)
        text_node_with_bold = TextNode("*some bold text* more text *more bold text* end of text", TextType.TEXT, None)
        text_nodes = [text_node_with_italic, text_node_with_bold]
        self.assertEqual([
            TextNode("Some text ", TextType.TEXT, None),
            TextNode("some italic text", TextType.ITALIC, None),
            TextNode(" more text", TextType.TEXT, None),
            TextNode("*some bold text* more text *more bold text* end of text", TextType.TEXT, None)
        ], split_nodes(text_nodes, TextType.ITALIC))

    def test_split_italic_and_bold_nodes_input(self):
        text_node_with_italic = TextNode("Some text **some italic text** more text", TextType.TEXT, None)
        text_node_with_bold = TextNode("*some bold text* more text *more bold text* end of text", TextType.TEXT, None)
        text_nodes = [text_node_with_italic, text_node_with_bold]
        text_nodes_with_italics = split_nodes(text_nodes, TextType.ITALIC)
        text_nodes_result = split_nodes(text_nodes_with_italics, TextType.BOLD)
        self.assertEqual([
            TextNode("Some text ", TextType.TEXT, None),
            TextNode("some italic text", TextType.ITALIC, None),
            TextNode(" more text", TextType.TEXT, None),
            TextNode("some bold text", TextType.BOLD, None),
            TextNode(" more text ", TextType.TEXT, None),
            TextNode("more bold text", TextType.BOLD, None),
            TextNode(" end of text", TextType.TEXT, None)
        ], text_nodes_result)
