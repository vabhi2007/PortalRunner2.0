import math
import random
import time
import pygame

clock = pygame.time.Clock()
clockTick = 120
seconds = 0

pygame.init()

pygame.display.set_caption("Portal Runner")
Logo = pygame.image.load("Sprites/Logo.png")
pygame.display.set_icon(Logo)

# Basic Colors
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

StartingScreen = pygame.image.load("Sprites/Starting Screen.png")
Controls = pygame.image.load("Sprites/Controls.png")
StarterImages = [StartingScreen, Controls]
StartIndex = 0
EscapeIndex = 0
totalMove = 0

Win = False

platform = pygame.image.load("Sprites/Platform.png")
VerticalSpike = pygame.image.load("Sprites/Vertical Spikes.png")
background = pygame.image.load("Sprites/Background.png")
bluePortal = pygame.image.load("Sprites/BluePortal.png")
redPortal = pygame.image.load("Sprites/RedPortal.png")
RightCharacter = pygame.image.load("Sprites/Right.png")
LeftCharacter = pygame.image.load("Sprites/Left.png")

redPortalCoord = 0
bluePortalCoord = 0

DisplayX = 700
DisplayY = 500
Display = pygame.display.set_mode((DisplayX, DisplayY))
Display.fill(white)
pygame.mouse.set_cursor(pygame.cursors.arrow)
pygame.mouse.set_visible(False)
blueCursor = pygame.image.load("Sprites/Blue Cursor.png")
redCursor = pygame.image.load("Sprites/RedCursor.png")
defaultCursor = pygame.image.load("Sprites/DefaultCursor.png")
variation = 'default'
RedPortal = []
BluePortal = []
TotalDistance = 0

class Platform:
    width = 150
    height = 25
    color = black
class VerticalSpikes:
    width = 28
    height = 49

def MakePlatform(x, y):
    Display.blit(platform, (x, y))
    PossibleMovementCoords.append((x,y))


def LoadLevel(level):
    TotalDistance = 0
    if level == 1:
        Level1()
    pass


CharacterX = 75
CharacterY = 50
CharacterDirection = 'right'


def makeCharacter(direction):
    if direction == 'right':
        Display.blit(RightCharacter, (CharacterX, CharacterY))
    else:
        Display.blit(LeftCharacter, (CharacterX, CharacterY))


PossibleMovementCoords = []

centerX = 350
centerY = 250

AdjustDistance = 0
def teleport(Portal, PlusOrMinus):
    global Adjusted, CharacterX, CharacterY, AdjustDistance, TotalDistance
    OldCharacterX = CharacterX
    OldCharacterY = CharacterY
    TelePortAddOn = 29
    if PlusOrMinus == '+':
        if Portal == 'Red':
            Adjusted = 0
            CharacterX = RedPortal[0][1][0]+TelePortAddOn
            CharacterY = RedPortal[0][1][1]

        else:
            Adjusted = 0
            CharacterX = BluePortal[0][1][0]+TelePortAddOn
            CharacterY = BluePortal[0][1][1]
    else:
        if Portal == 'Red':
            Adjusted = 0
            CharacterX = RedPortal[0][1][0]-TelePortAddOn
            CharacterY = RedPortal[0][1][1]
        else:
            Adjusted = 0
            CharacterX = BluePortal[0][1][0]-TelePortAddOn
            CharacterY = BluePortal[0][1][1]
    NewCharacterX = CharacterX
    NewCharacterY = CharacterY
    AdjustDistance = NewCharacterX-OldCharacterX
    TotalDistance += AdjustDistance

def adjust (distance):
    global CharacterX, centerX, RedPortal, BluePortal
    CharacterX += distance
    centerX += distance
    if len(RedPortal)>0:
        RedPortal[0][1][0] += distance
    if len(BluePortal)>0:
        BluePortal[0][1][0] += distance
