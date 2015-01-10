#!/usr/bin/env python

def main():
    # This pixel values were taken from the back side of the PCB.
    # It looks like the mounting holes are a #2.

    holes = [
      ("Upper left corner", 0, 0),
      ("Upper left mount hole", 140, 145),
      ("Upper left mount hole upper edge", 140, 65),
      ("Upper left mount hole lower edge", 140, 215),
      ("Pin 10 (lower) left", 125, 1113),
      ("Pin 8", 300, 1114),
      ("Pin 6", 470, 1115),
      ("Pin 4", 641, 1115),
      ("Pin 2", 815, 1114),
      ("Lower right mount hole", 1055, 1055),
      ("Lower right corner", 1200, 1200)]

    scale = 0.7/1200.0
    offset = 0.7/2.0


    previous_x = 0.0
    previous_y = 0.0
    for hole in holes:
	label = hole[0]
	x = -float(hole[1])
	y = float(hole[2])
	print("{0:.6f}, {1:.6f} {2} {3} {4}".
	  format(x * scale + offset, y * scale - offset, label,
          (x - previous_x) * scale, (y - previous_y) * scale))
	previous_x = x
	previous_y = y

main()

    
