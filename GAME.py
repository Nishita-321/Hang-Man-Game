import pygame
import math
import random
import sys
# setup display
pygame.init()
WIDTH, HEIGHT = 800, 500
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Hangman Game!")

# button variables
RADIUS = 20
GAP = 15
letters = []
startx = round((WIDTH - (RADIUS * 2 + GAP) * 13) / 2)
starty = 400
A = 65
for i in range(26):
    x = startx + GAP * 2 + ((RADIUS * 2 + GAP) * (i % 13))
    y = starty + ((i // 13) * (GAP + RADIUS * 2))
    letters.append([x, y, chr(A + i), True])

# fonts
LETTER_FONT = pygame.font.SysFont('comicsans', 30)
WORD_FONT = pygame.font.SysFont('comicsans', 40)
TITLE_FONT = pygame.font.SysFont('comicsans', 30)

# load images.
images = []
for i in range(7):
    image = pygame.image.load("hangman" + str(i) + ".png")
    images.append(image)

# game variables
hangman_status = 0
words = [ "APPLE", "BANANA", "ORANGE", "STRAWBERRY", "KIWI", "WATERMELON", "GRAPE", "PINEAPPLE", "MANGO", "PEACH",
    "ELEPHANT", "LION", "TIGER", "GIRAFFE", "ZEBRA", "HIPPO", "KOALA", "PENGUIN", "KANGAROO", "CROCODILE","SOCCER", 
    "BASKETBALL", "TENNIS", "VOLLEYBALL", "CRICKET", "SWIMMING", "BOXING", "GOLF", "RUGBY", "SURFING",
    "COMPUTER", "INTERNET", "ALGORITHM", "DATABASE", "SOFTWARE", "HARDWARE", "KEYBOARD", "MOUSE", "MONITOR",
    "COFFEE", "TEA", "CHOCOLATE", "PIZZA", "SUSHI", "BURGER", "PASTA", "ICE CREAM", "CAKE", "SANDWICH",
    "SUNFLOWER", "ROSE", "DAISY", "TULIP", "LILY", "ORCHID", "DANDELION", "CACTUS", "POPPY", "LAVENDER",
    "CARROT", "POTATO", "TOMATO", "BROCCOLI", "CUCUMBER", "LETTUCE", "ONION", "PEPPER", "SPINACH", "GARLIC",
    "CAR", "BICYCLE", "TRAIN", "AIRPLANE", "SHIP", "HELICOPTER", "MOTORCYCLE", "BUS", "TRUCK", "SCOOTER",
    "OCEAN", "MOUNTAIN", "DESERT", "FOREST", "RIVER", "LAKE", "WATERFALL", "ISLAND", "CANYON", "VOLCANO",
    "BOOK", "MOVIE", "MUSIC", "ART", "POETRY", "DANCE", "THEATER", "PHOTOGRAPHY", "SCULPTURE"]
word = random.choice(words)
guessed = []

# colors
WHITE = (255,255,255)
BLACK = (0,0,0)


def draw():
    win.fill(WHITE)

    # draw title
    text = TITLE_FONT.render("HANGMAN GAME", 1, BLACK)
    win.blit(text, (WIDTH/2 - text.get_width()/2, 20))

    # draw word
    display_word = ""
    for letter in word:
        if letter in guessed:
            display_word += letter + " "
        else:
            display_word += "_ "
    text = WORD_FONT.render(display_word, 1, BLACK)
    win.blit(text, (320, 200))

    # draw buttons
    for letter in letters:
        x, y, ltr, visible = letter
        if visible:
            pygame.draw.circle(win, BLACK, (x, y), RADIUS, 3)
            text = LETTER_FONT.render(ltr, 1, BLACK)
            win.blit(text, (x - text.get_width()/2, y - text.get_height()/2))

    win.blit(images[hangman_status], (100, 120))
    pygame.display.update()


def display_message(message):
    while True:
        win.fill(WHITE)
        text = WORD_FONT.render(message, 1, BLACK)
        correctword = WORD_FONT.render("The Word is: " + word, 1, BLACK)
        win.blit(text, (WIDTH/2 - text.get_width()/2, HEIGHT/4 - text.get_height()/4))
        # win.blit(correctword, (WIDTH/2 - correctword.get_width()/2, HEIGHT/2 - correctword.get_height()/2))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

def main():
    global hangman_status

    FPS = 60
    clock = pygame.time.Clock()
    run = True

    while run:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                m_x, m_y = pygame.mouse.get_pos()
                for letter in letters:
                    x, y, ltr, visible = letter
                    if visible:
                        dis = math.sqrt((x - m_x)**2 + (y - m_y)**2)
                        if dis < RADIUS:
                            letter[3] = False
                            guessed.append(ltr)
                            if ltr not in word:
                                hangman_status += 1
        
        draw()

        won = True
        for letter in word:
            if letter not in guessed:
                won = False
                break
        
        if won:
            display_message("You WON!")
            break

        if hangman_status == 6:
            display_message("You LOST!")
            break
    
while True:
    
    main()
pygame.quit()