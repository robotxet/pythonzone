"""
Find Cost of Tile to Cover W x H Floor:
Calculate the total cost of tile if would take to cover a floor plan of
width and height, using a cost entered by the user.
"""

width = float(raw_input("Width of floor: "))
length = float(raw_input("Length of floor: "))
cost = float(raw_input("Cost of tile: "))

tile_width = float(raw_input("Width of tile: "))
tile_height = float(raw_input("Height of tile: "))

total_tile_number = (round(width / tile_width)) * (round(length / tile_height))

print "Total tile cost for %sx%s floor is  \
      %s" % (width, length, total_tile_number * cost)
