import pygame
import math

class Player:
    
    def __init__(self,screen, playerNum, color, startX, startY, controlType):
        self.x = startX;
        self.y = startY;
        self.xSpeed = 0;
        self.ySpeed = 0;
        self.screen = screen;
        self.attackCooldown = 120;
        self.attackTimer = 0;
        self.attackDirection = [0,0];
        self.attack = 1;
        self.defence = 1;
        self.bodySize = 64;
        self.nucleusSize = 16;
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
        self.active = False;
        self.innerVertices = [];
        self.outerVertices = [];
        self.controlType = controlType; #keyboard/joystick
        
        self.calculateVectors()
        
    
    def calculateVectors(self):
        for i in range(36):
            radians = math.radians(i * 10);
            self.outerVertices.append([]);
            self.outerVertices[i].append(math.floor(math.cos(radians)*self.bodySize + 0.5));
            self.outerVertices[i].append(math.floor(math.sin(radians)*self.bodySize + 0.5));
            
            self.innerVertices.append([]);
            self.innerVertices[i].append(math.floor(math.cos(radians)*self.nucleusSize + 0.5));
            self.innerVertices[i].append(math.floor(math.sin(radians)*self.nucleusSize + 0.5));

    
    def draw(self):
        currentInnerVertices = [];
        currentOuterVertices = [];
        for i in range(36):
            currentInnerVertices.append([]);
            currentInnerVertices[i].append(self.innerVertices[i][0] + self.x);
            currentInnerVertices[i].append(self.innerVertices[i][1] + self.y);

            currentOuterVertices.append([]);
            currentOuterVertices[i].append(self.outerVertices[i][0] + self.x);
            currentOuterVertices[i].append(self.outerVertices[i][1] + self.y);
            pygame.draw.rect(self.screen, self.color, [currentOuterVertices[i][0]-6,currentOuterVertices[i][1]-6,12,12]);
            
        """pygame.draw.polygon(self.screen, (0,0,255), currentOuterVertices);
        pygame.draw.aalines(self.screen, self.color, True, currentOuterVertices, 5);
            
        pygame.draw.polygon(self.screen, (0,0,155), currentInnerVertices);
        pygame.draw.aalines(self.screen, (155,0,0), True, currentInnerVertices, 5);"""
        
    
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
    
        
        if self.x != prevX or self.y != prevY:
            self.attackDirection[0] = math.copysign(1,self.x-prevX) if self.x != prevX else 0;
            self.attackDirection[1] = math.copysign(1,self.y-prevY) if self.y != prevY else 0;
        
        if self.attackTimer > 0:
            self.attackTimer -= 1;
        
    
    """def attack(self):
        if attackTimer == 0:
            spikeCenterX = 32*self.attackDirection[0]
            spikeCenterY = 32*self.attackDirection[1]
            spikeVectors = [[spikeCenterX +,0],[spikeCenterX,spikeCenterY],[0,0]]"""
            
            
            
            
        
        
