Printing values
===============

Printing values

There are two main functions you can use to print values: ``(to-string)`` and ``(repr)``

``(to-string)`` is easy to understand: it converts a value to a string that can be printed: ::


    (to-string '(1 2 3))  # "(1 2 3)"
    (print (to-string "x"))  # "x"



``(repr)`` is similar to Python's repr(). It is used to generate a literal represental of a value that could be evaluated: ::


    (print (repr "x"))  # "\"x\""
