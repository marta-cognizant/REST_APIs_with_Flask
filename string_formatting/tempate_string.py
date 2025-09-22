name = "Bob"
greetings = "Hello, {}"
with_name = greetings.format(name)
print(with_name)  # Output: Hello, Bob
with_name = greetings.format("Rolf")
print(with_name)  # Output: Hello, Rolf