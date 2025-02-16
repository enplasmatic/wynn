# Wynn: A new way to code
A programming language with the simplicity of Python and the functionality of a language like C.** Developer-friendly** and **easily readable**! \
This minimalistic language encourages **creativity** and out-of-the-box thinking, with **bare-bone** functions and uncomplicated syntax! \
Below is a guide of keywords and functions to use in the language.

# Structure
Wynn is an **interpreted**, **high-level**, dynamically-typed, **general purpose** programming language. Similar to Python, it uses indentation instead of brackets. It can be used for a wide variety of things, but is typically aimed towards statistical analysis, quick coding (prototyping), and simple app / game development. 

# Basic Keywords

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

## for
Use the `for` keyword to define a for loop in the following format: `for(C1, C2, C3);`. The line of code `C1` will execute once at the start. The line of code `C2` is the condition that will keep the loop going. Once that condition is false, the loop will end. The line of code `C3` will execute once at the end of each iteration of the loop.
```cpp
for(new i = 0, i<100, new i+=1);
  println(fmt("Wynn is the best", "\n"));
```
This will again print "Wynn is the best" 100 times, but the code is shorter now.

## macro
Use the `macro` keyword to define a macro. The declaration of a macro is formatted in the following way: \
`macro NAME(new ARG1, new ARG2, new imm WHY_NOT, ...); `\
A macro is a function with a void return type (returns nothing). Wynn is a language that stands against recursion (boo!!!) so it does not support it. 
```cpp
macro PrintNewline(new content);
  println(fmt(content, "\n"));
```

## call
Use the `call` keyword to simply call a macro. Using the example from the `macro` keyword explanation:
```cpp
call PrintNewline("Who hates recursion? I hate recursion!");
```

## and / or / not
These all correspond to their logical operator equivalent. If you do not know what a logical operator is, see https://www.geeksforgeeks.org/logical-operators-in-programming/ 
```cpp
println(fmt(1 and 1, '\n', (not 0) or 1));
```

## in/is
The keyword `in` is used for the condition checking if a value is inside a container. The keyword `is` is used to check if something points to the same location in memory as another value. These have the exact same functionality as they do in Python.
```py
println(3 in [3,4,5]);
new third = 3;
new three = 3;
println("\n");
println(third is three);
```

## switch / case / else
These keywords are used for switch statements. They are pretty self-explanatory with a few examples:
```cpp
new imm x = 3;
switch x;
  case 3;
    println("X is 3");
  case 99;
    println("X is 99");
  else;
    println("Bruh, x is not 3 or 100");

```
This is literally equivalent to:
```cpp
new imm x = 3;
if (x == 3);
    println("X is 3");
else if (x == 99);
    println("X is 99");
else;
    println("Bruh, x is not 3 or 100");
```
Switch statements are just faster and easier to write, so they're preferred over if-statements.

## setat / enter / free 
These are label keywords, similar to `goto` in C/C++. `setat` defines a new label, `enter` jumps to that label, and `free` removes the label from the program.

**ALWAYS FREE YOUR LABELS WHEN YOU'RE DONE USING THEM!**
Not freeing your labels will more often than not lead to undefined behavior.

```cpp
new i = 0;
while True;
    if (i==100);
        enter END;
    println(fmt(i, '\n'));
    new i += 1;
setat END;
free END;
```

## include
The keyword `include` tells the interpreter to add all of the contents of a specified file into the current running file before execution.
```py
(file1.w)
new Number = 100;
```
```lua
(file2.w)
include "file1.w";
println(Number);
```

## enum
Declare an enumeration [group] of integer constants. You can define them to certain integer values, or leave them blank for their values to default to their indices. If you make the first value `1`, for example, all the other values will be `2, 3, 4...` and so on if not explicitly declared. Enum constants be accessed using the format `[NAME].[VARIABLE]`.
```cpp
enum Days{
    SUNDAY, MONDAY, TUESDAY, WEDNESDAY, THURSDAY, FRIDAY, SATURDAY
};
println(Days.MONDAY);
```
That outputs the following:
```
1
```

