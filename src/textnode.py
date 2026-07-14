from __future__ import annotations

from enum import Enum
class TextType(Enum):
    Bold = 1
    Italic = 2
    Code = 3
    Link = 4
    Image = 5

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
