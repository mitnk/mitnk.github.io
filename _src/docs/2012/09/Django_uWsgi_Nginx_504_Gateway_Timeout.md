A couple of days ago I encountered the  
"Django + uWsgi + Nginx = 504 Gateway Time-out" issue  

And, solution first:

    server {
        listen 80;
        server_name example.com;

        location / {
            uwsgi_pass 127.0.0.1:38717;
        }

        location /upload/ {
            uwsgi_pass 127.0.0.1:38717;
            uwsgi_read_timeout 1800;
        }
    }

The `uwsgi_read_timeout` line is what we need.

现在吐槽。。

I dig lot though the web within several hours  
Read every docs of `Nginx` and `uwsgi`  
Even the second page of Google results!!!  
I read carefully every related articles  
None of it could solve my problem  

Finally, an answer on stackoverflow mentioned a param `fastcgi_read_timeout`  
You know, I just got a hit  
I respell it as `uwsgi_read_timeout` and solved my problem!  
The problem is, neither `Nginx` nor `uwsgi` docs mentioned it!!!