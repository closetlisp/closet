Closet standard library
===========================


This part focuses on standard Closet libraries.
Since Closet is a code generation language, Closet libraries are focused on code generation in specific languages rather than implementing features in Closet directly.

Due to the way the Closet interpreter is built, these libraries can either be imported or directly built into the interpreter.
Embedding libraries in the interpreter gives a startup performance boost because the libraries don't have to be executed. However, to do this you will need to compile the interpreter yourself.


.. toctree::
   :maxdepth: 2
   :caption: Contents:

   lib/config
