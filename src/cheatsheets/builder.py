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
first_directory = re.compile("[^\/]*\/")


parser = argparse.ArgumentParser(description=description)
parser.add_argument('file_path', type=str, nargs="?",
                    help='the Filepath to read cheatsheet rst files from', default="cheatsheets")
parser.add_argument('build_path', type=str, nargs="?",
                    help='the Filepath to generate templates in', default="build")
args = parser.parse_args()


def main():
    args = parser.parse_args()
    root_directory = args.file_path
    for directory, dirnames, filenames in os.walk(root_directory):
        for f in filenames:
            if f.endswith('.rst'):
                source_path = os.path.join(directory, f)
                build_path = os.path.join(args.build_path,
                                          first_directory.sub('', directory),
                                          rst_match.sub(".html", f))
                generate_page(source_path, build_path)
                print "wrote %s" % build_path

if __name__ == "__main__":
    main()
