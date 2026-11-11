"""Jogo da velha com uma IA baseada no algoritmo minimax."""

from .game import (
    EMPTY,
    O,
    X,
    actions,
    initial_state,
    player,
    result,
    terminal,
    utility,
    winner,
)
from .ai import minimax

__all__ = [
    "EMPTY",
    "O",
    "X",
    "actions",
    "initial_state",
    "minimax",
    "player",
    "result",
    "terminal",
    "utility",
    "winner",
]
