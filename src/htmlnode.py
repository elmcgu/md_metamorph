class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        # Initializing the HTMLNode with tag, value, children, and properties
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        # Placeholder method that needs to be implemented by child classes
        raise NotImplementedError("to_html method not implemented")

    def props_to_html(self):
        # Generate HTML string for properties
        if self.props is None:
            return ""
        props_html = ""
        for prop in self.props:
            props_html += f' {prop}="{self.props[prop]}"'
        return props_html

    def __repr__(self):
        # Generating a string representation of the HTMLNode
        return f"HTMLNode({self.tag}, {self.value}, children: {self.children}, {self.props})"


class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        # Initialize LeafNode by calling the parent's constructor with children set to None
        super().__init__(tag, value, None, props)

    def to_html(self):
        # Render HTML for LeafNode
        if self.value is None:
            raise ValueError("Invalid HTML: no value")
        if self.tag is None:
            return self.value
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"

    def __repr__(self):
        # Generating a string representation of the LeafNode
        return f"LeafNode({self.tag}, {self.value}, {self.props})"


class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        # Initialize ParentNode by calling the parent's constructor
        super().__init__(tag, None, children, props)

    def to_html(self):
        # Render HTML for ParentNode
        if self.tag is None:
            raise ValueError("Invalid HTML: no tag")
        if self.children is None:
            raise ValueError("Invalid HTML: no children")
        children_html = ""
        for child in self.children:
            children_html += child.to_html()
        return f"<{self.tag}{self.props_to_html()}>{children_html}</{self.tag}>"

    def __repr__(self):
        # Generating a string representation of the ParentNode
        return f"ParentNode({self.tag}, children: {self.children}, {self.props})"
