def print_board(board):
    print("  0 1 2")
    for row in range(3):
        print(row, end=' ')
        for col in range(3):
            print(board[row][col], end=' ')
        print()


def check_winner(board):
    # Проверка строк и столбцов
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != '-':
            return board[i][0]  # Победитель найден
        if board[0][i] == board[1][i] == board[2][i] != '-':
            return board[0][i]

    # Проверка диагоналей
    if board[0][0] == board[1][1] == board[2][2] != '-':
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != '-':
        return board[0][2]

    # Проверка на ничью
    if all(cell != '-' for row in board for cell in row):
        return 'Ничья'

    return None  # Игра продолжается


def is_valid_move(board, row, col):
    return 0 <= row < 3 and 0 <= col < 3 and board[row][col] == '-'


def main():
    board = [['-' for _ in range(3)] for _ in range(3)]
    current_player = 'X'

    while True:
        print_board(board)
        row = int(input(f"Игрок {current_player}, введите номер строки (0-2): "))
        col = int(input(f"Игрок {current_player}, введите номер столбца (0-2): "))

        if is_valid_move(board, row, col):
            board[row][col] = current_player
        else:
            print("Некорректный ход. Попробуйте снова.")
            continue

        winner = check_winner(board)
        if winner:
            print_board(board)
            if winner == 'Ничья':
                print("Игра завершилась ничьей!")
            else:
                print(f"Игрок {winner} выиграл!")
            break

        current_player = 'O' if current_player == 'X' else 'X'


if __name__ == "__main__":
    main()