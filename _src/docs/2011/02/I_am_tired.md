这段时间工作超级没有状态，总是想着什么时候下班。

就写了一段代码：

    :::bash
    unit=`uptime | sed -e 's/^.*up //' -e 's/,.*//' | cut -d " " -f2`
    if [ $unit = "min" ]; then
        echo "I don't think so... You've been here less than an Hour !!"
    elif [ $unit = "day" ]; then
        echo "Just Go! You've been here for days!!!!"
    else
        hour=`uptime | awk '{print $3}' | cut -d ":" -f1`
        min=`uptime | awk '{print $3}' | cut -d ":" -f2 | cut -d "," -f1`
        if [ $hour -ge 9 ]; then
            echo "You can go NOW !!!"
        else
            echo "You can leave office in `expr 8 - $hour` hours, `expr 60 - $min` minutes!"
        fi
    fi

测试环境：  
Ubuntu 10.10 / Ubuntu 9.10

用法：  

1) 把上面代码保存为 iamtired 文件  
2) 将这个文件保存到 /usr/local/bin 文件夹下  
3) 将其属性改成 755 （sudo chmod 755 /usr/local/bin/iamtired ）  

在你的机器上执行 iamtired 命令  

    $ iamtire
    I don't think so... You've been here less than an Hour !!
