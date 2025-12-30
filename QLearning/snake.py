import random
import numpy as np
import pygame

#BASIC SETUP
pygame.init()
width = 300
height = 300
gridSize = 5
cellSize = width // gridSize
fps = 200

#COLORS
white = (255, 255, 255)
green = (0, 255, 0)
red   = (255, 0, 0)
black = (0, 0, 0)

#ACTIONS
ACTIONS = [(0,-1), (0,1), (-1,0), (1,0)]

#WINDOW
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Snake Q-Learning (Optimized)")
font = pygame.font.SysFont(None, 20)

#FOOD
class Food:
    def randomize(self, snake):
        while True:
            pos = (
                random.randint(0, gridSize - 1),
                random.randint(0, gridSize - 1)
            )
            if pos not in snake.positions:
                self.position = pos
                break

#SNAKE
class Snake:
    def __init__(self):
        self.positions = [(2, 2)]
        self.grow_pending = False
        self.totalCorrectHit = 0

    def move(self, action):
        hx, hy = self.positions[0]
        dx, dy = action
        new_head = (hx + dx, hy + dy)

        self.positions.insert(0, new_head)
        if not self.grow_pending:
            self.positions.pop()
        else:
            self.grow_pending = False

    def grow(self):
        self.grow_pending = True

    def collision(self):
        hx, hy = self.positions[0]
        return (
            (hx, hy) in self.positions[1:] or
            hx < 0 or hx >= gridSize or
            hy < 0 or hy >= gridSize
        )

#Q-TABLE
q_table = {}

#HYPERPARAMETERS
alpha = 0.15
gamma = 0.95

epsilon = 1.0
epsilon_min = 0.05
epsilon_decay = 0.995

num_episodes = 5000
MAX_STEPS = 200
overall_hits = 0

#STATE
def get_state(snake, food):
    hx, hy = snake.positions[0]
    fx, fy = food.position

    danger = (
        int((hx, hy-1) in snake.positions or hy-1 < 0),
        int((hx, hy+1) in snake.positions or hy+1 >= gridSize),
        int((hx-1, hy) in snake.positions or hx-1 < 0),
        int((hx+1, hy) in snake.positions or hx+1 >= gridSize)
    )

    food_dir = (np.sign(fx - hx), np.sign(fy - hy))
    return danger + food_dir

#REWARD
def get_reward(snake, food, prev_dist):
    hx, hy = snake.positions[0]
    fx, fy = food.position
    curr_dist = abs(hx - fx) + abs(hy - fy)

    if snake.collision():
        return -100, curr_dist

    if (hx, hy) == (fx, fy):
        return 25, curr_dist

    return (2 if curr_dist < prev_dist else -2), curr_dist

#TRAINING
clock = pygame.time.Clock()

for episode in range(1, num_episodes + 1):
    snake = Snake()
    food = Food()
    food.randomize(snake)

    prev_dist = abs(snake.positions[0][0] - food.position[0]) + \
                abs(snake.positions[0][1] - food.position[1])

    done = False
    total_reward = 0
    steps = 0

    while not done and steps < MAX_STEPS:
        steps += 1
        clock.tick(fps)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        state = get_state(snake, food)
        q_table.setdefault(state, np.zeros(4))

        if random.random() < epsilon:
            action_idx = random.randint(0, 3)
        else:
            action_idx = np.argmax(q_table[state])

        snake.move(ACTIONS[action_idx])

        reward, prev_dist = get_reward(snake, food, prev_dist)
        total_reward += reward

        next_state = get_state(snake, food)
        q_table.setdefault(next_state, np.zeros(4))

        q_table[state][action_idx] += alpha * (
            reward + gamma * np.max(q_table[next_state]) - q_table[state][action_idx]
        )

        if snake.positions[0] == food.position:
            snake.totalCorrectHit += 1
            snake.grow()
            food.randomize(snake)

        if snake.collision():
            done = True

        #DRAW
        win.fill(white)
        for i in range(gridSize):
            for j in range(gridSize):
                pygame.draw.rect(win, black,
                    (i*cellSize, j*cellSize, cellSize, cellSize), 1)

        for pos in snake.positions:
            pygame.draw.rect(win, green,
                (pos[0]*cellSize, pos[1]*cellSize, cellSize, cellSize))

        pygame.draw.rect(win, red,
            (food.position[0]*cellSize, food.position[1]*cellSize, cellSize, cellSize))

        pygame.display.update()

    epsilon = max(epsilon_min, epsilon * epsilon_decay)
    overall_hits += snake.totalCorrectHit

    if episode % 100 == 0:
        print(f"Episode {episode} | Avg Hits: {overall_hits/episode:.2f} | Epsilon: {epsilon:.3f}")

#SUMMARY
print("\n===== TRAINING SUMMARY =====")
print(f"Episodes           : {num_episodes}")
print(f"Total Food Eaten   : {overall_hits}")
print(f"Average Hits/Ep    : {overall_hits / num_episodes:.2f}")
print(f"Learned States     : {len(q_table)}")
