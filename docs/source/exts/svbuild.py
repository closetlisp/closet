"""
custom extension to add a custom .svelte pages output.

The build is done with `make svelte`, which invokes the custom svelte builder, which uses the svelte translator to convert sphinx rst nodes to svelte code


This code is based on the builtin Sphinx builders and writers.

main source example: https://github.com/sphinx-doc/sphinx/blob/master/sphinx/builders/html/__init__.py
revision eaebbec4d165efcb5048fc06431e3bf796c9d224 (Sep 1, 2025)

"""


# make type annotations not evaluate
# needed for circular definitions
from __future__ import annotations

# utils
from sphinx.locale import __
from sphinx.util import logging

# keep for later use
#from sphinx.highlighting import PygmentsBridge

# base classes
from sphinx.builders import Builder
from docutils.writers import Writer
from sphinx.util.docutils import SphinxTranslator

# type imports
from sphinx.application import Sphinx
from sphinx.util.typing import ExtensionMetadata
from docutils.nodes import document as Document


logger = logging.getLogger(__name__)


class SvelteTranslator(SphinxTranslator):
    """
    convert document nodes to svelte
    """
    builder: SvelteBuilder

    def __init__(self, document: Document, builder: SvelteBuilder):
        super().__init__(document, builder)

        self.parts = []


    # hooks to override in order to finish without errors and warnings
    def visit_Text(self, node):
        self.parts.append(node.astext())
    def depart_Text(self, node):
        pass
    def visit_title(self, node):
        pass
    def depart_title(self, node):
        pass
    def visit_paragraph(self, node):
        pass
    def depart_paragraph(self, node):
        pass
    def visit_reference(self, node):
        pass
    def depart_reference(self, node):
        pass
    def visit_target(self, node):
        pass
    def depart_target(self, node):
        pass
    def visit_list_item(self, node):
        pass
    def depart_list_item(self, node):
        pass
    def visit_bullet_list(self, node):
        pass
    def depart_bullet_list(self, node):
        pass
    def visit_compound(self, node):
        pass
    def depart_compound(self, node):
        pass
    def visit_section(self, node):
        pass
    def depart_section(self, node):
        pass
    def visit_document(self, node):
        pass
    def depart_document(self, node):
        self.body = '\n'.join(self.parts)
    def visit_literal(self, node):
        pass
    def depart_literal(self, node):
        pass
    def visit_literal_block(self, node):
        pass
    def depart_literal_block(self, node):
        pass
    def visit_comment(self, node):
        pass
    def depart_comment(self, node):
        pass
    def visit_colspec(self, node):
        pass
    def depart_colspec(self, node):
        pass
    def visit_entry(self, node):
        pass
    def depart_entry(self, node):
        pass
    def visit_row(self, node):
        pass
    def depart_row(self, node):
        pass
    def visit_thead(self, node):
        pass
    def depart_thead(self, node):
        pass
    def visit_tbody(self, node):
        pass
    def depart_tbody(self, node):
        pass
    def visit_tgroup(self, node):
        pass
    def depart_tgroup(self, node):
        pass
    def visit_table(self, node):
        pass
    def depart_table(self, node):
        pass



class SvelteBuilder(Builder):
    """
    builds .svelte SPA pages
    """
    name = "svelte"
    format = "svelte"
    epilog = "The .svelte files are in %(outdir)s"

    default_translator_class = SvelteTranslator

    def init(self):
        "hook called during __init__"
        pass

    def get_outdated_docs(self) -> Iterator[str]:
        """
        called during init

        source:
        https://github.com/sphinx-doc/sphinx/blob/master/sphinx/builders/text.py
        TextBuilder.get_outdated_doc

        should filter outdated files to override or delete them
        """
        # TODO: test and finish implementing
        # currently, regenerate everything every time
        for docname in self.env.found_docs:
            yield docname


    def write_doc(self, docname: str, doctree: Document):
        dest = self.outdir / docname / "+page.svelte"
        dest.parent.mkdir(parents=True, exist_ok=True)

        visitor = self.create_translator(doctree, self)
        assert isinstance(visitor, SvelteTranslator)
        doctree.walkabout(visitor)
        output = visitor.body
        dest.write_text(output)

    def get_target_uri(self, docname, typ: str | None = None):
        return ''

    def finish(self):
        """
        hook called after building everything
        """
        pass


def setup(app: Sphinx) -> ExtensionMetadata:
    app.add_builder(SvelteBuilder)

    return {
        'version': 'embedded',
        'parallel_read_safe': True,
        'parallel_write_safe': True,
    }

