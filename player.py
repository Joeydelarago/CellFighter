import pygame
import math

class Player:
    
    def __init__(self,screen, playerNum, color, startX, startY, controlType):
        self.x = startX;
        self.y = startY;
        self.screen = screen;
        self.attack = 1;
        self.defence = 1;
        self.bodySize = 32;
        self.nucleusSize = 8;
        self.color = color;
        self.speed = 10;
        self.mutations = {};
        self.attackRate = 1;
        self.spikeLength = 32;
        self.parryTime = 1;
        self.direction = 0;
        self.dashCooldown = 1;
        self.playerNum = playerNum;
        self.right = False;
        self.left = False;
        self.up = False;
        self.down = False;
        self.vertices = [];
        self.controlType = controlType #keyboard/joystick
        
        self.calculateVectors()
    
    
    def calculateVectors(self):
        for i in range(12):
            radians = math.radians(i * 30);
            self.vertices.append([]);
            self.vertices[i].append(math.floor(math.cos(radians)*self.bodySize + 0.5));
            self.vertices[i].append(math.floor(math.sin(radians)*self.bodySize + 0.5));

    
    def draw(self):
        currentVertices = [];
        for i in range(12):
            currentVertices.append([])
            currentVertices[i].append(self.vertices[i][0] + self.x);
            currentVertices[i].append(self.vertices[i][1] + self.y);
        pygame.draw.lines(self.screen, self.color, True, currentVertices, 2);
        
    
        