PossibleDeathCoord = [] #Contains x,y,width of object
Direction = 'Right'
MovingSpikeLocation = 75
def makeMovingEnemy (x,y):
    global Direction, MovingSpikeLocation
    if Direction =='Right':
        if MovingSpikeLocation < 120:
            MovingSpikeLocation+=1
        else:
            Direction = 'Left'
            MovingSpikeLocation-=1
    elif Direction =='Left':
        if MovingSpikeLocation > 0:
            MovingSpikeLocation-=1
        else:
            Direction = 'Right'
            MovingSpikeLocation+=1
    SpikeX = MovingSpikeLocation + x
    SpikeY = y - VerticalSpikes.height
    PossibleDeathCoord.append((SpikeX,SpikeY,28))
    Display.blit(VerticalSpike,(SpikeX,SpikeY))

def makeEnemy(x,y, SpikeLocation):
    SpikeX = x + SpikeLocation
    SpikeY = y - VerticalSpikes.height
    Display.blit(VerticalSpike,(SpikeX, SpikeY))
    PossibleDeathCoord.append((SpikeX,SpikeY,28))

def checkDeath():
    global PossibleDeathCoord, CharacterX, CharacterY, CharacterDirection
    for Coords in PossibleDeathCoord:
        DeathX = Coords[0]
        DeathY = Coords[1]
        DeathWidth = Coords[2]

        if CharacterY + 50 >= DeathY and CharacterY - 50 <= DeathY:
            if CharacterX + VerticalSpikes.width >= DeathX and CharacterX + VerticalSpikes.width <= DeathX + DeathWidth or CharacterX >= DeathX and CharacterX <= DeathX + VerticalSpikes.width:
                dead()
def Level1():
    global centerX, centerY, PossibleMovementCoords, seconds
    PossibleMovementCoords.clear()
    MakePlatform(centerX - 275, centerY - 150)
    makeEnemy(centerX - 275, centerY - 150, 75)
    MakePlatform(centerX + 300, centerY + 50)
    makeMovingEnemy(centerX + 300, centerY + 50)
    MakePlatform(centerX + 800, centerY - 75)
    MakePlatform(centerX + 1050, centerY + 150)
    MakePlatform(centerX + 1400, centerY - 175)
    MakePlatform(centerX + 1850, centerY + 50)
    MakePlatform(centerX + 2450, centerY)
    # Example of disappearing platform
    # if seconds<=5:
    #     MakePlatform(centerX+300,centerY+50)
    #     PossibleMovementCoords.append((centerX + 300, centerY + 50))



def dead():
    Death = font.render("You died", True, black)
    Display.blit(Death, (300, 250))
    pygame.display.update()
    time.sleep(3)
    quit()


Adjusted = 0

def checkIfOffPlatform():
    global PossibleMovementCoords, CharacterX, CharacterY, centerX
    for coord in PossibleMovementCoords:
        CoordX = coord[0]
        CoordY = coord[1]
        if CharacterY + 85 >= CoordY and CoordY - 30 >= CharacterY:
            if CharacterX >= CoordX - 40 and CharacterX <= CoordX + Platform.width + 40:
                Limit = Platform.width+CoordX
                Min = CoordX
                if CharacterX  > Limit:
                    CharacterX = Limit - 29
                    adjust(29)
                elif CharacterX  < Min:
                    CharacterX = Min
