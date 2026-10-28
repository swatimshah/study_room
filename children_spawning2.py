from vpython import box, cylinder, sphere, vector, color, compound

def create_girl(start_x=-5.5, door_z=-3.0):
    """Generates a unified compound mesh for the girl character model (Swati)."""
    skyblue = vector(0.53, 0.81, 0.98)
    skin_color = vector(0.9, 0.75, 0.65)
    
    l_leg = cylinder(pos=vector(start_x, 0, door_z - 0.15), axis=vector(0, 0.8, 0), radius=0.06, color=skin_color)
    r_leg = cylinder(pos=vector(start_x + 0.1, 0, door_z + 0.15), axis=vector(0, 0.8, 0), radius=0.06, color=skin_color)
    skirt = cylinder(pos=vector(start_x, 0.8, door_z), axis=vector(0, 0.6, 0), radius=0.22, radius2=0.15, color=skyblue)
    torso = box(pos=vector(start_x, 1.8, door_z), size=vector(0.3, 0.8, 0.35), color=color.white)
    tie = box(pos=vector(start_x + 0.16, 1.8, door_z), size=vector(0.02, 0.4, 0.08), color=vector(0.6, 0.0, 0.0))
    head = sphere(pos=vector(start_x, 2.4, door_z), radius=0.18, color=skin_color)
    hair = sphere(pos=vector(start_x - 0.02, 2.45, door_z), radius=0.2, color=color.black, opacity=0.95)
    l_arm = cylinder(pos=vector(start_x, 2.1, door_z - 0.22), axis=vector(0.1, -0.6, 0), radius=0.04, color=color.white)
    r_arm = cylinder(pos=vector(start_x, 2.1, door_z + 0.22), axis=vector(-0.1, -0.6, 0), radius=0.04, color=color.white)
    
    girl_mesh = compound([l_leg, r_leg, skirt, torso, tie, head, hair, l_arm, r_arm])
    girl_mesh.visible = False
    
    return girl_mesh

def create_boy(start_x=-5.5, door_z=-3.0):
    """Generates a unified compound mesh for the boy (Jim) and an independent football."""
    boy_navy = vector(0.1, 0.1, 0.4)
    skin_color = vector(0.9, 0.75, 0.65)
    
    l_leg = cylinder(pos=vector(start_x, 0, door_z - 0.12), axis=vector(0, 0.6, 0), radius=0.05, color=skin_color)
    r_leg = cylinder(pos=vector(start_x + 0.1, 0, door_z + 0.12), axis=vector(0, 0.6, 0), radius=0.05, color=skin_color)
    shorts = cylinder(pos=vector(start_x, 0.6, door_z), axis=vector(0, 0.4, 0), radius=0.18, radius2=0.18, color=boy_navy)
    torso = box(pos=vector(start_x, 1.4, door_z), size=vector(0.28, 0.7, 0.32), color=color.red)
    head = sphere(pos=vector(start_x, 1.95, door_z), radius=0.16, color=skin_color)
    hair = sphere(pos=vector(start_x - 0.02, 2.0, door_z), radius=0.17, color=vector(0.2, 0.1, 0.0))
    l_arm = cylinder(pos=vector(start_x, 1.6, door_z - 0.18), axis=vector(0, -0.5, 0), radius=0.04, color=color.red)
    r_arm = cylinder(pos=vector(start_x, 1.5, door_z + 0.18), axis=vector(0.2, -0.1, -0.15), radius=0.04, color=color.red)
    
    boy_mesh = compound([l_leg, r_leg, shorts, torso, head, hair, l_arm, r_arm])
    boy_mesh.visible = False
    
    football = sphere(pos=vector(start_x + 0.25, 0.18, door_z + 0.05), radius=0.18, color=color.orange, visible=False)
    
    return boy_mesh, football
