# Ipe Stylefile Collection

The Ipe stylefile collection contains a set of stylefiles for the popular SVG editor [Ipe](https://ipe.otfried.org/). The styles are sorted into folders according to the attributes defined within them. The Readme files in the specific folders display the contents of the contained stylefiles with a preview of the defined attributes (where possible).

## Usage
To use a stylefile download it and import it via "Edit -> Stylesheets" (Shortcut [CTRL]+[SHIFT]+[S]).

## Contribution
If you have an useful and/or interesting stylesheet that you would be happy to contribute to this collection (for example if you adapted one of the style files in this repository), you can either email us directly or open a new discussion on this repository.

Most stylesheets in this repository contain only one type of defined attribute (see below) and are documented at the beginning of the file (see further below). We are happy to recieve any contribution. Submitted stylesheets might be split or slightly changed to fit the standard of this repository. 

## Categories
The stylesheets are loosely sorted into the following categories.

### Angles
Stylesheets that modifiy the possible angle values for Ipe's angular snap ([Angular snap in the Ipe manual](https://ipe.otfried.org/manual/manual_25.html)).

### Arrowheads
Stylesheets that provide additional and different arrowhead shapes (and placements). These are useful for drawing directed graph edges, distance indicators, etc...
This folder includes previews.

### Backgrounds
Stylesheets that set a specific background for the Ipe canvas. 
Can be useful when designing a slide or poster template and
wanting a background on each page that can not be modified.

### Colors
Different colors to the default ones defined in Ipe.
This folder includes previews.

### Dashes
Different dash-patterns for the line and curve tools of Ipe.
This folder includes previews.

### Decorations
Different group decorations that can be used to box text or groups of graphical objects. A decoration defines a decorative element, which encloses grouped element and scales to the group size.
For a short explanation on how to use decorations look [here](https://ipe.otfried.org/manual/manual_19.html).
This folder includes previews.

### PDF Effects
Stylesheets that provide effects. This currently only covers PDF slide transitions. For reference on how to use them, please see [this section in the ipe manual](https://ipe.otfried.org/manual/manual_40.html).

### Grid Sizes
Different spacings for the background grid that can be used for grid snapping.

### LaTeX preambles
Predefined latex commands/package imports (different fonts, bulletpoint definitions, etc.)

### Layouts for the Ipe Canvas
Different canvas sizes for the drawing area of ipe. Various standard sizes are provided (DIN norms, US sizes). Some restrict the background grid and include side margins (for example to represent the predefined margins of publisher templates like LNCS).

### Marks
Different symbol styles for the marks tool of IPE. These are useful for styling point objectes or graph vertices.
This folder includes previews.

### Opacities
Different opacitiy values for objects in IPE.

### Pens
Different stroke widths for the line and curve tool of IPE.

### Templates
Stylesheets that contain a variety of different attributes, and can be used as templates for presentation or posters. Some of these stylesheets might be intended to be used as a REPLACEMENT of the preloaded basic.isy. Please refer to the documentation of the individual files.

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
