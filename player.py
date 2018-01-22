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
        self.attackCooldown = 30;
        self.attackRange = 128;
        self.attackTimer = 0;
        self.attackDirection = 0
        self.attacking = 0;
        self.attackPoints = [[0,0],[0,0],[0,0]];
        self.dashSpeed = 6;
        self.dashCooldown = 30;
        self.dashLength = 6;
        self.dashTimer = 0;
        self.dashing = 0;
        self.bodySize = 64;
        self.nucleusSize = 16;
        self.colorPrimary = pygame.Color(color[0],color[1],color[2],255);
        self.colorSecondary = pygame.Color(color[0],color[1],color[2],140);
        self.speed = 3;
        self.mutations = {};
        self.direction = 0;
        self.alive = True;
        self.playerNum = playerNum;
        self.right = 0;
        self.left = 0;
        self.up = 0;
        self.down = 0;
        self.innerVertices = [];
        self.outerVertices = [];
        self.currentInnerVertices = [];
        self.currentOuterVertices = [];
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
        playerSurface = pygame.Surface((pygame.display.Info().current_w,pygame.display.Info().current_h))
        playerSurface.set_colorkey((0,0,0))
        playerSurface.set_alpha(self.colorSecondary.a) 
        
        if self.attacking:
            currentAttackVertices = [] 
            for i in range(3):
                currentAttackVertices.append([])
                currentAttackVertices[i].append(self.attackPoints[i][0] + self.x)
                currentAttackVertices[i].append(self.attackPoints[i][1] + self.y)

            pygame.draw.polygon(playerSurface, self.colorSecondary, currentAttackVertices)
            pygame.draw.lines(self.screen,self.colorPrimary, False, currentAttackVertices, 3)

        pygame.draw.polygon(playerSurface, self.colorSecondary, self.currentOuterVertices);
        pygame.draw.lines(self.screen, self.colorPrimary, True, self.currentOuterVertices, 3);
            
        pygame.draw.polygon(self.screen, (0,0,155), self.currentInnerVertices);
        pygame.draw.aalines(self.screen, (155,0,0), True, self.currentInnerVertices, 5);
        self.screen.blit(playerSurface,(0,0))
        
    
    def update(self):
        maxXSpeed = self.speed
        maxYSpeed = self.speed
        movementMagnitude = math.sqrt((self.left + self.right)**2 + (self.up + self.down)**2)
        if movementMagnitude > 0:
            maxXSpeed *= math.fabs(self.right + self.left)*(1/movementMagnitude)
            maxYSpeed *= math.fabs(self.up + self.down)*(1/movementMagnitude)
            self.left *= 1/movementMagnitude
            self.right*= 1/movementMagnitude
            self.up *= 1/movementMagnitude
            self.down *= 1/movementMagnitude
            

        if (self.right + self.left):
            self.xSpeed += self.acceleration * (self.right + self.left)
            if abs(self.xSpeed) > maxXSpeed:
                self.xSpeed = math.copysign(maxXSpeed,self.xSpeed)
        else:
            if self.xSpeed > 0 - self.acceleration and self.xSpeed < 0 + self.acceleration:
                self.xSpeed = 0
            else:
                self.xSpeed -= math.copysign(self.acceleration, self.xSpeed)
        if (self.up + self.down):
            self.ySpeed += self.acceleration * (self.up + self.down)
            if abs(self.ySpeed) > maxYSpeed:
                self.ySpeed = math.copysign(maxYSpeed,self.ySpeed)
        else:
            if self.ySpeed > 0 - self.acceleration and self.ySpeed < 0 + self.acceleration:
                self.ySpeed = 0
            else:
                self.ySpeed -= math.copysign(self.acceleration, self.ySpeed)
        
        prevX = self.x;
        prevY = self.y;

        self.x += self.xSpeed
        self.y += self.ySpeed

        if self.dashing:
            self.dashing -= 1
            self.x += self.xSpeed * self.dashSpeed
            self.y += self.ySpeed * self.dashSpeed

        if self.xSpeed == 0 and self.ySpeed == 0:
            self.stretch = 0;
        else:
            if self.xSpeed == 0:
                self.direction = math.radians(270) if self.ySpeed < 0 else math.radians(90)
            else:
                self.direction = math.atan2(self.ySpeed,self.xSpeed)
            self.stretch = math.sqrt(self.xSpeed**2+self.ySpeed**2)


        if self.x < self.settings.arena_x + 32 : 
            self.x = self.settings.arena_x +  32
            self.xSpeed -= self.xSpeed//4
        elif self.x > self.settings.arena_x + self.settings.arena_dimension - 32:
            self.x =  self.settings.arena_x + self.settings.arena_dimension - 32
            self.xSpeed = self.xSpeed//4

        if self.y < 32 : 
            self.y = 32
            self.ySpeed -= self.ySpeed//4
        elif self.y > self.settings.arena_dimension - 32:
            self.y = self.settings.arena_dimension - 32
            self.ySpeed -= self.ySpeed//4
    
        
        self.nucleusX = self.x - (self.xSpeed / self.speed)*8
        self.nucleusY = self.y - (self.ySpeed / self.speed)*8 

        self.calculateVectors()


        self.currentInnerVertices = [];
        self.currentOuterVertices = [];

        for i in range(36):
            self.currentInnerVertices.append([]);
            self.currentInnerVertices[i].append(self.innerVertices[i][0] + self.nucleusX);
            self.currentInnerVertices[i].append(self.innerVertices[i][1] + self.nucleusY);

            self.currentOuterVertices.append([]);
            self.currentOuterVertices[i].append(self.outerVertices[i][0] + self.x);
            self.currentOuterVertices[i].append(self.outerVertices[i][1] + self.y);

            if self.currentOuterVertices[i][0] < self.settings.arena_x:
                self.currentOuterVertices[i][0] = self.settings.arena_x
            elif self.currentOuterVertices[i][0] > self.settings.arena_x + self.settings.arena_dimension:
                self.currentOuterVertices[i][0] = self.settings.arena_x + self.settings.arena_dimension

            if self.currentOuterVertices[i][1] < 0:
                self.currentOuterVertices[i][1] = 0
            elif self.currentOuterVertices[i][1] > self.settings.arena_dimension:
                self.currentOuterVertices[i][1] = self.settings.arena_dimension


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

        if self.dashTimer > 0:
            self.dashTimer -= 1
        if self.attackTimer > 0:
            self.attackTimer -= 1
        

    def checkCollisions(self, other):
        if self.attacking > 0:
            if math.sqrt((self.attackPoints[1][0] + self.x - other.nucleusX)**2 + (self.attackPoints[1][1] + self.y - other.nucleusY)**2)<other.nucleusSize:
                other.kill()
                self.attacking *= -1

        moveDirection = math.atan2(self.y - other.y,self.x - other.x)
        if math.sqrt((self.x - other.x)**2 + (self.y - other.y)**2)<self.bodySize * 1.5:
            moveDistance = (self.bodySize * 1.5)-(math.sqrt((self.x - other.x)**2 + (self.y - other.y)**2))
            self.x += math.cos(moveDirection) * moveDistance
            self.y += math.sin(moveDirection) * moveDistance
        for point in self.currentOuterVertices:
            if math.sqrt((point[0] - other.x)**2 + (point[1] - other.y)**2)<other.bodySize:
                moveDistance = ((other.bodySize) - (math.sqrt((point[0] - other.x)**2 + (point[1] - other.y)**2)))/2
                point[0] += math.cos(moveDirection) * moveDistance
                point[1] += math.sin(moveDirection) * moveDistance


    def dash(self):
        if self.dashTimer == 0:
            self.dashing = self.dashLength
            self.dashTimer = self.dashCooldown


    def attack(self):
        if self.attackTimer == 0:
            attackStartDistance = self.bodySize - (self.bodySize // 4)
            spikeWidth = math.radians(10)
            self.attackDirection = math.degrees(self.direction)
            self.attackDirection = math.radians(round(self.attackDirection / 10) * 10)
            self.attackPoints = []
            self.attackPoints.append([round(math.cos(self.attackDirection - spikeWidth) * attackStartDistance),round(math.sin(self.attackDirection-spikeWidth)*attackStartDistance)])
            self.attackPoints.append([round(math.cos(self.attackDirection) * attackStartDistance),round(math.sin(self.attackDirection)*attackStartDistance)])
            self.attackPoints.append([round(math.cos(self.attackDirection + spikeWidth) * attackStartDistance),round(math.sin(self.attackDirection+spikeWidth)*attackStartDistance)])
            self.attacking = 1
            self.attackTimer = self.attackCooldown
        
            
    def kill(self):
         self.living = False
         self.settings.living_players -= 1

    def respawn(self):
        self.alive = True
        self.x = self.settings.arena_x + 50 + (200 * self.playerNum)
        self.y = 50  + (400 * self.playerNum)
        self.settings.living_players += 1

            
        
        
