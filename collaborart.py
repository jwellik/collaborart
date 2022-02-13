import utils


def main(input_image, N):
	print("::: COLLABORART :::")

	utils.chop_file(input_image, N)
	#print(" - {}".format(arg1))
	#print(" - {}".format(arg2))
	print("Done")


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
[ ] Automatically parse extension type
[ ] Fix drawing of grid
[ ] Don't make incomplete cells
[ ] Add option to center grid if extra space exists
[ ] Clean up col, row incrementing (make smarter)

"""