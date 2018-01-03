import pygame
import math

class Player:
    
    def __init__(self,screen, playerNum, color, startX, startY, controlType):
        self.x = startX;
        self.y = startY;
        self.outerX = startX;
        self.outerY = startY;
        self.xSpeed = 0;
        self.ySpeed = 0;
        self.screen = screen;
        self.attackCooldown = 120;
        self.attackTimer = 0;
        self.attackDirection = [0,0];
        self.attack = 1;
        self.defence = 1;
        self.bodySize = 32;
        self.nucleusSize = 8;
        self.color = color;
        self.speed = 1;
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
        self.innerVertices = [];
        self.outerVertices = [];
        self.controlType = controlType #keyboard/joystick
        
        
        for i in range(12):
            radians = math.radians(i * 30);
            self.outerVertices.append([]);
            self.outerVertices[i].append(math.floor(math.cos(radians)*self.bodySize + 0.5));
            self.outerVertices[i].append(math.floor(math.sin(radians)*self.bodySize + 0.5));
            
            self.innerVertices.append([]);
            self.innerVertices[i].append(math.floor(math.cos(radians)*self.nucleusSize + 0.5));
            self.innerVertices[i].append(math.floor(math.sin(radians)*self.nucleusSize + 0.5));

    
    def draw(self):
        currentInnerVertices = [];
        currentOuterVertices = [];
        for i in range(12):
            currentInnerVertices.append([])
            currentInnerVertices[i].append(self.innerVertices[i][0] + self.x);
            currentInnerVertices[i].append(self.innerVertices[i][1] + self.y);
            
            currentOuterVertices.append([])
            currentOuterVertices[i].append(self.outerVertices[i][0] + self.outerX);
            currentOuterVertices[i].append(self.outerVertices[i][1] + self.outerY);
            
        pygame.draw.polygon(self.screen, (0,0,255), currentOuterVertices);
        pygame.draw.lines(self.screen, self.color, True, currentOuterVertices, 2);
            
        pygame.draw.polygon(self.screen, (0,0,155), currentInnerVertices);
        pygame.draw.lines(self.screen, (155,0,0), True, currentInnerVertices, 1);
        
    
    def update(self):
        xSpeed = self.right + self.left;
        ySpeed = self.up + self.down;
        maxSpeed = self.speed
        if math.fabs(xSpeed + ySpeed) == 2:
            maxSpeed = maxSpeed*0.7 + 0.5;
        
        prevX = self.x;
        prevY = self.y;
        
        self.x += xSpeed*maxSpeed;
        self.y += ySpeed*maxSpeed;    
        
        if math.fabs(self.x - self.outerX) > 4:
            self.outerX += (self.x - self.outerX)/2
            
        if math.fabs(self.y - self.outerY) > 4:
            self.outerY += (self.y - self.outerY)/2
        
        if self.x != prevX or self.y != prevY:
            self.attackDirection[0] = math.copysign(1,self.x-prevX) if self.x != prevX else 0;
            self.attackDirection[1] = math.copysign(1,self.y-prevY) if self.y != prevY else 0;
        
        if self.attackTimer > 0:
            self.attackTimer -= 1;
        
    
    def attack(self):
        if attackTimer == 0:
            spikeVectors = [[0,0],[32*self.attackDirection,],[0,0]]
            
            
            
            
        
        
