Why Closet ?
=============



Closet is a Lisp dialect intended for code generation.

It is usually used by adding a build step that will run the Closet scripts to output code in the base language of your project (Java, Python, C,...).


There are two main reasons why doing this can be attractive.

The first one is when you have to follow platform requirements (JS, C, Swift, Java, Cobol,...). Closet lets you add abstractions on top of existing languages, such as static analysis steps or higher level abstractions like `Tagged unions <https://en.wikipedia.org/wiki/Tagged_union>`_ or pattern matching, without changeing the rest of your program. This leads to shorter, cleaner and more maintainable code.

The second reason is to extend the language to fit your specific use case: web components, banking, asynchronous protocols, serialization,... Most languages cannot support all of these areas, mainly because the language designer does not know about your problem, but also because it is not the job of the compiler writer to solve your problems.

Since the latter is very rare outside of Lisp-based languages, the paradigm of extending the language with metaprogramming is often misunderstood and difficult to explain in simple words. Hopefully, this documentation introduces metaprogramming in a way that's easy to understand.



However, please note that Closet is still in development.
While Closet can be used for throwaway generation, it is not recommended to base things on it in production (if you decide to do so, please contact us so we can assist you).
Furthermore, due to the lack of libraries, you will have to write your own AST modeling and code generation for languages which are not yet supported.

If you are still willing to learn Closet, this documentation will teach you everything you need to get started.
