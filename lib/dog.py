#!/usr/bin/env python3
import types


class Dog:
    def bark(self):
        print("Woof!")


fido = Dog()

# Call the bark method on the fido instance
fido.bark()
# Output: Woof!

snoopy = Dog()

# Call the bark method on the snoopy instance
snoopy.bark()
# Output: Woof!

class Dog:
    def sit(self):
        print("The dog is sitting.")

# Create another instance of the Dog class
buddy = Dog()

# Call the sit method on the buddy instance
buddy.sit()
# Output: The dog is sitting.
