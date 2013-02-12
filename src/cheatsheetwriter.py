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

    default_stylesheet = \
        "../skeleton/stylesheets/base.css," + \
        "../skeleton/stylesheets/skeleton.css," + \
        "../skeleton/stylesheets/layout.css," + \
        "../stylesheets/cheatsheets.css"

    default_stylesheet_path = [utils.relative_path(
        os.path.join(os.getcwd(), 'dummy'),
        os.path.join(os.path.dirname(__file__), stylesheet)) for stylesheet in default_stylesheet.split(",")]

    settings_spec = (
        'HTML-Specific Options',
        None,
        (('Specify the template file (UTF-8 encoded).  Default is "%s".'
          % default_template_path,
          ['--template'],
          {'default': default_template_path, 'metavar': '<file>'}),
        ('Specify comma separated list of stylesheet URLs. '
          'Overrides previous --stylesheet and --stylesheet-path settings.',
          ['--stylesheet'],
          {'metavar': '<URL>', 'overrides': 'stylesheet_path',
           'validator': frontend.validate_comma_separated_list}),
         ('Specify comma separated list of stylesheet paths. '
          'With --link-stylesheet, '
          'the path is rewritten relative to the output HTML file. '
          'Default: "%s"' % default_stylesheet_path,
          ['--stylesheet-path'],
          {'metavar': '<file>', 'overrides': 'stylesheet',
           'validator': frontend.validate_comma_separated_list,
           'default': default_stylesheet_path}),
         ('Embed the stylesheet(s) in the output HTML file.  The stylesheet '
          'files must be accessible during processing. This is the default.',
          ['--embed-stylesheet'],
          {'default': 1, 'action': 'store_true',
           'validator': frontend.validate_boolean}),
         ('Link to the stylesheet(s) in the output HTML file. '
          'Default: embed stylesheets.',
          ['--link-stylesheet'],
          {'dest': 'embed_stylesheet', 'action': 'store_false'}),
         ('Specify the initial header level.  Default is 1 for "<h1>".  '
          'Does not affect document title & subtitle (see --no-doc-title).',
          ['--initial-header-level'],
          {'choices': '1 2 3 4 5 6'.split(), 'default': '1',
           'metavar': '<level>'}),
         ('Specify the maximum width (in characters) for one-column field '
          'names.  Longer field names will span an entire row of the table '
          'used to render the field list.  Default is 14 characters.  '
          'Use 0 for "no limit".',
          ['--field-name-limit'],
          {'default': 14, 'metavar': '<level>',
           'validator': frontend.validate_nonnegative_int}),
         ('Specify the maximum width (in characters) for options in option '
          'lists.  Longer options will span an entire row of the table used '
          'to render the option list.  Default is 14 characters.  '
          'Use 0 for "no limit".',
          ['--option-limit'],
          {'default': 14, 'metavar': '<level>',
           'validator': frontend.validate_nonnegative_int}),
         ('Format for footnote references: one of "superscript" or '
          '"brackets".  Default is "brackets".',
          ['--footnote-references'],
          {'choices': ['superscript', 'brackets'], 'default': 'brackets',
           'metavar': '<format>',
           'overrides': 'trim_footnote_reference_space'}),
         ('Format for block quote attributions: one of "dash" (em-dash '
          'prefix), "parentheses"/"parens", or "none".  Default is "dash".',
          ['--attribution'],
          {'choices': ['dash', 'parentheses', 'parens', 'none'],
           'default': 'dash', 'metavar': '<format>'}),
         ('Remove extra vertical whitespace between items of "simple" bullet '
          'lists and enumerated lists.  Default: enabled.',
          ['--compact-lists'],
          {'default': 1, 'action': 'store_true',
           'validator': frontend.validate_boolean}),
         ('Disable compact simple bullet and enumerated lists.',
          ['--no-compact-lists'],
          {'dest': 'compact_lists', 'action': 'store_false'}),
         ('Remove extra vertical whitespace between items of simple field '
          'lists.  Default: enabled.',
          ['--compact-field-lists'],
          {'default': 1, 'action': 'store_true',
           'validator': frontend.validate_boolean}),
         ('Disable compact simple field lists.',
          ['--no-compact-field-lists'],
          {'dest': 'compact_field_lists', 'action': 'store_false'}),
         ('Added to standard table classes. '
          'Defined styles: "borderless". Default: ""',
          ['--table-style'],
          {'default': ''}),
         ('Math output format, one of "MathML", "HTML", "MathJax" '
          'or "LaTeX". Default: "MathJax"',
          ['--math-output'],
          {'default': 'MathJax'}),
         ('Omit the XML declaration.  Use with caution.',
          ['--no-xml-declaration'],
          {'dest': 'xml_declaration', 'default': 1, 'action': 'store_false',
           'validator': frontend.validate_boolean}),
         ('Obfuscate email addresses to confuse harvesters while still '
          'keeping email links usable with standards-compliant browsers.',
          ['--cloak-email-addresses'],
          {'action': 'store_true', 'validator': frontend.validate_boolean}),))


    def __init__(self):
        html4css1.Writer.__init__(self)
        self.translator_class = CheatsheetHTMLTranslator


