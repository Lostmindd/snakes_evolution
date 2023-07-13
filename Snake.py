import random
import game_field


class Snake:
    current_id = 0

    def __init__(self):
        self.dnk = [random.randint(0, 31) for i in range(32)]
        self.snake_id = Snake.current_id
        Snake.current_id += 1
        self.head_coord, self.tail_coord = game_field.create_snake(self.snake_id)
