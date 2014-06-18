Setting Up:

    $ sudo defaults write com.apple.loginwindow LoginHook "/Users/$(logname)/Bin/loginhook.sh"

<span class="cg">注：一定要加sudo，否则不管用。</span>

    $ sudo defaults read com.apple.loginwindow LoginHook
    /Users/mitnk/Bin/loginhook.sh

    $ cat ~/Bin/loginhook.sh
    #!/bin/sh
    logger -i "Login Hook Test at `date`"

    $ open -a Console /private/var/log/system.log

也可以设置Logout Hook:

    $ sudo defaults write com.apple.loginwindow LogoutHook "/Users/$(logname)/Bin/logouthook.sh"

参考：<a href="http://hi.baidu.com/tianyu263/">雷哥</a> & <a href="http://support.apple.com/kb/Ht2420">Apple</a>
