simple\_curses\_menu
====================

Super simple function for interactively asking user to choose from options. Function returns index of choice.

Example invocation
------------------

    choice = simple_curses_menu("Do you like this?", ["Yes", "No"])
    if choice == 0:
      print "Glad you like it!"
    else:
      print "Sorry to hear that, anything I can do to help?"
