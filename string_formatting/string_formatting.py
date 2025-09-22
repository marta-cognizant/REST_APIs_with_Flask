name = "Bob"
greeting = "Hello, Bob"
print(greeting)  # Output: Hello, Bob
name = "Rolf"
print(greeting)

name = "Bob"
# Using f-strings (formatted string literals)
greeting = f"Hello, {name}"
print(greeting)  # Output: Hello, Bob
print(f"Hello, {name}")  # Output: Hello, Bob
name = "Rolf"
print(greeting)  # Output: Hello, Bob
print(f"Hello, {name}")  # Output: Hello, Rolf