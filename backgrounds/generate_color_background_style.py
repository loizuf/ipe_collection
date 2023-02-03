import os
import sys

color = input("Enter the color (it must be available in the ipe file you are using this background in): ")
x_start = input("Enter the low x-coordinate: ")
y_start = input("Enter the low y-coordinate: ")
x_width = input("Enter the x-width: ")
y_width = input("Enter the y-width: ")
x_end = int(x_start) + int(x_width)
y_end = int(y_start) + int(y_width)

new_style_file = open(f"background_{color}_{x_width}_{y_width}.isy", "w")

ipe_string = f'''<!---
    TITLE: Background_{color}_{x_width}_{y_width}
    DESC: This style adds a {x_width}pt by {y_width}pt object (starting at ({x_start},{y_start})) to the ipe file. It can be used as a template to create backgrounds of any size and color.
-->
<?xml version="1.0"?>
<!DOCTYPE ipestyle SYSTEM "ipe.dtd">
<ipestyle name="background_{color}_{x_width}_{y_width}"> 
<symbol name="Background">
<path layer="background" fill="{color}">
{x_start} {y_start} m
{x_end} {y_start} l
{x_end} {y_end} l
{x_start} {y_end} l
h
</path>
</symbol>
</ipestyle>'''

new_style_file.write(ipe_string)

new_style_file.close()