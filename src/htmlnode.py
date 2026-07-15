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
        raise NotImplementedError()

    def props_to_html(self) -> str:
        return f"{"".join([" " + str(k) + "=" + f"\"{str(v)}\"" for k,v in self.props.items()]) if self.props is not None else ""}"
        pass

    def __repr__(self) -> str:
        return f"Tag: {self.tag}\nValue: {self.value}\nChildren: {self.children}\nProps: {self.props}"
        pass

class LeafNode(HTMLNode):
    def __init__(
        self,
        tag: str,
        value: str,
        props: dict[str,str|None]|None = None
    ):
        if value is None:
            raise ValueError()
        super().__init__(
            tag,
            value,
            None,
            props
        )
    def to_html(self) -> str:
        #        if self.value is None:
        #   raise ValueError()
        if self.tag is None:
            return self.value
        return f"<{self.tag}{self.props_to_html() if self.props is not None else ""}>{self.value}</{self.tag}>"


class ParentNode(HTMLNode):
    def __init__(
        self,
        tag: str,
        children : list[HTMLNode],
        props: dict[str, str|None]|None = None

    ):
        if tag is None:
            raise ValueError()
        if children is None:
            raise ValueError()
        super().__init__(
            tag,
            None,
            children,
            props
        )

    def to_html(self) -> str:
        if self.tag is None:
            raise ValueError()
        if self.children is None:
            raise ValueError()
        return f"<{self.tag}{self.props_to_html()}>{"".join([child.to_html() for child in self.children])}</{self.tag}>"
