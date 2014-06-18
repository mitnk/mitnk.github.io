Make sure you have `openssl`  
Or install it with `sudo apt-get install openssl`

Download:

    :::bash
    wget http://nginx.org/download/nginx-1.3.5.tar.gz
    wget ftp://ftp.csx.cam.ac.uk/pub/software/programming/pcre/pcre-8.30.tar.gz

Install:

    :::bash
    ./configure --with-http_ssl_module --with-pcre=../pcre-8.30


配置
----

    sudo vim /usr/local/nginx/conf/nginx.conf

Add the following info

    worker_processes  2;

    events {
        worker_connections  1024;
    }

    http {
        include       mime.types;
        include       uwsgi_params;
        default_type  application/octet-stream;

        sendfile        on;
        #tcp_nopush     on;

        keepalive_timeout  65;

        gzip  on;
    }


启动

<blockquote>
-s signal Send signal to a master process: stop, quit, reopen, reload. (version >= 0.7.53)
-v Print version.
</blockquote>

    sudo /usr/local/nginx/sbin/nginx

让nginx自动启动, [出处](http://serverfault.com/questions/69350/launch-nginx-on-startup)

    cd /etc/init.d
    sudo vim ngnix.sh

Input the following code:

    #!/bin/bash
    # this script starts the nginx process attached to passenger
    sudo /usr/local/nginx/sbin/nginx

save and exit.

    sudo chmod +x nginx.sh
    sudo update-rc.d ngnix.sh defaults

Done.