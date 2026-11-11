"""IA de jogo da velha que escolhe jogadas com minimax."""

import math

from .game import actions, player, result, terminal, utility, X


def minimax(board):
    """Retorna uma jogada ótima para o jogador da vez, ou None se acabou."""
    if terminal(board):
        return None

    if player(board) == X:
        best_value = -math.inf
        best_action = None
        for action in actions(board):
            value = min_value(result(board, action))
            if value > best_value:
                best_value = value
                best_action = action
        return best_action

    best_value = math.inf
    best_action = None
    for action in actions(board):
        value = max_value(result(board, action))
        if value < best_value:
            best_value = value
            best_action = action
    return best_action


def max_value(board):
    if terminal(board):
        return utility(board)

    value = -math.inf
    for action in actions(board):
        value = max(value, min_value(result(board, action)))
    return value


def min_value(board):
    if terminal(board):
        return utility(board)

    value = math.inf
    for action in actions(board):
        value = min(value, max_value(result(board, action)))
    return value
