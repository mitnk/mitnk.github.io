Linux curl 用法
==============

curl 是用HTTP、FTP等协议取得一个服务器上的内容。

不加任何参数是将网页源码取下来：

    curl ifconfig.me
    curl mitnk.com

可以用 -i 来同时取得 HTTP-header：

    curl -i ifconfig.me

而用 -I 只取 HEADER 本身：

    curl -I mitnk.com
    curl -I www.google.com/ncr


-o Write output to a file instead of stdout.
-O Write output to a local file named like the remote file we get.

    curl mitnk.com
    curl mitnk.com -o index.html
    curl http://mitnk.com/site_media/images/djangosite.gif
    curl -O http://mitnk.com/site_media/images/djangosite.gif


-L (HTTP/HTTPS) If the server reports that the requested page has moved to a different location (indicated with a Location: header and a 3XX response kode), this option will make curl redo the request on the new place.

    curl www.mitnk.com
    curl -L www.mitnk.com

    curl -LI google.com/ncr


-A (HTTP) Specify the User-Agent string to send to the HTTP server.

    curl mitnk.com/webapps/user_agent/
    curl -A "My little rebot" mitnk.com/webapps/user_agent/


-v Make the fetching more verbose. Mostly useful for debugging.
-x Use the specified HTTP proxy.
--socks5 Use socket 5 proxy

    curl -v www.mitnk.com
    curl -x xxx.xxx.xxx.xxx:3128 www.python.org/download/
    curl -IL --socks5 127.0.0.1:7070 http://t.co/w8pAFpP


-b (HTTP) Pass the data to the HTTP server as a cookie.
-e (HTTP) Sends the "Referer Page" information to the HTTP server.

    curl -b "name=joe;passwd=123456" mitnk.com
    curl -e mitnk.com/ -LI mitnk.com/1

--max-time 整个过程限时
--connect-timeout 连接服务器的时间限制

    curl --connect-timeout 10 --max-time 30 www.youtube.com

以上命令为获取youtube的内容，但如果10秒内没有连接上服务器，curl退出。
如果整个获取时间超过30秒的话，curl也退出。


--header 请求时定制HEADER内容

    curl --header 'good: morning' --header 'bad: afternoon' www.google.com


POST Requests:

With fields:

    curl --data "param1=value1&param2=value2" http://example.com/resource.cgi

Multipart:

    curl --form "fileupload=@filename.txt" http://example.com/resource.cgi

Without data:

    curl --data '' http://example.com/resource.cgi
    curl -X POST http://example.com/resource.cgi
    curl --request POST http://example.com/resource.cgi

These post request examples are from [Superuser.com](http://superuser.com/a/149335/100560)

实例

Send HTTP DELETE

    curl -X DELETE http://127.0.0.1:8000/api/entry/4/


从纵横网上取《永生》第一章的网页
http://wap.zongheng.com/chapter?bookid=48552&cid=1181961


    curl -L -b "WAPPageSize=0" -d "bookid=48552&cid=1181961" -A "Mozilla/5.0 Firefox/6.0" http://wap.zongheng.com/chapter


------
Related Python library: <a href="http://docs.python-requests.org/en/latest/index.html">Requests</a>
