#import pygame
from theSettlers.player import Player

class GameRunner:
    def __init__(self, numPlayers):

        self.players = []
        for i in range(numPlayers):
            self.players.append(Player(game=self, num=i))