Expressions
===========

Expressions

Lisp code is entirely composed of expressions. This means every import, variable declaration, function definition, and if statement evaluates to a value.
Expressions are written using either axioms (simple elements, like value literals) or lists, which represent function calls.

.. .. highlight:: hy

Here are some examples of expressions that evaluate to true: ::

    # logic operators are written like function calls.
    # While this is confusing at first, this gives every construct the same syntax and helps to mainstream the structure of code
    (and (not (<= 1 2)) true)
    (= nil (define x 5))
    (if (= x 5)  # if is also written with parenthesis
      true
      false)
    (= if if)  # if is a first-class citizen
    (= () nil)  # nil is the empty list
    (= 'x (quote x))  # ' is just a shortcut for (quote)
    (or true (do-heavy-stuff))  # or does not evaluate beyond the first true value
    # if is a function, although it works differently and can choose how to evaluate its arguments:
    (is-instance if function)
    (= -14 (+ 1 2 (- 3 (* 4 5))))
