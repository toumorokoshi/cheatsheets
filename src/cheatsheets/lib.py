"""
Library file for cheatsheets
"""
from jinja2 import Template


def find_text_node(minidom_node):
    """
    returns the first text node found in the minidom
    """
    if minidom_node.nodeType == minidom_node.TEXT_NODE:
        return minidom_node
    for n in minidom_node.childNodes:
        result = find_text_node(n)
        if result is not None:
            return result
    return None


def parse_attribute_table(table_node, return_object):
    attribute_nodes = table_node.getElementsByTagName("row")
    for an in attribute_nodes:
        key = find_text_node(an.childNodes[0]).nodeValue.lower()
        value = find_text_node(an.childNodes[1]).nodeValue
        if key != "attributes":
            return_object[key] = value
    return return_object


def format_document(minidom_document):
    """
    return a python object that jinja2 can parse from a docutil document
    """
    return_object = {}
    root = minidom_document.asdom().childNodes[0]
    root_table = (root.getElementsByTagName("table")[0] if
        len(root.getElementsByTagName("table")) > 0 else None)
    if(root_table):
        parse_attribute_table(root_table, return_object)
    """for c in docutil_document.nodeList:
        if c.tagname == "table":
            parse_attribute_table(c, return_object)
        elif c.tagname == "section":
            pass
        else:
            raise Exception("Invalid format detected!")
        pass
    return {}"""
    return return_object


def render_cheatsheet(minidom_document, template_path):
    """
    Render a docutil document into a template
    """
    template = Template(open(template_path, "r+").read())
    return template.render(format_document(minidom_document))
