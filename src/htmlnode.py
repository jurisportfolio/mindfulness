class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError("to_html method not implemented")

    def props_to_html(self):
        html_props = []
        if self.props:
            for prop in self.props:
                html_props.append(f" {prop}=\"{self.props[prop]}\"")
        return "".join(html_props)

    def open_tag_to_html(self):
        return f"<{self.tag}>" if not self.props else f"<{self.tag}{self.props_to_html()}>"

    def closing_tag_to_html(self):
        return f"</{self.tag}>"

    def __repr__(self):
        node_repr = "\n"
        node_repr += f"HTMLNode: {id(self)}"
        if self.tag:
            node_repr += f"\n     Tag: <{self.tag}>"
        if self.value:
            node_repr += f"\n   Value: \"{self.value}\""
        if self.props:
            node_repr += f"\n   Props: {self.props}"
        if self.children:
            node_repr += f"\nChildren:"
            for index, child in enumerate(self.children):
                tag_to_print = f"tag <{child.tag}>"
                node_repr += f"\n {index}: {tag_to_print if child.tag else 'has no tag'}"
        return node_repr


class LeafNode(HTMLNode):
    def __init__(self, tag: str, value: str, props=None):
        super().__init__(tag=tag, value=value, props=props)

    def to_html(self) -> str:
        if self.value is None:
            raise ValueError(f"LeafNode {id(self)} "
                             f"Value property is None. Expecting to be string.")
        if self.tag is None:
            return self.value
        if isinstance(self.tag, str):
            return f"{super().open_tag_to_html()}{self.value}{super().closing_tag_to_html()}"
        raise ValueError(f"LeafNode {id(self)} "
                         f"Tag property expecting to be string or None.")

    def __repr__(self):
        return super().__repr__()


class ParentNode(HTMLNode):
    def __init__(self, tag: str, children: [HTMLNode], props: dict = None):
        super().__init__(tag=tag, children=children, props=props)

    def to_html(self):
        if self.tag is None:
            raise ValueError(f"ParentNode {id(self)} "
                             f"Tag property is None. Expecting to be string.")
        if not self.children:
            raise ValueError(f"ParentNode {id(self)} "
                             f"Children property is not set. Expecting to be not empty list of HTMLNodes")
        children = ["    " + child.to_html() for child in self.children]
        children_html = "\n".join(children)
        return (f"{super().open_tag_to_html()}\n" +
                f"{children_html}"
                f"\n{super().closing_tag_to_html()}")

    def __repr__(self):
        return super().__repr__()
