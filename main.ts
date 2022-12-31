input.onButtonPressed(Button.A, function () {
    snake.turn(Direction.Left, 90)
})
input.onButtonPressed(Button.B, function () {
    snake.turn(Direction.Right, 90)
})
let snake: game.LedSprite = null
let SnakeX = 2
let SnakeY = 2
let dir = 0
snake = game.createSprite(SnakeX, SnakeY)
basic.forever(function () {
    if (dir == 0) {
        SnakeY += -1
    } else if (dir == 1) {
    	
    } else if (dir == 2) {
    	
    } else {
    	
    }
    snake.set(LedSpriteProperty.X, SnakeX)
    snake.set(LedSpriteProperty.Y, SnakeY)
    basic.pause(500)
})
control.inBackground(function () {
	
})
