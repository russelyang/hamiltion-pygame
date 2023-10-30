# Week 2 summary

We introduce the data type used in the `lession-1/01.py`, start code is in `lesson-2.py`

## Tuple

A tuple consists of a number of values separated by commas

### display set_mode

```python
# set display mode
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
```

set_mode take a tuple to set the window hight and width 2.

### Fill the color

```python
# fill with black
display_surface.fill((0, 0, 0))
```

color is a tuple with 3 values, the sequence is (red, green , blue)

| color         | tuple |
| ------------- | ----- |
| (0,0,0)       | black |
| (255,255,255) | white |
| (255,0,0)     | red   |
| (0,255,0)     | green |
| (0,0,255)     | green |

## Boolean

Booleans represent one of two values: True or False. read more from https://www.w3schools.com/python/python_booleans.asp

## Number

There are three numeric types in Python:

- int
- float
- complex (we do not need know this one now)

read more from https://www.w3schools.com/python/python_numbers.asp

## String

Strings in python are surrounded by either single quotation marks, or double quotation marks.
read more from https://www.w3schools.com/python/python_strings.asp

## Homework

please type the code in lesson-2/02.py yourself and try it, we will draw a circle, and use keyboard A,S,D,W (this is a tuple) to move it.
