class settings:
    """存储游戏中的设置"""
    def __init__(self):
        self.screen_width = 1200
        self.screen_height = 600
        self.bg_color = (230, 230, 230)

        self.ship_limit = 3

        self.bullet_color = (60, 60, 60)
        self.bullet_width = 100
        self.bullet_height = 15
        self.bullet_number_allowed = 3

        self.alien_drop_speed = 10

        self.speedup_scale = 2  # 加速游戏节奏
        self.init_dynamic_settings()

    def init_dynamic_settings(self):
        self.ship_speed = 1.5
        self.bullet_speed = 1
        self.alien_speed = 1.0

        self.alien_direction = 1  # 1表示右 -1表示左

    def increase_speed(self):
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale