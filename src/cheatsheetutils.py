# Author: yusuket
"""
A docutils writer to write to a cheatsheet html file
"""

__docformat__ = 'reStructuredText'

import docutils
from docutils import nodes, writers
from docutils.writers import html4css1


class CheatsheetHTMLTranslator(html4css1.HTMLTranslator):
    """
    """
    pass


class CheatsheetWriter(html4css1.Writer):
    pass

    def __init__(self):
        html4css1.Writer.__init__(self)
        self.translator_class = CheatsheetWriter
