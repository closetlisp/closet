List Processing
===============


Lists (singly linked lists) are the main data structure used to represent code in Lisp. There are many ways to create lists: ::


    (cons 1 nil)  # concatenate to the empty list
    (list 1)  # use the list constructor
    '(1)  # quote code



Lists are immutable. In order to create modify a list, you have to create a new one.
Here are the main operations used to manipulate lists: ::


    (car '(1 2 3)) # 1
    (cdr '(1 2 3))) # (2 3)
    (map (fn (x) (+ x 1))  # (2 3 4)
        '(1 2 3))
    (filter (fn (x) false)  # ()
        '(1 2 3))
    (reduce + '(1 2 3))  # 6
    (reverse '(1 2 3))  # (3 2 1)
    (is-list '(1 2 3))  # true


Note: list processing is often used in metaprogramming
