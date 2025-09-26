Object oriented programming
===========================

OOP in Antilisp relies on two independant abstractions: generics and classes

Generics are polymorphic functions with runtime multiple dispatch over the types of their arguments.
The dispatched definitions of a generic are called methods.

Classes allow the user to define their own types and inherit methods and attributes defined on parent classes.

Generics
--------

Generics are defined with ``(defgeneric)``, and implemented with ``(defmethod)``: ::

    (defgeneric (to-list x))

    # default implementation: raise an error
    (defmethod (to-list x)
      (error "undefined-method"
             (+ "to-list is not defined for " (repr x))))

    # define to-list for strings
    # the last definition has higher priority over the previous ones
    (defmethod (to-list (x string))
      # convert the string to a list of characters
      # ...
      '())



Methods are stored in the method-store global dictionary.

Classes
-------

Antilisp provides primitive OOP constructs to manipulate objects: ::

    (make-class parent-classes ...attributes)  # create and return a class
    (make-instance class)  # create and return an instance of class
    (get-attr object 'attribute)
    (set-attr object 'attribute value)
    (is-instance object class)

    # reflection
    (is-subclass class-1 class-2)
    (get-class-attributes class)
    (get-class-env class)
    (get-type object)

However, the recommended way of using objects is with the ``(defclass)`` macro: ::

    ; the defclass macro automatically defines a constructor (make-vector), a type predicate (is-vector) and a generic type cast (to-vector)
    (defclass vector ()
      "a 2D vector class"
      x y)

    (let v (make-vector 1 2)
      (set (x v) 3)
      (print (x v))) ; prints 3

    (defmethod (length (x vector))
      ; TODO
      0)

    (defmethod (to-vector (x cell))
      (make-vector (car x) (car (cdr x))))

    (let v (make-vector 1 2)
      (print (is-vector v)))

    ; the class docstring is parsed by defclass to set the docstring
    (print (get-doc vector))  ; "a 2D vector class"

Generic casts and type predicates have been defined for builtin types as well: ::

    (to-symbol (+ "to-" (to-string 'vector)))  # 'to-vector
    (is-integer 0)
    (is-string "string")
    (is-symbol 'variable)


Many builtins, like ``(repr)``, ``(at)`` or ``(iter)``, are implemented as generics. A special case is ``(+)``, which can accept any number of arguments, and internally uses the ``(add)`` generic to add with type dispatch.
