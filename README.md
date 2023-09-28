
**Exercise 1: Implementing a Common Character Class**

In our game, both the player and the enemy share some common attributes, namely `health` and `strength`. These commonalities can be abstracted into a more generic class that other classes can inherit from.

1. **Task**: 
   - Create a class named `Character`.
   - This class should have two attributes: `health` and `strength`.
   - Provide an `__init__` method to initialize these attributes.
   - Implement any other methods you believe might be useful for both `Player` and `Enemy`.

2. **Further Implementation**:
   - Modify the `Player` and `Enemy` classes to inherit from the `Character` class.
   - Adjust the initialization methods (`__init__`) of `Player` and `Enemy` to make use of the attributes from the `Character` class.

---

**Exercise 2: Implementing a Common Item Class**

The items `Food`, `Medicine`, and `Weapon` have the shared attribute of `strength`. To avoid redundancy and make our code more organized, let's have them inherit from a common class.

1. **Task**: 
   - Create a class named `Item`.
   - This class should have an attribute named `strength`.
   - Provide an `__init__` method to initialize this attribute.
   - Implement any other methods that you think might be generally applicable to all items.

2. **Further Implementation**:
   - Modify the `Food`, `Medicine`, and `Weapon` classes to inherit from the `Item` class.
   - Adjust the initialization methods (`__init__`) of `Food`, `Medicine`, and `Weapon` to make use of the `strength` attribute from the `Item` class.

