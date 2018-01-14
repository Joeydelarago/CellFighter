import pygame
import math

class Player:
    
    def __init__(self,screen, settings, playerNum, color, startX, startY, controllerID):
        self.x = startX;
        self.y = startY;
        self.nucleusOffsetX = 0;
        self.nucleusOffsetY = 0;
        self.acceleration = 0.5;
        self.stretch = 0;
        self.direction = 0;
        self.xSpeed = 0;
        self.ySpeed = 0;
        self.screen = screen;
        self.settings = settings;
        self.attackFrames = 16;
        self.attackCooldown = 60;
        self.attackRange = 128;
        self.attackTimer = 0;
        self.attackDirection = 0
        self.attacking = 0;
        self.attackPoints = [[0,0],[0,0],[0,0]]
        self.bodySize = 64;
        self.nucleusSize = 16;
        self.colorPrimary = pygame.Color(color[0],color[1],color[2],255);
        self.colorSecondary = pygame.Color(color[0],color[1],color[2],140);
        self.speed = 3;
        self.mutations = {};
        self.direction = 0;
        self.playerNum = playerNum;
        self.right = 0;
        self.left = 0;
        self.up = 0;
        self.down = 0;
        self.innerVertices = [];
        self.outerVertices = [];
        self.controllerID = controllerID; #keyboard/joystick
        
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
        playerSurface = pygame.Surface((pygame.display.Info().current_w,pygame.display.Info().current_h))
        playerSurface.set_colorkey((0,0,0))
        playerSurface.set_alpha(self.colorSecondary.a) 
        for i in range(36):
            currentInnerVertices.append([]);
            currentInnerVertices[i].append(self.innerVertices[i][0] + self.x - self.nucleusOffsetX);
            currentInnerVertices[i].append(self.innerVertices[i][1] + self.y - self.nucleusOffsetY);

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


        pygame.draw.polygon(playerSurface, self.colorSecondary, currentOuterVertices);
        pygame.draw.lines(self.screen, self.colorPrimary, True, currentOuterVertices, 3);
            
        if self.attacking:
            currentAttackVertices = [] 
            for i in range(3):
                currentAttackVertices.append([])
                currentAttackVertices[i].append(self.attackPoints[i][0] + self.x)
                currentAttackVertices[i].append(self.attackPoints[i][1] + self.y)

            pygame.draw.polygon(playerSurface, self.colorSecondary, currentAttackVertices)
            pygame.draw.lines(self.screen,self.colorPrimary, False, currentAttackVertices, 3)

        pygame.draw.polygon(self.screen, (0,0,155), currentInnerVertices);
        pygame.draw.aalines(self.screen, (155,0,0), True, currentInnerVertices, 5);
        self.screen.blit(playerSurface,(0,0))
        
    
    def update(self):
        maxSpeed = self.speed
        if abs(self.left + self.right) + abs(self.up + self.down) == 2:
            maxSpeed = maxSpeed*0.7;

        if (self.right + self.left):
            self.xSpeed += self.acceleration * (self.right + self.left)
            if abs(self.xSpeed) > maxSpeed:
                self.xSpeed = math.copysign(maxSpeed,self.xSpeed)
        else:
            if self.xSpeed > 0 - self.acceleration and self.xSpeed < 0 + self.acceleration:
                self.xSpeed = 0
            else:
                self.xSpeed -= math.copysign(self.acceleration, self.xSpeed)
        if (self.up + self.down):
            self.ySpeed += self.acceleration * (self.up + self.down)
            if abs(self.ySpeed) > maxSpeed:
                self.ySpeed = math.copysign(maxSpeed,self.ySpeed)
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
                self.direction = math.radians(270) if self.ySpeed < 0 else math.radians(90)
            elif self.ySpeed == 0 :
                self.direction = math.radians(180) if self.xSpeed < 0 else 0
            elif self.xSpeed > 0 and self.ySpeed > 0:
                self.direction =  math.atan(self.ySpeed/self.xSpeed)
            elif self.xSpeed > 0 and self.ySpeed < 0:
                self.direction = math.radians(360) + math.atan(self.ySpeed/self.xSpeed)
            elif self.xSpeed < 0 and self.ySpeed > 0:
                self.direction  = math.radians(180) + math.atan(self.ySpeed/self.xSpeed)
            else:
                self.direction = math.radians(180) + math.atan(self.ySpeed/self.xSpeed)
            self.stretch = math.sqrt(self.xSpeed**2+self.ySpeed**2)


        if self.x < 32 : 
            self.x = 32
            self.xSpeed -= self.xSpeed//4
        elif self.x > self.settings.screensize[0] - 32:
            self.x = self.settings.screensize[0] - 32
            self.xSpeed = self.xSpeed//4

        if self.y < 32 : 
            self.y = 32
            self.ySpeed -= self.ySpeed//4
        elif self.y > self.settings.screensize[1] - 32:
            self.y = self.settings.screensize[1] - 32
            self.ySpeed -= self.ySpeed//4
    
        
        self.nucleusOffsetX = (self.xSpeed / maxSpeed)*8
        self.nucleusOffsetY = (self.ySpeed / maxSpeed)*8 

        self.calculateVectors()

        """if self.x != prevX or self.y != prevY:
            self.attackDirection[0] = math.copysign(1,self.x-prevX) if self.x != prevX else 0;
            self.attackDirection[1] = math.copysign(1,self.y-prevY) if self.y != prevY else 0;"""

        if self.attacking > 0:
            if self.attacking > self.attackFrames:
                self.attacking = self.attackFrames * -1
            else:
                self.attacking += 1
            self.attackPoints[1][0] += round(math.cos(self.attackDirection)*self.attackRange/self.attackFrames)
            self.attackPoints[1][1] += round(math.sin(self.attackDirection)*self.attackRange/self.attackFrames)
        elif self.attacking < 0:
            self.attacking += 1
            self.attackPoints[1][0] -= round(math.cos(self.attackDirection)*self.attackRange/self.attackFrames)
            self.attackPoints[1][1] -= round(math.sin(self.attackDirection)*self.attackRange/self.attackFrames)

        
        if self.attackTimer > 0:
            self.attackTimer -= 1;
        
    def attack(self):
        if self.attackTimer == 0:
            attackStartDistance = self.bodySize - (self.bodySize // 8)
            spikeWidth = math.radians(10)
            self.attackDirection = math.degrees(self.direction)
            self.attackDirection = math.radians(round(self.attackDirection / 10) * 10)
            self.attackPoints = []
            self.attackPoints.append([round(math.cos(self.attackDirection - spikeWidth) * attackStartDistance),round(math.sin(self.attackDirection-spikeWidth)*attackStartDistance)])
            self.attackPoints.append([round(math.cos(self.attackDirection) * attackStartDistance),round(math.sin(self.attackDirection)*attackStartDistance)])
            self.attackPoints.append([round(math.cos(self.attackDirection + spikeWidth) * attackStartDistance),round(math.sin(self.attackDirection+spikeWidth)*attackStartDistance)])
            self.attacking = 1
            self.attackTimer = self.attackCooldown
            
            
            
            
        
        
