

    # Immutable data class

from dataclasses import dataclass

@dataclass(frozen=True)
class MyClass:
    value_one: str
    value_two: int

obj = MyClass("Another string", 20)
# The following line would raise a FrozenInstanceError
# obj.value_two = 10 
print(obj.value_one)
print(obj.value_two)

#The following code is commented out because it will raise an error.
# def some_func(new_val):
#     self.value_two = new_val

# some_func(100)
