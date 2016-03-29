# This is a sample config file, meant to give you an idea of how to format your
# config file and what's possible.

# Define the path to your world here. 'My World' in this case will show up as
# the world name on the map interface. If you change it, be sure to also change
# the referenced world names in the render definitions below.
worlds['Overworld'] = "/world"

# Define where to put the output here.
outputdir = "/var/www/html"

# This is an item usually specified in a renders dictionary below, but if you
# set it here like this, it becomes the default for all renders that don't
# define it.
# Try "smooth_lighting" for even better looking maps!
rendermode = "lighting"


# This example is the same as above, but rotated
renders["mini"] = {
        'world': 'Overworld',
        'title': 'tiny',
	'crop': (-500, -500, 500, 500),
}


