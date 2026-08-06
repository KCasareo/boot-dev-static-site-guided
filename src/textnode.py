from __future__ import annotations

from functools import reduce
from enum import Enum
from htmlnode import LeafNode
from typing import Tuple
import operator
import re


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
        #print(f"ss value: {ss}")
        ## look for pairs
        for item in range(len(ss)):
            res.append((TextType.TEXT if item % 2 == 0 else text_type, ss[item]))
        #print(f"res value: {res}")
        return res
        pass
    # take the list of nodes, then flatten to a single dimensional list for processing
    ## FUTURE: loop through all list of old nodes to allow for matching, then flatten the combined list after everything is done
    new_nodes : list[Tuple[TextType,str]] = reduce(operator.add, [munch_token(node) for node in old_nodes])
    #print(f"new_nodes value: {new_nodes}")
    return [TextNode(item[1],item[0]) for item in new_nodes]
    pass


def extract_markdown_images(
    text: str
) -> list[Tuple[str, str]]:
    matches = re.findall(
        r"!\[(.*?)\]\((.*?)\)",
        text
    )
    return matches
    pass

def extract_markdown_links(
        text: str
) -> list[Tuple[str, str]]:
    matches = re.findall(
        r"\[(.*?)\]\((.*?)\)",
        text
    )
    return matches

def split_nodes_image(
    old_nodes: list[TextNode]
) -> list[TextNode]:
    result : list[TextNode]= []
    # happy path
    # 1. get md list
    #image_nodes = extract_markdown_images(old_nodes)
    # 2. use as delim
    def munch_nodes(
        remaining : str, # chunks leftover for processing
        pattern : list[str], # next delimiter to check
    ) -> list[str]:
        # base case
        if len(remaining) == 0:
            return []
        ## needs logic to append if there are still remaining nodes
        r = re.split(
            pattern[0],
            remaining,
            maxsplit=1
        )
        # result should be the first chunk, followed by the delimiter, then munch_nodes called with the slice from pos 1
        # # needs guard clauses and defaults
        result = [r[0], pattern[0]] + munch_nodes(r[], pattern[1:] if pattern )
        pass

    for node in old_nodes:
        if node.text_type is not TextType.TEXT:
            # maybe just push onto result list as is
            result.append(node)
            continue
        # otherwise, parse the node and rip 
        image_nodes = extract_markdown_images(node.text)
        # start running through each separator
        # generate a delimiter from a regex pipe match of an image link string
        # 
        pattern = "|".join(map(re.escape, [ f"![{inode[0]}]({inode[1]})" for inode in image_nodes ]))
        # maybe a function that just munches on nodes
        # get the first chunk, eat, then insert?
        text_only : str = re.split(
            pattern,
            node.text,
            maxsplit=1
        )
        ## get first chunk
        ## insert next node
        # parsing behavior here on each node
        # start creating 
        tnode_images = []
        #for inode in image_nodes:


    return result
        
    raise NotImplementedError()

def split_nodes_link(
    old_nodes: list[TextNode]
) -> list[TextNode]:
    raise NotImplementedError()
