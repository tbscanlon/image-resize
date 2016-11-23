import os, sys
from PIL import Image
from glob import glob # allows wildcard args in Windows

basewidth = 200 # set the size of the output image

# Print instructions if no args are supplied
if len(sys.argv) <= 1:
	print "HOW TO USE:"
	print "image-resize.py name-of-file.jpg"
	exit(0)

for infile in glob(sys.argv[1]):

	# skip if the file has already been resized
	if "resize" in infile:
		print "Skipping %s as it has already been resized" % infile
		continue

	outfile = os.path.splitext(infile)[0] + "-resize.jpg" # create output files for each arg

	if infile != outfile:
		try:
			im = Image.open(infile)
			wpercent = (basewidth / float(im.size[0]))
			hsize = int((float(im.size[1]) * float(wpercent)))
			im = im.resize((basewidth, hsize), Image.ANTIALIAS)
			im.save(outfile, "JPEG")

			print "Successfully resized %s" % infile
			print "The resized image can be found at %s" % outfile

			try:
				os.remove(infile)

			except WindowsError: # stop script halting if permission is denied
				print "Don't have permission to delete ''%s'" % infile

		except IOError:
			print "cannot create thumbnail for '%s' - is it a valid filename?" % infile