type = ''
def checkKey():
    global type, centerX, centerY, CharacterDirection, PossibleMovementCoords, CharacterX, CharacterY, variation, RedPortal, BluePortal, Adjusted, StartIndex, EscapeIndex, totalMove, AdjustDistance, TotalDistance
    #Getting events when they happen
    for event in pygame.event.get():
        #Quit if player exits
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        elif event.type == pygame.KEYDOWN:
            if StartIndex < 2:
                if event.key == pygame.K_SPACE:
                    StartIndex += 1
            if event.key == pygame.K_ESCAPE:
                if StartIndex == 1:
                    StartIndex = 5
                if EscapeIndex % 2 == 0:
                    StartIndex = 1
                EscapeIndex += 1

            for Coord in PossibleMovementCoords:
                CoordX = Coord[0]
                CoordY = Coord[1]
                if CharacterY + 85 >= CoordY and CoordY - 30 >= CharacterY:
                    # If and elif for moving player if it's possible
                    if CharacterX - 10 >= CoordX and CharacterX + 30 <= CoordX + Platform.width:
                        if event.key == pygame.K_LEFT or event.key == pygame.K_a :
                            type = "NormalLeft"
                            break
                        elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                            type = 'NormalRight'
                            break
                    # Following two elif statements are exceptions for movement when player is at the edge of a platform
                    elif CharacterX - 10 >= CoordX and CharacterX  <= CoordX + Platform.width+15:

                        if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                            type = 'EdgeLeft'
                            break
                    elif CharacterX + 30 <= CoordX + Platform.width and CharacterX >= CoordX-15:
                        if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                            type = 'EdgeRight'
                            break

            if event.key == pygame.K_2:
                variation = 'red'
            if event.key == pygame.K_3:
                variation = 'blue'
            if event.key == pygame.K_1:
                variation = 'default'
        elif event.type == pygame.MOUSEBUTTONDOWN:
            addPortal()

def move(type):
    global centerX, TotalDistance, RedPortal, CharacterDirection, PossibleMovementCoords, AdjustDistance
    moveSpeed = 1
    for platforms in PossibleMovementCoords:
        CoordX = platforms[0]
        CoordY = platforms[1]
        if CharacterY + 85 >= CoordY and CoordY - 30 >= CharacterY:
            if CharacterX - 10 >= CoordX and CharacterX + 30 <= CoordX + Platform.width:
                if type == "NormalLeft":
                    if len(RedPortal) > 0:
                        RedPortal[0][1][0] += moveSpeed
                    if len(BluePortal) > 0:
                        BluePortal[0][1][0] += moveSpeed
                    centerX += moveSpeed
                    CharacterDirection = 'left'
                    TotalDistance -= moveSpeed

                if type == 'NormalRight':
                    if len(RedPortal) > 0:
                        RedPortal[0][1][0] -= moveSpeed
                    if len(BluePortal) > 0:
                        BluePortal[0][1][0] -= moveSpeed
                    centerX -= moveSpeed
                    CharacterDirection = 'right'
                    TotalDistance += moveSpeed

            if CharacterX - 10 >= CoordX and CharacterX <= CoordX + Platform.width + 15:
                if type == 'EdgeLeft':
                    if len(RedPortal) > 0:
                        RedPortal[0][1][0] += moveSpeed
                    if len(BluePortal) > 0:
                        BluePortal[0][1][0] += moveSpeed
                    centerX += moveSpeed
                    CharacterDirection = 'left'
                    TotalDistance -= moveSpeed

            if type == 'EdgeRight':
                if CharacterX + 30 <= CoordX + Platform.width and CharacterX >= CoordX - 15:
                    if len(RedPortal) > 0:
                        RedPortal[0][1][0] -= moveSpeed
                    if len(BluePortal) > 0:
                        BluePortal[0][1][0] -= moveSpeed
                    centerX -= moveSpeed
                    TotalDistance += moveSpeed
                    CharacterDirection = 'right'

        if len(RedPortal) > 0 and len(BluePortal) > 0:

            if CharacterDirection == 'right':
                if CharacterX + 29 >= RedPortal[0][1][0] and CharacterX + 29 <= RedPortal[0][1][0] + 28:
                    if CharacterY <= RedPortal[0][1][1] + 50 and CharacterY + 50 >= RedPortal[0][1][1]:
                        teleport('Blue', '+')
                elif CharacterX + 29 >= BluePortal[0][1][0] and CharacterX + 29 <= BluePortal[0][1][0] + 28:
                    if CharacterY <= BluePortal[0][1][1] + 50 and CharacterY + 50 >= BluePortal[0][1][1]:
                        teleport('Red', '+')
            elif CharacterDirection == 'left':
                if CharacterX >= RedPortal[0][1][0] and CharacterX <= RedPortal[0][1][0] + 28:
                    if CharacterY <= RedPortal[0][1][1] + 50 and CharacterY + 50 >= RedPortal[0][1][1]:
                        teleport('Blue', '-')
                elif CharacterX >= BluePortal[0][1][0] and CharacterX <= BluePortal[0][1][0] + 28:
                    if CharacterY <= BluePortal[0][1][1] + 50 and CharacterY + 50 >= BluePortal[0][1][1]:
                        teleport('Red', '-')
    # Code for auto adjust
    adjust(-1 * AdjustDistance)
    AdjustDistance = 0
