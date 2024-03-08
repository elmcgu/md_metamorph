import re

from textnode import (
    TextNode,
    text_type_text,
    text_type_bold,
    text_type_italic,
    text_type_code,
    text_type_image,
    text_type_link,
)

def text_to_textnodes(text):
    nodes = [TextNode(text, text_type_text)]
    nodes = split_nodes_delimiter(nodes, "**", text_type_bold)
    nodes = split_nodes_delimiter(nodes, "*", text_type_italic)
    nodes = split_nodes_delimiter(nodes, "`", text_type_code)
    nodes = split_nodes_image(nodes)
    nodes = split_nodes_link(nodes)
    return nodes



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

def split_nodes_image(old_nodes):
    # Initialize an empty list to store new nodes
    new_nodes = []
    
    # Iterate through each old node in the input list
    for old_node in old_nodes:
        # Check if the text type of the old node is not text (e.g., it's an image or a link)
        if old_node.text_type != text_type_text:
            # If not text, add the old node directly to the new nodes list and continue to the next iteration
            new_nodes.append(old_node)
            continue
        
        # Store the original text of the old node
        original_text = old_node.text
        
        # Extract images from the original text
        images = extract_markdown_images(original_text)
        
        # Check if there are no images in the original text
        if len(images) == 0:
            # If no images, add the old node directly to the new nodes list and continue to the next iteration
            new_nodes.append(old_node)
            continue
        
        # Iterate through each image found in the original text
        for image in images:
            # Split the original text into sections based on the current image
            sections = original_text.split(f"![{image[0]}]({image[1]})", 1)
            
            # Check if the sections are not exactly two (image section not closed properly)
            if len(sections) != 2:
                # Raise a ValueError indicating an issue with the markdown format
                raise ValueError("Invalid markdown, image section not closed")
            
            # Check if there is any text before the current image section
            if sections[0] != "":
                # Add the text before the image section as a new text node to the new nodes list
                new_nodes.append(TextNode(sections[0], text_type_text))
            
            # Add a new image node to the new nodes list with the image's alt text and source URL
            new_nodes.append(
                TextNode(
                    image[0],
                    text_type_image,
                    image[1],
                )
            )
            
            # Update the original text to the remaining part after the current image section
            original_text = sections[1]
        
        # Check if there is any text remaining after processing all images
        if original_text != "":
            # Add the remaining text as a new text node to the new nodes list
            new_nodes.append(TextNode(original_text, text_type_text))
    
    # Return the final list of new nodes
    return new_nodes


def split_nodes_link(old_nodes):
    # Initialize an empty list to store new nodes
    new_nodes = []
    
    # Iterate through each old node in the input list
    for old_node in old_nodes:
        # Check if the text type of the old node is not text (e.g., it's an image or a link)
        if old_node.text_type != text_type_text:
            # If not text, add the old node directly to the new nodes list and continue to the next iteration
            new_nodes.append(old_node)
            continue
        
        # Store the original text of the old node
        original_text = old_node.text
        
        # Extract links from the original text
        links = extract_markdown_links(original_text)
        
        # Check if there are no links in the original text
        if len(links) == 0:
            # If no links, add the old node directly to the new nodes list and continue to the next iteration
            new_nodes.append(old_node)
            continue
        
        # Iterate through each link found in the original text
        for link in links:
            # Split the original text into sections based on the current link
            sections = original_text.split(f"[{link[0]}]({link[1]})", 1)
            
            # Check if the sections are not exactly two (link section not closed properly)
            if len(sections) != 2:
                # Raise a ValueError indicating an issue with the markdown format
                raise ValueError("Invalid markdown, link section not closed")
            
            # Check if there is any text before the current link section
            if sections[0] != "":
                # Add the text before the link section as a new text node to the new nodes list
                new_nodes.append(TextNode(sections[0], text_type_text))
            
            # Add a new link node to the new nodes list with the link's text and URL
            new_nodes.append(TextNode(link[0], text_type_link, link[1]))
            
            # Update the original text to the remaining part after the current link section
            original_text = sections[1]
        
        # Check if there is any text remaining after processing all links
        if original_text != "":
            # Add the remaining text as a new text node to the new nodes list
            new_nodes.append(TextNode(original_text, text_type_text))
    
    # Return the final list of new nodes
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