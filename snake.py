import pygame
import sys
import random
import time
pygame.init()

window_size=[600,650]

width=10
height=10

bg=(24, 3, 3)
white=(255,255,255)
red=(255,0,0)
score=0
myfont=pygame.font.SysFont("monospace",35)

screen=pygame.display.set_mode(window_size)

pygame.display.set_caption("Snake Game")

margin=3
grid=[]
snake=[]
food=[]
extend = False

clock = pygame.time.Clock()

def initial_snake_pos():
    x=random.randrange(0,46,1)
    y=random.randrange(0,46,1)
    snake.append([x,y])

def update_food(score):
    x=random.randrange(3,40,1)
    y=random.randrange(3,40,1)
    if [x,y] in snake:
        update_food(score) 
        return                            
    food.append(x)k/    food.atkl.
    ppend(y)
    return score+5

def move_down():
    a=snake[-1]
    if a[0]+1 > 45 or ([a[0]+1,a[1]] in snake):
        return True
    snake.append([a[0]+1,a[1]])
    if not extend:
        snake.pop(0)
    return False

def  move_up():
    a=snake[-1]
    if a[0]-1 <0 or ([a[0]-1,a[1]] in snake):
        return True
    snake.append([a[0]-1,a[1]])
    if not extend:
        snake.pop(0)
    return False

def  move_right():
    a=snake[-1]
    if a[1]+1 > 45 or ([a[0],a[1]+1] in snake):
        return True
    snake.append([a[0],a[1]+1])
    if not extend:
        snake.pop(0)
    return False

def  move_left():
    a=snake[-1]
    if a[1]-1 <0 or ([a[0],a[1]-1] in snake):
        return True
    snake.append([a[0],a[1]-1])
    if not extend:
        snake.pop(0)
    return False
    
gameover = False
score=update_food(-5)
initial_snake_pos()
move='down'
while not gameover:
    # print(snake)
    grid=[]
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            gameover = True

    if snake[-1]==food:
        food.clear()
        score=update_food(score)
        extend = True

    keys=pygame.key.get_pressed()
    if keys[pygame.K_DOWN] and move!='up':
        move='down'
    if keys[pygame.K_UP] and move!='down':
        move='up'
    if keys[pygame.K_RIGHT] and move!='left':
        move='right'
    if keys[pygame.K_LEFT] and move!='right':
        move='left'

           
    if move=='down':
        if move_down():
            gameover = True
    if move=='up':
        if move_up():
            gameover = True
    if move=='right':
        if move_right():
            gameover = True
    if move=='left':
        if move_left():
            gameover = True
    
    
    for row in range(46):
        grid.append([])
        for col in range(46):
            if [row,col]==food:
                grid[row].append(1)
            else:
                grid[row].append(0)

    for i in snake:
        grid[i[0]][i[1]]=2
    for row in range(46):
        for col in range(46):
            color=bg
            if grid[row][col] == 1:
                color=red
            if grid[row][col]==2:
                color=white
           
            pygame.draw.rect(screen,color,[(margin+width)*col+margin,(margin+height)*row+margin,width,height])

    extend=False
    clock.tick(10)
    
    pygame.draw.rect(screen,(0,0,0),(300,600,350,80))
    text="Score : "+str(score)
    label=myfont.render(text,0,white)
    screen.blit(label,(350,600))
    pygame.display.update()


if gameover:
    screen.fill((0,0,0))
    text='Game Over'
    pygame.draw.rect(screen,(0,0,0),(300,600,350,80))
    label=myfont.render(text,0,white)
    screen.blit(label,(350,600))

pygame.quit()