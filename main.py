from vpython import canvas, rate, vector, color
import time
import os
from gtts import gTTS
import pygame
import sys

# ========================================================
# CRITICAL VPYTHON RE-RUN CACHE & SCENE RESET
# ========================================================
if 'scene' in globals() or 'scene' in locals():
    try:
        for obj in list(scene.objects):
            obj.visible = False
            del obj
    except Exception:
        pass

# Wipe runtime caching to catch updates cleanly
for module in ['room_creation', 'children_spawning2', 'girl_controller', 'boy_controller']:
    if module in sys.modules:
        del sys.modules[module]

import room_creation
import children_spawning2
from girl_controller import GirlController
from boy_controller import BoyController
# ========================================================

# ----------------- VOICE ENGINE PREPARATION -----------------
pygame.mixer.init()

def speak(audio_filename, text_to_say):
    """Generates audio files dynamically and plays them back asynchronously."""
    if not os.path.exists(audio_filename):
        tts = gTTS(text=text_to_say, lang='en')
        tts.save(audio_filename)
        
    pygame.mixer.music.load(audio_filename)
    pygame.mixer.music.play()

# Initialize localized room setup modules
room_creation.init_scene()
room_creation.build_room(room_size=10)
room_creation.build_furniture(room_size=10)

# Central Coordinates Layout Matrix
door_z = -3.0
start_x_spawn = -5.5
speed_step = 0.04

g_target_x, g_target_z = 0.0, -2.2
b_target_x, b_target_z = 3.8, -0.6 

# Instantiate raw compound meshes
girl_mesh = children_spawning2.create_girl(start_x_spawn, door_z)
boy_mesh, football = children_spawning2.create_boy(start_x_spawn, door_z)

# Bind structural mechanics to decoupled independent class systems
girl_engine = GirlController(girl_mesh, start_x_spawn, door_z, g_target_x, g_target_z, speed_step)
boy_engine = BoyController(boy_mesh, football, start_x_spawn, door_z, b_target_x, b_target_z, speed_step)

start_time = time.time()
print("[MONITOR CORE]: Simulation online. Press CTRL+C in this terminal window to stop at any time.")

try:
    while True:
        rate(60)
        current_real_time = time.time()
        elapsed_seconds = current_real_time - start_time

        # Tick independent loop updates without thread blocks
        girl_engine.update(current_real_time, elapsed_seconds, speak)
        boy_engine.update(current_real_time, girl_engine.entered_room, speak)

except KeyboardInterrupt:
    print("\n[SYSTEM ALERT]: Termination signal received. Safely stopping animation loops...")
    pygame.mixer.quit()
    sys.exit(0)
