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
        node_repr = ""
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
    def __init__(self, tag, value, props=None):
        super().__init__(tag=tag, value=value, props=props)

    def to_html(self):
        if isinstance(self.tag, str):
            return f"{super().open_tag_to_html()}{self.value}{super().closing_tag_to_html()}"
        if self.tag is None:
            return f"{self.value}"
        raise ValueError(f"Tag property for LeafNode {id(self)} should be string or None.")
