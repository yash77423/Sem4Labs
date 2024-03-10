import random

class WumpusWorld:
    def __init__(self, size=4):
        self.size = size
        self.agent_pos = (0, 0)
        self.wumpus_pos = self.generate_random_position()
        self.gold_pos = self.generate_random_position()
        self.pit_pos = [self.generate_random_position() for _ in range(size)]
        self.arrows = 1
        self.is_game_over = False
        self.is_wumpus_killed = False
        self.has_gold = False

    def generate_random_position(self):
        return random.randint(0, self.size - 1), random.randint(0, self.size - 1)

    def check_adjacent(self, pos1, pos2):
        x1, y1 = pos1
        x2, y2 = pos2
        return (x1 == x2 and abs(y1 - y2) == 1) or (y1 == y2 and abs(x1 - x2) == 1)

    def move_agent(self, direction):
        x, y = self.agent_pos
        if direction == 'up' and x > 0:
            self.agent_pos = (x - 1, y)
        elif direction == 'down' and x < self.size - 1:
            self.agent_pos = (x + 1, y)
        elif direction == 'left' and y > 0:
            self.agent_pos = (x, y - 1)
        elif direction == 'right' and y < self.size - 1:
            self.agent_pos = (x, y + 1)

    def shoot_arrow(self, direction):
        if self.arrows > 0:
            self.arrows -= 1
            x, y = self.agent_pos
            if direction == 'up' and x > 0:
                self.is_wumpus_killed = (x - 1, y) == self.wumpus_pos
            elif direction == 'down' and x < self.size - 1:
                self.is_wumpus_killed = (x + 1, y) == self.wumpus_pos
            elif direction == 'left' and y > 0:
                self.is_wumpus_killed = (x, y - 1) == self.wumpus_pos
            elif direction == 'right' and y < self.size - 1:
                self.is_wumpus_killed = (x, y + 1) == self.wumpus_pos

    def check_game_status(self):
        if self.agent_pos == self.wumpus_pos:
            self.is_game_over = True
            print("Game Over! You were eaten by the Wumpus.")
        elif self.agent_pos in self.pit_pos:
            self.is_game_over = True
            print("Game Over! You fell into a pit.")
        elif self.agent_pos == self.gold_pos:
            self.has_gold = True
            print("You found the gold! Return to the starting position to win.")
        elif self.agent_pos == (0, 0) and self.has_gold:
            self.is_game_over = True
            print("Congratulations! You won the game by returning to the starting position with the gold.")

    def print_board(self):
        for i in range(self.size):
            for j in range(self.size):
                if (i, j) == self.agent_pos:
                    print("A", end=" ")
                elif (i, j) == self.wumpus_pos:
                    print("W", end=" ")
                elif (i, j) == self.gold_pos:
                    print("G", end=" ")
                elif (i, j) in self.pit_pos:
                    print("P", end=" ")
                else:
                    print("-", end=" ")
            print()

# Example usage
world = WumpusWorld()
world.print_board()

while not world.is_game_over:
    action = input("Enter action (wumpus, shoot, left, right, up, down): ")
    if action == 'wumpus':
        print("Wumpus location:", world.wumpus_pos)
    elif action == 'shoot':
        direction = input("Enter direction to shoot (left, right, up, down): ")
        world.shoot_arrow(direction)
    elif action in ['left', 'right', 'up', 'down']:
        world.move_agent(action)
        world.check_game_status()
        world.print_board()
    else:
        print("Invalid action. Please try again.")

