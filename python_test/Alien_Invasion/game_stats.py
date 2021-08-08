class Game_Stats:
    def __init__(self, aigame):
        self.settings = aigame.settings
        self.game_active = False
        self.level_button_state = True
        self.high_score = 0
        self.get_high_score()
        self.reset_stats()
    
    def get_high_score(self):
    	with open('high_score.txt') as f:
    		self.high_score = int(f.read())
    		print(self.high_score)

    def reset_stats(self):
        """游戏运行期间变化的统计信息"""
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1
