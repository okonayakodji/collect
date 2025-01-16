# How to create a plugin?
1. Create a `.py` file in the `plugins` folder.
2. Import class `Plugin` from module `plugin`.
3. Create a plugin class inherited from the imported class (don't forget to add aliases).
4. Implement abstract methods in the class.
5. Add class import to `plugins/__init__.py`.
