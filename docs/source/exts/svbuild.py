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


class SvelteWriter(Writer):
    """
    produce a svelte code output
    """
    def __init__(self, builder):
        super().__init__()
        self.builder = builder
        print("writer init:")
        print(builder)

    def translate(self) -> None:
        # TODO: implement
        # https://github.com/sphinx-doc/sphinx/blob/master/sphinx/writers/text.py (TextWriter.translate)
        print("writer translate:")
        self.output = "svelte result"


class SvelteTranslator(SphinxTranslator):
    """
    convert document nodes to svelte
    """
    builder: SvelteBuilder

    def __init__(self, document: Document, builder: SvelteBuilder):
        super().__init__(document, builder)
        print("translator init:")
        print(document)
        print(builder)


class SvelteBuilder(Builder):
    """
    builds .svelte SPA pages
    """
    name = "svelte"
    format = "svelte"
    epilog = "The .svelte files are in %(outdir)s"

    default_translator_class = SvelteTranslator

    def init(self):
        print("builder init:")

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
        dest = self.outdir / (docname + ".svelte")
        dest.parent.mkdir(parents=True, exist_ok=True)
        logger.warning('did not process %s', dest)

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

