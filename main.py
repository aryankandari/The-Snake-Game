#Beating my own highscore in this game was the ultimate goal of mine in this game
import pygame
import time
import random

pygame.init()

white = (255, 255, 255)
gray = (190, 190, 190)
black = (0, 0, 0)
blue = (0, 0, 255)
green = (0, 255, 0)
yellow = (255, 255, 102)
red = (255, 0, 0)
orange = (255, 165, 0)
pink = (255, 100, 180)

dis_width = 500
dis_height = 500

dis = pygame.display.set_mode((dis_width,dis_height))
pygame.display.set_caption('SNAKESSS BY ARYAN')     #title of the window

clock = pygame.time.Clock()

snake_speed = 15
snake_block = 10

font_style = pygame.font.SysFont("comicsansms", 15)
score_font = pygame.font.SysFont("timesnewroman",20)

def game_score(score):
    value = score_font.render("SCORE: " + str(score), True, pink)
    dis.blit(value, [200,0])


def our_snake(snake_block,snake_list):
    for x in snake_list:
        pygame.draw.rect(dis, black, [x[0], x[1], snake_block, snake_block])


def message(msg,color):
    mssg = font_style.render(msg, True, color)
    dis.blit(mssg, [dis_width/6, dis_height/3])


def gameLoop():
    game_over = False
    game_close = False

    x1 = dis_width / 2
    y1 = dis_height / 2

    x1_change = 0      #for updating value of snake 
    y1_change = 0

    snake_List = []     #this will have all the food that the snake will eat
    snake_length = 1     #this the total length of the snake after eating

    foodx = (round(random.randrange(0, dis_width - snake_block) / 10.0)) * 10.0
    foody = (round(random.randrange(0, dis_height - snake_block) / 10.0)) * 10.0

    while not game_over:

        while game_close == True:
            dis.fill(black)
            message("YOU LOST! PRESS Q-QUIT OR C-PLAY AGAIN",red)
            game_score(snake_length - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:     #when the user pressed q the game will quit
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:     #when the uesr presses c the game will quit
                        gameLoop()


        for event in pygame.event.get():        #taking all the events taking place in the pygame
            # print(event)    #get all the action performed in the game screen in the debug console
            if event.type == pygame.QUIT:
                game_over = True      #quits the window when pressed cross
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block     #for updating value of snake to the LEFT 
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block     #for updating value of snake to the RIGHT 
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    x1_change = 0     #for updating value of snake to the UP
                    y1_change = -snake_block
                elif event.key == pygame.K_DOWN:
                    x1_change = 0     #for updating value of snake to the DOWN
                    y1_change = snake_block

        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:     #when the snake hits the wall, game will be over
            game_close = True

        x1 += x1_change
        y1 += y1_change
        dis.fill(gray)

        pygame.draw.rect(dis, green, [foodx, foody, snake_block, snake_block])       #this is food for our snake
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)

        if len(snake_List) > snake_length:
            del snake_List[0]

        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True

        our_snake(snake_block,snake_List)
        game_score(snake_length - 1)

        pygame.display.update()

        # pygame.draw.rect(dis, black, [x1, y1, snake_block, snake_block])     #this is our snake
        
        if x1 == foodx and y1 == foody:     #we will get this comment in the terminal when the snake eats the food
            print("DELICIOUS!")
            foodx = (round(random.randrange(0, dis_width - snake_block) / 10.0)) * 10.0
            foody = (round(random.randrange(0, dis_height - snake_block) / 10.0)) * 10.0
            snake_length += 1

        clock.tick(snake_speed)      #controlling the speed of the snake calculating the number of milliseconds since previous call


    pygame.quit()
    quit()

gameLoop()