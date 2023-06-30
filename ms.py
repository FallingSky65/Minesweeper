import pygame as pg
from random import random, randint
import sys, math
from colorsys import hsv_to_rgb

pg.init()

theme = "classic"
LIGHTTONE = (245,245,245)
MIDTONE = (224,224,224)
DARKTONE = (158,158,158)
colorList = [(25,118,210),
             (56,142,60),
             (211,47,47),
             (123,31,162),
             (255,143,0),
             (0,121,121),
             (0,0,0),
             (79,79,72)]

mouse = (0,0)
status = "rules"
fontname = "Microsoft Sans Serif"
boardsizex = 9
boardsizey = 9
tilesize = 32
scale = tilesize/64
bombCount = 10
difficulty = "beginner"
font = pg.font.SysFont(fontname, int(18*scale))
size = width, height = boardsizex * tilesize + tilesize, boardsizey * tilesize + 3 * tilesize
screen = pg.display.set_mode(size, pg.RESIZABLE, 32)

clock = pg.time.Clock()

while status == "rules":
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
        if event.type == pg.KEYUP:
            if event.key == pg.K_ESCAPE:
                pg.quit()
                sys.exit()
        if event.type == pg.MOUSEBUTTONUP:
            if event.button == 1:
                status = "choosingTheme"
    
    screen.fill(MIDTONE)
    
    text = '''Minesweeper is a game where mines are hidden in a grid of squares. 
Safe squares have numbers telling you how many mines touch the 
square. You can use the number clues to solve the game by opening 
all of the safe squares. If you click on a mine you lose the game!

My version of Minesweeper always makes the first click safe. You 
open squares with the left mouse button and put flags on mines with
the right mouse button. Pressing the right mouse button again 
removes that flag. When you open a square that does not touch any 
mines, it will be empty and the adjacent squares will automatically 
open in all directions until reaching squares that contain numbers. 
A common strategy for starting games is to randomly click until you 
get a big opening with lots of numbers.

The three difficulty levels are Beginner (9x9 with 10 mines), 
Intermediate (16x16 with 40 mines) and Expert (30x16 with 99 mines). 
The game ends when all safe squares have been opened. A counter 
shows the number of mines without flags, and a clock shows your time 
in seconds.

Have Fun, 
-FallingSky65 (also i totally didn't steal these rules)'''
    lineNumber = 0
    lineCount = text.count("\n") + 1
    for line in text.split("\n"):    
        ruleLine = font.render(line, True, (0,0,0))
        ruleRect = ruleLine.get_rect()
        ruleRect.width = tilesize*boardsizex
        ruleRect.height = (tilesize*2 + tilesize*boardsizey)/lineCount
        ruleRect.left = tilesize//2
        ruleRect.top = lineNumber*(tilesize*2 + tilesize*boardsizey)/lineCount + tilesize//2
        screen.blit(ruleLine, ruleRect)
        lineNumber +=1
    
    pg.display.flip()
    clock.tick(60)

font = pg.font.SysFont(fontname, int(30*scale))