class CheatsheetHTMLTranslator(html4css1.HTMLTranslator):

    doctype = "<!DOCTYPE html>"

    meta_viewport = \
        '<meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1">\n'

    def __init__(self, document):
        html4css1.HTMLTranslator.__init__(self, document)
        self.meta.append(self.meta_viewport)
        print utils.get_stylesheet_list(self.settings)
        pass

    def visit_start_of_file(self, node):
        # only occurs in the single-file builder
        self.body.append('<span id="document-%s"></span>' % node['docname'])

    def visit_title(self, node):
        if isinstance(node.parent, nodes.document):
            self.body.append(self.starttag(node, 'div', '', CLASS='sixteen columns'))
            self.body.append("<h1>")
            #self.body.append(self.starttag(node, 'h1', '', CLASS='title'))
            self.in_document_title = len(self.body)
            self.context.append("</h1><hr/></div>\n")
        elif isinstance(node.parent, nodes.section):
            self.body.append("<h2>")
            #self.body.append(self.starttag(node, 'h1', '', CLASS='title'))
            self.in_document_title = len(self.body)
            self.context.append("</h2>\n")
        else:
            html4css1.HTMLTranslator.visit_title(self, node)

    def visit_subtitle(self, node):
        if isinstance(node.parent, nodes.document):
            self.body.append("<!--")
            self.context.append("-->")
            pass
        else:
            html4css1.HTMLTranslator.visit_subtitle(self, node)

    def visit_section(self, node):
        self.section_level += 1
        self.body.append(
            self.starttag(node, 'div', CLASS='section one-third column'))

    def depart_start_of_file(self, node):
        pass

    def depart_document(self, node):
        self.head_prefix.extend([self.doctype,
                                 self.head_prefix_template %
                                 {'lang': self.settings.language_code}])
        self.html_prolog.append(self.doctype)
        self.meta.insert(0, self.content_type % self.settings.output_encoding)
        self.head.insert(0, self.content_type % self.settings.output_encoding)
        if self.math_header:
            self.head.append(self.math_header)
        # skip content-type meta tag with interpolated charset value:
        self.html_head.extend(self.head[1:])
        self.body_prefix.append(self.starttag(node, 'div', CLASS='container'))
        self.body_suffix.insert(0, '</div>\n')
        self.fragment.extend(self.body) # self.fragment is the "naked" body
        self.html_body.extend(self.body_prefix[1:] + self.body_pre_docinfo
                              + self.docinfo + self.body
                              + self.body_suffix[:-1])
        assert not self.context, 'len(context) = %s' % len(self.context)
