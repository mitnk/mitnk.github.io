终于完成了一个LFS系统。将这个过程用到的包包们整理一下：

- **Linux-3.5.2 API Headers**
    - The Linux API Headers expose the kernel's API for use by Glibc.

- **Man-Pages-3.42**
    - This package contains over 1900 man pages

- **Glibc-2.16.0 (17.6)**
    - This package contains the main C library. This library provides the basic
        routines for allocating memory, searching directories, opening and 
        closing files, reading and writing files, string handling, pattern
        matching, arithmetic, and so on.
    - Installed programs: catchsegv, gencat, getconf, getent, iconv,
        iconvconfig, ldconfig, ldd, lddlibc4, locale, localedef, mtrace, nscd,
        pcprofiledump, pt_chown, rpcgen, sln, sotruss, sprof, tzselect, xtrace,
        zdump, and zic

- **Zlib-1.2.7**
    - The Zlib package contains compression and decompression routines used by
        some programs

- **File-5.11**
    - The File package contains a utility for determining the type of files.
    - Installed programs: file

- **Bintuils-2.22**
    - The Bintuils package contains a linker, an assembler, and other tools
        for handling object files
    - Installed programs: addr2line, ar, as, c++filt, elfedit, gprof, ld,
        ld.bfd, nm, objcopy, objdump, ranlib, readelf, size, strings, and strip

- **GMP-5.0.5**
    - The GMP package contains math libraries. These have useful functions for
        arbitrary presision arithmetic

- **MPFR-3.1.1**
    - The MPFR package contains functions for multiple precision math

- **MPC-1.0**
    - The MPC package contains a library for the arithmetic of complex number
        with arbitrarily high precision and correct rounding of the result.

- **GCC-4.7.1 (53.5)**
    - The GCC package contains the GNU compiler collection, which includes the
        C and C++ compilers.
    - Installed programs: c++, cc (link to gcc), cpp, g++, gcc, gccbug,
        and gcov

- **Sed-4.2.1**

- **Bzip2-1.0.6**
    - The Bzip2 package contains programs for compressing and decompressing
        files. Compressing text files with bzip2 yields a much better
        compression percentage than with the traditional gzip.
    - Installed programs: bunzip2 (link to bzip2), bzcat (link to bzip2),
        bzcmp (link to bzdiff), bzdiff, bzegrep (link to bzgrep), 
        bzfgrep (link to bzgrep), bzgrep, bzip2, bzip2recover, bzless 
        (link to bzmore), and bzmore

- **Pkg-config-0.27**
    - the pkg-config package contains a tool for passing the include path
        and/or library paths to build tools during the configure and make
        file execution.
    - Installed programs: pkg-config

- **Ncurses-5.9**
    - The Ncurses package contains libraries for terminal-independent handling
        of character screens.
    - Installed programs: captoinfo (link to tic), clear, infocmp,
        infotocap (link to tic), ncursesw5-config, reset (link to tset),
        tabs, tic, toe, tput, and tset

- **Util-linux-2.21.2**
    - The Util-linux package contains miscellaneous utility programs. Among
        them are utilities for handling file systems, consoles, partitions,
        and messages.
    - Installed programs: addpart, agetty, blkid, blockdev, cal, cfdisk, chcpu,
        chkdupexe, chrt, col, colcrt, colrm, column, ctrlaltdel, cytune,
        delpart, dmesg, fallocate, fdformat, fdisk, findfs, findmnt, flock,
        fsck, fsck.cramfs, fsck.minix, fsfreeze, fstrim, getopt, hexdump,
        hwclock, i386, ionice, ipcmk, ipcrm, ipcs, isosize, ldattach, linux32,
        linux64, logger, look, losetup, lsblk, lscpu, mcookie, mkfs, mkfs.bfs,
        mkfs.cramfs, mkfs.minix, mkswap, more, mount, mountpoint, namei, partx,
        pg, pivot_root, prlimit, raw, readprofile, rename, renice, rev,
        rtcwake, script, scriptreplay, setarch, setsid, setterm, sfdisk,
        swaplabel, swapoff (link to swapon), swapon, switch_root, tailf,
        taskset, tunelp, ul, umount, unshare, uuidd, uuidgen, wall, whereis,
        wipefs, and x86_64

