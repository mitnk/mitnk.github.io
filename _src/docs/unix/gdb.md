gdb cheat sheet
===============

> I don't like debuggers. Never have, probably never will.
> I use gdb all the time, but I tend to use it not as a debugger,
> but as a disassembler on steroids that you can program.

> -- Linus Torvalds [Sep 2000](http://static.lwn.net/2000/0914/a/lt-debugger.php3)


    :::
    +---------+--------------+---------------------------------------------+
    | Group   | Command      | Meaning                                     |
    +---------+--------------+---------------------------------------------+
    | Go      | run          | Run the program from the start.             |
    |         |              |                                             |
    |         | run args     | Run the program from the start, with the    |
    |         |              | given command-line arguments.               |
    |         |              |                                             |
    | Stop    | b get_rss    | Pause your program at a certain function.   |
    |         |              |                                             |
    |         | b foo.c:105  | Pause just before a certain line of code.   |
    |         |              |                                             |
    |         | break 105    | Same as b foo.c:105 if you are already      |
    |         |              | stopped in foo.c.                           |
    |         |              |                                             |
    |         | info break   | List breakpoints.                           |
    |         |              |                                             |
    |         | watch url    | Break if the value of the given variable    |
    |         |              | changes.                                    |
    |         |              |                                             |
    |         | dis 3 / ena  | Disable/reenable/delete breakpoint3. If you |
    |         | 3 / del 3    | have a lot of breakpoints set, disable by   |
    |         |              | itself turns them all off, and then you can |
    |         |              | enable the one or two that you need at the  |
    |         |              | moment; likewise forenable/ delete.         |
    |         |              |                                             |
    | Inspect | p url        | Print the value ofurl. You may specify any  |
    |         |              | expression, including function calls.       |
    |         |              |                                             |
    |         | p            | Print the first 10 elements of an_array.    |
    |         | *an_array@10 | The next 10 are p *(an_array+10)@10.        |
    |         |              |                                             |
    |         | mem read     | Read a count of 10 items of type double     |
    |         | -tdouble     | from an_array. The next 10 are mem read     |
    |         | -c10         | -tdouble -c10 an_array+10.                  |
    |         | an_array     |                                             |
    |         |              |                                             |
    |         | info args /  | Get the values of all arguments to the      |
    |         | info vars    | function or all local variables.            |
    |         |              |                                             |
    |         | disp url     | Display the value ofurlevery time the       |
    |         |              | program stops.                              |
    |         |              |                                             |
    |         | undisp 3     | Stop the display the of display item 3.     |
    |         |              | GDB: with no number, turn them all off.     |
    |         |              |                                             |
    | Threads | info thread  | List the active threads.                    |
    |         |              |                                             |
    |         | thread 2     | Switch focus to thread2                     |
    |         |              |                                             |
    | Frames  | bt           | List the stack of frames.                   |
    |         |              |                                             |
    |         | f 3          | Look at frame 3.                            |
    |         |              |                                             |
    |         | up / down    | Go numerically one up or down in the stack  |
    |         |              | of frames.                                  |
    |         |              |                                             |
    | Step    | s            | Step one line, even if that means entering  |
    |         |              | another function.                           |
    |         |              |                                             |
    |         | n            | Next line, but do not enter subfunctions,   |
    |         |              | and possibly back up to the head of a loop. |
    |         |              |                                             |
    |         | u            | Until the next line forward from the        |
    |         |              | current line (so let an already- visited    |
    |         |              | loop run through until forward progress).   |
    |         |              |                                             |
    |         | c            | Continue until the next breakpoint or the   |
    |         |              | end of the program.                         |
    |         |              |                                             |
    |         | ret / ret 3  | Return from the current function            |
    |         |              | immediately with the given return value (if |
    |         |              | any).                                       |
    |         |              |                                             |
    |         | j 105        | Jump to whatever line you please (within    |
    |         |              | reason).                                    |
    |         |              |                                             |
    | Code    | l            | list prints the 10 lines around the line    |
    |         |              | you are currently on.                       |
    |         |              |                                             |
    | Repeat  | Enter        | Just hitting Enter will repeat the last     |
    |         |              | command, which makes stepping easier, or    |
    |         |              | afterl, Enter will list the next 10 lines   |
    |         |              | after those you just saw.                   |
    |         |              |                                             |
    | Compile | make         | Runmakewithout exiting GDB. You can also    |
    |         |              | specify a target, like make myprog.         |
    |         |              |                                             |
    | Help    | help         | Explore everything else the debugger        |
    |         |              | offers.                                     |
    +---------+--------------+---------------------------------------------+


From: [21st Century C: C Tips from the New School](http://www.amazon.com/gp/product/1491903899/)
