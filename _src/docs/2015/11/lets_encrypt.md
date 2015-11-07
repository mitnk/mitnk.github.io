使用 Let's Encrypt SSL 证书
==========================


随着大众越来越关注隐私问题，HTTPS应用得越来越广泛了。国外大站基本全部
HTTPS，但国内情况还差很多。很多大工厂的网站（如阿里的域名管理页面）还
没有启用HTTPS。 而百度的搜索页面已经启用HTTPS已经有段时间了。

现在市面上的单域名的SSL证书已经很便宜了。比如Namecheap旗下的
[ssls.com](https://www.ssls.com/) 提供每年5刀的SSL证书（需要一次性买3年）。
实质意义上的免费SSL证书一直没有出现，直到
[Let's Encrypt](https://letsencrypt.org/) 的出现：
[2014年11月](https://www.eff.org/deeplinks/2014/11/certificate-authority-encrypt-entire-web)
Let's Encrypt 宣布要推出永久免费非营利性的SSL证书。
当时这个新闻[在Hacker News](https://news.ycombinator.com/item?id=8624160)
首页呆了很长时间。

Let's Encrypt是由EFF、Mozilla等公司赞助的一个非营利SSL证书颁发机构。虽然可能
比不上 Wikipedia，但不出意外这个机构在以后会变得非常非常有名。她的出现基本
改变了SSL证书的市场或者SSL证书的历史。

过了整整一年，Let's Encrypt终于进行了封测阶段。前两天收到了
[Let's Encrypt](https://letsencrypt.org/) 的内测邀请。经过折腾终于将两个域名
都归于HTTPS之下。接下来的内容是获取SSL证书的命令记录。


为Nignx手动获取Let's Encrypt的SSL证书
-------------------------------------

LE的一个愿景是让HTTP Server（如Apache、Nginx等）的HTTPS/SSL设置完全自动化。
就是说你只需要执行一个命令，一切都搞定。但实现情况太复杂，也许你的HTTP
Server不能随意重启（因为即时用户太多）；也许设置太过定制，LE命令无法帮你
修改设置。所以这里只说如何只从LE拿到所需的各个证书文件，然后手动应用这些文件。

1. **安装letsencrypt客户端**

用git从Github上拿到最新代码，然后用``生成一个VirtualEnv环境。

    :::bash
    $ git clone https://github.com/letsencrypt/letsencrypt
    $ cd letsencrypt/
    $ ./letsencrypt-auto

最后一步会花一定时间创建环境，并安装各种pip包


2. **预先设置Nignx Host静态文件以备LE验证**

当第一次向LE获取证书时，LE会验证你是否拥有申请证书的域名。

在你的`your-domain.com` 和 `www.your-domain.com` 的Nignx设置中均加入以下设置：

    :::
    location /.well-known/acme-challenge/ {
        default_type text/plain;
        alias /home/mitnk/acme-challenge/;
    }

注意把 `/home/mitnk/acme-challenge/` 中的 mitnk 替换成你的用户名并创建这个文件夹。
然后Reload Nginx应用这个设置

    :::
    $ mkdir -p /home/mitnk/acme-challenge/
    $ sudo nginx -s reload


3. **获取SSL证书**

确保你已经收到内测邀请，并且域名 `your-domain.com` 在白名单之内，
然后打开两个console；在Console1中输入以下命令：

    :::bash
    $ source .local/share/letsencrypt/bin/activate
    (letsencrypt) $ sudo .local/share/letsencrypt/bin/letsencrypt \
        --agree-dev-preview \
        -d your-domain.com \
        -d www.your-domain.com \
        --server https://acme-v01.api.letsencrypt.org/directory \
        -a manual \
        certonly

    注：这里的命令都可以用 `letsencrypt-auto` 来代替，这里这样用的好处是有有问题方便用pdb调试。
    关于 `letsencrypt-auto` 的用法可以看[官方文档](https://letsencrypt.readthedocs.org/en/latest/using.html#installation-and-usage)。

认真阅读输出信息，如是蓝屏问题时回车确认；如果是以下内容（不是原话，大意如此）：

    :::
    Please make sure http://your-domain.com/home/mitnk/acme-challenge/ABCXYZ
    have the following content:

    ABCXYZ.456789

    When you ready, type Enter Key to continue

注意你用了几个 `-d` 这个信息就会出现几次，域名部分和后缀问题是不同的。请确保
你这几个子域名都会前面设置的Nginx所覆盖。对**每一次**这样的信息都要去Console2里
做以下事情：

    :::bash
    $ cd /home/mitnk/acme-challenge/
    $ vim ABCXYZ

然后复制内容 `ABCXYZ.456789` 进 `ABCXYZ` 文件，保存退出vim。然后去掉文件里的 `\n` 字符
（如果有这个字符，LE现在就认为内容不匹配）:

    :::bash
    $ cat ABCXYZ | tr -d '\n' > abc
    $ mv abc ABCXYZ

然后切换加Console1回车。


4. **遇到错误 Error creating new authz ？ **

现在LE还不稳定，有各种问题。我遇到最多的问题就是 `Error creating new authz`。
这个是LE Server的问题，貌似只对某些Name Server有此问题。

我的 .COM 域名没有遇到这个问题，但 .WANG 域名遇到了。然后我将 Name Server从
阿里万网的 hichina.com 换成 NameCheap 的 FreeDNS 后成功拿到 SSL 证书。


5. ** 成功拿到SSL证书，设置Nginx **

成功之后，你的SSL证书默认会在 `/etc/letsencrypt` 下面，
你可以用 `sudo tree /etc/letsencrypt` 查看里面的文件列表。
给Nginx设置HTTPS只用到两个文件，密钥文件（需要保密）和 chain 文件（是公开的）

    :::
    listen 80;
    listen 443 ssl;
    ssl_protocols TLSv1.2 TLSv1.1 TLSv1;
    server_name your-domain.com your-domain.com;

    ssl_certificate     /etc/letsencrypt/live/your-domain.com/fullchain.pem;
    ssl_certificate_key /etc/letsencrypt/live/your-domain.com/privkey.pem;

然后Reload Nginx即可。最后可以在任意文件夹下用下面命令既出 letsencrypt VirtualEnv:

    :::
    $ deactivate

关于LE的HTTPS效果可以点击现在这个页面左上角的 HTTPS （绿色）小锁。从详情里可以看出
LE发布的证书当前只有3个月有效期。在此之前必须 renew 你的SSL 证书。