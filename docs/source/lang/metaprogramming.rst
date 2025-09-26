Metaprogramming
===============

.. highlight:: hy

You can parse Lisp values with the ``(read)`` function: ::

    (read (repr '(1 2 3)))  # (1 2 3)

Since Lisp code is written using builtin data structures, you can also generate and execute code dynamically: ::

    (list 'print 5)  ; same result as '(print 5)
    (define x '(1 2 3))
    (define f print)
    (eval '(f x) current-scope)  ; the scope in which to run the code is an explicit parameter

Note: The ``current-scope`` special variable will be phased out in future versions

In order to fill templates with dynamic values, you can use ` ``(quasiquote)``, , ``(unquote)`` and ,@ ``(unquote-splicing)``: ::

    `(f x)  ; same as '(f x)
    (define x (heavy-computations))
    `(f ,x)  ; replace x with its value
    (define y '(1 2 3))
    `(f ,@y)  ; returns (f 1 2 3)

Together, these features are used to write templated code generators at compile-time.
In Lisp, we use macros to define functions that run at compile-time and process code before its execution.
Here is an example: ::

    (defmacro (let name value . body)
      `((fn (,name) ,@body) ,value))

This code defines a ``(let)`` macro, which simply returns a block of code that happens to be an IIFE.
Once this macro is defined, you can write: ::

    (let x 5
      (print x))

This code will then be transformed into: ::

    ((fn (x) (print x)) 5)

In javascript, the equivalent code would be::

    ((x) => { console.log(x) })(5)

With this simple example, you can see how simple it is to bootstrap new syntaxes and abstractions, or just syntax sugar.
There are many examples of Lisp macros being used to do things that would usually not be possible in other languages, like bootstrapping OOP or compiling user-written regexes to machine code.

Note: while writing macros, you may encounter a situation where you need to create a variable in the resulting runtime code. To avoid conflict with variables used by the programmer, you can use ``(gensym)`` to create unique symbols that do not conflict with any user-defined variables.
