import unittest

from htmlnode import HTMLNode
from htmlnode import LeafNode
class TestHTMLNode(unittest.TestCase):
    def test_props_to_html(self):
        print("Test/test_props_to_html")
        node : HTMLNode = HTMLNode(props={
            "href": "https://www.google.com",
            "target": "_blank",
        })
        print(f"node contents:\n{node}")
        print(f"props_to_html() result:\n\"{node.props_to_html()}\"")
        self.assertEqual(
            node.props_to_html(),
            " href=\"https://www.google.com\" target=\"_blank\""
        )
    pass

    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        print(f"node contents:\n{node}")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")
    
    def test_leaf_to_html_a_props(self):
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        print(f"node contents:\n{node}")
        print(f"to_html value:\n{node.to_html()}")
        self.assertEqual(node.to_html(), "<a href=\"https://www.google.com\">Click me!</a>")

    def test_leaf_to_html_b(self):
        node = LeafNode("b", "I am bold!")
        print(f"node contents:\n{node}")
        print(f"to_html value:\n{node.to_html()}")
        self.assertEqual(node.to_html(), "<b>I am bold!</b>")
if __name__ == "__main__":
    unittest.main()
