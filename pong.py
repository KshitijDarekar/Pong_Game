#Simple Pong GAME made using Python following Youtube :)    =>#Learning

## Getting Started
import turtle    


# Variables- For Repeatedly used Numbers 
## Reduces time and errors if values are changed :)
paddle_speed=40
screen_width=800 ## width set hardcorded
screen_height=600 ## height set hardcorded
paddle_height=5*20 ## 5 hardcoded and 20 is turtle standard
paddle_width=1*10  ## 1 hardcoded 



wn = turtle.Screen()
wn.title("Pong @ Kshitij")
# wn.bgpic("bg.jpg")
# wn.setup(width=screen_width,height=screen_height)
wn.setup(width=800,height=600)
wn.bgcolor("black")
wn.bgpic("sky2.gif")


wn.tracer(0)

# Border
border_pen=turtle.Turtle()
border_pen.speed(0)
border_pen.color("white")
border_pen.penup()
border_pen.pensize(4)
border_pen.goto(-screen_width/2,screen_height/2)
# border_pen.setposition(-300,-300)
border_pen.pendown()
for i in range(2):
   border_pen.forward(screen_width)           
   border_pen.right(90)
   border_pen.forward(screen_height)
   border_pen.right(90)               
border_pen.hideturtle()


#GameOver display 
display=turtle.Turtle()
display.color("white")
display.fillcolor("green")
display.goto(0,0)
display.penup()
display.hideturtle()
#Score
score_a=0
score_b=0

# Paddle A
paddle_a=turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("blue")
paddle_a.penup()
# paddle_a.shapesize(stretch_wid=5,stretch_len=1)
paddle_a.shapesize(5,1)
#  
#  paddle start at (-350,0)
paddle_a.goto(-(screen_width/2-50),0)

#Paddle B
paddle_b=turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("red")
paddle_b.penup()
paddle_b.shapesize(stretch_wid=5,stretch_len=1) 
#  paddle start at (350,0)
paddle_b.goto((screen_width/2-50),0)


#Ball
ball=turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("yellow")
ball.penup()
ball.dx= 1
ball.dy= 1

#Player Name
# player_a=input("Player A :")
player_a=turtle.textinput(title="Player A",prompt="What is Your Name Player A?")
player_b=turtle.textinput(title="Player B",prompt="What is Your Name Player B?")

#Pen
pen=turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.goto(0,(screen_height/2-40))
pen.hideturtle()
pen.write("Player {}: 0 | Player {}: 0".format(player_a,player_b),align="center",font=("Nunito",28,"italic"))
 

#Function
def paddle_a_up():
    y=paddle_a.ycor()
    y+=paddle_speed    
    paddle_a.sety(y)
    # x= paddle_a.xcor()
def paddle_b_up():
    y=paddle_b.ycor()
    y+=paddle_speed    
    paddle_b.sety(y)

def paddle_a_down():
    y=paddle_a.ycor()
    y-=paddle_speed   
    paddle_a.sety(y)
    # x= paddle_a.xcor()
def paddle_b_down():
    y=paddle_b.ycor()
    y-=paddle_speed    
    paddle_b.sety(y)


#Keyword 
wn.listen() 

wn.onkeypress(paddle_a_up,"w")
wn.onkeypress(paddle_b_up,"Up")   
wn.onkeypress(paddle_a_down,"s")
wn.onkeypress(paddle_b_down,"Down")   


#  ball start at (0,0)
ball.goto(0,0)

# Main Game Loop

while True :
    wn.update()


    #Move Ball
    ball.setx(ball.xcor()+ball.dx)
    ball.sety(ball.ycor()+ball.dy)

    # Ball Border Checking
    if ball.ycor()>(screen_height/2)-10:
        ball.sety((screen_height/2)-10)
        ball.dy*=-1
    
    if ball.ycor()<-((screen_height/2)-10):
        ball.sety(-((screen_height/2)-10))
        ball.dy*=-1
    
    if ball.xcor()>((screen_width/2)-10):
        ball.goto(0,0)
        ball.dx*=-1
        pen.clear()
        score_a+=1
        pen.write("Player {}: {} | Player {}: {}".format(player_a,score_a,player_b,score_b),align="center",font=("Nunito",28,"italic"))

    
    if ball.xcor()<-((screen_width/2)-10):
        ball.goto(0,0)
        ball.dx*=-1
        pen.clear()
        score_b+=1
        pen.write("Player {}: {} | Player {}: {}".format(player_a,score_a,player_b,score_b),align="center",font=("Nunito",28,"italic"))
    
    # Paddle border checking-12/7/20
    if paddle_a.ycor()>((screen_height/2)-(paddle_height/2)-10):  ##240
       paddle_a.sety((screen_height/2)-(paddle_height/2)-10)
        
    if paddle_b.ycor()>((screen_height/2)-(paddle_height/2)-10):
       paddle_b.sety((screen_height/2)-(paddle_height/2)-10)
    
    if paddle_a.ycor()<-((screen_height/2)-(paddle_height/2)-10):
        paddle_a.sety(-((screen_height/2)-(paddle_height/2)-10))
        
    if paddle_b.ycor()<-((screen_height/2)-(paddle_height/2)-10):
        paddle_b.sety(-((screen_height/2)-(paddle_height/2)-10))
        
    

    #Ball and Paddle Collision
    if (ball.xcor()>(screen_width/2-50-10) and ball.xcor()<(screen_width/2-50))and (ball.ycor()<paddle_b.ycor()+60 and ball.ycor()>paddle_b.ycor()-60):
        ball.setx(screen_width/2-50-10)
        ball.dx *= -1
        ## the equalities(limits) are coded using logic and (trial and error)   i.e(screen_width/2-50-10) ,....etc     

    if (ball.xcor()<-(screen_width/2-50-10) and ball.xcor()>-(screen_width/2-50))and (ball.ycor()<paddle_a.ycor()+60 and ball.ycor()>paddle_a.ycor()-60):
        ball.setx(-(screen_width/2-50-10))
        ball.dx *= -1


    # Game Over
    if(score_a==10 or score_b==10):
        if(score_a==10 ):
            display.write("Game Over \n  {} Won! ".format(player_a),align="center",font=("Nunito",50,"italic","bold"))
        if(score_b==10):
            display.write("Game Over \n {} Won! ".format(player_b),align="center",font=("Nunito",50,"italic","bold"))
        turtle.done()
        
    
    