## struct
Declare a structure of values that groups together variables of potentially different types under a single name. You can declare an instance of a `struct` using the following format: `new <StructName> VARIABLE_NAME = [arg1, arg2... argN]` Structs are useful for template variables that can be copied and declared under similar circumstances but different values. Below is an example of the modifiable values of a `struct`.
```cpp
struct Point{
    new x, new y
};
new <Point> origin = [0,0];
new origin.x = 4;
new origin.y = -104;
println(fmt(origin.x, ', ', origin.y));
```
That outputs the following:
```
4, -104
```


# Advanced Keywords

## using
Use the `using` keyword to define a macro substitution. It is an alternative way to define a immutable variable by the preprocessor. This keyword requires the following format: `using NEW_NAME :: OLD_NAME` The new name of the macro is on the left side of the double colon, while the old name (name to replace with) is on the right side of the double colon.
```cpp
using World :: "Hello world!";
println(World);
```
That outputs the following:
```
Hello world!
```

## define
Alternatively, you can use the `define` keyword to define a **strict** macro substitution. This will literally replace all instances of a variable "three" with "3" and is highly unsafe. This keyword requires the following format: `define NEW_NAME :: OLD_NAME` The new name of the macro is on the left side of the double colon, while the old name (name to replace with) is on the right side of the double colon.
> It is not recommended to use this unless you know what you're doing, because it can seriously mess up code. 
```cpp
define three :: 3;
println(threethree);
```
That outputs the following:
```
33
```

## static / end static
A static window in a Wynn code file is a piece of code that can only execute when that file is run. When using `include "FILENAME.w"` anything encapsulated inside a static window will not be added to the file. The `static` keyword opens a static window, and the `end static` keyword closes the most recent static window.
```cpp
(file1.w)
static;
new Number = 100;
end static;
```
```lua
(file2.w, this will throw an error)
include "file1.w";
println(Number);
```

## expand / expansion
An expanded function is a function that expands inline wherever it is declared, similar to `inline` in C/C++. These are one line statements that can return a simple type (`int`, `boolean`, `string`, `float`). Create an expansion by using `expand NAME(args) -> expression`. It is important to remember that the `new` keyword is restricted inside of the argument declaration of the expansion.\
`expand NAME(new args) -> return expression` **Wrong**! \
`expand NAME(args) -> expression` **Correct**! \

Declare a variable that is created via expansion using `new expansion NAME = EXPANDED_FUNC_NAME(ARGS)`. Below is an example of the expand / expansion keywords in action.
```cpp
expand square(x) -> x*x;
new expansion f = square(5);
println(f);
```
## throw
Use `throw` to throw an internal error in the system and stop execution of the code. You can put a string next to it so that you can log your error message.
```cpp
throw "Oh no!";
```
That outputs the following:
```
 -- internal error thrown --
Callback: Oh no!
```

## break

> This keyword has been deprecated and is only here for my historical / completion purposes.

This does the same thing as the `break` keyword in other languages too; it simply breaks out of a loop. ***This keyword has been deprecated*** and is only still a keyword so that other older programs using it will not lose functionality. However, using it *may cause undefined behavior*, so use it at your own risk. 
```cpp
for(new i = 0, i<100, new i+=1);
    println(fmt(i, '\n'));
    if (i>=50);
        break;
```
That outputs the following:
```
1
2
3
...
48
49
50
```
## ptr

> This keyword has been deprecated and is only here for my historical / completion purposes.

**Never** use this. I am only putting this here so that it is recognized as a keyword. This is only ever used by the interpreter and is not meant for you to use. 

> If you must know, it jumps to a line with the specified index [0-indexed]. It's very hard to pull off using this correctly, so I will not provide an example for this keyword.

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
