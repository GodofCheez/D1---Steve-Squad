import pygame        #Imports Pygame Module
import time
import random

pygame.init()   #Intialises all Pygame Modules and functions

display_width = 800   
display_height = 600

gameDisplay = pygame.display.set_mode((display_width,display_height))  #Creates display for the Menu


pygame.display.set_caption('Tanks')  #Header/Title of the game

#icon = pygame.image.load("tank-152362_640.png")       
#pygame.display.set_icon(icon)

white = (255,255,255)                                   #RGB colour presets
black = (0,0,0)


red = (200,0,0)
light_red = (255,0,0)

yellow = (200,200,0)
light_yellow = (255,255,0)

green = (34,177,76)
light_green = (0,255,0)

clock = pygame.time.Clock()




tankWidth = 40
tankHeight = 20

turretWidth = 5
wheelWidth = 5

ground_height = 35





smallfont = pygame.font.SysFont("bauhaus 93", 25)  #setting the font and size of the menu
medfont = pygame.font.SysFont("bauhaus 93", 40)
largefont = pygame.font.SysFont("bauhaus 93", 85)

#img = pygame.image.load('tank-152362_640.png')
#appleimg = pygame.image.load('tank-152362_640.png')

def text_objects(text, color,size = "small"):      #renders out the option to have small, meduim or large font size in the text objects

    if size == "small":
        textSurface = smallfont.render(text, True, color)
    if size == "medium":
        textSurface = medfont.render(text, True, color)
    if size == "large":
        textSurface = largefont.render(text, True, color)

    return textSurface, textSurface.get_rect()

def text_to_button(msg, color, buttonx, buttony, buttonwidth, buttonheight, size = "small"): #Function to make the button 
    textSurf, textRect = text_objects(msg,color,size)                                        #shape, colour, size and text
    textRect.center = ((buttonx+(buttonwidth/2)), buttony+(buttonheight/2))
    gameDisplay.blit(textSurf, textRect)
   
def message_to_screen(msg,color, y_displace = 0, size = "small"):                            #
    textSurf, textRect = text_objects(msg,color,size)
    textRect.center = (int(display_width / 2), int(display_height / 2)+y_displace)
    gameDisplay.blit(textSurf, textRect)

def button(text, x, y, width, height, inactive_color, active_color, action = None):
    cur = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    #print(click)
    if x + width > cur[0] > x and y + height > cur[1] > y:
        pygame.draw.rect(gameDisplay, active_color, (x,y,width,height))
        if click[0] == 1 and action != None:
            if action == "quit":
                pygame.quit()
                quit()

            if action == "controls":
                game_controls()

            if action == "play":
                gameLoop()

            if action == "main":
                game_intro()
            
    else:
        pygame.draw.rect(gameDisplay, inactive_color, (x,y,width,height))

    text_to_button(text,black,x,y,width,height)

def game_intro():
    intro = True
    while intro:
        for event in pygame.event.get():
                print(event)
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_c:
                        intro = False
                    elif event.key == pygame.K_q:
                        pygame.quit()
                        quit()

        gameDisplay.fill(black)
        message_to_screen("Girls Gone Wild Russian Edition (Tanks)",white,-100,size="medium")  #Prints out the tile of the game     
        message_to_screen("The objective is to chose your perks",white,-30)                    #and objectives so that the display 
        message_to_screen("Strategy is the key",white,10)                                      #would have text and the buttons also
        message_to_screen("The last one stands.",white,50)
        message_to_screen("Press C to play, P to pause or Q to quit",white,180)             


        button("play", 150,500,100,50, green, light_green, action="Play")                   #The buttons of the game
        button("controls", 350,500,100,50, yellow, light_yellow, action="Controls")         #that shows up on the window screen
        button("quit", 550,500,100,50, red, light_red, action ="Quit")                      #i.e Play, Control and Quit
                                                                                            #Mouse Hover function should also work too


        pygame.display.update()

        clock.tick(15)                                                                      # FPS=Refreshes every 15mm/s




    






    pygame.quit()                                                                       #Quits game, when you press Q
    quit()

game_intro()
gameLoop()                                                                              #Gameloops over the code when you press play