while status == "choosingTheme":
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
        if event.type == pg.KEYUP:
            if event.key == pg.K_ESCAPE:
                pg.quit()
                sys.exit()
        if event.type == pg.MOUSEBUTTONUP:
            if event.button == 1:
                if mY < (tilesize*3+tilesize*boardsizey)/2:
                    theme = "classic"
                elif mY >= (tilesize*3+tilesize*boardsizey)/2:
                    theme = "google"
                    LIGHTTONE = (170,215,81)
                    MIDTONE = (162,209,73)
                    DARKTONE = (74,117,44)
                    REVCOLORLIGHT = (229,194,159)
                    REVCOLORDARK = (215,184,153)
                status = "choosingDiff"
    
    screen.fill(MIDTONE)
    
    mY = pg.mouse.get_pos()[1]

    pg.draw.rect(screen, MIDTONE, pg.Rect(0,0,tilesize+tilesize*boardsizex,(tilesize*3+tilesize*boardsizey)/2))
    pg.draw.rect(screen, (162,209,73), pg.Rect(0,(tilesize*3+tilesize*boardsizey)/2,tilesize+tilesize*boardsizex,(tilesize*3+tilesize*boardsizey)/2))
    
    text = font.render("Classic Theme", True, (0,0,0))
    textRect = text.get_rect()
    textRect.centerx = tilesize*(1+boardsizex)//2
    textRect.centery = tilesize*(3+boardsizex)//4
    screen.blit(text,textRect)
    
    text = font.render("Google Minesweeper Theme", True, (0,0,0))
    textRect = text.get_rect()
    textRect.centerx = tilesize*(1+boardsizex)//2
    textRect.centery = 3*tilesize*(3+boardsizex)//4
    screen.blit(text,textRect)
    
    pg.display.flip()
    clock.tick(60)

while status == "choosingDiff":
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
        if event.type == pg.KEYUP:
            if event.key == pg.K_ESCAPE:
                pg.quit()
                sys.exit()
        if event.type == pg.MOUSEBUTTONUP:
            if event.button == 1:
                if mY < (tilesize*3+tilesize*boardsizey)/3:
                    difficulty = "beginner"
                elif mY >= (tilesize*3+tilesize*boardsizey)/3 and mY < 2*(tilesize*3+tilesize*boardsizey)/3:
                    difficulty = "intermediate"
                elif mY >= 2*(tilesize*3+tilesize*boardsizey)/3:
                    difficulty = "expert"
                status = "alive"
    
    screen.fill(MIDTONE)
    
    mY = pg.mouse.get_pos()[1]

    if mY < (tilesize*3+tilesize*boardsizey)/3:
        pg.draw.rect(screen, LIGHTTONE, pg.Rect(0,0,tilesize+tilesize*boardsizex,(tilesize*3+tilesize*boardsizey)/3))
    elif mY >= (tilesize*3+tilesize*boardsizey)/3 and mY < 2*(tilesize*3+tilesize*boardsizey)/3:
        pg.draw.rect(screen, LIGHTTONE, pg.Rect(0,(tilesize*3+tilesize*boardsizey)/3,tilesize+tilesize*boardsizex,(tilesize*3+tilesize*boardsizey)/3))
    elif mY >= 2*(tilesize*3+tilesize*boardsizey)/3:
        pg.draw.rect(screen, LIGHTTONE, pg.Rect(0,2*(tilesize*3+tilesize*boardsizey)/3,tilesize+tilesize*boardsizex,(tilesize*3+tilesize*boardsizey)/3))

    pg.draw.rect(screen, DARKTONE, pg.Rect(0,0,tilesize+tilesize*boardsizex,(tilesize*3+tilesize*boardsizey)/3), width=8)
    pg.draw.rect(screen, DARKTONE, pg.Rect(0,(tilesize*3+tilesize*boardsizey)/3,tilesize+tilesize*boardsizex,(tilesize*3+tilesize*boardsizey)/3), width = 8)
    pg.draw.rect(screen, DARKTONE, pg.Rect(0,2*(tilesize*3+tilesize*boardsizey)/3,tilesize+tilesize*boardsizex,(tilesize*3+tilesize*boardsizey)/3), width = 8)
    
    text = font.render("BEGINNER", True, (0,0,0))
    textRect = text.get_rect()
    textRect.centerx = tilesize*(1+boardsizex)//2
    textRect.centery = tilesize*(3+boardsizex)//6
    screen.blit(text,textRect)
    text = font.render("INTERMEDIATE", True, (0,0,0))
    textRect = text.get_rect()
    textRect.centerx = tilesize*(1+boardsizex)//2
    textRect.centery = tilesize*(3+boardsizex)//2
    screen.blit(text,textRect)
    text = font.render("EXPERT", True, (0,0,0))
    textRect = text.get_rect()
    textRect.centerx = tilesize*(1+boardsizex)//2
    textRect.centery = 5*tilesize*(3+boardsizex)//6
    screen.blit(text,textRect)
    
    pg.display.flip()
    clock.tick(60)

