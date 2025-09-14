import hashlib

# Define three different hashers, each with its own use case.
# This is done because the update() function appends the
# input text to the end of the original string.
hasherA = hashlib.sha256()
hasherB = hashlib.sha256()
hasherC = hashlib.sha256()

# Display the input and output of each hasher. The
# text of each input has capitalization variations.
print("Input: Hello World")
hasherA.update(b'Hello World')
print(hasherA.hexdigest() + "\n")

print("Input: HELLO WORLD")
hasherB.update(b'HELLO WORLD')
print(hasherB.hexdigest() + "\n")

print("Input: hElLo WoRlD")
hasherC.update(b'hElLo WoRlD')
print(hasherC.hexdigest())