def addPortal():
    global variation, RedPortal, BluePortal, PossibleMovementCoords
    if variation == 'red':
        RedPortal.clear()
        for coord in PossibleMovementCoords:
            PlatformX = coord[0]
            PlatformY = coord[1]
            MouseX = pygame.mouse.get_pos()[0]
            if MouseX >= PlatformX+2 and MouseX <= PlatformX + Platform.width-7:
                RedPortal.append((redPortal, list((MouseX-7, PlatformY - 50))))
    elif variation == 'blue':
        BluePortal.clear()
        for coord in PossibleMovementCoords:
            PlatformX = coord[0]
            PlatformY = coord[1]
            MouseX = pygame.mouse.get_pos()[0]
            if MouseX >= PlatformX+2 and MouseX <= PlatformX + Platform.width-7:
                BluePortal.append((bluePortal, list((MouseX-7, PlatformY - 50))))


def makePortal():
    global RedPortal, BluePortal
    for item in RedPortal:
        Display.blit(item[0], item[1])
    for item in BluePortal:
        Display.blit(item[0], item[1])


def makeCursor():
    global variation
    if variation == 'red':
        Display.blit(redCursor, pygame.mouse.get_pos())
    elif variation == 'blue':
        Display.blit(blueCursor, pygame.mouse.get_pos())
    else:
        Display.blit(defaultCursor, pygame.mouse.get_pos())


font = pygame.font.Font('Fonts/CollegiateBlackFLF.ttf', 52)
while Win == False:
    clock.tick(clockTick)
    seconds+=0.00833333333
    text = font.render(str(math.floor(seconds)), True, black)
    Display.blit(text, (650, 50))

    makeCursor()
    checkKey()

    if StartIndex < 2:
        Display.blit(StarterImages[StartIndex], (0, 0))
    else:
        makePortal()
        makeCharacter(CharacterDirection)
        LoadLevel(1)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a] or keys[pygame.K_d] or keys[pygame.K_RIGHT] or keys[pygame.K_LEFT]:
            move(type)
        checkDeath()
        checkIfOffPlatform()

    pygame.display.update()
    pygame.display.update()
    if StartIndex > 1:
        Display.blit(background, (0, 0))
    if TotalDistance >= 2820:
        break

Seconds = str(math.floor(seconds))
CurrentTime = font.render("Seconds: " + Seconds, True, black)
Display.blit(CurrentTime, (170, 250))

ScoreFile = open("Scores", 'a')
ScoreFile.write(Seconds + '\n')
ScoreFile.close()
ScoreFile = open("Scores", 'r')
TempCurrentNumbers = ScoreFile.readlines()
CurrentNumbers = []
for nums in TempCurrentNumbers:
    if nums != '\n':
        CurrentNumbers.append(int(nums))

HighScore = 100000
for values in CurrentNumbers:
    if values < HighScore:
        HighScore = values
ScoreFile.close()
CurrentHighScore = font.render("High Score: " + str(HighScore), True, black)
Display.blit(CurrentHighScore, (170, 150))

pygame.display.update()
time.sleep(5)

#Find how to use text input instead of keydown and keyup