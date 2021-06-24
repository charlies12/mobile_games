class ShipClass:
    def __init__(self, affiliation, name, ship_type, armor, level):
        self.affiliation = affiliation
        self.name = name
        self.ship_type = ship_type
        self.armor = armor
        self.level = level


class ShipParameters(ShipClass):
    def __init__(self, affiliation, name, ship_type, armor, level, hp, aa, reload, evasion, cost, firepower=0, trp=0, aviation=0):
        super().__init__(affiliation, name, ship_type, armor, level)
        self.hp = hp
        self.aa = aa
        self.reload = reload
        self.evasion = evasion
        self.cost = cost
        self.firepower = firepower
        self.trp = trp
        self.aviation = aviation

    def __str__(self):
        return f"Affiliation: {self.affiliation}\n" \
               f"       Name: {self.name}\n" \
               f"  Ship type: {self.ship_type}\n" \
               f"      Armor: {self.armor}\n" \
               f"--------------------------------------------------\n" \
               f"      Level: {self.level}     |      Hp: {self.hp}        |      AA: {self.aa}\n " \
               f"    Reload: {self.reload}     | Evasion: {self.evasion}          |    Cost: {self.cost}\n" \
               f"  firepower: {self.firepower}     | Torpedo: {self.trp}           |Aviation: {self.aviation}\n"


if __name__ == '__main__':
    new_jersey = ShipParameters('Eagle Union', 'New Jersey', 'Battleship', "Heavy", 120, 10059, 451, 179, 41, 17, 473)
    shinano= ShipParameters('Sakura Empire', 'Shinano', 'Aircraft Carrier', 'Heavy', 120, 9104, 335, 133, 51, 15, 0, 0, 462)
    warspite = ShipParameters('Royal Navy', 'Warspite', 'Battleship', 'Heavy', 120, 8244, 296, 183, 34, 15, 458)
    drake = ShipParameters('Royal Navy', 'Drake', 'Heavy Cruiser', 'Medium', 120, 5828, 297, 143, 77, 15, 297, 252)
    azuma = ShipParameters('Sakura Empire', 'Azuma', 'Large Cruiser', 'Medium', 120, 7968, 238, 179, 53, 16, 323)
    fdg = ShipParameters('Iron Blood', 'Friedrich der Grosse', 'Battleship', 'Heavy', 120, 10445, 255, 168, 28, 19, 474)
    ships = [new_jersey, shinano, warspite, drake, azuma, fdg]

    for obj in ships:
        print(obj)

'''print(f"         Affiliation: {self.affiliation} Name: {self.name} Ship type: {self.ship_type}\n"\
            
      
               f"      Armor: {self.armor} Level: {self.level} Hp: {self.hp}\n " \
      
               f"         AA: {self.aa} Reload: {self.reload} Evasion: {self.evasion}\n" \

               f"       Cost: {self.cost} firepower: {self.firepower} Torpedo: {self.trp}\n" \

               f"   Aviation: {self.aviation}\n")
'''
