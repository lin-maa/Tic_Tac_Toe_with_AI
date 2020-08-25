import random


class TicTacToe:

    def __init__(self):
        self.coord = [[1, 3], [2, 3], [3, 3],
                      [1, 2], [2, 2], [3, 2],
                      [1, 1], [2, 1], [3, 1]]
        self.xo_list = [' ' for x in range(9)]
        self.coord_dict = dict(zip([repr(i) for i in self.coord], self.xo_list))
        self.board = list()
        self.board_rows = list()
        self.command_list = list()
        self.coord_user_input = list()
        self.state_test_bool = False
        self.coord_test_bool = False
        self.player_move = 'X'
        self.next_step = 'X'

    def game_board(self):
        self.board = list()
        self.board = [x if x != '_' else ' ' for x in self.xo_list]
        print('---------')
        print(f'| {self.board[0]} {self.board[1]} {self.board[2]} |')
        print(f'| {self.board[3]} {self.board[4]} {self.board[5]} |')
        print(f'| {self.board[6]} {self.board[7]} {self.board[8]} |')
        print('---------')

    def game_start(self):  # Initialize the xo_list
        print('Input command:')
        self.command_list = input().split()
        if len(self.command_list) == 3 \
                and self.command_list[0] == 'start' \
                and all(x in ["user", "easy"] for x in self.command_list[1:3]):
            self.game_board()
            return
        elif self.command_list[0] == 'exit':
            return
        else:
            print('Bad parameters!')
            print(self.command_list)
            self.game_start()

    def game_move(self):
        if self.command_list[0] != 'exit':
            while not self.state_test_bool:
                self.next_step = self.choose_xo()
                self.user_or_easy(self.command_list[1])
                if self.state_test_bool:
                    break
                else:
                    self.user_or_easy(self.command_list[2])
                # else:
                #    self.__init__()
                #    self.game_start()

    def user_or_easy(self, x):
        if x == "user":
            self.user_move()
        elif x == 'easy':
            self.easy_move()

    def user_move(self):
        while not self.coord_test_bool:
            self.coord_input()
            self.coord_test()  # Test if the element of the coord is number and in range(1, 4)
            if self.coord_test_bool:
                self.xo_coord()  # Test if the coord is not occupied and update the xo_list

    def easy_move(self):
        self.coord_random()
        self.xo_coord()

    def coord_input(self):
        print('Enter the coordinates:')
        self.coord_user_input = input().split()
        print(self.coord_user_input)

    def coord_random(self):
        print('Making move level "easy"')
        # self.coord_user_input = [random.randint(1,2), random.randint(1,2)]
        # self.coord_user_input = random.sample(range(1, 4, 1), 2)
        self.coord_user_input = random.choice(self.coord)
        print(self.coord_user_input)

    def coord_test(self=False):
        if len(self.coord_user_input) == 2 \
                and all([str(x).isdigit() for x in self.coord_user_input]):
            self.coord_user_input = [int(x) for x in self.coord_user_input]
            if self.coord_test_range():
                self.coord_test_bool = True
                return True
        else:
            print("You should enter numbers!")
            return False

    def coord_test_range(self):
        if all([int(x) in range(1, 4) for x in self.coord_user_input]):
            return True
        else:
            print('Coordinates should be from 1 to 3!')
            return False

    def xo_coord(self):
        if self.coord_dict[repr(self.coord_user_input)] not in ['X', 'O']:
            index = self.coord.index(self.coord_user_input)
            self.xo_list[index] = self.next_step
            self.coord_dict[repr(self.coord_user_input)] = self.next_step  # update xo_list and dict
            self.coord_test_bool = True
            self.game_board()
            self.game_state()
            return True
        else:
            print("This cell is occupied! Choose another one!")
            self.coord_test_bool = False
            return False

    def choose_xo(self):
        return 'X' if self.xo_list.count('X') <= self.xo_list.count('O') else 'O'

    def game_state(self):
        self.check_list()
        if any(row for row in self.board_rows if row.count('X') == 3):
            print('X wins')
            self.state_test_bool = True
        elif any(row for row in self.board_rows if row.count('O') == 3):
            print('O wins')
            self.state_test_bool = True
        elif self.xo_list.count(' ') > 0:
            self.state_test_bool = False
            self.coord_test_bool = False
            return False
        else:
            print('Draw')
            self.state_test_bool = True
            return True

    def check_list(self):
        self.board_rows = [self.xo_list[0:3],
                           self.xo_list[3:6],
                           self.xo_list[6:9],
                           [self.xo_list[0], self.xo_list[4], self.xo_list[8]],
                           [self.xo_list[2], self.xo_list[4], self.xo_list[6]],
                           [self.xo_list[0], self.xo_list[3], self.xo_list[6]],
                           [self.xo_list[1], self.xo_list[4], self.xo_list[7]],
                           [self.xo_list[2], self.xo_list[5], self.xo_list[8]]]

    def game(self):
        self.game_start()
        self.game_move()


if __name__ == "__main__":
    game_once = TicTacToe()
    game_once.game()
