import curses
from curses import wrapper

def start_screen(stdscr):
    stdscr.clear()
    stdscr.addstr('Bem-Vindo ao Teste de Velocidade de Digitação!')
    stdscr.addstr('\nAperte qualquer tecla.')
    stdscr.refresh()
    stdscr.getkey()



def main(stdscr):
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_YELLOW, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_WHITE, curses.COLOR_BLACK)

    start_screen(stdscr)

wrapper(main)
