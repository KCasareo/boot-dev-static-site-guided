from __future__ import annotations


from enum import Enum
from htmlnode import LeafNode
from typing import Tuple

class TextType(Enum):
    TEXT = 0
    BOLD = 1
    ITALICS = 2
    CODE = 3
    LINK = 4
    IMAGE = 5

class TextNode(object):
    def __init__(
        self: TextNode,
        text: str,
        text_type: TextType,
        url: str = None
    ):
        self.text = text
        self.text_type = text_type
        self.url = url


    def __eq__(
        self: TextNode, 
        other: TextNode
    ) -> bool:
        return self.text == other.text and self.text_type == other.text_type and self.url == other.url

    def __repr__(self) -> str:
        return "TextNode(TEXT,TEXT_TYPE, URL)"

"""
====================
Conversion functions
====================
"""

def text_node_to_html_node(text_node: TextNode) -> LeafNode:
## Prepare object then return
## LeafNode(tag, value, props)
    ## Helper function
    def prepare_html(type: TextType) -> Tuple[str|None,str|None,dict[str,str]|None]:
        nonlocal text_node
        match(type):
            case TextType.TEXT:
                return None, text_node.text, None
            case TextType.BOLD:
                return "b", text_node.text, None
            case TextType.ITALICS:
                return "i", text_node.text, None
            case TextType.CODE:
                return "code", text_node.text, None
            case TextType.LINK:
                return "a", text_node.text, { "href" : f"{text_node.url}"}
            case TextType.IMAGE:
                return "img", "", { "src" : f"{text_node.url}", "alt" : f"{text_node.text}" }
    tag,val,props = prepare_html(text_node.text_type)

    return LeafNode(tag,val,props)

