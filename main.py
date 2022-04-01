import math
import time
import pygame

clock = pygame.time.Clock()
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


def MakePlatform(x, y):
    Display.blit(platform, (x, y))


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
    if PlusOrMinus == '+':
        if Portal == 'Red':
            Adjusted = 0
            CharacterX = RedPortal[0][1][0]
            CharacterY = RedPortal[0][1][1]

        else:
            Adjusted = 0
            CharacterX = BluePortal[0][1][0]
            CharacterY = BluePortal[0][1][1]
    else:
        if Portal == 'Red':
            Adjusted = 0
            CharacterX = RedPortal[0][1][0]
            CharacterY = RedPortal[0][1][1]
        else:
            Adjusted = 0
            CharacterX = BluePortal[0][1][0]
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
def Level1():
    global centerX, centerY, PossibleMovementCoords, seconds
    PossibleMovementCoords.clear()
    MakePlatform(centerX - 275, centerY - 150)
    PossibleMovementCoords.append((centerX - 275, centerY - 150))
    MakePlatform(centerX + 300, centerY + 50)
    PossibleMovementCoords.append((centerX + 300, centerY + 50))
    MakePlatform(centerX + 800, centerY - 75)
    PossibleMovementCoords.append((centerX + 800, centerY - 75))
    MakePlatform(centerX + 1050, centerY + 150)
    PossibleMovementCoords.append((centerX + 1050, centerY + 150))
    MakePlatform(centerX + 1400, centerY - 175)
    PossibleMovementCoords.append((centerX + 1400, centerY - 175))
    MakePlatform(centerX + 1850, centerY + 50)
    PossibleMovementCoords.append((centerX + 1850, centerY + 50))
    MakePlatform(centerX + 2450, centerY)
    PossibleMovementCoords.append((centerX + 2450, centerY))
    # Example of disappearing platform
    # if seconds<=5:
    #     MakePlatform(centerX+300,centerY+50)
    #     PossibleMovementCoords.append((centerX + 300, centerY + 50))
    seconds += 0.01


def dead():
    Death = font.render("You died", True, black)
    Display.blit(Death, (300, 250))
    pygame.display.update()
    time.sleep(3)
    quit()


Adjusted = 0


