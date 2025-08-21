# Closet Documentation

This directory contains the reStructuredText (.rst) sources of the Closet documentation.

The documentation is generated from .rst files using Sphinx.


## How to use

This documentation is updated at the same time as the code in this repository. This means each branch grows in sync with the documentation for that same version.

To view the documentation of a specific version, you can build the documentation from the same commit.

Note: Until Closet is fully migrated to this repository, the documentation refers to v0.12, the last version of Closet before the source code was published.

## Build

To build the documentation, you will need to install the dependencies with pip:
``` sh
git clone https://github.com/closetlisp/closet/
cd closet/docs
python -m venv .venv
.venv/bin/pip install -r requirements.txt
```

To build the documentation, you can either run sphinx manually, or enable the virtualenv and run make:
```sh
source .venv/bin/activate
make html
# or
.venv/bin/sphinx-build -b html source build/html
```

You can also build the documentation in other languages.
``` sh
make html
```

The output will be stored in `build/html`.

Sphinx supports other output formats. The list of builtin formats can be found in [the sphinx documentation](https://www.sphinx-doc.org/en/master/usage/builders/index.html).
Some of the most common ones are `html` (website), `singlehtml` (single web page) and `latex` (to generate a PDF document).


## Translation

The documentation can be translated in other languages using Sphinx.

To build the translation in an other language:

```sh
source .venv/bin/activate
make -e SPHINXOPTS="-D language=jp" html
# or
.venv/bin/sphinx-build -b html source build/html -D language=jp
```

The localization files (when they exist) are stored in `sources/locales/{lang}/LC_MESSAGES/*.po`.


If you want to translate the documentation in a new language, you can generate up to date translation files with:

``` sh
make gettext  # generate generic translation files in build/gettext/
sphinx-intl update -p build/gettext -l {language} # replace {language} with en, es, fr, it, jp, kr,...
```
You can then edit the translation files in `sources/locales/{lang}/LC_MESSAGES/*.po`.

