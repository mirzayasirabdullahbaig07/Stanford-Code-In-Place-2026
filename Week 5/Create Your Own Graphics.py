from graphics import Canvas
    
CANVAS_WIDTH = 400
CANVAS_HEIGHT = 400

def main():
    canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)

    # Background
    canvas.create_rectangle(
        0, 0,
        CANVAS_WIDTH, CANVAS_HEIGHT,
        "skyblue"
    )

    # Sun
    canvas.create_oval(
        300, 30,
        370, 100,
        "yellow"
    )

    # Ground
    canvas.create_rectangle(
        0, 300,
        CANVAS_WIDTH, 400,
        "lightgreen"
    )

    # House body
    canvas.create_rectangle(
        120, 170,
        280, 300,
        "orange"
    )

    # Roof
    canvas.create_polygon(
        100, 170,
        200, 90,
        300, 170,
        "brown"
    )

    # Door
    canvas.create_rectangle(
        175, 220,
        225, 300,
        "saddlebrown"
    )

    # Door knob
    canvas.create_oval(
        215, 255,
        220, 260,
        "yellow"
    )

    # Left window
    canvas.create_rectangle(
        135, 200,
        170, 235,
        "white"
    )

    # Right window
    canvas.create_rectangle(
        230, 200,
        265, 235,
        "white"
    )

    # Tree trunk
    canvas.create_rectangle(
        50, 220,
        75, 300,
        "sienna"
    )

    # Tree leaves
    canvas.create_oval(
        20, 160,
        105, 245,
        "darkgreen"
    )

    # Cloud 1
    canvas.create_oval(
        40, 40,
        100, 80,
        "white"
    )
    canvas.create_oval(
        70, 20,
        130, 80,
        "white"
    )
    canvas.create_oval(
        100, 40,
        160, 80,
        "white"
    )

    # Cloud 2
    canvas.create_oval(
        200, 50,
        250, 90,
        "white"
    )
    canvas.create_oval(
        230, 30,
        290, 90,
        "white"
    )
    canvas.create_oval(
        260, 50,
        320, 90,
        "white"
    )

if __name__ == '__main__':
    main()