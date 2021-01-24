import pygame

class Buttons:
    def __init__(self):
        self.new_game_menu_button = pygame.Rect(295, 265, 200, 50)
        self.new_game_menu_button = pygame.Rect(295, 265, 200, 50)
        self.options_menu_button = pygame.Rect(295, 365, 200, 50)
        self.credits_menu_button = pygame.Rect(295, 465, 200, 50)
        self.quit_menu_button = pygame.Rect(295, 565, 200, 50)
        # Buttons Riverwood
        self.first_left_button = pygame.Rect(140, 350, 200, 50)
        self.second_left_button = pygame.Rect(140, 420, 200, 50)
        self.third_left_button = pygame.Rect(140, 490, 200, 50)
        self.fourth_left_button = pygame.Rect(140, 565, 200, 50)
        self.first_right_button = pygame.Rect(390, 350, 200, 50)
        self.second_right_button = pygame.Rect(390, 420, 200, 50)
        self.third_right_button = pygame.Rect(390, 490, 200, 50)
        self.fourth_right_button = pygame.Rect(390, 565, 200, 50)
        self.dungeon_button = pygame.Rect(600, 490, 130, 65)
        self.map_button = pygame.Rect(600, 560, 195, 70)
        # Buttons Blacksmith
        self.upgrade_sword_button = pygame.Rect(150, 510, 125, 80)
        self.upgrade_armor_button = pygame.Rect(307, 510, 125, 80)
        self.upgrade_bow_button = pygame.Rect(465, 510, 125, 80)
        self.upgrade_arrows_button = pygame.Rect(622, 510, 125, 80)
        self.back_button_left = pygame.Rect(0, 595, 130, 55)
        self.sword_info = pygame.Rect(175, 380, 75, 75)
        self.armor_info = pygame.Rect(325, 380, 75, 75)
        self.bow_info = pygame.Rect(490, 380, 75, 75)
        self.arrow_info = pygame.Rect(640, 380, 75, 75)
        # Buttons Market
        self.market_button_01 = pygame.Rect(140, 380, 200, 50)   # First row
        self.market_button_02 = pygame.Rect(140, 450, 200, 50)
        self.market_button_03 = pygame.Rect(140, 520, 200, 50)
        self.market_button_04 = pygame.Rect(140, 590, 200, 50)
        self.market_button_05 = pygame.Rect(370, 380, 200, 50)   # Second row
        self.market_button_06 = pygame.Rect(370, 450, 200, 50)
        self.market_button_07 = pygame.Rect(370, 520, 200, 50)
        self.market_button_08 = pygame.Rect(370, 590, 200, 50)
        self.market_button_09 = pygame.Rect(600, 380, 200, 50)   # Third row
        self.market_button_10 = pygame.Rect(600, 450, 200, 50)
        self.market_button_11 = pygame.Rect(600, 520, 200, 50)
        self.market_button_12 = pygame.Rect(600, 590, 200, 50)
        # Character button
        self.char_button_01 = pygame.Rect(140, 100, 195, 50)
        self.char_button_02 = pygame.Rect(140, 175, 195, 50)
        self.char_button_03 = pygame.Rect(365, 70, 195, 50)
        self.char_button_04 = pygame.Rect(365, 140, 195, 50)
        self.char_button_05 = pygame.Rect(365, 210, 195, 50)
        self.char_button_06 = pygame.Rect(590, 70, 195, 50)
        self.char_button_07 = pygame.Rect(590, 140, 195, 50)
        self.char_button_08 = pygame.Rect(590, 210, 195, 50)
        # Tavern
        self.quest_button = pygame.Rect(140, 325, 195, 50)
        self.bounties_button = pygame.Rect(360, 325, 195, 50)
        self.bulletin_button = pygame.Rect(580, 325, 195, 50)
        # battle screen
        self.first_enemy = pygame.Rect(140, 55, 212, 268)
        self.second_enemy = pygame.Rect(352, 55, 212, 268)
        self.third_enemy = pygame.Rect(564, 55, 212, 268)
        self.sword = pygame.Rect(221, 352, 122, 100)
        self.bow = pygame.Rect(384, 352, 122, 100)
        # Training field
        self.first_button = pygame.Rect(150, 360, 260, 80)
        self.second_button = pygame.Rect(150, 455, 260, 80)
        self.third_button = pygame.Rect(150, 550, 260, 80)
        self.fourth_button = pygame.Rect(430, 360, 260, 80)
        self.fifth_button = pygame.Rect(430, 455, 260, 80)
        self.sixth_button = pygame.Rect(430, 550, 260, 80)
        # Events buttons
        self.choice_1 = pygame.Rect(220, 258, 200, 20)
        self.choice_2 = pygame.Rect(220, 296, 200, 20)
        self.event_return = pygame.Rect(660, 295, 90, 35)
        # LC Render buttons
        self.my_quests_button = pygame.Rect(15, 412, 100, 20)
        self.my_bounties_button = pygame.Rect(5, 453, 110, 20)


buttons = Buttons()

class MapLocations:
    def __init__(self):
        self.one = pygame.Rect(470, 70, 30, 30)

map_locations = MapLocations()