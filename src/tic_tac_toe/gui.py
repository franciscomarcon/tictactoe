"""Interface gráfica do jogo feita com Pygame."""

import sys
import time

import pygame

from . import EMPTY, O, X, initial_state, minimax, player, result, terminal, winner


def main():
    """Inicia o jogo gráfico."""
    pygame.init()
    width, height = 600, 400
    black = (0, 0, 0)
    white = (255, 255, 255)
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Jogo da Velha — Minimax")

    medium_font = pygame.font.SysFont("Arial", 28)
    large_font = pygame.font.SysFont("Arial", 40)
    move_font = pygame.font.SysFont("Arial", 60)

    user = None
    board = initial_state()
    ai_turn = False

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        screen.fill(black)

        if user is None:
            title = large_font.render("Jogue jogo da velha", True, white)
            screen.blit(title, title.get_rect(center=(width / 2, 50)))

            play_x_button = pygame.Rect(width / 8, height / 2, width / 4, 50)
            play_o_button = pygame.Rect(5 * (width / 8), height / 2, width / 4, 50)
            for button, label in ((play_x_button, "Jogar como X"), (play_o_button, "Jogar como O")):
                pygame.draw.rect(screen, white, button)
                text = medium_font.render(label, True, black)
                screen.blit(text, text.get_rect(center=button.center))

            if pygame.mouse.get_pressed()[0]:
                mouse = pygame.mouse.get_pos()
                if play_x_button.collidepoint(mouse):
                    user = X
                    time.sleep(0.2)
                elif play_o_button.collidepoint(mouse):
                    user = O
                    time.sleep(0.2)
        else:
            tile_size = 80
            tile_origin = (width / 2 - 1.5 * tile_size, height / 2 - 1.5 * tile_size)
            tiles = []
            for row in range(3):
                tile_row = []
                for column in range(3):
                    rect = pygame.Rect(
                        tile_origin[0] + column * tile_size,
                        tile_origin[1] + row * tile_size,
                        tile_size,
                        tile_size,
                    )
                    pygame.draw.rect(screen, white, rect, 3)
                    if board[row][column] != EMPTY:
                        mark = move_font.render(board[row][column], True, white)
                        screen.blit(mark, mark.get_rect(center=rect.center))
                    tile_row.append(rect)
                tiles.append(tile_row)

            game_over = terminal(board)
            current_player = player(board)
            if game_over:
                winning_player = winner(board)
                title_text = "Fim de jogo: empate." if winning_player is None else f"Fim de jogo: {winning_player} venceu."
            elif user == current_player:
                title_text = f"Sua vez: {user}"
            else:
                title_text = "A IA está pensando..."
            title = large_font.render(title_text, True, white)
            screen.blit(title, title.get_rect(center=(width / 2, 30)))

            if user != current_player and not game_over:
                if ai_turn:
                    time.sleep(0.2)
                    board = result(board, minimax(board))
                    ai_turn = False
                else:
                    ai_turn = True

            if pygame.mouse.get_pressed()[0] and user == current_player and not game_over:
                mouse = pygame.mouse.get_pos()
                for row in range(3):
                    for column in range(3):
                        if board[row][column] == EMPTY and tiles[row][column].collidepoint(mouse):
                            board = result(board, (row, column))

            if game_over:
                again_button = pygame.Rect(width / 3, height - 65, width / 3, 50)
                pygame.draw.rect(screen, white, again_button)
                again_text = medium_font.render("Jogar novamente", True, black)
                screen.blit(again_text, again_text.get_rect(center=again_button.center))
                if pygame.mouse.get_pressed()[0] and again_button.collidepoint(pygame.mouse.get_pos()):
                    time.sleep(0.2)
                    user = None
                    board = initial_state()
                    ai_turn = False

        pygame.display.flip()


if __name__ == "__main__":
    main()
