import unittest
from utils import log_name

from textnode import TextNode, TextType, text_node_to_html_node, split_nodes_delimiter
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
    @log_name(
        prefix = "test_textnode"
    )
    def test_convert_html_bold(self):
        node = TextNode("This is bolded", TextType.BOLD)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "b")
        self.assertEqual(html_node.value, "This is bolded")
        pass
    @log_name(
        prefix = "test_textnode"
    )
    def test_convert_html_italics(self):
        node = TextNode("This is italicised", TextType.ITALICS)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "i")
        self.assertEqual(html_node.value, "This is italicised")
        pass
    def test_convert_html_code(self):
        node = TextNode("This is code", TextType.CODE)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "code")
        self.assertEqual(html_node.value, "This is code")
        pass

    def test_convert_html_link(self):
        node = TextNode("Click me!", TextType.LINK, "http://www.google.com")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "a")
        self.assertEqual(html_node.value, "Click me!")
        self.assertEqual(html_node.props["href"], "http://www.google.com")

    def test_convert_html_image(self):
        node = TextNode("Hover over here!", TextType.IMAGE, "http://static.getfunnyimage.com")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.props["src"], "http://static.getfunnyimage.com")
        self.assertEqual(html_node.props["alt"], "Hover over here!")
    @log_name(
        prefix = "test_textnode"
    )
    def test_textnode_splice(self):
        node = TextNode("I have code text in `here it is` and this isn't", TextType.TEXT)
        lnode : list[TextNode] = [node]
        result = split_nodes_delimiter(
            lnode,
            "`",
            TextType.CODE
        )
        for i in result:
            print(f"{i.text} {i.text_type}")
        pass
if __name__ == "__main__":
    unittest.main()
