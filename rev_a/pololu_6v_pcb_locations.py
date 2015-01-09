#!/usr/bin/env python

def main():
    holes = [
      ("Upper left corner", 0, 0),
      ("Upper left mount hole", 140, 145),
      ("Pin 1 (lower) left", 125, 1113),
      ("Pin 2", 300, 1114),
      ("Pin 3", 470, 1115),
      ("Pin 4", 641, 1115),
      ("Pin 5", 815, 1114),
      ("Lower right mount hole", 1055, 1055),
      ("Lower right corner", 1200, 1200)]

    scale = 0.7/1200.0

    previous_x = 0.0
    previous_y = 0.0
    for hole in holes:
	label = hole[0]
	x = float(hole[1])
	y = float(hole[2])
	print("{0:.6f}, {1:.6f} {2} {3} {4}".
	  format(x * scale, y * scale, label, x - previous_x, y - previous_y))
	previous_x = x
	previous_y = y

main()

    
