import pgzrun 

gameOver = False

ball_x = 400
ball_y = 500
sd
speed_x = 2
speed_y = -3

paddle = Rect(350, 500, 150, 20)

boxList = []

box_w = 90
box_h = 31

x = 25


gap = 8

numBoxes = 4


for i in range(numBoxes + 3):
    
    y = 100
    for i in range(numBoxes + 2):
        testBox = Rect(x, y, box_w, box_h)
        boxList.append(testBox)
        y += box_h + gap
    x += box_w + gap


def checkBounce(block):
    global speed_y, speed_x
    ball_box = Rect(ball_x - 20, ball_y - 20, 40, 40)

    # chechk it is colliding

    '''variables we're using
    block: location of the block we might bouncing off of
        -top   -bottom    -left     -right

    ball_x & ball_y: where the ball is located (center)

    speed_x & speed_y: the movement of the ball

    ball_box: make it easier to check when ball collides with another block
    '''
    
    # make sure going down
    # make sure that center is above top of the block
    # check inbetween left and right of the block


    if ball_box.colliderect(block):
        # checking the top
        if ball_y < block.top and speed_y > 0 and ball_x > block.left and ball_x < block.right : 
            speed_y *= -1
            return True
        #checking the bottom
        elif ball_y > block.bottom and speed_y < 0 and ball_x > block.left and ball_x < block.right : 
            speed_y *= -1
            return True
            
        #TODO: add elif to check the left and right
        elif ball_x > block.right and speed_x < 0 and ball_y > block.bottom and ball_x < block.top : 
            speed_x *= -1
            return True
        elif ball_x > block.left and speed_x > 0 and ball_y > block.bottom and ball_x < block.top : 
            speed_x *= -1
            return True
            
            


    return False

def update():
    global ball_x, ball_y, speed_x, speed_y, gameOver, boxList
    ball_x += speed_x
    ball_y += speed_y
    if gameOver == False:

        if speed_x > 0 and ball_x >= 800:
            speed_x = -3
    
        if speed_x < 0 and ball_x <= 0:
            speed_x = 3
    
        if speed_y > 0 and ball_y >= 600:
            gameOver = True
    
        if speed_y < 0 and ball_y <= 0:
            speed_y = 3

        if paddle.collidepoint(ball_x, ball_y):
            speed_y = -3

        if keyboard.left:
            paddle.x -= 4

        if keyboard.right:
            paddle.x += 4
    
        #loop through "boxList" and call checkBounce for each item in that list
        newBoxList = []
        for i in range(len(boxList)):

            block = boxList[i]
            if checkBounce(block):
                print("bounce")
            else:
                newBoxList.append(block)  # only keep blocks that haven't been hit

        boxList = newBoxList




def draw(): 
    if gameOver == False:
        screen.fill("navy")
        screen.draw.filled_circle((ball_x, ball_y), 20, "red")

        screen.draw.filled_rect(paddle, "red")

        for b in boxList:
            screen.draw.filled_rect(b, "white")

pgzrun.go()