def checkKey():
    global centerX, centerY, CharacterDirection, PossibleMovementCoords, CharacterX, CharacterY, variation, RedPortal, BluePortal, Adjusted, StartIndex, EscapeIndex, totalMove, AdjustDistance, TotalDistance
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

            # Code for adjusting view
            # if Adjusted > -10:
            #     if event.key == pygame.K_UP:
            #         totalMove -= 1
            #         Adjusted -= 1
            #         centerX += 40
            #         CharacterX += 40
            #         if len(RedPortal) > 0:
            #             RedPortal[0][1][0] += 40
            #         if len(BluePortal) > 0:
            #             BluePortal[0][1][0] += 40
            # if Adjusted < 10:
            #     if event.key == pygame.K_DOWN:
            #         totalMove += 1
            #         Adjusted += 1
            #         centerX -= 40
            #         CharacterX -= 40
            #         if len(RedPortal) > 0:
            #             RedPortal[0][1][0] -= 40
            #         if len(BluePortal) > 0:
            #             BluePortal[0][1][0] -= 40


            for Coord in PossibleMovementCoords:
                CoordX = Coord[0]
                CoordY = Coord[1]
                if CharacterY + 85 >= CoordY and CoordY - 30 >= CharacterY:
                    # If and elif for moving player if it's possible
                    if CharacterX - 10 >= CoordX and CharacterX + 30 <= CoordX + Platform.width:
                        if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                            if len(RedPortal) > 0:
                                RedPortal[0][1][0] += 10
                            if len(BluePortal) > 0:
                                BluePortal[0][1][0] += 10
                            centerX += 10
                            CharacterDirection = 'left'
                            TotalDistance-=10
                            break
                        elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                            if len(RedPortal) > 0:
                                RedPortal[0][1][0] -= 10
                            if len(BluePortal) > 0:
                                BluePortal[0][1][0] -= 10
                            centerX -= 10
                            CharacterDirection = 'right'
                            TotalDistance += 10
                            break
                    # Following two elif statements are exceptions for movement when player is at the edge of a platform
                    elif CharacterX - 10 >= CoordX and CharacterX  <= CoordX + Platform.width+15:

                        if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                            if len(RedPortal) > 0:
                                RedPortal[0][1][0] += 10
                            if len(BluePortal) > 0:
                                BluePortal[0][1][0] += 10
                            centerX += 10
                            CharacterDirection = 'left'
                            TotalDistance -= 10
                            break
                    elif CharacterX + 30 <= CoordX + Platform.width and CharacterX >= CoordX-15:
                        if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                            if len(RedPortal) > 0:
                                RedPortal[0][1][0] -= 10
                            if len(BluePortal) > 0:
                                BluePortal[0][1][0] -= 10
                            centerX -= 10
                            TotalDistance += 10
                            CharacterDirection = 'right'
                            break
            if len(RedPortal) > 0 and len(BluePortal) > 0:
                if CharacterDirection == 'right':
                    if CharacterX + 29 >= RedPortal[0][1][0] and CharacterX + 29 <= RedPortal[0][1][0] + 28:
                        if CharacterY <= RedPortal[0][1][1] + 50 and CharacterY + 50 >= RedPortal[0][1][1]:
                            teleport('Blue', '+')
                            # Adjusted = 0
                            # CharacterX = BluePortal[0][1][0]+20
                            # CharacterY = BluePortal[0][1][1]
                    elif CharacterX + 29 >= BluePortal[0][1][0] and CharacterX + 29 <= BluePortal[0][1][0] + 28:
                        if CharacterY <= BluePortal[0][1][1] + 50 and CharacterY + 50 >= BluePortal[0][1][1]:
                            teleport('Red', '+')
                            # Adjusted = 0
                            # CharacterX = RedPortal[0][1][0]+20
                            # CharacterY = RedPortal[0][1][1]
                elif CharacterDirection == 'left':
                    if CharacterX >= RedPortal[0][1][0] and CharacterX <= RedPortal[0][1][0] + 28:
                        if CharacterY <= RedPortal[0][1][1] + 50 and CharacterY + 50 >= RedPortal[0][1][1]:
                            teleport('Blue', '-')
                            # Adjusted = 0
                            # CharacterX = BluePortal[0][1][0]-20
                            # CharacterY = BluePortal[0][1][1]
                    elif CharacterX >= BluePortal[0][1][0] and CharacterX <= BluePortal[0][1][0] + 28:
                        if CharacterY <= BluePortal[0][1][1] + 50 and CharacterY + 50 >= BluePortal[0][1][1]:
                            teleport('Red', '-')
                            # Adjusted = 0
                            # CharacterX = RedPortal[0][1][0]-20
                            # CharacterY = RedPortal[0][1][1]

            if event.key == pygame.K_2:
                variation = 'red'
            if event.key == pygame.K_3:
                variation = 'blue'
            if event.key == pygame.K_1:
                variation = 'default'
        elif event.type == pygame.MOUSEBUTTONDOWN:
            addPortal()

        #Code for auto adjust
        adjust(-1*AdjustDistance)
        AdjustDistance = 0

# def addPortal():
#     global variation, RedPortal, BluePortal
#     if variation == 'red':
#         RedPortal.clear()
#         RedPortal.append((redPortal, list(pygame.mouse.get_pos())))
#     elif variation == 'blue':
#         BluePortal.clear()
#         BluePortal.append((bluePortal, list(pygame.mouse.get_pos())))
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


font = pygame.font.Font('freesansbold.ttf', 32)
while Win == False:
    clock.tick(100)
    # seconds+=0.01
    text = font.render(str(math.floor(seconds)), True, black)
    Display.blit(text, (650, 50))

    makeCursor()
    checkKey()

    if StartIndex < 2:
        Display.blit(StarterImages[StartIndex], (0, 0))
    else:
        LoadLevel(1)
        makePortal()
        makeCharacter(CharacterDirection)

    pygame.display.update()
    pygame.display.update()
    if StartIndex > 1:
        Display.blit(background, (0, 0))
    if TotalDistance >= 2820:
        break

CurrentTime = font.render("Seconds: " + str(math.floor(seconds)), True, black)
Display.blit(CurrentTime, (300, 250))


pygame.display.update()
time.sleep(5)

