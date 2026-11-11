"""Regras e estado do jogo da velha."""

from copy import deepcopy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """Retorna um tabuleiro vazio de 3 por 3."""
    return [[EMPTY for _ in range(3)] for _ in range(3)]


def player(board):
    """Retorna o símbolo que deve jogar no próximo turno."""
    x_count = sum(cell == X for row in board for cell in row)
    o_count = sum(cell == O for row in board for cell in row)
    return O if x_count > o_count else X


def actions(board):
    """Retorna as posições vazias como tuplas (linha, coluna)."""
    return {
        (row, column)
        for row in range(3)
        for column in range(3)
        if board[row][column] == EMPTY
    }


def result(board, action):
    """Retorna uma cópia do tabuleiro após uma jogada válida."""
    row, column = action
    if row not in range(3) or column not in range(3):
        raise ValueError("A jogada deve estar dentro do tabuleiro.")
    if board[row][column] != EMPTY:
        raise ValueError("A posição escolhida já está ocupada.")

    next_board = deepcopy(board)
    next_board[row][column] = player(board)
    return next_board


def winner(board):
    """Retorna X ou O se houver vencedor; caso contrário, None."""
    lines = [
        *board,
        *[[board[row][column] for row in range(3)] for column in range(3)],
        [board[index][index] for index in range(3)],
        [board[index][2 - index] for index in range(3)],
    ]
    for line in lines:
        if line[0] is not EMPTY and line[0] == line[1] == line[2]:
            return line[0]
    return None


def terminal(board):
    """Indica se a partida terminou por vitória ou empate."""
    return winner(board) is not None or not actions(board)


def utility(board):
    """Retorna 1 para vitória de X, -1 para vitória de O e 0 para empate."""
    winning_player = winner(board)
    if winning_player == X:
        return 1
    if winning_player == O:
        return -1
    return 0
