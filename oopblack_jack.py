import random
class Card:
    def __init__(self, rank: str, suit: str) -> None:
        self.rank = rank
        self.suit = suit

    def get_value(self) -> int:
        if self.rank in "TVDK":
            return 10
        else:
            return " A23456789".index(self.rank)
    
    def get_rank(self):
        return f"{self.suit}{self.rank}"

class DeskCard:
    def __init__(self):
        _rank = " A23456789TVDK"
        _suit = "ПБЧК"
        self.__cards = [Card(r,s) for s in _suit for r in _rank]
        random.shuffle(self.__cards)

    def get_card(self) -> Card:
        return self.__cards.pop()

class Gamer:
    def __init__(self, name: str) -> None:
        self._hand = []
        self.count = 0
        self.name = name

    @property
    def hand(self):
        return f" Карты на руках {self._hand} очков {self.count}"

    @hand.setter
    def hand(self, card: Card):
        self.count += card.get_value()
        self._hand.append(card.get_rank())

class Play:
    def __init__(self, player_name):
        self.cards = DeskCard()
        self.gamer = Gamer(name = player_name)

    def start(self):
        self.gamer.hand = self.cards.get_card()
        self.gamer.hand = self.cards.get_card()
        print(self.gamer.hand)

def main():
    name = input("You name please ")
    game = Play(name)
    game.start()

if __name__ == "__main__":
    main()


