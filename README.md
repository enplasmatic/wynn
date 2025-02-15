# Wynn
A programming language with the simplicity of python with the functionality of a language like C. Developer-friendly and easily readable! 

# Keywords

## new
Use the `new` keyword to define a variable. It is similar to `let` in Rust, and this allows for dynamic typing.
```cpp
new Number = 4;
new Text = "Wynn is cool";
new done = False;
```


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
