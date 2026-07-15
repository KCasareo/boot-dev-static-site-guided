import unittest

from htmlnode import HTMLNode
from htmlnode import LeafNode
from htmlnode import ParentNode

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
    
    def test_parent_node_init(self):
        print("Test/test_parent_node_init")
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode("b", "Bold text"),
            ],
            None
        )
        print(f"node contents:\n{node}")
        self.assertNotEqual(node.children, None)

    def test_parent_to_html(self):
        print("Test/test_parent_to_html")
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        print(f"node contents:\n{node}")
        print(f"Parent Node Children:\n{node.to_html()}")
        self.assertEqual(node.to_html(), "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>")

    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")



    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

    def test_parent_no_children(self):
        with self.assertRaises(ValueError):
            p = ParentNode("div", None)
            p.to_html()

    def test_parent_no_tag(self):
        with self.assertRaises(ValueError):
            p = ParentNode(None, [])
            p.to_html()
if __name__ == "__main__":
    unittest.main()
