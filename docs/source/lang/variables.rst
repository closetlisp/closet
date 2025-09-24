Variables
=========

Global variables can be defined with ``(define)``: ::

    (define x 5)

Functions can also be defined that way, but you can also use the ``(def)`` macro: ::

    (define f
      (fn (x)
        x))

    (def (f x)
      x)


``(define)`` always defines things in the global environment.
To define local variables, you can use ``(let)``: ::

    (let x (get-value)
      (print x))

Once defined, variables can be modified with the low level ``(set-symbol)``, or the ``(set)`` macro: ::

    (let x (get-value)
      (set x (get-other-value))
      (print x))

    (define a-list '())
    (set-symbol 'a-list (cons 5 a-list))

The ``(set)`` macro can also be used to modify properties: ::

    (define d (dict))
    (set (at d "key") "value")
    (print (at d "key"))
    ; value

Internally, ``(set)`` rewrites ``(set (f ...) v)`` forms to ``(g ... v)``, where g is a pre-defined setter in the global setter-store dictionary.
In this case, ``'at`` is associated with ``'set-at`` in the dictionary, so ``(set)`` will rewrite ``(set (at d "key") value)`` to ``(set-at d "key")``.

Note: the ``(unset)`` function can be used to remove global definitions. However, using it is not recommended as it can break things that depend on the definitions you remove.
