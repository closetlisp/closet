Procedural programming
======================

Local variables: ::

    (let x 5
      (print x))

    (let* (x 5
           y (+ x 1))
      (print y))

For loops work with generators like ``(range)``: ::

    (for i (range 10)
      (print i))

Generators are functions which can be called repeatedly until they return nil. The values are wrapped in cons cells to allow generators to generate nil values: ::


    (let generator (range 1)
      (print (generator))   # (0)
      (print (generator)))  # nil



The ``(iter)`` generic can be implemented to create generators that iterate over values: ::

    (for x (iter '(1 2 3))
      (print x))

Code blocks can be written as a single expression using ``(begin)``: ::

    (begin
      (print "message 1")
      (print "message 2"))


``(when)`` and ``(cond)`` can also be used for conditionals: ::


    (when (> x 4)
      (print "x > 4"))

    (cond
      (> x 3) (print "> 3")
      (< x 2) (print "< 2")
      true (print "x is 2 or 3"))
