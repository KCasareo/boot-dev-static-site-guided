import unittest
from utils import log_name

from textnode import TextNode, TextType, text_node_to_html_node
from htmlnode import LeafNode

class TestTextNode(unittest.TestCase):
    @log_name()
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)
    @log_name()
    def test_neq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is not a text node", TextType.BOLD)
        node3 = TextNode("This is not a text node", TextType.ITALICS)
        self.assertNotEqual(node, node2)
        self.assertNotEqual(node, node3)
        self.assertNotEqual(node2, node3)
    
    @log_name()
    def test_url_none(self):
        node = TextNode("", TextType.BOLD)
        self.assertEqual(node.url, None)
    
    @log_name(
        prefix = "test_textnode", 
        description = "Convert basic text to html.",
        postfix = "test finished"
    )
    def test_convert_html_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")
        pass

if __name__ == "__main__":
    unittest.main()
