"""
A cheatsheet builder.
Builds cheatsheets organizational structure and prints it.
"""
import argparse
import os
import re
import shutil
import sys

from docutils.core import publish_string
from docutils.frontend import OptionParser
from docutils.utils import new_document
from docutils.parsers.rst import Parser

from cheatsheets.lib import generate_page
from jinja2 import Template

description = \
"""
Generates A cheatsheet site from reStructuredText.
"""

rst_match = re.compile(".rst$")


parser = argparse.ArgumentParser(description=description)
parser.add_argument('file_path', type=str, nargs=1, help='the Filepath to generate templates in')
parser.add_argument('template_path', type=str, nargs=1, help='the template name to specialize against')
args = parser.parse_args()


def main():
    args = parser.parse_args()
    template_path = args.template_path[0]
    root_directory = os.path.abspath(args.file_path[0])
    for directory, dirnames, filenames in os.walk(root_directory):
        for f in filenames:
            if f.endswith('.rst'):
                generate_page(os.path.join(directory, f), template_path,
                              os.path.join(directory, rst_match.sub(".html", f)))
                print "%s, %s , %s" % (directory, dirnames, filenames)
    # generates a blank document
    #document = new_document(file_name.name, settings)
    # build document with output from parser.
    #Parser().parse(file_name.read(), document)
    #parsed_document = format_document(document)
    #output = render_cheatsheet(document, args.templateName[0])
    #import pdb; pdb.set_trace()

if __name__ == "__main__":
    main()
