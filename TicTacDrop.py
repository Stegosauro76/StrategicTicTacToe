import random

class TicTacToe:
    def __init__(self):
        self.single_player = False
        self.ai_level = None
        self.reset_game()

    def reset_game(self):
        self.board = [[' ' for _ in range(3)] for _ in range(3)]
        self.players = ['X', 'O']
        self.current_player = 0
        self.moves = {'X': [], 'O': []}
        # NON resetto single_player e ai_level!

    def print_board(self):
        print("    0   1   2")
        print("  -------------")
        for i, row in enumerate(self.board):
            print(f"{chr(65 + i)} | {' | '.join(row)} |")
            print("  -------------")

    def is_valid_move(self, row, col):
        return 0 <= row < 3 and 0 <= col < 3 and self.board[row][col] == ' '

    def make_move(self, row, col):
        player = self.players[self.current_player]
        if self.is_valid_move(row, col):
            if len(self.moves[player]) >= 3:
                old_row, old_col = self.moves[player].pop(0)
                self.board[old_row][old_col] = ' '
            self.board[row][col] = player
            self.moves[player].append((row, col))
            self.current_player = 1 - self.current_player
            return True
        return False

    def check_winner(self):
        for i in range(3):
            if self.board[i][0] == self.board[i][1] == self.board[i][2] != ' ':
                return self.board[i][0]
            if self.board[0][i] == self.board[1][i] == self.board[2][i] != ' ':
                return self.board[0][i]
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != ' ':
            return self.board[0][0]
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != ' ':
            return self.board[0][2]
        return None

    def is_board_full(self):
       
        return False  

    def parse_input(self, input_str):
        if len(input_str) != 2:
            return None
        row_char, col_char = input_str[0].upper(), input_str[1]
        if row_char not in ['A', 'B', 'C'] or col_char not in ['0', '1', '2']:
            return None
        row = ord(row_char) - 65
        col = int(col_char)
        return row, col

    def play(self):
        print("Benvenuto al Tris!")
        mode = input("Quanti giocatori? ( 1 o 2): ").strip()
        if mode == '1':
            self.single_player = True
            level = input("Scegli livello AI - facile (f) o difficile (d): ").strip().lower()
            self.ai_level = 'facile' if level == 'f' else 'difficile'
            print(f"Hai scelto livello: {self.ai_level}")
        else:
            self.single_player = False
            print("Modalità 2 giocatori!")

        while True:
            self.reset_game()
            print("Griglia iniziale:")
            self.print_board()

            while True:
                player = self.players[self.current_player]
                if self.single_player and player == 'O':
                    print("Turno del computer (O)...")
                    if self.ai_level == 'facile':
                        self.random_move()
                    else:
                        self.minimax_move()
                else:
                    print(f"Turno del giocatore {player}")
                    input_str = input("Inserisci la casella (es. 'A1'): ").strip()
                    coordinates = self.parse_input(input_str)

                    if not coordinates:
                        print("Input non valido. Usa formato 'A0', 'B1', ecc.")
                        continue

                    row, col = coordinates
                    if not self.make_move(row, col):
                        print("Mossa non valida. Casella occupata.")
                        continue

                self.print_board()

                winner = self.check_winner()
                if winner:
                    if self.single_player and winner == 'O':
                        print("Il computer ha vinto!")
                    else:
                        print(f"Il giocatore {winner} ha vinto!")
                    break

                if self.is_board_full():
                    print("Pareggio!")
                    break

            play_again = input("Vuoi giocare di nuovo? (s/n): ").strip().lower()
            if play_again != 's':
                print("Grazie per aver giocato! Arrivederci!")
                break

    def random_move(self):
        empty_cells = [(i, j) for i in range(3) for j in range(3) if self.is_valid_move(i, j)]
        if empty_cells:
            row, col = random.choice(empty_cells)
            self.make_move(row, col)

    def minimax_move(self):
        best_score = float('-inf')
        best_move = None

        for i in range(3):
            for j in range(3):
                if self.is_valid_move(i, j):
                    player = self.players[self.current_player]
                    removed = None

                    if len(self.moves[player]) >= 3:
                        removed = self.moves[player].pop(0)
                        old_row, old_col = removed
                        self.board[old_row][old_col] = ' '

                    self.board[i][j] = player
                    self.moves[player].append((i, j))

                    score = self.minimax(0, False)

                    self.moves[player].pop()
                    self.board[i][j] = ' '
                    if removed:
                        self.moves[player].insert(0, removed)
                        self.board[removed[0]][removed[1]] = player

                    if score > best_score:
                        best_score = score
                        best_move = (i, j)

        if best_move:
            print(f"Il computer gioca in {chr(65 + best_move[0])}{best_move[1]}")
            self.make_move(best_move[0], best_move[1])

    def minimax(self, depth, is_maximizing):
        if depth > 7:
            return 0

        winner = self.check_winner()
        if winner == 'O':
            return 1
        elif winner == 'X':
            return -1
       
        player = self.players[self.current_player if is_maximizing else 1 - self.current_player]
        best_score = float('-inf') if is_maximizing else float('inf')

        for i in range(3):
            for j in range(3):
                if self.is_valid_move(i, j):
                    removed = None

                    if len(self.moves[player]) >= 3:
                        removed = self.moves[player].pop(0)
                        old_row, old_col = removed
                        self.board[old_row][old_col] = ' '

                    self.board[i][j] = player
                    self.moves[player].append((i, j))

                    score = self.minimax(depth + 1, not is_maximizing)

                    self.moves[player].pop()
                    self.board[i][j] = ' '
                    if removed:
                        self.moves[player].insert(0, removed)
                        self.board[removed[0]][removed[1]] = player

                    if is_maximizing:
                        best_score = max(score, best_score)
                    else:
                        best_score = min(score, best_score)

        return best_score

if __name__ == "__main__":
    game = TicTacToe()
    game.play()


