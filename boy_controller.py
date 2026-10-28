from vpython import text, vector, color, pi

class BoyController:
    def __init__(self, boy_mesh, football, start_x, door_z, target_x, target_z, speed):
        self.boy = boy_mesh
        self.football = football
        self.start_x = start_x
        self.door_z = door_z
        self.target_x = target_x
        self.target_z = target_z
        
        # Calculate steps
        self.b_steps = int(abs(target_x - start_x) / speed)
        self.b_curr_step = 0
        
        # State Flags
        self.allowed_to_spawn = False
        self.spawn_timestamp = None
        self.spawned = False
        self.entered_room = False
        self.entry_timestamp = None
        self.ball_dropped = False
        self.rotated = False
        self.exiting = False
        
        # Non-blocking Speech Engine variables
        self.speaking_state = 0  
        self.speech_timer = 0
        self.text_banner = None

    def update(self, current_real_time, girl_entered, speak_func):
        # 1. Trigger Scheduling Post Girl Threshold Cross
        if girl_entered and not self.allowed_to_spawn:
            self.spawn_timestamp = current_real_time + 30.0
            self.allowed_to_spawn = True
            print("[MONITOR]: Scheduled boy spawn for 30s post-girl entry.")

        # 2. Sequential Delay Spawning Trigger
        if self.allowed_to_spawn and not self.spawned and current_real_time >= self.spawn_timestamp:
            self.boy.visible = True
            self.football.visible = True
            # Match football starting alignment relative to compound position
            self.football.pos = vector(self.boy.pos.x + 0.25, 1.35, self.boy.pos.z + 0.05)
            print("[MONITOR]: 30s elapsed. Jim + Football spawned.")
            self.spawned = True

        if not self.spawned:
            return

        # 3. Greeting Dialogue Sequencing Logic
        if self.boy.pos.x >= -4.8 and self.speaking_state == 0:
            self.text_banner = text(text="Good Evening Jim!", pos=vector(self.boy.pos.x - 1, 2.8, self.boy.pos.z), 
                                 align='center', height=0.4, depth=0.1, color=color.blue, billboard=True)
            print("[AUDIO SPEAKER]: Monitoring System greets 'Good Evening Jim!'")
            speak_func("monitor_evening_jim.mp3", "Good Evening Jim")
            self.speaking_state = 1
            self.speech_timer = current_real_time

        elif self.speaking_state == 1 and (current_real_time - self.speech_timer >= 1.5):
            print("[AUDIO SPEAKER]: Boy replies 'Good Evening!'")
            speak_func("boy_reply.mp3", "Good Evening")
            self.speaking_state = 2
            self.speech_timer = current_real_time

        elif self.speaking_state == 2 and (current_real_time - self.speech_timer >= 1.5):
            self.entered_room = True
            self.speaking_state = 3

        # 4. Ball Drop Milestone Check
        if self.b_curr_step >= self.b_steps and not self.ball_dropped:
            self.football.pos = vector(self.target_x, 0.18, self.target_z) 
            print("[MONITOR SUCCESS]: Football dropped near sofa.")
            self.ball_dropped = True
            self.entry_timestamp = current_real_time

        # 5. 180-Degree Turning Milestone Check
        if self.ball_dropped and self.entry_timestamp and (current_real_time - self.entry_timestamp >= 5.0) and not self.rotated:
            print("[MONITOR]: 5s over. Rotating Jim 180 degrees cleanly.")
            self.boy.rotate(angle=pi, axis=vector(0, 1, 0), origin=self.boy.pos)
            self.rotated = True
            self.exiting = True
            if self.text_banner:
                self.text_banner.visible = False

        # 6. Movement Execution (No leg swing animations)
        is_walking = (self.speaking_state == 0) or (self.speaking_state == 3)

        if is_walking and not self.exiting and self.b_curr_step < self.b_steps:
            bdx = (self.target_x - self.start_x) / self.b_steps
            bdz = (self.target_z - self.door_z) / self.b_steps
            self.boy.pos.x += bdx
            self.boy.pos.z += bdz
            if self.text_banner:
                self.text_banner.pos.x += bdx
                self.text_banner.pos.z += bdz
            if not self.ball_dropped:
                self.football.pos.x += bdx
                self.football.pos.z += bdz
            self.b_curr_step += 1
            
        elif is_walking and self.exiting and self.b_curr_step > 0:
            bdx = (self.target_x - self.start_x) / self.b_steps
            bdz = (self.target_z - self.door_z) / self.b_steps
            self.boy.pos.x -= bdx
            self.boy.pos.z -= bdz
            if self.text_banner:
                self.text_banner.pos.x -= bdx
                self.text_banner.pos.z -= bdz
            self.b_curr_step -= 1
