from vpython import canvas, box, cylinder, vector, color

def init_scene():
    """Initializes the 3D scene canvas and camera positions."""
    scene = canvas(title="Delayed Entry Study Room Layout", width=1000, height=700, 
                   center=vector(0, 2, 0), background=color.gray(0.9))
    scene.camera.pos = vector(5, 7, 10)
    scene.camera.axis = vector(-5, -5, -10)
    return scene

def build_room(room_size=10, wall_height=5, wall_thickness=0.2):
    """Generates room boundary structures, floor planes, and windows."""
    # Floor
    box(pos=vector(0, 0, 0), size=vector(room_size, wall_thickness, room_size), color=color.gray(0.4))

    # Back Wall (North) + Window Setup
    box(pos=vector(0, wall_height/2, -room_size/2), size=vector(room_size, wall_height, wall_thickness), color=color.white)
    box(pos=vector(0, 3, -room_size/2 + 0.1), size=vector(3, 1.8, 0.1), color=color.gray(0.2))
    box(pos=vector(0, 3, -room_size/2 + 0.12), size=vector(2.8, 1.6, 0.05), color=color.cyan, opacity=0.5)

    # Left Wall (West) + Open Hinged Door Frame
    box(pos=vector(-room_size/2, wall_height/2, 0), size=vector(wall_thickness, wall_height, room_size), color=color.white)
    box(pos=vector(-room_size/2 + 0.1, 1.75, -3), size=vector(0.1, 3.5, 1.5), color=vector(0.4, 0.2, 0.1), opacity=0.3)
    door_panel = box(pos=vector(-room_size/2 + 0.6, 1.75, -2.3), size=vector(0.1, 3.4, 1.4), color=vector(0.5, 0.25, 0.1))
    door_panel.rotate(angle=1.0, axis=vector(0, 1, 0), origin=vector(-room_size/2, 1.75, -3.7))

    # Right Wall (East) & Clear Viewing Cutout Front Wall (South)
    box(pos=vector(room_size/2, wall_height/2, 0), size=vector(wall_thickness, wall_height, room_size), color=color.white)
    box(pos=vector(0, wall_height/2, room_size/2), size=vector(room_size, wall_height, wall_thickness), color=color.white, opacity=0.1)

def build_furniture(room_size=10):
    """Instantiates and arranges tables, couches, lamps, and bookshelves inside the matrix."""
    # Bookshelf assembly with colorful books
    box(pos=vector(-room_size/2 + 0.4, 2, 1), size=vector(0.6, 4, 1.8), color=vector(0.3, 0.15, 0.05))
    for h in [1.0, 2.2, 3.3]:
        box(pos=vector(-room_size/2 + 0.4, h, 1), size=vector(0.6, 0.05, 1.8), color=vector(0.3, 0.15, 0.05))
    colors = [color.red, color.blue, color.green, color.orange, color.yellow]
    for i in range(5):
        box(pos=vector(-room_size/2 + 0.4, 1.3, 0.4 + i*0.2), size=vector(0.4, 0.5, 0.12), color=colors[i % 5])
        box(pos=vector(-room_size/2 + 0.4, 2.5, 1.2 - i*0.2), size=vector(0.4, 0.5, 0.12), color=colors[(i+2) % 5])

    # Desk Setup & Chair Assembly
    box(pos=vector(0, 1.2, -room_size/2 + 1.2), size=vector(3.5, 0.1, 1.8), color=vector(0.6, 0.4, 0.2))
    for x_offset in [-1.6, 1.6]:
        for z_offset in [0.5, 1.9]:
            cylinder(pos=vector(x_offset, 0, -room_size/2 + z_offset), axis=vector(0, 1.2, 0), radius=0.08, color=color.black)
    box(pos=vector(0, 0.7, -room_size/2 + 2.6), size=vector(0.8, 0.08, 0.8), color=color.black)
    box(pos=vector(0, 1.2, -room_size/2 + 2.96), size=vector(0.8, 1.0, 0.08), color=color.black)
    for cx in [-0.35, 0.35]:
        for cz in [2.3, 2.9]:
            cylinder(pos=vector(cx, 0, -room_size/2 + cz), axis=vector(0, 0.7, 0), radius=0.04, color=color.gray(0.3))

    # Working Desk Lamp
    cylinder(pos=vector(-1, 1.25, -room_size/2 + 1), axis=vector(0, 0.05, 0), radius=0.2, color=color.red)
    cylinder(pos=vector(-1, 1.3, -room_size/2 + 1), axis=vector(0, 0.5, 0), radius=0.02, color=color.gray(0.8))
    cylinder(pos=vector(-1, 1.8, -room_size/2 + 1), axis=vector(0, 0.3, 0), radius=0.25, radius2=0.1, color=color.red)
    box(pos=vector(-1, 1.6, -room_size/2 + 0.08), size=vector(0.4, 0.3, 0.04), color=color.white)
    box(pos=vector(-1, 1.6, -room_size/2 + 0.11), size=vector(0.06, 0.1, 0.04), color=color.gray(0.5))

    # Lounge Armchair Sofa Assembly
    box(pos=vector(room_size/2 - 0.8, 0.4, 1), size=vector(1.2, 0.5, 3.0), color=vector(0.2, 0.4, 0.6))
    box(pos=vector(room_size/2 - 0.2, 1.1, 1), size=vector(0.3, 1.3, 3.0), color=vector(0.2, 0.4, 0.6))
    box(pos=vector(room_size/2 - 0.6, 0.7, -0.6), size=vector(0.9, 0.6, 0.3), color=vector(0.15, 0.35, 0.55))
    box(pos=vector(room_size/2 - 0.6, 0.7, 2.6), size=vector(0.9, 0.6, 0.3), color=vector(0.15, 0.35, 0.55))
