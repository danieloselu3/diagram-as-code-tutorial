from diagrams import Diagram
from diagrams.generic.blank import Blank

# Create the diagram object
with Diagram("Programming Languages", show=False, filename="languages"):
    languages = ["Python", "Java", "C++", "Go", "Rust", "JavaScript", "Ruby", "PHP"]

    # Divide the representation in two lines
    mid_index = len(languages) // 2
    first_line = languages[:mid_index]
    second_line = languages[mid_index:]

    # Add nodes in the first row
    prev_node = None

    for language in first_line:
        current_node = Blank(language)
        if prev_node is not None:
            prev_node >> current_node
        prev_node = current_node

    # Add nodes in the second row
    prev_node = None

    for language in second_line:
        current_node = Blank(language)
        if prev_node is not None:
            prev_node >> current_node
        prev_node = current_node
