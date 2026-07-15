import unittest

from htmlnode import HTMLNode

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




if __name__ == "__main__":
    unittest.main()
