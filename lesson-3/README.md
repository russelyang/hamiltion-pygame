# Week 3 Summary

## Tuple

### Tuple can access by index

For exmaple

```python
name = ("John", "Smith")
print(name[0]) # "John"
print(name[1]) # "Smith"
```

### Check if something in the tuple

we can use `in` to check if an item in the tuple

```python
name = ("John", "Smith")
print("John" in name) # True
print("john" in name) # False
```

Please pay attension to second print, Python is case sensitive, upper caes `John` and lower case `john` is different.

### Display image using pygame

The reason why the sample did not work is that pygame can not load `svg` file directly. it supports `jpg`,`gif`, `png`, but `svg` require extra steps.

`03.py` is showing the image.

### Homework

Search the internet and see how we can use pygame show `svg` file
