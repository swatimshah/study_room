from vpython import text, vector, color, pi

class GirlController:
    def __init__(self, girl_mesh, start_x, door_z, target_x, target_z, speed):
        self.girl = girl_mesh
        self.start_x = start_x
        self.door_z = door_z
        self.target_x = target_x
        self.target_z = target_z
        
        # Calculate steps
        self.g_steps = int(abs(target_x - start_x) / speed)
        self.g_curr_step = 0
        
        # State Flags
        self.spawned = False
        self.entered_room = False
        self.entry_timestamp = None
        self.rotated = False
        self.exiting = False
        
        # Non-blocking Speech Engine variables
        self.speaking_state = 0  
        self.speech_timer = 0
        self.text_banner = None

    def update(self, current_real_time, elapsed, speak_func):
        # 1. Spawning Automation Trigger
        if elapsed >= 5.0 and not self.spawned:
            self.girl.visible = True
            print("[MONITOR]: Target 1 (Swati) initialized outside door.")
            self.spawned = True

        if not self.spawned:
            return

        # 2. Greeting Dialogue Sequencing Logic
        if self.girl.pos.x >= -4.8 and self.speaking_state == 0:
            self.text_banner = text(text="Good Afternoon Swati!", pos=vector(self.girl.pos.x - 1, 3.2, self.girl.pos.z), 
                                   align='center', height=0.4, depth=0.1, color=color.green, billboard=True)
            print("[AUDIO SPEAKER]: Monitoring System greets 'Good Afternoon Swati!'")
            speak_func("monitor_afternoon.mp3", "Good Afternoon Swati")
            self.speaking_state = 1
            self.speech_timer = current_real_time

        elif self.speaking_state == 1 and (current_real_time - self.speech_timer >= 1.5):
            print("[AUDIO SPEAKER]: Girl replies 'Good Afternoon!'")
            speak_func("girl_reply.mp3", "Good Afternoon")
            self.speaking_state = 2
            self.speech_timer = current_real_time

        elif self.speaking_state == 2 and (current_real_time - self.speech_timer >= 1.5):
            self.entered_room = True
            self.entry_timestamp = current_real_time
            self.speaking_state = 3

        # 3. 180-Degree Turning Milestone Check
        if self.entered_room and (current_real_time - self.entry_timestamp >= 5.0) and not self.rotated:
            print("[MONITOR]: 5s over. Rotating Swati 180 degrees cleanly.")
            self.girl.rotate(angle=pi, axis=vector(0, 1, 0), origin=self.girl.pos)
            self.rotated = True
            self.exiting = True
            if self.text_banner:
                self.text_banner.visible = False

        # 4. Movement Execution (No leg swing animations)
        is_walking = (self.speaking_state == 0) or (self.speaking_state == 3)

        if is_walking and not self.exiting and self.g_curr_step < self.g_steps:
            dx = (self.target_x - self.start_x) / self.g_steps
            dz = (self.target_z - self.door_z) / self.g_steps
            self.girl.pos.x += dx
            self.girl.pos.z += dz
            if self.text_banner:
                self.text_banner.pos.x += dx
                self.text_banner.pos.z += dz
            self.g_curr_step += 1
            
        elif is_walking and self.exiting and self.g_curr_step > 0: 
            dx = (self.target_x - self.start_x) / self.g_steps
            dz = (self.target_z - self.door_z) / self.g_steps
            self.girl.pos.x -= dx
            self.girl.pos.z -= dz
            if self.text_banner:
                self.text_banner.pos.x -= dx
                self.text_banner.pos.z -= dz
            self.g_curr_step -= 1
