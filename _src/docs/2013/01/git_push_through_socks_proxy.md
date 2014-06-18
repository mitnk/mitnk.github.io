终于，github在中国被墙了：网站打不开，git pull/push失败。

对现在中国开发者来说，一个能用的代理是非常必须的了。假定你已经有了一个可用的Socks v5代理了（如果你没有，强烈建议看下[Shadowsocks工程](https://github.com/clowwindy/shadowsocks)系列）。那么让git走这个代理是非常简单的事情。

将 `~/.ssh/config` 里加入以下内容：

    Host github.com
        ProxyCommand nc -x 127.0.0.1:9999 -X 5 %h %p

然后用git pull 和 push时记得用 ssh 协义，如  
`git clone git@github.com:xxx/xxx.git`
