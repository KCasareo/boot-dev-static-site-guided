from __future__ import annotations

from functools import reduce
from enum import Enum
from htmlnode import LeafNode
from typing import Tuple
import operator

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
        #nonlocal text_node
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

def split_nodes_delimiter(
    old_nodes: list[TextNode],
    delimiter: str,
    text_type: TextType
) -> list[TextNode]:
    # this method is for paired tags only
    # special cases for link and image require their own function
    def munch_token(text_node : TextNode) -> list[Tuple[TextType,str]]:
        # ordered list of all elements
        res : list[Tuple[TextType,str]] = []
        # list of all elements
        # elems in pos 1, 3, 5, etc. are inside a code block
        ss : list[str] = text_node.text.split(delimiter)
        print(f"ss value: {ss}")
        ## look for pairs
        for item in range(len(ss)):
            res.append((TextType.TEXT if item % 2 == 0 else text_type, ss[item]))
        print(f"res value: {res}")
        return res
        pass
    # take the list of nodes, then flatten to a single dimensional list for processing
    ## FUTURE: loop through all list of old nodes to allow for matching, then flatten the combined list after everything is done
    new_nodes : list[Tuple[TextType,str]] = reduce(operator.add, [munch_token(node) for node in old_nodes])
    print(f"new_nodes value: {new_nodes}")
    return [TextNode(item[1],item[0]) for item in new_nodes]
    pass