if difficulty == "beginner":
    bombCount = 10
elif difficulty == "intermediate":
    bombCount = 40
elif difficulty == "expert":
    bombCount = 99
    
if theme == "classic":
    if difficulty == "beginner":
        boardsizex, boardsizey = 9, 9
    elif difficulty == "intermediate":
        boardsizex, boardsizey = 16, 16
    elif difficulty == "expert":
        boardsizex, boardsizey = 30, 16
else:
    if difficulty == "beginner":
        boardsizex, boardsizey = 10, 8
    elif difficulty == "intermediate":
        boardsizex, boardsizey = 18, 14
    elif difficulty == "expert":
        boardsizex, boardsizey = 24, 20
        
font = pg.font.SysFont(fontname, int(40*scale))
font.bold = True

size = width, height = boardsizex * tilesize + tilesize, boardsizey * tilesize + 3 * tilesize
screen = pg.display.set_mode(size, pg.RESIZABLE, 32)

clock = pg.time.Clock()

numberTilesList = [pg.image.load("assets/"+str(i)+"Tile.png") for i in range(9)]
numberTilesList = [pg.transform.scale(numberTilesList[i], (tilesize,tilesize)) for i in range(9)]

otherTilesList = [pg.image.load("assets/bombTile.png"),
                  pg.image.load("assets/detBombTile.png"),
                  pg.image.load("assets/flaggedTile.png"),
                  pg.image.load("assets/unrevealedTile.png"),
                  pg.image.load("assets/wrongFlaggedTile.png")]
otherTilesList = [pg.transform.scale(otherTilesList[i], (tilesize,tilesize)) for i in range(5)]

faces = [pg.image.load("assets/faceAlive.png"),
         pg.image.load("assets/faceDead.png"),
         pg.image.load("assets/faceWin.png")]
