#!/usr/bin/env python

import curses

def simple_curses_menu(prompt, choices):
  def impl(stdscr, prompt, choices):
    curses.use_default_colors()
    selected = 0
    ch = curses.KEY_RESIZE
    while ch != ord('\n'):
      if ch == curses.KEY_DOWN:
        selected = min(selected + 1, len(choices) - 1)
      elif ch == curses.KEY_UP:
        selected = max(0, selected - 1)
      (height, width) = stdscr.getmaxyx()
      stdscr.addnstr(0, 0, prompt, width, curses.A_BOLD)
      for (i, choice) in enumerate(choices):
        if i + 1 < height:
          stdscr.addnstr(1 + i, 0, choice, width)
          stdscr.clrtoeol()
      number_string = "({0}/{1})".format(selected + 1, len(choices))
      stdscr.addnstr(min(height-1, selected+1), 0, choices[selected], width - len(number_string), curses.A_REVERSE)
      stdscr.addstr(min(height-1, selected+1), width - len(number_string), number_string)
      ch = stdscr.getch()
    stdscr.clear()
    return selected
  return curses.wrapper(impl, prompt, choices)