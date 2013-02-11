# $Id$
# Author: David Goodger <goodger@python.org>
# Copyright: This module has been placed in the public domain.

"""
PEP HTML Writer.
"""

__docformat__ = 'reStructuredText'


import sys
import os
import os.path
import codecs
import docutils
from docutils import frontend, nodes, utils, writers
from docutils.core import publish_string
from docutils.writers import html4css1


class CheatsheetWriter(html4css1.Writer):

    default_template = 'template.txt'

    default_template_path = utils.relative_path(
        os.path.join(os.getcwd(), 'dummy'),
        os.path.join(os.path.dirname(__file__), default_template))

    def __init__(self):
        html4css1.Writer.__init__(self)
        self.translator_class = CheatsheetHTMLTranslator


class CheatsheetHTMLTranslator(html4css1.HTMLTranslator):

    def visit_start_of_file(self, node):
        # only occurs in the single-file builder
        self.body.append('<span id="document-%s"></span>' % node['docname'])

    def visit_title(self, node):
        if isinstance(node.parent, nodes.document):
            self.body.append(self.starttag(node, 'h1', '', CLASS='title'))
            close_tag = '</h1>\n'
            self.in_document_title = len(self.body)
            self.context.append(close_tag)
        else:
            html4css1.HTMLTranslator.visit_title(self, node)

    def visit_section(self, node):
        self.section_level += 1
        self.body.append(
            self.starttag(node, 'div', CLASS='section one-third column'))

    def depart_start_of_file(self, node):
        pass
