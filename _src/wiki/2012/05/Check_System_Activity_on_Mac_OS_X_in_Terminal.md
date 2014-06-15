From: [http://betabug.ch/blogs/ch-athens/227](http://betabug.ch/blogs/ch-athens/227)

So I'm logging into a Mac OS X machine (Server or not) remotely by ssh to do some maintenance and check on the health of the system. What I might be interested in is how CPU, memory and disk usage is coping with the jobs the server has to do. If I was sitting in front of the machine I could open "Activity Monitor" and click my way through the GUI. Not an option for this machine, since there is no GUI level remote access. So what do I do? There are some command line tools to give me the information I need, let me show you `top`, `vm_stat` and `iostat` ...

On my OpenBSD box "systat vmstat" is what I use for a full overview. That is not available for OS X, but some other tools are there. Most often used is "top", followed by "vm_stat" and "iostat".

top
---

"top" is well known and you likely have heard about it and probably used it before. The version on OS X is quite useable. After switching to "compatibility mode" (with 'x'), one can see only the processes of a single user (with 'U' and entering the user id or name). Top is good for checking what eats all the CPU time.

vm_stat
------

If it comes to memory usage, especially for the question "how much swap space am I using", then vm_stat can help. On Mac OS X that's vm_stat with an underscore, not vmstat. You just give vm_stat a delay in seconds (by calling it like "vm_stat 10" on the command line) and it updates the display repeatedly. Go on, try that out and then open a bunch of applications to see if pageouts are going up (which would mean that your machine has to page memory out on disk to make room for the new ones).

    $ vm_stat 5

...looks like my workstation is OK, even with starting up Acrobat Reader and a bunch of smaller programs at once.

iostat
-----

It took me longer to discover iostat. The man page says that "Iostat displays kernel I/O statistics on terminal, device and cpu operations." Which is quite a lot and probably more than I usually want. I just use it with a line like:

    $ iostat -d -K -w 5

to show me only devices (-d), kilobytes instead of blocks (-K), and have a wait interval of 5 seconds (-w 5). Go ahead, try it and watch it while doing a find for "foobar" on your disks. As usual with all command line tools, read the fine man pages.
