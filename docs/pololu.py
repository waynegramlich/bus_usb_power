#!/usr/bin/env python

def main():
    print("s18v20fx")
    s18v20fx()

def show(board, point):
    # Extract values from *board*:
    board_dx_dy = board[0]
    upper_left_corner = board[1]
    lower_right_corner = board[2]

    x_scale = board_dx_dy[0] / (lower_right_corner[0] - upper_left_corner[0])
    y_scale = board_dx_dy[1] / (lower_right_corner[1] - upper_left_corner[1])

    x_center = (lower_right_corner[0] + upper_left_corner[0]) * x_scale / 2.0
    y_center = (lower_right_corner[1] + upper_left_corner[1]) * y_scale / 2.0

    x = point[0]
    y = point[1]
    text = point[2]
    print("{0:.3f} {1:.3f}  {2}".
      format((x * x_scale) - x_center, (y * y_scale) - y_center, text))

def s18v20fx():

    upper_left_corner = (69.0, 0.0, "upper_left_corner")
    upper_left_mount =  (81.0, 12.0, "upper_left_mount")

    lower_left_mount =  (81.0, 117.0, "lower_left_mount")
    lower_left_corner = (69.0, 127.0, "lower_left_corner")

    left_ground1 = (99.0, 34.0, "left_ground1")
    left_ground2 = (99.0, 50.0, "left_ground2")
    left_vin1 =    (99.0, 66.0, "left_vin1")
    left_vin2 =    (99.0, 81.0, "left_vin2")
    left_enable =  (99.0, 98.0, "left_enable")

    right_ground1 = (306.0, 34.0 , "right_ground1")
    right_ground2 = (306.0, 51.0, "right_ground2")
    right_vout1 =   (306.0, 67.0, "right_vout1")
    right_vout2 =   (306.0, 82.0, "right_vout2")

    upper_right_corner = (336.0,  0.0, "upper_right_corner")
    upper_right_mount =  (325.0, 13.0, "upper_right_mount")

    lower_right_mount =  (325.0, 117.0, "lower_right_mount")
    lower_right_corner = (336.0, 127.0, "lower_right_corner")

    board_dx_dy_inch = (1.700, 0.825)
    mount_dx_dy_inch = (1.530, 0.655)

    board = (board_dx_dy_inch, upper_left_corner, lower_right_corner)
    board = (mount_dx_dy_inch, upper_left_mount, lower_right_mount)

    show(board, upper_left_mount)
    show(board, lower_left_mount)
    show(board, upper_right_mount)
    show(board, lower_right_mount)

    show(board, left_ground1)
    show(board, left_ground2)
    show(board, left_vin1)
    show(board, left_vin2)
    show(board, left_enable)

    show(board, right_ground1)
    show(board, right_ground2)
    show(board, right_vout1)
    show(board, right_vout2)

main()
