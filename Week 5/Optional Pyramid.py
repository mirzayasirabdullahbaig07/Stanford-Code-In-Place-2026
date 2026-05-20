from graphics import Canvas

CANVAS_WIDTH = 600
CANVAS_HEIGHT = 300

BRICK_WIDTH = 30
BRICK_HEIGHT = 12
BRICKS_IN_BASE = 14

def main():
    canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
    draw_pyramid(canvas)

def draw_pyramid(canvas):
    # Loop over each row: row 0 = base (most bricks), last row = top (1 brick)
    for row in range(BRICKS_IN_BASE):
        bricks_in_row = BRICKS_IN_BASE - row

        # Total width of this row
        row_width = bricks_in_row * BRICK_WIDTH

        # Center this row horizontally on the canvas
        start_x = (CANVAS_WIDTH - row_width) / 2

        # Row 0 is at the bottom, each row above moves up by BRICK_HEIGHT
        start_y = CANVAS_HEIGHT - (row + 1) * BRICK_HEIGHT

        # Draw each brick in this row
        for col in range(bricks_in_row):
            brick_x = start_x + col * BRICK_WIDTH
            brick_y = start_y
            canvas.create_rectangle(
                brick_x,
                brick_y,
                brick_x + BRICK_WIDTH,
                brick_y + BRICK_HEIGHT,
                "orange",
                "black"
            )

if __name__ == '__main__':
    main()