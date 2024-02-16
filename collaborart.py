# COLLABORART.PY


def main(input_image, N):
	import os
	from PIL import Image, ImageDraw

	print("::: COLLABORART :::")

	# Define name of input images and initialize output folder
	infile = input_image
	name = infile.replace(".jpg", "").replace(" ", "_")  # replace extension and blank spaces
	name = name[0:15]  # make name short
	name_n = "{}_{:03}".format(name, N)  # e.g., obama_040

	# Define outputdir and output paths
	outputdir = name_n  # outputdirectory
	# cell_filename = "{}_{}{}_x{}_y{}.jpg"  # (e.g., obama_40_A1_x1_y1.jpg)
	# cell_fullpath = os.path.jon(outputdir, cell_filename)
	grid_filename = '{}_grid.jpg'.format(name_n)  # e.g., obama_040_grid.jpg
	# grid_fullpath = os.path.join(outputdir, grid_filename)  # e.g., obama_040/obama_040_grid.jpg
	os.mkdir(outputdir)

	# Initialize output images
	img = Image.open(infile)  # image for cropping
	img2 = Image.open(infile)  # image for drawing grid
	sz, grid = grid_size(img.size, N)  # size in pixels, (col-by-row) for grid
	width, height = img.size  # image size in pixels

	print('Drawing grid & cropping file...')
	# Nested "for y: ..., for x:" loops mean you are working left to right, then
	# top to bottom. I.e., A1, B1, ... BN, A2, B2, ... BN, ....
	draw = ImageDraw.Draw(img2)  # create an object to draw on
	row = 1  # initialize first row as 1 (vertical)
	for y in range(0,grid[1]):  # for every row
		col = "A"  # initiale A as first column
		draw.line((0,y*sz,grid[0]*sz,y*sz), fill=128)  # draw horizontal line (top)
		for x in range(0, grid[0]):  # for every column
			draw.line((x*sz,0,x*sz,grid[1]*sz), fill = 128)  # draw vertical line (left)
			draw.text((x*sz, y*sz), "{} ({}x{})".format(
				"{}{}".format(col, row),
				x*sz, y*sz))  # put text in cell (top left)
			box = (x*sz, y*sz, x*sz + sz, y*sz + sz)  # define cell box (l, t, r, b)
			cell_filename = '{}_{}_x{}-y{}.jpg'.format(
				name_n, "{}{}".format(col, row), x, y)  # define cell filename
			cell_fullpath = os.path.join(outputdir, cell_filename)
			img.crop(box).save(cell_fullpath)  # crop the file
			print(cell_fullpath)  # print the filename when done
			col = chr(ord(col)+1)  # increment column
		row += 1  # increment row
	draw.line((0,grid[1]*sz,grid[0]*sz,grid[1]*sz), fill=128)  # add bottom line
	draw.line((grid[0]*sz,0,grid[0]*sz,grid[1]*sz), fill = 128)  # add right line
	# grid_filename = '{}_{:03}_grid.jpg'.format(infile.replace('.jpg',''), N)
	grid_fullpath = os.path.join(outputdir, grid_filename)
	img2.save(grid_fullpath)  # save image w grid

	print("Done")


def grid_size(img_size, N):
#'''
#Determine the grid size for an image of h pixels x w pixels given N divisions
#N is automatically rounded up to the largest number to complete the rectangle
# img_size : tuple : width x height
# N : int : desired number of squares
#'''
	import math
	w = img_size[0]
	h = img_size[1]
	No = math.ceil(N/2)*2  # round up to nearest whole number
	R = max(h/w,w/h)  # positive ratio of the image
	d1 = math.ceil(math.sqrt(No/R))  # ideal number of cells along one dimension
	s = math.floor(min(h,w)/d1)  # ideal size of cell; must be whole number
	d2 = math.ceil(No/d1)  # ideal number of cells along other dimension
	if (h > w): # put dimension 1 and 2 in correct order for landscape and portrait
		print('Portrait')
		grid = (min(d1,d2), max(d1,d2))
	else:
		print('Landscape')
		grid = (max(d1,d2), min(d1,d2))
	print('Cell size: {}-by-{} px, {}x{} grid --> {}x{} px'.format(s, s, grid[0],grid[1], s*grid[0],s*grid[1]))
	return s, grid


if __name__ == "__main__":
	import argparse

	parser = argparse.ArgumentParser(description='Run COLLABORART.')
	parser.add_argument('image', metavar='I', type=str,
                    help='an image to divide (obama.jpg')
	parser.add_argument('N', metavar='N', type=int,
                    help='Minimum number of cells to create')
	args = parser.parse_args()

	main(args.image, args.N)


"""
TO DO:

[ ] Add documentation; fix README.md; update github
[ ] Store input images in images/
Instead of reading images like obama/obama.jpg,
read image like images/obama.jpg,
and then make results/obama/obama.jpg, results/obama_grid.jpg, results/obama_<>.jpg

# INPUTFILE = "image/{input_image}"
filename, ext = os.path.splitext(input_image)
# OUTPUTGRID = "image/{filename:}/{filename}_grid.{ext}"
# OUTPUTCELL = "image/{filename:}/{filename}_{col}{row}_{xpos}{ypos}.{ext}"
# CELLLABEL = "{col}{row} ({xpos}x{ypos})"


[ ] Automatically parse extension type
[X] Fix drawing of grid
[X] Don't make incomplete cells
[ ] Add option to center grid if extra space exists
[x] Clean up col, row incrementing (make smarter)

"""
