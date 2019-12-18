import ezdxf
import math
import argparse

parser = argparse.ArgumentParser(description='A tutorial of argparse!')
parser.add_argument("--side", required=True, type=float, help="This is the side of the hexagone")
parser.add_argument("--gap", required=True, type=float, help="This is the gap between hexagons in the honeycomb")
args = parser.parse_args()

print("args", args)

side = args.side
gap = args.gap

def hexagon_by_coords(x, y, side):
	# Returns the points of an hexagone of side "side" and left 
	# down vertex placed in x, y
	points = []
	height = side*math.sqrt(3)
	points.append((x + side, y))
	points.append((x, y))
	points.append((x -0.5*side, y + 0.5*height))
	points.append((x, y + height))
	points.append((x + side, y + height))
	points.append((x + 1.5*side, y + 0.5*height))
	return points
	

doc = ezdxf.new('R2010')  # create a new DXF R2010 drawing, official DXF version name: 'AC1024'

doc.header['$INSUNITS'] = 4 # Work in millimeters

msp = doc.modelspace()  # add new entities to the modelspace

# Some useful vars
height = side*math.sqrt(3)
hor_gap = 0.5*math.sqrt(3)*gap
# Up
x_up = height + gap
# Diag
x_diag = 1.5*side + hor_gap
y_diag = 0.5*height + 0.5*gap

for x_val in range(1, 12, 2):
	for y_val in range(1, 13, 2):
		myshape = msp.add_polyline2d(hexagon_by_coords(x_val*x_diag, y_val*y_diag, side)).close(True)

for x_val in range(2, 12, 2):
	for y_val in range(0, 14, 2):
		myshape = msp.add_polyline2d(hexagon_by_coords(x_val*x_diag, y_val*y_diag, side)).close(True)

doc.saveas('line.dxf')

exit()


# First hexagon, placed on (0, 0)
myshape = msp.add_polyline2d(hexagon_by_coords(0*x_diag, 0*x_up, side)).close(True)
# Up and down the first hexagon
myshape = msp.add_polyline2d(hexagon_by_coords(0*x_diag, 1*x_up, side)).close(True)
myshape = msp.add_polyline2d(hexagon_by_coords(0*x_diag, 2*x_up, side)).close(True)
myshape = msp.add_polyline2d(hexagon_by_coords(0*x_diag, 3*x_up, side)).close(True)
myshape = msp.add_polyline2d(hexagon_by_coords(0*x_diag, 4*x_up, side)).close(True)
# Right columns
# 1st
myshape = msp.add_polyline2d(hexagon_by_coords(1*x_diag, 1*y_diag, side)).close(True)
myshape = msp.add_polyline2d(hexagon_by_coords(1*x_diag, 3*y_diag, side)).close(True)
myshape = msp.add_polyline2d(hexagon_by_coords(1*x_diag, 5*y_diag, side)).close(True)
myshape = msp.add_polyline2d(hexagon_by_coords(1*x_diag, 7*y_diag, side)).close(True)
# 2nd 
myshape = msp.add_polyline2d(hexagon_by_coords(2*x_diag, 0*y_diag, side)).close(True)
myshape = msp.add_polyline2d(hexagon_by_coords(2*x_diag, 2*y_diag, side)).close(True)
myshape = msp.add_polyline2d(hexagon_by_coords(2*x_diag, 4*y_diag, side)).close(True)
myshape = msp.add_polyline2d(hexagon_by_coords(2*x_diag, 6*y_diag, side)).close(True)
myshape = msp.add_polyline2d(hexagon_by_coords(2*x_diag, 8*y_diag, side)).close(True)
# 3rd 
myshape = msp.add_polyline2d(hexagon_by_coords(3*x_diag, 1*y_diag, side)).close(True)
myshape = msp.add_polyline2d(hexagon_by_coords(3*x_diag, 3*y_diag, side)).close(True)
myshape = msp.add_polyline2d(hexagon_by_coords(3*x_diag, 5*y_diag, side)).close(True)
myshape = msp.add_polyline2d(hexagon_by_coords(3*x_diag, 7*y_diag, side)).close(True)
# 4th
myshape = msp.add_polyline2d(hexagon_by_coords(4*x_diag, 0*y_diag, side)).close(True)
myshape = msp.add_polyline2d(hexagon_by_coords(4*x_diag, 2*y_diag, side)).close(True)
myshape = msp.add_polyline2d(hexagon_by_coords(4*x_diag, 4*y_diag, side)).close(True)
myshape = msp.add_polyline2d(hexagon_by_coords(4*x_diag, 6*y_diag, side)).close(True)
myshape = msp.add_polyline2d(hexagon_by_coords(4*x_diag, 8*y_diag, side)).close(True)
# 5th
myshape = msp.add_polyline2d(hexagon_by_coords(5*x_diag, 1*y_diag, side)).close(True)
myshape = msp.add_polyline2d(hexagon_by_coords(5*x_diag, 3*y_diag, side)).close(True)
myshape = msp.add_polyline2d(hexagon_by_coords(5*x_diag, 5*y_diag, side)).close(True)
myshape = msp.add_polyline2d(hexagon_by_coords(5*x_diag, 7*y_diag, side)).close(True)

doc.saveas('line.dxf')
