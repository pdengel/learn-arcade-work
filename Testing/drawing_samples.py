"""
This is a sample program to demonstrate drawing with
the arcade library
"""

import arcade

# open a window for drawing within
arcade.open_window(600, 600, "Drawing Example")

# set the background color
arcade.set_background_color(arcade.csscolor.SKY_BLUE)

# get ready to draw
arcade.start_render()

# drawing code will be inserted here

# finish drawing
arcade.finish_render()

# keep the window open until it is closed
arcade.run()
