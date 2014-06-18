这两天想玩三国杀，web版总加载不出来。 就去安装Adoba Air版的[桌面版三国杀](http://www.sanguosha.com/web2/downloads.asp)

点击那个“在线安装”按钮后，Air倒是安装好了，不过安装三国杀时总是下载不下来。而这个页面提供一个air包，就下载下来了

    $ open SanGuoSha.air

不过这个命令不能执行或安装。

好吧，继续用页面上安装，试了N次都安装不好，有次都下载了80%左右后又没反应了！！！

然后想，这个air包在Windows上应该能双击打开，但在Mac上应该也能用上才对

在页面上再点“在线安装”按钮一次，然后在Shell运行：

    $ pa ax | grep -i "air"


还真找到air安装的进程了，上面用的是sanguosha.com的地址

我把它改成本地后是这样：

    $ ~/Library/Preferences/Macromedia/Flash\ Player/www.macromedia.com/bin/airinstaller2x0/airinstaller2x0 -playerVersion=10,3,183,5 -sandboxType=remote -securityDomain=airdownload.adobe.com -https=false -fromUserEvent=true -- -x1 file:///Users/mitnk/Downloads/SanGuoSha.air -- launchFromBrowser


不过Flash不让访问http以外的资源。没问题，咱们用http协议应该就成，执行python 的 SimpleHTTPServer

    $ cd ~/Downloads
    $ python -m SimpleHTTPServer 8001

再执行下面命令(注意我们改掉了地址参数)：

    $ ~/Library/Preferences/Macromedia/Flash\ Player/www.macromedia.com/bin/airinstaller2x0/airinstaller2x0 -playerVersion=10,3,183,5 -sandboxType=remote -securityDomain=airdownload.adobe.com -https=false -fromUserEvent=true -- -x1 http://127.0.0.1:8001/SanGuoSha.air -- launchFromBrowser


成功啦！！耶！