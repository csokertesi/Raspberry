import curses

raspi = """,--------------------------------.
| ###ooo#oo#oooo#o#ooo J8   +======
| #ooo#ooo#ooo#oooooo#  PoE |   Net
|  Wi                    1o +======
|  Fi  Pi Model 4B  V1.5 oo      |
|        ,----. +---+         +====
| |D|    |SoC | |RAM|         |USB3
| |S|    |    | |   |         +====
| |I|    `----' +---+            |
|                   |C|       +====
|                   |S|       |USB2
| pwr   |hd|   |hd| |I||A|    +====
`-| |---|m0|---|m1|----|V|-------'"""

class Color:
    HIGHLIGHT = 1
    GREEN = 2
    RED = 3

def main(scr):
    scr.clear()
    curses.noecho()
    curses.curs_set(0)
    scr.keypad(1)
    curses.mousemask(1)
    curses.init_pair(Color.HIGHLIGHT, curses.COLOR_BLACK, curses.COLOR_WHITE)
    curses.init_pair(Color.RED, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(Color.GREEN, curses.COLOR_GREEN, curses.COLOR_BLACK)

    scr.addstr(0,0, "Raspberry Easy Pin Controller", curses.color_pair(Color.HIGHLIGHT))
    scr.addstr(2,0, raspi)
    while True:
        e = scr.getch()
        if e == ord("q"): break
        #if e == curses.KEY_MOUSE: scr.addstr(0,0, f"{curses.getmouse()}")
        scr.addstr(2,0, raspi)



        scr.refresh()


    
    curses.curs_set(1)
    scr.keypad(0)
    curses.mousemask(0)

curses.wrapper(main)