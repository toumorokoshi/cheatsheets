"""
A cheatsheet builder.
Builds cheatsheets organizational structure and prints it.
"""
import argparse
import sys

from docutils.core import publish_string
from docutils.frontend import OptionParser
from docutils.utils import new_document
from docutils.parsers.rst import Parser

from cheatsheets.lib import format_document, render_cheatsheet
from jinja2 import Template

description = \
"""
Generates A cheatsheet site from reStructuredText.
"""


parser = argparse.ArgumentParser(description=description)
parser.add_argument('fileName', type=str, nargs=1, help='the Filename to pass in')
parser.add_argument('templateName', type=str, nargs=1, help='the template name to specialize against')
args = parser.parse_args()

def main():
    args = parser.parse_args()
    file_name = open(args.fileName[0], "r+")
    settings = OptionParser(components=(Parser,)).get_default_values()
    # generates a blank document
    document = new_document(file_name.name, settings)
    # build document with output from parser.
    Parser().parse(file_name.read(), document)
    parsed_document = format_document(document)
    output = render_cheatsheet(document, args.templateName[0])
    import pdb; pdb.set_trace()

if __name__ == "__main__":
    main()
