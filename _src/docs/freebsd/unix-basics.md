FreeBSD - UNIX Basics
=====================

## Virtual Consoles and Terminals

The key combinations Alt+F1 through Alt+F8 have been reserved by FreeBSD for switching between virtual consoles. Use Alt+F1 to switch to the system console (ttyv0), Alt+F2 to access the first virtual console (ttyv1), Alt+F3 to access the second virtual console (ttyv2), and so on.

- syscons, sc -- the    console    driver
- atkbd -- the AT keyboard interface
- vidcontrol    -- system console control and configuration utility
- kbdcontrol    -- keyboard control and    configuration utility

virtual consoles is configured in this section of /etc/ttys. Note that the last virtual console (ttyv8) is used to access the graphical environment.

- ttys(5) -- terminal initialization information

The FreeBSD boot menu provides an option labelled as “Boot Single User”. This mode is typically used to repair a system that will not boot or to reset the root password when it is not known. While in single user mode, networking and other virtual consoles are not available. However, full root access to the system is available, and by default, the root password is not needed.

The settings which control single user mode are found in /etc/ttys.

### Changing Console Video Modes

The FreeBSD console default video mode may be adjusted to 1024x768, 1280x1024, or any other size supported by the graphics chip and monitor. To use a different video mode load the VESA module:

    :::
    # kldload vesa

To determine which video modes are supported by the hardware:

    :::
    # vidcontrol -i mode

To select a new video mode:

    :::
    # vidcontrol MODE_279

A mode can be permanently set on boot by adding it to /etc/rc.conf:

    :::
    # allscreens_flags="MODE_279"

[1] https://www.freebsd.org/doc/en_US.ISO8859-1/books/handbook/basics.html
