import pygame
from fontz import fontz
from globals import game
from random import randint
clock = pygame.time.Clock()
class MainTips:
    def __init__(self):
        self.tips = [

            "Try not to die",
            "Every time you die, a day passes.",
            "If you die in the game, you don't die in real life.",
            "You always have a sword and a bow.",
            "Leveling up gives you HP, gold and armor",
            "WTF why you have a hunter in your pocket? - Jenda 2020",
            "This game was developed in pygame!",
            "You can only take 12 items with you in the battle.",
            "Leaving a dungeon before finishing will reset the doors.",
            "In the market you can buy items which will go to your inventory.",
            "Right click on an item in the inventory to send it to the battle inventory.",
            "If you keep losing battles, try visiting the blacksmith to upgrade your weapons.",
            "Visit the training grounds to improve your hero stats.",
            "If you run out of gold, try doing some quests, they pay the best!",
            "In the character menu you can check your hero stats and inventory. ",
            "In the tavern you can get quests, which gives you gold in return.",
            "In the tavern you can check bounties, if you fulfill them, you get gold!",
            "In the tavern you can check the bulletin, there will be the most wanted enemies!",
            "Deception can turn one enemy against the others.",
            "Perception can tell you when to use the shield to be effective at most.",
            "Some enemies are stronger than others, keep that in mind during battles.",
            "You can check your quests in My Quests.",
            "Some things are unlocked by increasing your character level.",
            "You can increase inventory slots by leveling up!",
            "text",
            "text",
        ]
        self.tip = self.tips[randint(0, 20)]

    def draw(self):
        game.screen.blit(fontz.old_font_15.render("Tip: " + self.tip, True, game.white), (20, 220))

tips = MainTips()