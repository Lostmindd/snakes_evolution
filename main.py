import pygame
import random
import game_field
import Snake

WIDTH = 1800
HEIGHT = 1000
FPS = 10000 #100
SNAKES_NUMBER = 30
APPLES_NUMBER = 30 #40
MAXIMUM_MOVES_NUM_PER_ROUND = 600 #200
NEW_GENERATION_ANCESTORS_NUM = 5
MUTANTS_NUM_IN_EACH_FAMILY = 3 #1
MAX_GENERATION = 2000


# SNAKE_NAMES = []

SNAKE_NAMES = ["Авторханов Арби", "Шустров Василий", "Колчин Даниил", "Петрова Ксения", "Авдеев Евгений", "Мартынов Игорь", "Иванов Николай", "Потапенко Егор", "Артамонов Дмитрий", "Большаков Иван",
                "Гуревич Кирилл", "Кругликов Артем", "Машенков Иван", "Суслов Анатолий", "Гуторов Михаил", "Аниськин Артём", "Зарманбетов Эмиль", "Иванов Денис", "Шапкина Алена", "Морозов Сергей",
                "Складник Любовь", "Кунец Никита", "Угрюмова Мария", "Нечаев Михаил", "Макаров Владимир", "Жгун Татьяна", "Радаев Кирилл", "Михайлов Дмитрий", "Телина Ирина", "Цымбалюк Лариса"]


# SNAKE_FILE_PATH = "generation64_1200.txt"
SNAKE_FILE_PATH = ""

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Еvolution of snakes")
clock = pygame.time.Clock()

generation = 0

# draw field
game_field.init_game_field(WIDTH, HEIGHT, screen)


snake_list = []

if SNAKE_FILE_PATH != "":
    with open(SNAKE_FILE_PATH, 'r', encoding='utf-8') as f:
        generation = int(f.readline().replace('\n',""))
        while True:
            line = f.readline()
            if not line:
                break

            SNAKE_NAMES.append(line.replace('\n', ''))

            dnk_string = f.readline().split(',')
            dnk_string.pop(-1)
            dnk = list(map(int, dnk_string))
            snake = Snake.Snake(dnk)
            snake_list.append(snake)

else:
    for i in range(SNAKES_NUMBER):
        snake = Snake.Snake()
        snake_list.append(snake)

for i in range(APPLES_NUMBER):
    game_field.create_random_apple()



while generation < MAX_GENERATION:
    generation += 1
    moves_per_current_round = 0
    destroyed_snakes = []
    current_snake_number = SNAKES_NUMBER
    while current_snake_number > NEW_GENERATION_ANCESTORS_NUM and moves_per_current_round < MAXIMUM_MOVES_NUM_PER_ROUND:
        pygame.display.flip()

        for snake in snake_list:
            if snake.snake_id in destroyed_snakes: continue
            if snake.is_destroyed:
                destroyed_snakes.append(snake.snake_id)
                current_snake_number -= 1
                continue
            snake.make_decision()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        moves_per_current_round+=1
        clock.tick(FPS)

    snake_list_copy =  snake_list.copy()
    game_field.draw_score(snake_list_copy, SNAKE_NAMES, generation)

    survivors_list = []
    for snake in snake_list:
        if not snake.is_destroyed:
            survivors_list.append(snake)

    survivors_list.sort(key=lambda snake: snake.weight, reverse=True)
    ancestors_list = survivors_list[:NEW_GENERATION_ANCESTORS_NUM]

    game_field.refsresh_field()

    #------
    descendants_num = int(SNAKES_NUMBER / NEW_GENERATION_ANCESTORS_NUM) - MUTANTS_NUM_IN_EACH_FAMILY
    snake_list = []
    Snake.Snake.current_id = 0
    for ancestor in ancestors_list:
        for descendant in range(descendants_num):
            snake = Snake.Snake(ancestor.dnk.copy())
            snake_list.append(snake)
        for mutants in range(MUTANTS_NUM_IN_EACH_FAMILY):
            new_dnk = ancestor.dnk.copy()
            for i in range(random.randint(0,31)):
                memory_slot_num = random.randint(0,31)
                new_dnk[memory_slot_num] = random.randint(0,31)
            snake = Snake.Snake(new_dnk)
            snake_list.append(snake)

    for i in range(APPLES_NUMBER):
        game_field.create_random_apple()
    print('generation =', generation)
    if (generation%200 ==0):
        with open('data.txt', 'w+') as f:
            f = open('generation256_' + str(generation) + '.txt', 'w+', encoding='utf-8')
            f.write(str(generation) + "\n")
            for snake in snake_list:
                f.write(SNAKE_NAMES[snake.snake_id] + "\n")
                for i in snake.dnk:
                    f.write(str(i) + ",")
                f.write("\n")
            f.close()



# запись обученных змей в файл
with open('data.txt', 'w+') as f:
    f = open('generation64_' + str(generation) + '.txt', 'w+', encoding='utf-8')
    f.write(str(generation) + "\n")
    for snake in snake_list:
        f.write(SNAKE_NAMES[snake.snake_id] + "\n")
        for i in snake.dnk:
            f.write(str(i) + ",")
        f.write("\n")
    f.close()
    #-----


