def draw():
    win.fill(WHITE)

    # draw title
    text = TITLE_FONT.render("HANGMAN GAME", 1, BLACK)
    win.blit(text, (WIDTH/2 - text.get_width()/2, 20))
    pygame.display.update()