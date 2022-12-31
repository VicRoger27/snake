def on_button_pressed_a():
    snake.turn(Direction.LEFT, 90)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    snake.turn(Direction.RIGHT, 90)
input.on_button_pressed(Button.B, on_button_pressed_b)

snake: game.LedSprite = None
SnakeX = 2
SnakeY = 2
dir2 = 0
snake = game.create_sprite(SnakeX, SnakeY)

def on_forever():
    global SnakeY
    if dir2 == 0:
        SnakeY += -1
    elif dir2 == 1:
        pass
    elif dir2 == 2:
        pass
    else:
        pass
    snake.set(LedSpriteProperty.X, SnakeX)
    snake.set(LedSpriteProperty.Y, SnakeY)
    basic.pause(500)
basic.forever(on_forever)

def on_in_background():
    pass
control.in_background(on_in_background)
