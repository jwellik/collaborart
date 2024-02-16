# COLLABORART
<img src="https://raw.githubusercontent.com/jwellik/collaborart/main/img/obama_grid.jpg" width=717 alt="Obama grid" />

## Description

This program takes an input image and splits it into a grid of N cells. Each cell is output as its own image. A reference image is with the grid overlay is also produced. Cells are named by row and column as well as x and y position.

## Usage

First, store an image in a directory under collaborart/ like this:
- collaborart/obama/obama.jpg

Then, navigate to the collaborart folder, and run the python file with the
filename and minimum number of desired cells.

```bash
$ cd collaborart
$ python collaborart.py obama/obama.jpg 40
```

This results in a new folder: 'obama_040' that contains the reference grid and a new image for each cell.

- collaborart/obama_040/obama_040_grid.jpg
- collaborart/obama_040/obama_040_x0-y0.jpg
.
.
.
- collaborart/obama_040/obama_040_x644-y460.jpg
