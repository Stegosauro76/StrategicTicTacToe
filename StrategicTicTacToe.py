class TicTacToe:
    def __init__(self):
        self.reset_game()

    def reset_game(self):
        # Reinizializza il gioco
        self.board = [[' ' for _ in range(3)] for _ in range(3)]
        self.players = ['X', 'O']
        self.current_player = 0
        self.moves = {'X': [], 'O': []}

    def print_board(self):
        print("    0   1   2")  # Intestazione delle colonne
        print("  -------------")
        for i, row in enumerate(self.board):
            print(f"{chr(65 + i)} | {' | '.join(row)} |")  # Usa lettere per le righe (A, B, C)
            print("  -------------")

    def is_valid_move(self, row, col):
        return 0 <= row < 3 and 0 <= col < 3 and self.board[row][col] == ' '

    def make_move(self, row, col):
        player = self.players[self.current_player]
        if self.is_valid_move(row, col):
            if len(self.moves[player]) >= 3:
                # Rimuovi la mossa più vecchia
                old_row, old_col = self.moves[player].pop(0)
                self.board[old_row][old_col] = ' '
            self.board[row][col] = player
            self.moves[player].append((row, col))
            self.current_player = 1 - self.current_player
            return True
        return False

    def check_winner(self):
        # Controlla righe, colonne e diagonali
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
        return all(self.board[i][j] != ' ' for i in range(3) for j in range(3))

    def parse_input(self, input_str):
        # Converte input come "A1" in coordinate (riga, colonna)
        if len(input_str) != 2:
            return None
        row_char, col_char = input_str[0].upper(), input_str[1]
        if row_char not in ['A', 'B', 'C'] or col_char not in ['0', '1', '2']:
            return None
        row = ord(row_char) - 65  # Converti 'A' -> 0, 'B' -> 1, 'C' -> 2
        col = int(col_char)
        return row, col

    def play(self):
        while True:
            self.reset_game()  # Resetta il gioco per una nuova partita
            print("Griglia iniziale:")
            self.print_board()

            while True:
                player = self.players[self.current_player]
                print(f"Turno del giocatore {player}")
                input_str = input("Inserisci la casella (es. 'A1' per la prima casella in alto a sinistra): ").strip()
                coordinates = self.parse_input(input_str)

                if not coordinates:
                    print("Input non valido. Usa il formato 'A1', 'B2', ecc.")
                    continue

                row, col = coordinates
                if not self.make_move(row, col):
                    print("Mossa non valida. Assicurati che la casella sia vuota.")
                    continue

                # Stampa la griglia aggiornata dopo ogni mossa
                self.print_board()

                winner = self.check_winner()
                if winner:
                    print(f"Il giocatore {winner} ha vinto!")
                    break
                if self.is_board_full():
                    print("Pareggio!")
                    break

            # Chiedi all'utente se vuole giocare di nuovo
            play_again = input("Vuoi giocare di nuovo? (s/n): ").strip().lower()
            if play_again != 's':
                print("Grazie per aver giocato! Arrivederci!")
                break

if __name__ == "__main__":
    game = TicTacToe()
    game.play()
