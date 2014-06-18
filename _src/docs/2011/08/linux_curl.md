curl is a tool to transfer data from or to a server, using one of the supported protocols (DICT, FILE, FTP, FTPS, GOPHER, HTTP, HTTPS, IMAP, IMAPS, LDAP, LDAPS, POP3, POP3S, RTMP, RTSP, SCP, SFTP, SMTP, SMTPS, TELNET AND TFTP). The command is designed to work without user interaction.

<span class="cr">Note</span>: When reading these examples, you'd better to open a shell to have a try yourself.

    curl ifconfig.me
    curl mitnk.com

-i (HTTP) Include the HTTP-header in the output.

    curl -i ifconfig.me

-I (HTTP/FTP/FILE) Fetch the HTTP-header only!

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


实例

Send HTTP DELETE

    curl -X DELETE http://127.0.0.1:8000/api/entry/4/


从纵横网上取《永生》第一章的网页
http://wap.zongheng.com/chapter?bookid=48552&cid=1181961


    curl -L -b "WAPPageSize=0" -d "bookid=48552&cid=1181961" -A "Mozilla/5.0 Firefox/6.0" http://wap.zongheng.com/chapter


------
Related Python library: <a href="http://docs.python-requests.org/en/latest/index.html">Requests</a>