- **Psmisc-22.19**
    - The Psmisc package contains programs for displaying information about
        running processes.
    - Installed programs: fuser, killall, peekfd, prtstat, pstree,
        and pstree.x11 (link to pstree)

- **E2fsprogs-1.42.5 (1.7)**
    - The E2fsprogs package contains the utilities for handling the ext2 file
        system. It also supports the ext3 and ext4 journaling file systems.
    - Installed programs: badblocks, chattr, compile_et, debugfs, dumpe2fs,
        e2freefrag, e2fsck, e2image, e2initrd_helper, e2label, e2undo,
        e4defrag, filefrag, fsck.ext2, fsck.ext3, fsck.ext4, fsck.ext4dev,
        logsave, lsattr, mk_cmds, mke2fs, mkfs.ext2, mkfs.ext3, mkfs.ext4,
        mkfs.ext4dev, mklost+found, resize2fs, and tune2fs

- **Shadow-4.1.5.1**
    - The Shadow package contains programs for handling passwords in secure way
    - Installed programs: chage, chfn, chgpasswd, chpasswd, chsh, expiry,
        faillog, gpasswd, groupadd, groupdel, groupmems, groupmod, grpck,
        grpconv, grpunconv, lastlog, login, logoutd, newgrp, newusers, nologin,
        passwd, pwck, pwconv, pwunconv, sg (link to newgrp), su, useradd,
        userdel, usermod, vigr (link to vipw), and vipw

- **Coreutils-8.19 (4.0)**
    - The Coreutils package contains utilities for showing and setting the
        basic system characteristics.
    - Installed programs: base64, basename, cat, chcon, chgrp, chmod, chown,
        chroot, cksum, comm, cp, csplit, cut, date, dd, df, dir, dircolors,
        dirname, du, echo, env, expand, expr, factor, false, fmt, fold, groups,
        head, hostid, id, install, join, link, ln, logname, ls, md5sum, mkdir,
        mkfifo, mknod, mktemp, mv, nice, nl, nohup, nproc, od, paste, pathchk,
        pinky, pr, printenv, printf, ptx, pwd, readlink, realpath, rm, rmdir,
        runcon, seq, sha1sum, sha224sum, sha256sum, sha384sum, sha512sum,
        shred, shuf, sleep, sort, split, stat, stdbuf, stty, sum, sync, tac,
        tail, tee, test, timeout, touch, tr, true, truncate, tsort, tty, uname,
        unexpand, uniq, unlink, users, vdir, wc, who, whoami, and yes

- **Iana-Etc-2.30**
    - The Iana-Etc package provides data for network services and protocols.

- **M4-1.4.16**
    - The M4 package contains a macro processor
    - Installed processor: m4

- **Bison-2.6.2**
    - The Bison contains a parser generator
    - Installed programs: bison and yacc

- **Procps-3.2.8**
    - The Procps package contains programs for monitoring processes.
    - Installed programs: free, kill, pgrep, pkill, pmap, ps, pwdx, skill,
        slabtop, snice, sysctl, tload, top, uptime, vmstat, w, and watch

- **Grep-2.14**
    - Installed programs: egrep, fgrep, and grep

- **Readline-6.2**
    - The Readline package is a set of libraries that offers command-line
        editing and history capabilities.

- **Bash-4.2 (1.7)**
    - The Bash package contains the Bourne-Again SHell.
    - Installed programs: bash, bashbug, and sh (link to bash)

- **Libtool-2.4.2 (3.0)**
    - The Libtool package contains the GNU generic library support script. It
        wraps the complexity of using shared libraries in a consistent, portable
        interface.
    - Installed programs: libtool and libtoolize

- **GDBM-1.10**
    - The GDBM package contains the GNU Database Manager. This is a disk file
        format database which stores key/data-pairs in single files. The actual
        data of any record being stored is indexed by a unique key, which
        can be retrieved in less time than if it was stored in a text file.

