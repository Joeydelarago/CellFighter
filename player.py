import pygame

class Player:
    
    def __init__(self, screen, playerNum, color, startX, startY):
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
        self.vertices = [[0,0]]*12;
        self.controlType = "keyboard"//joystick;
    
    
    def calculateVectors():
        for i in range(12):
            radians = math.radians(i * 30);
            self.vertices[i][0] = math.cos(radians);
            self.vertices[i][1] = math.sin(radians);
    
    
    def draw():
        currentVertices = [[0,0]]*12;
        for i in range(12):
            currentVertices[i][0] = self.vertices[i][0] + self.x;
            currentVertices[i][1] = self.vertices[i][1] + self.y;
            pygame.draw.lines(self.screen, True, (255,255,255), currentVertices, 1);
        
    
        
