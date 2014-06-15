On Ubuntu Server, when I run pg_dump or something, I got:


    perl: warning: Setting locale failed.
    perl: warning: Please check that your locale settings:
        LANGUAGE = (unset),
        LC_ALL = (unset),
        LANG = "en_US.utf8"
        are supported and installed on your system.
    perl: warning: Falling back to the standard locale ("C").


I googled a lot - <a href="http://www.cgurnik.com/2011/02/20/fixing-perl-warning-setting-locale-failed-in-ubuntu/">here</a>, <a href="http://www.thomas-krenn.com/de/wiki/Perl_warning_Setting_locale_failed_unter_Debian">here</a>, and <a href="http://blog.loftninjas.org/2008/11/17/perl-warning-setting-locale-failed/">here</a>.

Now I fixed it. But I don't know which one make it works (Or, without which one, it won't work :)

So you can try the steps bellow and see if the problem resolved after every step.

Step 1:
Add the following code at the end of ~/.bashrc

    export LANGUAGE=en_US.UTF-8
    export LANG=en_US.UTF-8
    export LC_ALL=en_US.UTF-8


Step 2:
Run this command:

    sudo apt-get install language-pack-en


Step 3:
Run this:

    sudo dpkg-reconfigure locales


Hope this helpful.
