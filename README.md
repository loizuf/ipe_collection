# Ipe Stylefile Collection

The Ipe stylefile collection contains a set of stylefiles for the popular SVG editor [Ipe](https://ipe.otfried.org/).

## Usage
To use a stylefile download it and import it via "Edit -> Stylesheets".

## Contribution
If you have an useful and/or interesting stylesheet that you would be happy to contribute to this collection, you can either email us directly or open a new discussion on this repository.
To keep the collection organized we made up some general guidelines to harmonize all the stylesheets in this collection:

*TODO*

## Categories
The stylefiles are loosely sorted into the following categories.

### Angles
Stylesheets that modifiy the possible angle values for Ipe's angular snap ([Angular snap in the Ipe manual](https://ipe.otfried.org/manual/manual_25.html)).

### Arrowheads
Contains stylefiles that provide additional and different arrowhead shapes (and placements). These are useful for drawing directed graph edges, distance indicators, etc...

### Backgrounds
Stylesheets that set a specific background for the Ipe canvas. 
Can be useful when designing a slide or poster template and
wanting a background on each page that can not be modified.

### Colors
Different colors to the default ones defined in Ipe.

### Dashes
Different dash-patterns for the line and curve tools of Ipe.

### Decorations
Group decorations that can be used to box text or groups of graphical objects.
For a quick tutorial on how to use decorations look [here]().

### PDF Effects
*TODO*

### Grid Sizes
Different spacings for the background grid.

### LaTeX preambles
Predefined latex commands/package imports

### Layouts for the Ipe Canvas
Different canvas sizes for the drawing area of ipe. Various standard sizes are provided. Some restrict the background grid and include side margins.

### Marks
Different symbol styles for the marks tool of IPE.

### Opacities
Different opacitiy values for objects in IPE.

### Pens
Different stroke widths for the line and curve tool of IPE.

### Text Modifications
Different text styles (e.g. bold, italic, right to left, etc.), text sizes and other text related variations.

### Tilings
Different tiling patterns for filled objects in IPE.

## Naming Scheme and Format
All files in this repository are named as follows:

`[attribute_type]_[name]_[number_of_defined_attributes].isy`

All style files in this repository start with a documenation containing:
- the title of the file that is displayed in Ipe (this is different from the file name)
- description of the attributes defined in this file
- a list of original contributors
- lists of the type and number of defined attributes

This documentation is entirely contained within a comment block. The documentation is not necessary for Ipe to be able to read the file, but is required in this repository, to create previews of the styles. An example is shown below

```
<!-- ipecol
    {
        "title" : "NAME",
        "description" : "Provides some anglesize styles.",
        "provided_by" : ["Contributor One"],
        "style_count" : [5],
        "style_types" : ["anglesize"]
    }
-->
```
