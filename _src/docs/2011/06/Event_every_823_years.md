在推上看到 @localhost_8080 发的[一条推](http://twitter.com/#!/localhost_8080/status/84842529660473344)：

<quote>
@localhost_8080:
 刚看到一条状态：“今年7月份有5个周五，5个周六和5个周日，这种现象每823年才发生一次，叫做钱袋子。” 男朋友评论了这条状态：“扯，2013年3月就还是这样。” 噗哈哈…这就是考据癖的男朋友么～
</quote>

看后觉得很有喜感，她男友同学很用心呀。然后就想到写个程序搜索一下就会知道哪个月份符合这个现象了。

先想如何实现：  
因为4周是28天，所以只有31天的月份才可能出现这个现象，并且当且仅需1号这天是周五。
想到这里后，写程序就很简单了。

Python程序如下：

    :::python
    import datetime

    FRIDAY = 4
    MONTHS_TO_CHECK = (1, 3, 5, 7, 8, 10, 12)

    def check_1st_friday(day):
        if day.weekday() == FRIDAY:
            return True
        return False

            
    if __name__ == "__main__":
        year_from = 2000
        year_to = 2020

        for year in range(year_from, year_to + 1):
            for month in MONTHS_TO_CHECK:
                day = datetime.date(year, month, 1)
                if check_1st_friday(day):
                    print day


结果如下（见<a href="http://codepad.org/V2zSXyTP">这里</a>）：

    2000-12-01
    2002-03-01
    2003-08-01
    2004-10-01
    2005-07-01
    2006-12-01
    2008-08-01
    2009-05-01
    2010-01-01
    2010-10-01
    2011-07-01
    2013-03-01
    2014-08-01
    2015-05-01
    2016-01-01
    2016-07-01
    2017-12-01
    2019-03-01
    2020-05-01

几乎每年都会出现一次嘛！
