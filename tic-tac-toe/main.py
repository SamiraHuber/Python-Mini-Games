import board as board
import player as player
import cpu as cpu

board = board.board()
player = player.player()
cpu = cpu.cpu()

gameRunning = 0
currentPlayer = 0

while (gameRunning == 0):
    board.print_it()
    if (currentPlayer == 0):
        player.make_turn(board)
        currentPlayer = 1
    else:
        cpu.make_turn(board)
        currentPlayer = 0
    gameRunning = board.is_finished()

board.print_it()

