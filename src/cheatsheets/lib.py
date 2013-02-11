"""
Library file for cheatsheets
"""
from docutils.frontend import OptionParser
from docutils.parsers.rst import Parser
from docutils.utils import new_document

from jinja2 import Template

example_cheatsheet_object = {
    "title": "Unix Tips and Tricks",
    "description": "tips, tricks, and useful commands for unix",
    "author": "Yusuke Tsutsumi",
    "sections": [
        {"title": "Useful commands",
         "parts": [
           {"type": "list",
             "rows": [
               "row": "* $ sed -i s/SEARCH_PATTERN/REPLACE_PATTERN/g FILE_NAME: replace SEARCH_PATTERN with REPLACE_PATTERN is FILE_NAME"
           ]}
         ]
        }
    ]
}


def generate_page(source_path, template_path, output_path):
    """
    Writes a page with the source rest file source_path, using the
    template template_path, and outputs it to output_path.
    """
    f = open(source_path, "r+")
    settings = OptionParser(components=(Parser,)).get_default_values()
    # generates a blank document
    document = new_document(f.name, settings)
    # build document with output from parser.
    Parser().parse(f.read(), document)
    output = render_cheatsheet(document, template_path)
    open(output_path, "w+").write(output.encode('utf-8'))


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
    """
    Parses the attribute table stored in the reST file
    """
    attribute_nodes = table_node.getElementsByTagName("row")
    for an in attribute_nodes:
        key = find_text_node(an.childNodes[0]).nodeValue.lower()
        value = find_text_node(an.childNodes[1]).nodeValue
        if key != "attributes":
            return_object[key] = value
    return return_object


def build_cheatsheet_object(minidom_element, return_object):
    """ builds out a return_object recursively for the template """
    if minidom_element.tagName == 'section':
        if 'sections' not in return_object:
            return_object['sections'] = []
        section_dict = {}
        for
        build_cheatsheet_object(


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
    import pdb; pdb.set_trace()
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
    template = Template(open(template_path, "r+").read().decode('utf8'))
    return template.render(format_document(minidom_document))
