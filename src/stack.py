
# Stack → LIFO: Last in, first out

stack = []
word = "IA"

# Push: add each letter to the stack
for letter in word:
    stack.append(letter)

# Pop: remove letters to reverse the word
reversed_word = ""

while stack:
    reversed_word += stack.pop()

print(f"Reversed word: {reversed_word}")
