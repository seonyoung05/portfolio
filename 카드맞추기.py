import turtle as t
import random
import time
import os

def timer():
    global sec
    sec = 30
    while sec > 0:
        sec -= 1
        time.sleep(1)
        time_pen.clear()
        time_pen.write(f"남은 시간:{sec}초", False, "right", ("",15))
    game_over("Time's up!")

def setup_game(stage):
    global pos_x, pos_y, img_list, default_img, turtles, num_pairs, num_cards, sec
    sec = 30
    if stage == 1:
        num_cols, num_rows = 4,2     
    elif stage ==2:
        num_cols, num_rows = 4,3
    elif stage ==3:
        num_cols, num_rows = 4,4
    elif stage == 4:
        num_cols, num_rows = 4,5
    else:
        num_cols, num_rows = 4,6

    num_cards = num_cols * num_rows
    num_pairs = num_cards // 2
    
    turtles = []
    pos_x = [-225 + 150 * i for i in range(num_cols)]
    pos_y = [-260 + 105 * i for i in range(num_rows)]

    for x in range(num_cols):
            for y in range(num_rows):
                new_turtle = t.Turtle()
                new_turtle.up()
                new_turtle.color("black")
                new_turtle.speed(0)
                new_turtle.goto(pos_x[x], pos_y[y])
                turtles.append(new_turtle)

    default_img = "C:/Users/sunny/OneDrive/바탕 화면/fruits/default_img.gif"
    t.addshape(default_img)

    img_list = []
    for i in range(num_pairs):
         img = os.path.abspath(f"C:/Users/sunny/OneDrive/바탕 화면/fruits/img{i}.gif")
         t.addshape(img)
         img_list.append(img)
         img_list.append(img)

    random.shuffle(img_list)
     
    for i in range(num_cards):
          turtles[i].shape(img_list[i])

    time.sleep(3)

    for i in range(num_cards):
        turtles[i].shape(default_img)

        
                

def find_card(x,y):
    min_idx = 0
    min_dis = 100

    for i in range(num_cards):
        distance = turtles[i].distance(x,y)
        if distance < min_dis:
            min_dis = distance
            min_idx = i
    return min_idx


def play(x, y):
    global click_num
    global first_pick
    global second_pick
    global sec
    global stage
    global all_default

    if sec >0:
        click_num+= 1
        card_idx = find_card(x,y)
        turtles[card_idx].shape(img_list[card_idx])
        
        if click_num==1:
            first_pick = card_idx
        elif click_num==2:
            second_pick = card_idx
            click_num = 0


            if img_list[first_pick] != img_list[second_pick]:
                turtles[first_pick].shape(default_img)
                turtles[second_pick].shape(default_img)

        all_default = all(turtle.shape()!= default_img for turtle in turtles)
        if all_default:
            stage += 1
            if stage >5:
                game_over("성공! 기억력이 좋군.. \n공부도 그렇게 열심히 하시길")
            else: 
                setup_game(stage)
        
             

def game_over(message="Game Over"):
    time_pen.clear()
    time_pen.goto(0,-60)
    time_pen.write("Game Over", False, "center", ("", 30, "bold"))
    t.bye()
                

t.bgcolor("black")
t.setup(700,700)
t.color("white")
t.up()
t.ht()
t.goto(0,270)
t.write("같은 그림 카드 맞추기 게임", align="center",font=("",30,"bold"))

time_pen = t.Turtle()
time_pen.up()
time_pen.ht()
time_pen.goto(0, 260)
time_pen.color("red")

stage = 1 
setup_game(stage)


click_num = 0    #클릭횟수             
first_pick = ""   
second_pick = ""
all_default = False

t.onscreenclick(play)
timer()
t.done()
