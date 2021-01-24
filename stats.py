
class Stats:
    def __init__(self):
        self.agility = 0
        self.deception = 0
        self.perception = 0
        self.deception_level = 0
        self.perception_level = 0
        self.perception_max_level = 10
        self.strength = 0
        self.health = 50
        self.max_health = 50
        self.armor = 0
        self.defence = 0
        self.max_armor = 50
        self.exp = 0
        self.max_exp = 150
        self.level = 1
        self.gold = 50000
        self.sword_level = 0
        self.sword_max_level = 10
        self.agility_level = 0
        self.agility_max_level = 10
        self.strength_level = 0
        self.strength_max_level = 10
        self.deception_max_level = 10
        self.armor_level = 0
        self.armor_max_level = 10
        self.bow_level = 0
        self.bow_max_level = 10
        self.arrow_level = 0
        self.arrow_max_level = 10
        self.attack_level = 0
        self.attack_max_level = 10
        self.defence_level = 0
        self.defence_max_level = 10
        self.attack = float(2)
        self.arrow_attack = float(1)
        self.sword_bonus = float(1.5) + self.attack
        self.bow_bonus = float(1.5) + self.attack + self.arrow_attack
        self.day = 1

    def boost_gold(self, value):
        self.gold = self.gold + value

    def decrease_gold(self, value):
        self.gold = self.gold - value

    def boost_health(self, value):
        self.health = min(self.health + value, self.max_health)

    def boost_armor(self, value):
        self.armor = min(self.armor + value, self.max_armor)

    def decrease_armor(self, value):
        self.armor = max(self.armor - value, 0)

    def boost_max_armor(self, value):
        self.max_armor = self.max_armor + value

    def decrease_health(self, value):
        self.health = max(self.health - value, 0)

    def boost_xp(self, value):
        self.exp = value + self.exp
        if self.exp > self.max_exp:
            self.level += 1
            self.exp -= self.max_exp
            self.max_exp += 25

    def boost_attack(self, value):
        self.attack = self.attack + value

    def boost_sword_attack(self, value):
        self.sword_bonus = self.sword_bonus + value

    def boost_bow_attack(self, value):
        self.bow_bonus = self.bow_bonus + value

    def boost_agility(self, value):
        self.agility = min(self.agility_level + value, self.agility_max_level)

    def boost_strength(self, value):
        self.strength = min(self.strength_level + value, self.strength_max_level)

    def boost_deception(self, value):
        self.deception = min(self.deception_level + value, self.deception_max_level)

    def boost_perception(self, value):
        self.perception = min(self.perception_level + value, self.perception_max_level)

    def boost_day(self, value):
        self.day = self.day + value

    def boost_defence(self, value):
        self.defence = self.defence + value

    @property
    def sword_attack(self):
        return self.attack + self.sword_bonus

    @property
    def bow_attack(self):
        return self.attack + self.bow_bonus + self.arrow_attack
stats = Stats()