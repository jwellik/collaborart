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


def draw_grid(filepath, N):
# im 	: PIL image object
# grid 	: tuple	: grid size, e.g. (13,11) --> (13 columns, 11 rows)
# sz	: int	: pixel width & height of each grid cell 
# outpath : str	: filename.jpg --> will become 'filename_grid.jpg'
#
	import os
	from PIL import Image

	infile = filepath
	img = Image.open(infile)  # image for cropping
	img2 = Image.open(infile)  # image for drawing grid
	sz, grid = grid_size(img.size, N)  # size in pixels, (col-by-row) for grid
	width, height = img.size  # image size in pixels

	print('Drawing grid...')	
	draw = ImageDraw.Draw(img2)  # create an object to draw on
	col = "A"  
	row = 1  # initialize first row as 1 (vertical)
	for y in range(0,grid[1]):  # for every row
		col = "A"  # initiale A as first column
		draw.line((0,y*sz,grid[0]*sz,y*sz), fill=128)  # draw horizontal line
		for x in range(0, grid[0]):  # for every column
			draw.line((x*sz,0,x*sz,grid[1]*sz), fill = 128)  # draw vertical line
			draw.text((x*sz, y*sz), "{} ({}x{})".format(
				"{}{}".format(col, row),
				x*sz, y*sz))  # put text in cell
			box = (x*sz, y*sz, x*sz + sz, y*sz + sz)  # define cell box
			cell_filename = '{}_{}_x{}-y{}.jpg'.format(
				infile.replace('.jpg',''),
				"{}{}".format(col, row),
				x, y)  # define cell filename
			img.crop(box).save(cell_filename)  # crop the file
			print(cell_filename)  # print the filename when done
			col = chr(ord(col)+1)  # increment column
		row += 1  increment row
	draw.line((0,grid[1]*sz,grid[0]*sz,grid[1]*sz), fill=128)  # add bottom line
	draw.line((grid[0]*sz,0,grid[0]*sz,grid[1]*sz), fill = 128)  # add right line
	img2.save('{}_grid.jpg'.format(infile.replace('.jpg','')))  # save image w grid