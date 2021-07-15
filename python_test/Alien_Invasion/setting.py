class settings:
    """存储游戏中的设置"""
    def __init__(self):
        self.screen_width = 1200
        self.screen_height = 600
        self.bg_color = (230, 230, 230)

        self.ship_speed = 1.5

        self.bullet_color = (60, 60, 60)
        self.bullet_speed = 1
        self.bullet_width = 100
        self.bullet_height = 15
        self.bullet_number_allowed = 3

        self.alien_speed = 1.0
        self.alien_drop_speed = 10
        self.alien_direction = 1  # 1表示右 -1表示左