- **Inetutils-1.9.1**
    - The Inetutils package contains programs for basic networking
    - Installed programs: ftp, hostname, ping, ping6, rcp, rexec, rlogin, rsh,
        talk, telnet, tftp, and traceroute

- **Perl-5.16.1 (7.5)**
    - The Perl package contains the Practical Extraction and Report Language.
    - Install programs: a2p, c2ph, config_data, corelist, cpan, cpan2dist,
        cpanp, cpanp-run-perl, dprofpp, enc2xs, find2perl, h2ph, h2xs,
        instmodsh, json_pp, libnetcfg, perl, perl5.16.1 (link to perl),
        perlbug, perldoc, perlivp, perlthanks (link to perlbug), piconv,
        pl2pm, pod2html, pod2latex, pod2man, pod2text, pod2usage, podchecker,
        podselect, prove, psed (link to s2p), pstruct (link to c2ph), ptar,
        ptardiff, ptargrep, s2p, shasum, splain, and xsubpp

- **Autoconf-2.69 (4.5)**
    - The Autoconf package contains programs for producing shell scripts that
        can automatically configure source code
    - Install programs: autoconf, autoheader, autom4te, autoreconf, autoscan,
        autoupdate, and ifnames

- **Automake-1.12.3**
    - The Automake package contains programs for generating Makefiles for use
        with Autoconf.
    - Installed programs: acinstall, aclocal, aclocal-1.12, automake,
        automake-1.12, compile, config.guess, config.sub, depcomp, elisp-comp,
        install-sh, mdate-sh, missing, mkinstalldirs, py-compile, symlink-tree,
        and ylwrap

- **Diffutils-3.2**
    - The Diffutils package contains programs that show the differences between
        files or directories.
    - Installed programs: cmp, diff, diff3, and sdiff

- **Gawk-4.0.1**
    - The Gawk package contains programs for manipulating text files
    - Installed programs: awk (link to gawk), dgawk, gawk, gawk-4.0.1, grcat,
        igawk, pgawk, pgawk-4.0.1, and pwcat

- **Findutils-4.4.2**
    - The Findutils package contains programs to find files. These programs are
        provided to recursively search through a directory tree and to create,
        maintain, and search a database.
    - Installed programs: bigram, code, find, frcode, locate, oldfind,
        updatedb, and xargs

- **Flex-2.5.37**
    - The Flex package contains a utility for generating programs that recognize
        patterns in text
    - Installed programs: flex and lex

- **Gettext-0.18.1.1 (2.3)**
    - The Gettext package contains utilities for internationalization and 
        localization. These allow programs to be compiled with NLS (Native
        Language Support), enabling them to output messages in the user's native
        language.
    - Installed programs: autopoint, config.charset, config.rpath, envsubst,
        gettext, gettext.sh, gettextize, hostname, msgattrib, msgcat, msgcmp,
        msgcomm, msgconv, msgen, msgexec, msgfilter, msgfmt, msggrep, msginit,
        msgmerge, msgunfmt, msguniq, ngettext, recode-sr-latin, and xgettext

- **Groff-1.21**
    - The Groff package contains programs for processing and formatting text
    - Installed programs: addftinfo, afmtodit, chem, eqn, eqn2graph, gdiffmk,
        geqn (link to eqn), grap2graph, grn, grodvi, groff, groffer, grog,
        grolbp, grolj4, grops, grotty, gtbl (link to tbl), hpftodit, indxbib,
        lkbib, lookbib, mmroff, neqn, nroff, pdfroff, pfbtops, pic, pic2graph,
        post-grohtml, preconv, pre-grohtml, refer, roff2dvi, roff2html,
        roff2pdf, roff2ps, roff2text, roff2x, soelim, tbl, tfmtodit, and troff

- **Xz-5.0.4**
    - The Xz package contains programs for compressing and decompressing files.
        It provides capabilities for the lzma and the newer xz compression
        formats. Compressing text file with xz yields a better compression
        percentage than with gzip or bzip2 commands
    - Installed programs: lzcat (link to xz), lzcmp (link to xzdiff),
        lzdiff (link to xzdiff), lzegrep (link to xzgrep),
        lzfgrep (link to xzgrep), lzgrep (link to xzgrep),
        lzless (link to xzless), lzma (link to xz), lzmadec, lzmainfo,
        lzmore (link to xzmore), unlzma (link to xz), unxz, (link to xz), xz,
        xzcat (link to xz), xzcmp (link to xzdiff), xzdec, xzdiff,
        xzegrep (link to xzgrep), xzfgrep (link to xzgrep), xzgrep, xzless,
        xzmore

