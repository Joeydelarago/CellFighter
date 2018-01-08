import pygame
import math

class Player:
    
    def __init__(self,screen, settings, playerNum, color, startX, startY, controlType):
        self.x = startX;
        self.y = startY;
        self.acceleration = 0.5;
        self.stretch = 0;
        self.xSpeed = 0;
        self.ySpeed = 0;
        self.screen = screen;
        self.settings = settings;
        self.attackCooldown = 120;
        self.attackTimer = 0;
        self.attackDirection = [0,0];
        self.attack = 1;
        self.defence = 1;
        self.bodySize = 64;
        self.nucleusSize = 16;
        self.color = color;
        self.speed = 3;
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
        degrees_direction = math.degrees(self.direction)
        self.outerVertices = [];
        self.innerVertices = [];
        for i in range(36):
            modifier = 1;
            radians = math.radians(i * 10);
            if self.stretch:
                angle_difference = abs(degrees_direction - (i * 10)) % 180
                if angle_difference > 90:
                    angle_difference = 180 - angle_difference;

                modifier *= 1 - angle_difference/720 * (self.stretch/3)

            self.outerVertices.append([]);
            self.outerVertices[i].append(round(math.cos(radians)*self.bodySize*(modifier)));
            self.outerVertices[i].append(round(math.sin(radians)*self.bodySize*(modifier)));
            
            self.innerVertices.append([]);
            self.innerVertices[i].append(round(math.cos(radians)*self.nucleusSize));
            self.innerVertices[i].append(round(math.sin(radians)*self.nucleusSize));


    
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

            if currentOuterVertices[i][0] < 0:
                currentOuterVertices[i][0] = 0
            elif currentOuterVertices[i][0] > self.settings.screensize[0]:
                currentOuterVertices[i][0] = self.settings.screensize[0]

            if currentOuterVertices[i][1] < 0:
                currentOuterVertices[i][1] = 0
            elif currentOuterVertices[i][1] > self.settings.screensize[1]:
                currentOuterVertices[i][1] = self.settings.screensize[1]

           # pygame.draw.rect(self.screen, self.color, [currentOuterVertices[i][0]-6,currentOuterVertices[i][1]-6,12,12]);
            
        pygame.draw.polygon(self.screen, (0,0,255), currentOuterVertices);
        pygame.draw.lines(self.screen, self.color, True, currentOuterVertices, 3);
            
        #pygame.draw.polygon(self.screen, (0,0,155), currentInnerVertices);
        #pygame.draw.aalines(self.screen, (155,0,0), True, currentInnerVertices, 5);
        
    
    def update(self):
        """maxSpeed = self.speed
        if abs(self.left + self.right) + abs(self.up + self.down) == 2:
            maxSpeed = maxSpeed*0.7;"""

        if (self.right + self.left):
            self.xSpeed += self.acceleration * (self.right + self.left)
            if abs(self.xSpeed) > self.speed:
                self.xSpeed = math.copysign(self.speed,self.xSpeed)
        else:
            if self.xSpeed > 0 - self.acceleration and self.xSpeed < 0 + self.acceleration:
                self.xSpeed = 0
            else:
                self.xSpeed -= math.copysign(self.acceleration, self.xSpeed)
        if (self.up + self.down):
            self.ySpeed += self.acceleration * (self.up + self.down)
            if abs(self.ySpeed) > self.speed:
                self.ySpeed = math.copysign(self.speed,self.ySpeed)
        else:
            if self.ySpeed > 0 - self.acceleration and self.ySpeed < 0 + self.acceleration:
                self.ySpeed = 0
            else:
                self.ySpeed -= math.copysign(self.acceleration, self.ySpeed)
        
        prevX = self.x;
        prevY = self.y;

        self.x += self.xSpeed
        self.y += self.ySpeed

   
        if self.xSpeed == 0 and self.ySpeed == 0:
            self.stretch = 0;
        else:
            if self.xSpeed == 0:
                self.direction = math.radians(90) if self.ySpeed < 0 else math.radians(270)
            else:
                self.direction = math.atan(self.ySpeed/self.xSpeed)
            self.stretch = math.sqrt(self.xSpeed**2+self.ySpeed**2)
            print(self.stretch)
            

        if self.x < 32 : 
            self.x = 32
            self.xSpeed = 0
        elif self.x > self.settings.screensize[0] - 32:
            self.x = self.settings.screensize[0] - 32
            self.xSpeed = 0

        if self.y < 32 : 
            self.y = 32
            self.ySpeed = 0
        elif self.y > self.settings.screensize[1] - 32:
            self.y = self.settings.screensize[1] - 32
            self.ySpeed = 0
    
        self.calculateVectors()
        
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
            
            
            
            
        
        
