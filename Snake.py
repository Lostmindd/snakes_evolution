import random
import game_field

MAX_COMMAND_NUMBER = 10
SNAKE_MEMORY_SIZE = 32
CHECK_COMMAND = 7
MOVE_COMMAND = 10
GOTO_COMMAND = SNAKE_MEMORY_SIZE

# cell content
NONE = 1
APPLE = 2
WALL = 3
ANOTHER_BOT_BODY = 4
OWN_BODY = 5

class Snake:
    current_id = 0

    def __init__(self):
        self.dnk = [random.randint(0, SNAKE_MEMORY_SIZE-1) for i in range(SNAKE_MEMORY_SIZE)]
        self.dnk_cursor = 0
        self.snake_id = Snake.current_id
        Snake.current_id += 1
        self.current_direction = 'LEFT'
        self.head_coord, self.tail_coord = game_field.create_snake(self.snake_id)


    def make_decision(self):
        for i in range(MAX_COMMAND_NUMBER):
            current_command = self.dnk[self.dnk_cursor]
            if 0 <= current_command < CHECK_COMMAND:
                cursor_shift = self.check_cell(current_command)
                self.dnk_cursor = (self.dnk_cursor + cursor_shift) % SNAKE_MEMORY_SIZE
            elif CHECK_COMMAND <= current_command < MOVE_COMMAND:
                cursor_shift = self.check_cell(current_command)
                self.dnk_cursor = (self.dnk_cursor + cursor_shift) % SNAKE_MEMORY_SIZE
                # move
                return
            elif MOVE_COMMAND <= current_command < GOTO_COMMAND:
                self.dnk_cursor = (self.dnk_cursor + current_command) % SNAKE_MEMORY_SIZE

    def check_cell(self, command):
        coord_offset = self.get_coord_offset(command)
        check_coord = [self.head_coord[0]+coord_offset[0], self.head_coord[1]+coord_offset[1]]
        if not (0 <= check_coord[0] < game_field.field_size[0] and 0 <= check_coord[1] < game_field.field_size[1]):
            return WALL
        cell_content = game_field.get_cell_content(check_coord[0], check_coord[1])
        if cell_content == game_field.EMPTY:
            return NONE
        elif cell_content == game_field.APPLE:
            return APPLE
        elif cell_content == self.snake_id:
            return OWN_BODY
        elif 0 <= cell_content < 100:
            return ANOTHER_BOT_BODY

    def get_coord_offset(self, command):
        coord_offset = [[1,-1], [0,-1], [-1,-1], [-1,0], [-1,1], [0,1], [1,1], [1,0]]
        if self.current_direction == 'UP':
            coordinate_offset_index = [0,1,2,3,4,5,6,1,3,5]
            return coord_offset[coordinate_offset_index[command]]
        if self.current_direction == 'RIGHT':
            coordinate_offset_index = [2,3,4,5,6,7,0,3,5,7]
            return coord_offset[coordinate_offset_index[command]]
        if self.current_direction == 'DOWN':
            coordinate_offset_index = [4,5,6,7,0,1,2,5,7,1]
            return coord_offset[coordinate_offset_index[command]]
        if self.current_direction == 'LEFT':
            coordinate_offset_index = [6,7,0,1,2,3,4,7,1,3]
            return coord_offset[coordinate_offset_index[command]]