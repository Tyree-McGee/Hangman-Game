import os
import pygame
import math
import random

pygame.init() 
WIDTH, HEIGHT = 800, 500
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Hangman")

RADIUS = 20
GAP = 15
letters = [] 
startx = round((WIDTH - (RADIUS * 2 + GAP) * 13) / 2)
starty = 400
A = 65 # ASCII
for i in range(26):
    x = startx +  GAP * 2 + ((RADIUS * 2 + GAP) * (i % 13))
    y = starty + ((i//13) * (GAP + RADIUS * 2))
    letters.append([x,y, chr(A + i), True]) # letters is treated as an array

LETTER_FONT = pygame.font.SysFont('comicsans', 40)
WORD_FONT = pygame.font.SysFont('comicsans', 40)
TITLE_FONT = pygame.font.SysFont('comicsans', 70)

images = []
for i in range(7):
    image = pygame.image.load("hangman/hangman"+str(i)+ ".png")
    images.append(image)

hangman_status = 0
words = [
    "HELLO",
    "HELLO WORLD",
    "HANGMAN IS FUN"   
]
word = random.choice(words)
guessed = []

WHITE = (255,255,255)
BLACK = (0,0,0)


FPS = 60
clock = pygame.time.Clock()
run = True

def draw():
    win.fill(WHITE)

    text = TITLE_FONT.render("HANGMAN", 1, BLACK)
    win.blit(text, (WIDTH/2 - text.get_width()/2, 20))

    display_word = ""
    for letter in word:
        if letter in guessed:
            display_word += letter + " "
        elif letter.isspace():
            display_word += " "
        else:
            display_word += "_ "
        text = WORD_FONT.render(display_word, 1, BLACK)
        win.blit(text, (400,200))

    for letter in letters:
        x,y,ltr,visable = letter
        if visable:
            pygame.draw.circle(win, BLACK, (x, y), RADIUS, 3)
            text = LETTER_FONT.render(ltr, 1, BLACK)
            win.blit(text, (x - text.get_width()/2, y - text.get_height()/2))

    win.blit(images[hangman_status], (50,10))
    pygame.display.update()

def display_message(message):
     pygame.time.delay(1000)
     win.fill(WHITE)
     text = WORD_FONT.render(message, 1, BLACK)
     win.blit(text, (WIDTH/2 - text.get_width()/2, HEIGHT/2 - text.get_height()/2))
     pygame.display.update()
     pygame.time.delay(2000)


while run:
    clock.tick(FPS)
    
    

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            m_x, m_y = pygame.mouse.get_pos()
            for letter in letters:
                x, y, ltr, visable = letter # Each element of the array is going into the variable
                if visable:
                    dis = math.sqrt((x - m_x)**2 + (y - m_y)**2)
                    if dis < RADIUS:
                        letter[3] = False
                        guessed.append(ltr)
                        if ltr not in word:
                            hangman_status += 1
    draw()

    won = True
    for letter in word:
        if letter not in guessed and letter != " " :
            won = False
            break

    if won: 
        display_message("You Won!!")
        break
    
    if hangman_status == 6:
        display_message("You LOST!!!!! The Word was "+ word)
        break
        


pygame.quit()
