The problem
-----------

We I ran command:

    $ grep "allpage" . -rl | xargs sed -i 's/allpage/common/g'

Or specially I ran this:

    $ sed -i 's/allpage/common/g' ./server/docs/api.md

An Error occurred:

    $ sed: 1: "./server/docs/api.md": invalid command code .

When I changed the command into this:

    $ sed -i 's/allpage/common/g' server/docs/api.md

And error became this:

    $ sed: 1: "server/docs/api.md": unterminated substitute in regular expression

This sed version was `May 10, 2005` as I saw in `man sed`.

Fix It
-----

Download the newest version of GNU sed from [here](http://ftp.gnu.org/gnu/sed/):

    :::bash
    $ tar xfz sed-4.2.tar.gz
    $ cd sed-4.2
    $ ./configure
    $ make
    $ sudo make install

Then the former command will execute properly.
