def grid_size(img_size, N):
'''
Determine the grid size for an image of h pixels x w pixels given N divisions
N is automatically rounded up to the largest number to complete the rectangle
 img_size : tuple : width x height
 N : int : desired number of squares
'''
	import math
	w = img_size[0]
	h = img_size[1]
	No = math.ceil(N/2)*2 # round up to nearest whole number
	R = max(h/w,w/h) # positive ratio of the image
	d1 = math.ceil(math.sqrt(No/R)) # ideal number of cells along one dimension
	s = math.floor(min(h,w)/d1) # ideal size of cell; must be whole number
	d2 = math.ceil(No/d1) # number of cells along other dimension
	if (h > w): # put dimension 1 and 2 in correct order for landscape and portrait
		print('Portrait')
		grid = ( min(d1,d2), max(d1,d2) )
	else:
		print('Landscape')
		grid = ( max(d1,d2), min(d1,d2) )
	print('Cell size: {}-by-{}, {}x{} --> {}x{}'.format(s, s, grid[0],grid[1], s*grid[0],s*grid[1]))
	return s, grid


def chop_file(filepath, N):
	from PIL import Image
	import os

	infile = filepath
	img = Image.open(infile)
	chopsize, grid = grid_size(img.size, N)
	width, height = img.size

	#dir = os.path.splitext(filepath)[0]
	#os.mkdir(dir)
	#os.chdir(dir)

	# Save Chops of original image
	for x0 in range(0, width, chopsize):
		for y0 in range(0, height, chopsize):
			box = (x0, y0,
				x0+chopsize if x0+chopsize <  width else  width - 1,
				y0+chopsize if y0+chopsize < height else height - 1)
			print('{} {}'.format(infile, box))
			#img.crop(box).save('{}_x{}-y{}.jpg'.format(dir, x0, y0))
			img.crop(box).save('{}_x{}-y{}.jpg'.format(infile.replace('.jpg',''), x0, y0))
	#os.chdir('..')
	draw_grid(img, grid, chopsize, infile)

			
def draw_grid(im, grid, sz, outpath):
# im 	: PIL image object
# grid 	: tuple	: grid size, e.g. (13,11) --> (13 columns, 11 rows)
# sz	: int	: pixel width & height of each grid cell 
# outpath : str	: filename.jpg --> will become 'filename_grid.jpg'
#
	print('Drawing grid...')
	from PIL import Image, ImageDraw
	import os
	
	draw = ImageDraw.Draw(im)
	for y in range(0,grid[1]+1): # draw horizontal lines
		draw.line((0,y*sz,grid[0]*sz,y*sz), fill=128)
		for x in range(0, grid[0]+1):
			draw.text( (x*sz, y*sz), '({}x{})'.format(x*sz, y*sz) )
	for x in range(0, grid[0]+1): # draw vertical lines
		draw.line((x*sz,0,x*sz,grid[1]*sz), fill = 128)
	im.save('{}_grid.jpg'.format(outpath.replace('.jpg','')))