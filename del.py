import curses
import time

stdscr = curses.initscr()
curses.noecho()  # Disable echoing of input characters
curses.cbreak()

def update_line(stdscr, text):
    stdscr.addstr(0, 0, text)
    stdscr.refresh()

for i in range(3600):
    update_line(stdscr, f"{i}")
    time.sleep(1)
