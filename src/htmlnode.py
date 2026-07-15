from __future__ import annotations


class HTMLNode():
    def __init__(
        self,
        tag: str|None = None,
        value: str|None = None,
        children: list[HTMLNode]|None = None,
        props:  dict[str, str|None]|None = None
    ):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

        pass

    def to_html(self):
        raise NotImplementedError

    def props_to_html(self) -> str:
        return f"{"".join([" " + str(k) + "=" + f"\"{str(v)}\"" for k,v in self.props.items()])}"
        pass

    def __repr__(self) -> str:
        return f"Tag: {self.tag}\nValue: {self.value}\nChildren: {self.children}\nProps: {self.props}"
        pass
