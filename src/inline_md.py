import re

from textnode import (
    TextNode,
    text_type_text,
    text_type_bold,
    text_type_italic,
    text_type_code,
)

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    # Initialize a list to store the new nodes after splitting
    new_nodes = []

    # Iterate over the old_nodes
    for old_node in old_nodes:
        # Check if the text type of the old_node is not text, if so, add it as is to the new_nodes
        if old_node.text_type != text_type_text:
            new_nodes.append(old_node)
            continue

        # Initialize a list to store the split nodes
        split_nodes = []
        # Split the text of the old_node using the provided delimiter
        sections = old_node.text.split(delimiter)

        # Check if the sections are balanced (even number of sections)
        if len(sections) % 2 == 0:
            raise ValueError("Invalid markdown, bold section not closed")

        # Iterate over the sections
        for i in range(len(sections)):
            # Skip empty sections
            if sections[i] == "":
                continue

            # Create TextNode for even-indexed sections with text_type_text, and for odd-indexed sections with the provided text_type
            if i % 2 == 0:
                split_nodes.append(TextNode(sections[i], text_type_text))
            else:
                split_nodes.append(TextNode(sections[i], text_type))

        # Extend the new_nodes list with the split_nodes
        new_nodes.extend(split_nodes)

    # Return the list of new nodes after splitting
    return new_nodes

    
# Function to extract markdown images from text
def extract_markdown_images(text):
    pattern = r"!\[(.*?)\]\((.*?)\)"
    matches = re.findall(pattern, text)
    return matches

# Function to extract markdown links from text
def extract_markdown_links(text):
    pattern = r"\[(.*?)\]\((.*?)\)"
    matches = re.findall(pattern, text)
    return matches