faces = [pg.transform.scale(faces[i], (tilesize*3//2,tilesize*3//2)) for i in range(3)]

flags = [pg.image.load("assets/greenflaglight.png"),
         pg.image.load("assets/greenflagdark.png"),
         pg.image.load("assets/greenflagtop.png")]
flags = [pg.transform.scale(flags[i], (tilesize,tilesize)) for i in range(3)]

numbers = [pg.image.load("assets/n"+str(i)+".png") for i in range(10)]
numbers = [pg.transform.scale(numbers[i], (tilesize*3//4,tilesize*3//2)) for i in range(10)]

mineBoard = []
revBoard = [["hidden" for i in range(boardsizey)] for j in range(boardsizex)]

bombsLeft = bombCount
startTime = 0
endTime = 0

def clickBoard(x,y):
    global startTime
    if revBoard[x][y] == "flagged":
        return
    if len(mineBoard) == 0:
        setMineBoard()
        while mineBoard[x][y]!=0:
            setMineBoard()
        startTime = pg.time.get_ticks()
    clickBoard = [[False for i in range(boardsizey)] for j in range(boardsizex)]
    revealLoop(x,y,clickBoard)

def revealLoop(x,y,cb):
    global revBoard
    if revBoard[x][y] != "revealed":
        revBoard[x][y] = "revealed"
        if mineBoard[x][y] == 0 and not cb[x][y]:
            cb[x][y] = True
            for a in [-1,0,1]:
                for b in [-1,0,1]:
                    if x+a>=0 and x+a<boardsizex and y+b>=0 and y+b<boardsizey:
                        revealLoop(x+a,y+b,cb)

def setMineBoard():
    global mineBoard
    mineBoard = []
    minesLeft = bombCount
    tilesLeft = boardsizex*boardsizey
    for i in range(boardsizex):
        temp = []
        for j in range(boardsizey):
            if minesLeft/tilesLeft >= random():
                temp.append(-10-randint(0,255))
                minesLeft -= 1
            else:
                temp.append(0)
            tilesLeft -= 1
        mineBoard.append(temp)

    for i in range(boardsizex):
        for j in range(boardsizey):
            for a in [-1,0,1]:
                for b in [-1,0,1]:
                    if i+a>=0 and i+a<boardsizex and j+b>=0 and j+b<boardsizey:
                        if mineBoard[i+a][j+b] < 0:
                            mineBoard[i][j] += 1

def checkWin():
    for i in range(boardsizex):
        for j in range(boardsizey):
            if revBoard[i][j] == "revealed" and mineBoard[i][j] < 0:
                return False
            if revBoard[i][j] in ["hidden","flagged"] and mineBoard[i][j] >= 0:
                return False
    return True

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
        if event.type == pg.KEYUP:
            if event.key == pg.K_ESCAPE:
                pg.quit()
                sys.exit()
        if event.type == pg.MOUSEBUTTONUP and status == "alive":
            if event.button == 1:
                mouse = pg.mouse.get_pos()
                if mouse[0]<= tilesize//2 + tilesize*boardsizex and mouse[0]>= tilesize//2 and mouse[1]<= tilesize//2+tilesize*2+tilesize*boardsizey and mouse[1]>= tilesize//2 + tilesize*2:
                    x,y = math.floor((mouse[0]-tilesize//2)/tilesize), math.floor((mouse[1]-tilesize//2-2*tilesize)/tilesize)
                    if revBoard[x][y] != "flagged":
                        clickBoard(x,y)
                        if checkWin():
                            status = "win"
                            endTime = pg.time.get_ticks()
                            bombsLeft = 0
                        if mineBoard[x][y]<0:
                            status = "dead"
                            endTime = pg.time.get_ticks()
                            bombsLeft = 0
                            for i in range(boardsizex):
                                for j in range(boardsizey):
                                    if revBoard[i][j] == "flagged" and mineBoard[i][j] >= 0:
                                        revBoard[i][j] = "wrongFlagged"
                                    elif i == x and j == y:
                                        revBoard[i][j] = "detBomb"
                                    elif revBoard[i][j] != "flagged" and mineBoard[i][j] < 0:
                                        revBoard[i][j] = "revealed"
            elif event.button == 3 and startTime != 0:
                mouse = pg.mouse.get_pos()
                if mouse[0]<= tilesize//2 + tilesize*boardsizex and mouse[0]>= tilesize//2 and mouse[1]<= tilesize//2+tilesize*2+tilesize*boardsizey and mouse[1]>= tilesize//2 + tilesize*2:
                    x,y = math.floor((mouse[0]-tilesize//2)/tilesize), math.floor((mouse[1]-tilesize//2-2*tilesize)/tilesize)
                    if revBoard[x][y] == "hidden":
                        revBoard[x][y] = "flagged"
                        bombsLeft -= 1
                    elif revBoard[x][y] == "flagged":
                        revBoard[x][y] = "hidden"
                        bombsLeft += 1
    
    if theme == "classic":
        screen.fill(MIDTONE)
    else:
        screen.fill(DARKTONE)
    
    if theme == "classic":
        screen.blit(numbers[math.floor(max(bombsLeft,0)/100)%10],(tilesize//2,tilesize//2))
        screen.blit(numbers[math.floor(max(bombsLeft,0)/10)%10],(tilesize//2+tilesize*3//4,tilesize//2))
        screen.blit(numbers[math.floor(max(bombsLeft,0))%10],(tilesize//2+tilesize*6//4,tilesize//2))
    else:
        text = font.render(str(math.floor(max(bombsLeft,0)/100)%10)+str(math.floor(max(bombsLeft,0)/10)%10)+str(math.floor(max(bombsLeft,0))%10), True, (255,255,255))
        textRect = text.get_rect()
        textRect.centerx = tilesize//2+tilesize*9//8
        textRect.centery = tilesize//2+tilesize*3//4
        screen.blit(text,textRect)
    
    if startTime == 0:
        ticks = 0
    elif status == "dead" or status == "win":
        ticks = endTime
    else:
        ticks = pg.time.get_ticks() - startTime
    if theme == "classic":
        screen.blit(numbers[math.floor(ticks/100000)%10],(tilesize*boardsizex-tilesize*7//4,tilesize//2))
        screen.blit(numbers[math.floor(ticks/10000)%10],(tilesize*boardsizex-tilesize*4//4,tilesize//2))
        screen.blit(numbers[math.floor(ticks/1000)%10],(tilesize*boardsizex-tilesize*1//4,tilesize//2))
    else:
        text = font.render(str(math.floor(ticks/100000)%10)+str(math.floor(ticks/10000)%10)+str(math.floor(ticks/1000)%10), True, (255,255,255))
        textRect = text.get_rect()
        textRect.centerx = tilesize*boardsizex-tilesize*5//8
        textRect.centery = tilesize//2+tilesize*3//4
        screen.blit(text,textRect)
    
    if theme == "classic":
        if status == "alive":
            screen.blit(faces[0],(tilesize*boardsizex//2-tilesize//4,tilesize//2))
        elif status == "dead":
            screen.blit(faces[1],(tilesize*boardsizex//2-tilesize//4,tilesize//2))
        elif status == "win":
            screen.blit(faces[2],(tilesize*boardsizex//2-tilesize//4,tilesize//2))
        
    for i in range(boardsizex):
        for j in range(boardsizey):
            if theme == "classic":
                displayTile = otherTilesList[3]
                if revBoard[i][j] == "revealed":
                    if mineBoard[i][j]<0:
                        displayTile = otherTilesList[0]
                    else:
                        displayTile = numberTilesList[mineBoard[i][j]]
                elif revBoard[i][j] == "detBomb":
                    displayTile = otherTilesList[1]
                elif revBoard[i][j] == "flagged":
                    displayTile = otherTilesList[2]
                elif revBoard[i][j] == "wrongFlagged":
                    displayTile = otherTilesList[4]
                screen.blit(displayTile,(tilesize//2+tilesize*i,2*tilesize+tilesize//2+tilesize*j))
            else:
                if revBoard[i][j] == "revealed" or revBoard[i][j] == "detBomb" or revBoard[i][j] == "wrongFlagged":
                    if status == "win":
                        if (i + j) % 2 == 0:
                            pg.draw.rect(screen,(135, 192, 250),pg.Rect(tilesize//2+tilesize*i,2*tilesize+tilesize//2+tilesize*j,tilesize,tilesize))
                        else:
                            pg.draw.rect(screen,(125, 178, 232),pg.Rect(tilesize//2+tilesize*i,2*tilesize+tilesize//2+tilesize*j,tilesize,tilesize))
                    else:
                        if (i + j) % 2 == 0:
                            pg.draw.rect(screen,REVCOLORLIGHT,pg.Rect(tilesize//2+tilesize*i,2*tilesize+tilesize//2+tilesize*j,tilesize,tilesize))
                        else:
                            pg.draw.rect(screen,REVCOLORDARK,pg.Rect(tilesize//2+tilesize*i,2*tilesize+tilesize//2+tilesize*j,tilesize,tilesize))
                    if mineBoard[i][j] > 0 and status != "win" and revBoard[i][j] != "wrongFlagged":
                        text = font.render(str(mineBoard[i][j]), True, colorList[mineBoard[i][j]-1])
                        textRect = text.get_rect()
                        textRect.centerx = tilesize+tilesize*i
                        textRect.centery = 2*tilesize+tilesize+tilesize*j
                        screen.blit(text,textRect)
                    if revBoard[i][j] == "wrongFlagged":
                        if (i + j) % 2 == 0:
                            pg.draw.rect(screen,LIGHTTONE,pg.Rect(tilesize//2+tilesize*i,2*tilesize+tilesize//2+tilesize*j,tilesize,tilesize))
                        else:
                            pg.draw.rect(screen,MIDTONE,pg.Rect(tilesize//2+tilesize*i,2*tilesize+tilesize//2+tilesize*j,tilesize,tilesize))
                        pg.draw.line(screen, (250, 0, 0), (tilesize//2+tilesize*i,2*tilesize+tilesize//2+tilesize*j), (3*tilesize//2+tilesize*i,3*tilesize+tilesize//2+tilesize*j), width=tilesize//8)
                        pg.draw.line(screen, (250, 0, 0), (3*tilesize//2+tilesize*i,2*tilesize+tilesize//2+tilesize*j), (tilesize//2+tilesize*i,3*tilesize+tilesize//2+tilesize*j), width=tilesize//8)
                    elif mineBoard[i][j] < 0:
                        (h, s, v) = (-1*mineBoard[i][j]-10, 250, 160)
                        (h, s, v) = (h / 255, s / 255, v / 179)
                        (r, g, b) = hsv_to_rgb(h, s, v)
                        (r, g, b) = (int(r * 255), int(g * 255), int(b * 255))
                        pg.draw.rect(screen, (r, g, b),pg.Rect(tilesize//2+tilesize*i,2*tilesize+tilesize//2+tilesize*j,tilesize,tilesize))
                        (h2, s2, v2) = (-1*mineBoard[i][j]-10, 250, 100)
                        (h2, s2, v2) = (h2 / 255, s2 / 255, v2 / 179)
                        (r2, g2, b2) = hsv_to_rgb(h2, s2, v2)
                        (r2, g2, b2) = (int(r2 * 255), int(g2 * 255), int(b2 * 255))
                        pg.draw.circle(screen, (r2, g2, b2), (tilesize+tilesize*i, 3*tilesize+tilesize*j), tilesize//4)
                elif revBoard[i][j] == "hidden":
                    if (i + j) % 2 == 0:
                        pg.draw.rect(screen,LIGHTTONE,pg.Rect(tilesize//2+tilesize*i,2*tilesize+tilesize//2+tilesize*j,tilesize,tilesize))
                    else:
                        pg.draw.rect(screen,MIDTONE,pg.Rect(tilesize//2+tilesize*i,2*tilesize+tilesize//2+tilesize*j,tilesize,tilesize))
                else:
                    if revBoard[i][j] == "flagged":
                        if status == "win":
                            if (i + j) % 2 == 0:
                                pg.draw.rect(screen,LIGHTTONE,pg.Rect(tilesize//2+tilesize*i,2*tilesize+tilesize//2+tilesize*j,tilesize,tilesize))
                            else:
                                pg.draw.rect(screen,MIDTONE,pg.Rect(tilesize//2+tilesize*i,2*tilesize+tilesize//2+tilesize*j,tilesize,tilesize))
                        
                        else:
                            if (i + j) % 2 == 0:
                                displayTile = flags[0]
                            else:
                                displayTile = flags[1]
                            screen.blit(displayTile,(tilesize//2+tilesize*i,2*tilesize+tilesize//2+tilesize*j))
                    
    mouse = pg.mouse.get_pos()
    if mouse[0]<= tilesize//2 + tilesize*boardsizex and mouse[0]>= tilesize//2 and mouse[1]<= tilesize//2+tilesize*2+tilesize*boardsizey and mouse[1]>= tilesize//2 + tilesize*2:
        s = pg.Surface((tilesize,tilesize))
        s.set_alpha(48)
        s.fill((0,0,0))
        screen.blit(s, (math.floor((mouse[0]-tilesize//2)/tilesize)*tilesize+tilesize//2, math.floor((mouse[1]-tilesize//2-2*tilesize)/tilesize)*tilesize+tilesize//2+2*tilesize))
    
    pg.display.flip()
    clock.tick(60)