- **GRUB-2.00**
    - The GRUB package contains the GRand Unified Bootloader.

- **Less-444**
    - The Less package contains a text file viewer.
    - Installed programs: less, lessecho, and lesskey

- **Gzip-1.5**
    - The Gzip package contains programs for compressing and decompressing files.
    - Installed programs: gunzip, gzexe, gzip, uncompress, zcat, zcmp, zdiff,
        zegrep, zfgrep, zforce, zgrep, zless, zmore, and znew

- **IPRoute2-3.5.1**
    - The IPRoute2 package contains programs for basic and advanced IPV4-based
        networking.
    - Installed programs: ctstat (link to lnstat), genl, ifcfg, ifstat, ip,
        lnstat, nstat, routef, routel, rtacct, rtmon, rtpr,
        rtstat (link to lnstat), ss, and tc

- **Kbd-1.15.3**
    - The Kbd package contains key-table files, console fonts, and keyboard
        utilities.
    - Installed programs: chvt, deallocvt, dumpkeys, fgconsole, getkeycodes,
        kbd_mode, kbdrate, loadkeys, loadunimap, mapscrn, openvt,
        psfaddtable (link to psfxtable), psfgettable (link to psfxtable),
        psfstriptable (link to psfxtable), psfxtable, setfont, setkeycodes,
        setleds, setmetamode, showconsolefont, showkey, unicode_start,
        and unicode_stop

- **Kmod-9**
    - The Kmod package console libraries and utilities for loading kernel
        moudules
    - Installed programs: depmod (link to kmod), insmod (link to kmod), kmod,
        kmod-nolib, lsmod (link to kmod), modinfo (link to kmod),
        modprobe (link to kmod), and rmmod (link to kmod)

- **Libpipeline-1.2.1**
    - The Libpipeline package contains a library for manipulating pipelines of
        subprocess in a flexible and convenient way.

- **Make-3.82**
    - The Make package contains a program for compiling packages.
    - Installed programs: make

- **Man-DB-2.6.2**
    - The Man-DB package contains programs for finding and viewing man pages.
    - Installed programs: accessdb, apropos (link to whatis), catman, lexgrog,
        man, mandb, manpath, whatis, and zsoelim

- **Patch-2.6.1**
    - The Patch package contains a program for modifying or creating files by
        applying a “patch” file typically created by the diff program.
    - Installed programs: patch

- **Sysklogd-1.5**
    - The Sysklogd package contains programs for logging system messages,
        such as those given by the kernel when unusual things happen.
    - Installed programs: klogd and syslogd

- **Sysvinit-2.88dsf**
    - The Sysvinit package contains programs for controlling the startup,
        running, and shutdown of the system.
    - Installed programs: bootlogd, fstab-decode, halt, init, killall5, last,
        lastb (link to last), mesg, pidof (link to killall5),
        poweroff (link to halt), reboot (link to halt), runlevel, shutdown,
        sulogin, telinit (link to init), and utmpdump

- **Tar-1.26 (2.4)**
    - The Tar package contains an archiving program.
    - Installed programs: rmt and tar

- **Texinfo-4.13a**
    - The Texinfo package contains programs for reading, writing, and converting
        info pages.
    - Installed programs: info, infokey, install-info, makeinfo, pdftexi2dvi,
        texi2dvi, texi2pdf, and texindex

- **Udev-188 (from systemd-188)**
    - The Udev package contains programs for dynamic creation of device nodes.
        The development of udev has been merged with systemd, but most of
        systemd is incompatible with LFS. Here we build and install just the
        needed udev files.
    - Installed programs: accelerometer, ata_id, cdrom_id, collect, mtd_probe,
        scsi_id, v4l_id, udevadm, and udevd

- **Vim-7.3 (1.1)**
