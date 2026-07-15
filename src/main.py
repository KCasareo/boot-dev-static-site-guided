from __future__ import annotations

from textnode import TextNode
from textnode import TextType


def main():
    test : TextNode = TextNode("This is some anchor text", TextType.LINK, "https://www.boot.dev")
    print(f"{repr(test)}")


if __name__ == "__main__":
    main()
