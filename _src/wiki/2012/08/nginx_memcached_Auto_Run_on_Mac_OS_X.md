nginx
-----

Install nginx with `brew install nginx`

Config files at: `/usr/local/etc/nginx/`

nginx at: `/usr/local/sbin/nginx -v`

Output after installing:

In the interest of allowing you to run `nginx` without `sudo`, the default
port is set to localhost:8080.

If you want to host pages on your local machine to the public, you should
change that to localhost:80, and run `sudo nginx`. You'll need to turn off
any other web servers running port 80, of course.

You can start nginx automatically on login running as your user with:

    mkdir -p ~/Library/LaunchAgents
    cp /usr/local/Cellar/nginx/1.2.2/homebrew.mxcl.nginx.plist ~/Library/LaunchAgents/
    launchctl load -w ~/Library/LaunchAgents/homebrew.mxcl.nginx.plist

Though note that if running as your user, the launch agent will fail if you
try to use a port below 1024 (such as http's default of 80.)


memcached
----------


You can enable memcached to automatically load on login with:

    mkdir -p ~/Library/LaunchAgents
    cp /usr/local/Cellar/memcached/1.4.14/homebrew.mxcl.memcached.plist ~/Library/LaunchAgents/
    launchctl load -w ~/Library/LaunchAgents/homebrew.mxcl.memcached.plist

If this is an upgrade and you already have the homebrew.mxcl.memcached.plist loaded:

    launchctl unload -w ~/Library/LaunchAgents/homebrew.mxcl.memcached.plist
    cp /usr/local/Cellar/memcached/1.4.14/homebrew.mxcl.memcached.plist ~/Library/LaunchAgents/
    launchctl load -w ~/Library/LaunchAgents/homebrew.mxcl.memcached.plist

Or start it manually:

    /usr/local/bin/memcached

Add "-d" to start it as a daemon.
