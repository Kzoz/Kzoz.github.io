/*
Review
You’ve learned quite a bit! You now know a bit about how scope works for functions and files, 
as well as how to make functions more flexible for different use cases:

    ‡Scope is the region of code that has access to an element.
        ‡Globally scoped variables are accessible everywhere.
        ‡A variable created inside a function has local scope and can’t be accessed outside the function.
    ‡C++ functions are usually split to make code more modular:
        ‡The declaration in a header file.
        ‡The definition in another .cpp file.

    ‡Programs with multiple .cpp files need to be linked at compile time:

g++ main.cpp fns.cpp

    ‡Header files must be included in the file with main():

#include "fns.hpp"

You can define a function inline using the inline keyword, which may or may not improve execution speed.

Default arguments can be added to function declarations so that you can call 
the function without including those arguments.

You can overload C++ functions so that they handle different types of input and return different types.

A function template enables a function to behave the same with different types of parameters.
*/