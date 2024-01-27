#soal3karting
import matplotlib.pyplot as plt
import numpy as np
class Game:
    def __init__(self):
        self.health = dict()
        self.score = dict()
        self.name = []
        self.cards = {}
    def Add_Player(self, Name, Health):
        self.name.append(Name)
        self.health[Name] = int(Health)
        self.score[Name] = 0
    def Add_Card(self, Name, Damage):
        self.cards[Name] = int(Damage)
    def Play(self, card1, card2):
        self.health[self.name[0]] -= self.cards[card2]
        self.health[self.name[1]] -= self.cards[card1]
        if self.cards[card1] > self.cards[card2]:
            self.score[self.name[0]] += 1
        elif self.cards[card1] < self.cards[card2] :    
            self.score[self.name[1]] += 1   
game = Game()
try:
    player1, player2 = input().split()
    health1, health2 = map(int, input().split())
    damage1, damage2, damage3 = map(int, input().split())
    game1_card1, game1_card2 = input().split()
    game2_card1, game2_card2 = input().split()
    game3_card1, game3_card2 = input().split()
    game.Add_Player(player1, health1)
    game.Add_Player(player2, health2)
    game.Add_Card('A', damage1)
    game.Add_Card('B', damage2)
    game.Add_Card('C', damage3)
    game.Play(game1_card1, game1_card2)
    game.Play(game2_card1, game2_card2)
    game.Play(game3_card1, game3_card2)
    text = f'{game.name[0]} -> Score: {game.score[game.name[0]]}, Health: {game.health[game.name[0]]}\n{game.name[1]} -> Score: {game.score[game.name[1]]}, Health: {game.health[game.name[1]]}'
    f = open("result.txt","w+")
    with open('result.txt', 'w') as f:
        f.writelines(text)
    print(text)
except:
    print('Invalid Command.')
xpoints = np.array(game.name)
ypoints = np.array([point for point in game.score.values()])
plt.plot(xpoints, ypoints, 'o')
plt.show()
plt.draw()
#clean_code