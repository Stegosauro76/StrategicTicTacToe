# 🕹️ Tic Tac Toe - 3-Move Variant

Welcome to **Tic Tac Toe** with a twist!  
In this special version of the classic game, **each player can have only 3 active moves** on the board at a time, making the gameplay more dynamic and strategic.

---

## 📋 How the Game Works

- The board is a **3x3 grid**.
- There are **two players**: `X` and `O`.
- Players take turns placing their symbol by entering a cell coordinate (e.g., `A0`, `B2`).
- The goal is to align **three of your symbols** horizontally, vertically, or diagonally.

If the board fills up and no one wins, the game ends in a **draw**.

---

## 🔥 Special Rule: Maximum 3 Active Moves

- Each player can have **at most 3 active symbols** on the board.
- When a player makes a **fourth move**, their **oldest move** is automatically **removed**.
  
This rule adds a new level of strategy: you have to plan your moves carefully!

---

## 🚀 How to Play

1. Make sure you have **Python 3** installed.
2. Download the file: `tic_tac_toe.py`.
3. Open a terminal (or command prompt).
4. Navigate to the folder where you saved the file.
5. Run the game with the command:

   ```bash
   python tic_tac_toe.py

🎯 Input Format
When prompted, enter the cell coordinate where you want to place your move:

Rows are labeled A, B, C.

Columns are labeled 0, 1, 2.

Example:

rust
Copia
Modifica
Player X's turn
Enter the cell (e.g., 'A1' for the top center cell): B2
🔄 Play Again




After a match ends:

Type s to start a new game (yes).

Type n to exit the game (no).

💡 Features
Clear board display after every move.

Input validation (invalid or occupied cells are rejected).

Automatic move removal when exceeding 3 moves.

Win detection and draw handling.

Option to replay after each game.

👨‍💻 Author
Created with passion for coding and gaming fun! 🎮✨

