先在 [namecheap.com](http://namecheap.com) 购买ssl证书（这里比较便宜）

生成CSR
-------------

    :::bash
    openssl req -nodes -newkey rsa:2048 -keyout myserver.key -out server.csr

![ssl info](http://ww4.sinaimg.cn/large/a74ecc4cjw1dwlgiw7ozzj.jpg)

信息参考上面图片填写  
如果要一个证书同时支持多个子域名的话  
 `Common Name` 要用通配符 `*.example.com`

参考[这个教程](https://support.comodo.com/index.php?_m=knowledgebase&_a=viewarticle&kbarticleid=3&nav=0,33)

激活SSL证书
-------------------

在 namecheap.com 用上面的CSR激活

1. 提交CSR请求  
2. 等待认可Email  
3. 提交认证号码激活  
4. 会收到一个含有 crt 附件的邮件  


给Nginx配置SSL
--------------------

解压收到的附件，并合并三个文件：

    :::bash
    cat example_com.crt PositiveSSLCA2.crt AddTrustExternalCARoot.crt > example.com.crt

然后在Nignx 里设「[参考这里](http://nginx.org/en/docs/http/configuring_https_servers.html)」：

    :::c
    server {
        listen 80;
        listen 443 ssl;
        server_name xxx.example.com;
        ssl_certificate /path/to/example.com.crt;
        ssl_certificate_key /path/to/myserver.key;

        ...
    }

这样你的站点就同时支持 HTTP 和 HTTPS 了。

Done.

也可以参考[这个教程](http://blog.wensheng.com/2012/03/using-namecheap-ssl-with-nginx.html)
