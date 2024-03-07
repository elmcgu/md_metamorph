# Importing the LeafNode class from the htmlnode module
from htmlnode import LeafNode

# Constants representing different types of text nodes
text_type_text = "text"
text_type_bold = "bold"
text_type_italic = "italic"
text_type_code = "code"
text_type_link = "link"
text_type_image = "image"

# Class representing a text node
class TextNode:
    def __init__(self, text, text_type, url=None):
        # Initializing the TextNode with text content, text type, and an optional URL
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, other):
        # Defining equality for TextNode objects based on text type, text content, and URL
        return (
            self.text_type == other.text_type
            and self.text == other.text
            and self.url == other.url
        )

    def __repr__(self):
        # Generating a string representation of the TextNode
        return f"TextNode({self.text}, {self.text_type}, {self.url})"


# Function to convert a TextNode to a corresponding HTMLNode (LeafNode)
def text_node_to_html_node(text_node):
    # Check the text type and create a LeafNode accordingly
    if text_node.text_type == text_type_text:
        return LeafNode(None, text_node.text)  # LeafNode with no tag, raw text value
    if text_node.text_type == text_type_bold:
        return LeafNode("b", text_node.text)   # LeafNode with "b" tag and text
    if text_node.text_type == text_type_italic:
        return LeafNode("i", text_node.text)   # LeafNode with "i" tag and text
    if text_node.text_type == text_type_code:
        return LeafNode("code", text_node.text)  # LeafNode with "code" tag and text
    if text_node.text_type == text_type_link:
        return LeafNode("a", text_node.text, {"href": text_node.url})  # LeafNode with "a" tag, anchor text, and "href" prop
    if text_node.text_type == text_type_image:
        return LeafNode("img", "", {"src": text_node.url, "alt": text_node.text})  # LeafNode with "img" tag, empty value, "src" and "alt" props
    
    # Raise an exception for an invalid text type
    raise ValueError(f"Invalid text type: {text_node.text_type}")
