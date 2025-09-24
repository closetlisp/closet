Strings
=======

.. highlight:: hy

Antilisp strings are immutable. They can be processed with the following functions: ::

    (+ "a" "b")  ; "ab"
    (split "abc" "b")  ; ("a" "c")
    (join '("a" "b" "c") " ")  ; "a b c"
    (substring "string" 1 2)  ; "t"
    (at "string" 2)  ; r

    (to-string 'symbol) ; "symbol"
    (length "string")  ; 6
