from graphics import Canvas
import math
    
CANVAS_WIDTH = 400
CANVAS_HEIGHT = 300

CLOUD_WIDTH = 120
CLOUD_HEIGHT = 80

TRUNK_HEIGHT = 80
TRUNK_WIDTH = 20
LEAVES_SIZE = 60

TREE_BOTTOM_Y = CANVAS_HEIGHT - 20 

def main():
    canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
    
    # Sky background
    draw_sky(canvas)
    
    # Ground
    draw_ground(canvas)
    
    # Sun
    draw_sun(canvas, 340, 30, 'yellow')
    
    # Three clouds
    draw_cloud(canvas, 20,  10, 'pink')
    draw_cloud(canvas, 140, 10, 'salmon')
    draw_cloud(canvas, 270, 10, 'purple')
    
    # Three trees
    draw_tree(canvas, 50,  TREE_BOTTOM_Y, 'green',      'brown')
    draw_tree(canvas, 150, TREE_BOTTOM_Y, 'red',        'darkred')
    draw_tree(canvas, 320, TREE_BOTTOM_Y, 'darkorange', 'brown')

# ─────────────────────────────────────────────
# SKY
# ─────────────────────────────────────────────
def draw_sky(canvas):
    """Draws a light-blue sky rectangle covering the whole canvas."""
    canvas.create_rectangle(0, 0, CANVAS_WIDTH, CANVAS_HEIGHT, 'lightblue')

# ─────────────────────────────────────────────
# GROUND
# ─────────────────────────────────────────────
def draw_ground(canvas):
    """Draws a green ground strip at the bottom of the canvas."""
    ground_top_y = CANVAS_HEIGHT - 40
    canvas.create_rectangle(0, ground_top_y, CANVAS_WIDTH, CANVAS_HEIGHT, 'green')

# ─────────────────────────────────────────────
# SUN
# ─────────────────────────────────────────────
def draw_sun(canvas, x, y, color):
    """
    Draws a simple circle sun.
    x, y = top-left corner of the bounding box.
    """
    sun_size = 50
    canvas.create_oval(x, y, x + sun_size, y + sun_size, color)

# ─────────────────────────────────────────────
# CLOUD
# ─────────────────────────────────────────────
def draw_cloud(canvas, x, y, color):
    """
    Draws one cloud using three overlapping ovals.
    x, y = top-left corner of the cloud bounding box.
    color = fill color of the cloud.
    """
    cloud_bottom_start_y = y + (1/3) * CLOUD_HEIGHT
    cloud_bottom_end_y   = y + CLOUD_HEIGHT
    cloud_top_start_x    = x + (1/4) * CLOUD_WIDTH
    cloud_top_end_x      = x + (3/4) * CLOUD_WIDTH

    # Bottom-left puff
    canvas.create_oval(
        x,
        cloud_bottom_start_y,
        x + (3/4) * CLOUD_WIDTH,
        cloud_bottom_end_y,
        color
    )
    # Bottom-right puff
    canvas.create_oval(
        x + (1/4) * CLOUD_WIDTH,
        cloud_bottom_start_y,
        x + CLOUD_WIDTH,
        cloud_bottom_end_y,
        color
    )
    # Top centre puff
    canvas.create_oval(
        cloud_top_start_x,
        y,
        cloud_top_end_x,
        y + (2/3) * CLOUD_HEIGHT,
        color
    )

# ─────────────────────────────────────────────
# TREE
# ─────────────────────────────────────────────
def draw_tree(canvas, x, bottom_y, leaves_color, trunk_color):
    """
    Draws one tree: a circle for leaves on top of a rectangle trunk.
    x        = horizontal centre of the tree.
    bottom_y = y position of the bottom of the trunk.
    leaves_color = color of the circular leaves.
    trunk_color  = color of the rectangular trunk.
    """
    # Trunk
    trunk_left  = x - TRUNK_WIDTH  / 2
    trunk_right = x + TRUNK_WIDTH  / 2
    trunk_top   = bottom_y - TRUNK_HEIGHT
    canvas.create_rectangle(
        trunk_left, trunk_top,
        trunk_right, bottom_y,
        trunk_color
    )

    # Leaves (circle centred above the trunk)
    leaves_cx   = x
    leaves_cy   = trunk_top - LEAVES_SIZE / 2
    canvas.create_oval(
        leaves_cx - LEAVES_SIZE / 2,
        leaves_cy - LEAVES_SIZE / 2,
        leaves_cx + LEAVES_SIZE / 2,
        leaves_cy + LEAVES_SIZE / 2,
        leaves_color
    )


if __name__ == '__main__':
    main()