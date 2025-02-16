# Wynn: A new way to code
A programming language with the simplicity of python with the functionality of a language like C. Developer-friendly and easily readable! \
This minimalistic language encourages creativity and out-of-the-box thinking, with barebone functions and uncomplicated syntax! \
Below is a guide of keywords and functions to use in the language.

# Structure
Wynn is an interpreted, high-level, dynamically-typed, general purpose programming language. Similar to Python, it uses indentation instead of brackets. It can be used for a wide variety of things, but is typically aimed towards statistical analysis, quick coding (prototyping), and simple app / game development. 

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

## enum
Declare an enumeration [group] of constants. Can be accessed using the format `[NAME].[VARIABLE]`.
```cpp
enum Days{
    SUNDAY, MONDAY, TUESDAY, WEDNESDAY, THURSDAY, FRIDAY, SATURDAY
};
println(Days.MONDAY);
```

# Advanced Keywords

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
