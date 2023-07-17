import random
import game_field

MAX_ACTION_NUMBER = 10
SNAKE_MEMORY_SIZE = 32
PEEK_COMMAND = 6
MOVE_COMMAND = 9
GOTO_COMMAND = SNAKE_MEMORY_SIZE
class Snake:
    current_id = 0

    def __init__(self):
        self.dnk = [random.randint(0, SNAKE_MEMORY_SIZE-1) for i in range(SNAKE_MEMORY_SIZE)]
        self.dnk_cursor = 0
        self.snake_id = Snake.current_id
        Snake.current_id += 1
        self.current_direction = 'RIGHT'
        self.head_coord, self.tail_coord = game_field.create_snake(self.snake_id)


    def make_decision(self):
        for i in range(MAX_ACTION_NUMBER):
            current_action = self.dnk[self.dnk_cursor]
            if 0 <= current_action < PEEK_COMMAND:
                pass
            if PEEK_COMMAND <= current_action < MOVE_COMMAND:
                pass
            if MOVE_COMMAND <= current_action < GOTO_COMMAND:
                pass

    def get_coord_offset(self, cell_number):
        coordinate_offset = [[1,-1], [0,-1], [-1,-1], [-1,0], [-1,1], [0,1], [1,1], [1,0]]
        if self.current_direction == 'UP':
            coordinate_offset_index = [0,1,2,3,4,5,6,1,3,5]
            return coordinate_offset[coordinate_offset_index[cell_number]]
        if self.current_direction == 'RIGHT':
            coordinate_offset_index = [2,3,4,5,6,7,0,3,5,7]
            return coordinate_offset[coordinate_offset_index[cell_number]]
        if self.current_direction == 'DOWN':
            coordinate_offset_index = [4,5,6,7,0,1,2,5,7,1]
            return coordinate_offset[coordinate_offset_index[cell_number]]
        if self.current_direction == 'LEFT':
            coordinate_offset_index = [6,7,0,1,2,3,4,7,1,3]
            return coordinate_offset[coordinate_offset_index[cell_number]]