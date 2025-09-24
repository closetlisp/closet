Builtin types
=============

Here is the list of types defined in Antilisp: ::

    type  ; the parent type of all builtin types
    integer
    string
    dictionary  ; string->value hashmaps
    env  ; represent variable scopes
    symbol  ; variable identifiers, found in code when metaprogramming
    cell  ; cons cells, used for lists
    bool  ; booleans
    function
    class



The empty list, nil, also has a type, but its type is not bound to a global name: ::

    (print (repr (get-type nil)))
    ; <type nil-type>

Dictionaries work like Python dicts, but they can only store string keys: ::

    (define d (dict))
    (set (at d "key") "value")
    (has-key d "key")  # true
    (at d "key")  # "value"
    (list-keys d)  # ("key")



Environments use symbols as keys, and can have a parent scope: ::

    (let x 4
    (print (repr current-scope)))

    (env
    (env ...)
    x 5)


Cons cells are used to build lists from the empty list nil: ::


    (cons 1 nil)  # (1)
    (list 1)  # also (1)



Note: In Lisp, ' (or (quote)) is used to use code as a value without executing it: ::


    (cons 1 nil)  # (1)
    '(print x) # (print x)



It is common practice to describe lists with it: ::


    '(1)  # also (1)
    (quote (1)) # (1) again



Symbols are variable identifiers. Since code is data, symbols are needed to represent variable names in code. However, you can also use them as a simple way to send and process messages without declaring an enumeration: ::


    (if (= direction 'left)
      'right
      'left)



Functions are also values and can be set with anonymous function objects: ::


    (define f (fn (x)
                (print x)))
    (f 5)  # prints 5
