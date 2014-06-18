1) 安装django, fastcgi, nginx

    $ sudo apt-get install python-flup nginx subversion
    $ cd projects
    $ svn co http://code.djangoproject.com/svn/django/trunk/ django-trunk
    $ sudo ln -s /home/foo/projects/django-trunk/django /usr/lib/python2.6/dist-packages/django

2) 根据自己的需求修改nginx配置文件

    $ sudo vim /etc/nginx/nginx.conf

例如这样：

    user www-data;
    worker_processes  1;

    error_log  /var/log/nginx/error.log;
    pid        /var/run/nginx.pid;

    events {
        worker_connections  1024;
        # multi_accept on;
    }

    http {
        include       /etc/nginx/mime.types;

        access_log	/var/log/nginx/access.log;

        sendfile        on;
        #tcp_nopush     on;

        #keepalive_timeout  0;
        keepalive_timeout  65;
        tcp_nodelay        on;

        gzip  on;
        gzip_disable "MSIE [1-6]\.(?!.*SV1)";
        gzip_comp_level  6;
        gzip_types text/plain text/css application/json application/x-javascript text/xml application/xml application/xml+rss text/javascript;

        include /etc/nginx/conf.d/*.conf;
        include /etc/nginx/sites-enabled/*;
    }

3) 配置站点文件

    $ sudo vim /etc/nginx/sites-available/foo.com

内容如：

    server {
        listen 80;
        server_name demo.foo.com;
        location / { alias /home/foo/demo/; }
    } 

    server {
        listen 80;
        server_name www.foo.com foo.com;

        if ($host != 'foo.com') {
            rewrite ^/(.*)$ http://foo.com/$1 permanent;
        }
        
        access_log /home/foo/projects/foocom/log/access.log;
        error_log /home/foo/projects/foocom/log/error.log;

        location / {
            fastcgi_pass 127.0.0.1:7718;
            fastcgi_param PATH_INFO $fastcgi_script_name;
            fastcgi_param REQUEST_METHOD $request_method;
            fastcgi_param QUERY_STRING $query_string;
            fastcgi_param CONTENT_TYPE $content_type;
            fastcgi_param CONTENT_LENGTH $content_length;
            fastcgi_pass_header Authorization;
            fastcgi_intercept_errors off;
            fastcgi_param  REMOTE_ADDR        $remote_addr;
            fastcgi_param  REMOTE_PORT        $remote_port;
            fastcgi_param  SERVER_ADDR        $server_addr;
            fastcgi_param  SERVER_PORT        $server_port;
            fastcgi_param  SERVER_NAME        $server_name;
        }

        location /robots.txt {
            alias /home/foo/projects/foocom/media/robots.txt;
        }

        location /twitcn_media/ {
            alias /home/foo/projects/foocom/media/twitcn/;
        }

        location /site_media/ {
            expires 7d;
            alias /home/foo/projects/foocom/media/;
        }

        location /media/ {
            alias /home/foo/projects/django-trunk/django/contrib/admin/media/;
        }
    }

然后建立link：

    $ sudo ln -s /etc/nginx/sites-available/foo.com /etc/nginx/sites-enabled/foo.com

4) 启动djangosite, nginx

    sudo /etc/init.d/nginx restart
    python /home/foo/projects/foocom/manage.py runfcgi host=127.0.0.1 port=7718 pidfile=/home/foo/projects/foocom/foocom.pid maxspare=2

See also: <a href="/39/">Ubuntu 10.04 VPS 环境搭建</a>