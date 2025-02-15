# Wynn: A new way to code
A programming language with the simplicity of python with the functionality of a language like C. Developer-friendly and easily readable! \
This minimalistic language encourages creativity and out-of-the-box thinking, with barebone functions and uncomplicated syntax! \
Below is a guide of keywords and functions to use in the language.

# Structure
Wynn is an interpreted, high-level, dynamically-typed, general purpose programming language. Similar to Python, it uses indentation instead of brackets. It can be used for a wide variety of things, but is typically aimed towards statistical analysis, quick coding (prototyping), and simple app / game development. 

# Keywords

## new
Use the `new` keyword to define a variable. It is similar to `let` in Rust, and this allows for dynamic typing.
```cpp
new Number = 4;
new Text = "Wynn is cool";
new done = False;
```

## imm
Use the `imm` keyword paired with `new` to define a **constant variable**. It is similar to `const` in C/C++.
```cpp
new imm PI = 3.14159;
new imm PI = 1; (Throws ReferenceError: Cannot change value of read-only variable 'PI')
```

## if / else if / else
Use the `if` keyword to run the next pieces of code only if some condition is met. These pieces of code are set off by indentation. \
Use the `else if` keyword to run the next pieces of code only if the last condition was not met, and the following condition is met. These pieces of code are set off by indentation.\
Use the `else` keyword to run the next pieces of code only if none of the above conditions were met (in the same indentation level). These pieces of code are set off by indentation.
```cpp
new name = "Sam";
if (name=="John");
  println("That's my friend!");
else if (name == "Sam");
  println("That's my dad.");
else;
  println("I don't know who you are.");
```

## while
Use the `while` keyword to run the next pieces of code while some condition is met. The code will loop back to the start of the indent until the condition is no longer met. These pieces of code are set off by indentation. 
```cpp
new i = 0;
while (i<100);
  println(fmt("Wynn is the best", "\n"));
  new i+=1;
```
That piece of code will print "Wynn is the best" to the terminal 100 times. Perhaps... Wynn *is* the best? I don't know, but the terminal seems to think so.

## using
Use the `using` keyword to define a macro substitution. It is an alternative way to define a immutable variable by the preprocessor.
```cpp
using World :: "Hello world!";
println(World);
```
That outputs the following:
```
Hello world!
```

# Functions
## println()
Prints something to the standard output stream.
```cpp
println("Hello world");
```
That outputs the following:
```
Hello world
```
