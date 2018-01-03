import pygame
import math

class Player:
    
    def __init__(self,screen, playerNum, color, startX, startY, controlType):
        self.x = startX;
        self.y = startY;
        self.xSpeed = 0;
        self.ySpeed = 0;
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
        self.right = 0;
        self.left = 0;
        self.up = 0;
        self.down = 0;
        self.vertices = [];
        self.controlType = controlType #keyboard/joystick
        
        
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
            
        pygame.draw.polygon(self.screen, (0,0,255), currentVertices);
        pygame.draw.lines(self.screen, self.color, True, currentVertices, 2);
        
    
    def update(self):
        xSpeed = self.right + self.left;
        ySpeed = self.up + self.down;
        maxSpeed = self.speed
        if math.fabs(xSpeed + ySpeed) == 2:
            maxSpeed = math.floor(maxSpeed*0.7 + 0.5);
            
        self.x += xSpeed*maxSpeed;
        self.y += ySpeed*maxSpeed;        
        
        
    
        
