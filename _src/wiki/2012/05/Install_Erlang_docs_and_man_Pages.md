Assuming that we have installed erlang from source using `sudo make install`.
Then we can [install docs like this](http://www.erlang.org/doc/installation_guide/INSTALL.html#The-ErlangOTP-Documentation):

    $ cd otp_src_R15B
    $ export PATH=/usr/local/lib/erlang/bin:$PATH
    $ make docs
    $ sudo make install-docs
    $ cd /usr/local/lib/erlang/doc
    $ open index.html

Download Erlang man page from here:
[http://www.erlang.org/download.html](http://www.erlang.org/download.html)

Check manpath

    $ manpath
    /usr/local/share/man:/usr/share/man:/usr/X11/man:/usr/local/git/share/man

Copy man pages to man path:

    $ tar xfz otp_doc_man_R15B01.tar.gz
    $ ls man
    man1 man3 man4 man6 man7
    $ sudo cp -r man/* /usr/local/share/man/

Test:

    $ man erl

Updated: Erlang's man pages may not need to download, since there is already a copy at `/usr/local/lib/erlang/man`. Just copy them into manpath.