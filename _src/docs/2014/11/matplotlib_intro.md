画图表工具matplotlib
====================

matplotlib的安装

    $ sudo pip3.4 install matplotlib

当前版本：

    $ pip3.4 freeze | grep mat
    matplotlib==1.4.2

画一个直线吧

    :::python
    import pylab

    pylab.plot([1, 2, 3, 4])
    pylab.show()

<img src="/media/img/2014/11/line.png" alt="line" width="400">

可以保存为png图片

    :::python
    import pylab

    pylab.plot([1, 2, 3, 4])
    pylab.savefig('line.png')


画个 `y = x^2 - 300` 吧

    :::python
    L = range(-100, 101)
    pylab.plot(L, [x**2 - 300 for x in L])
    pylab.show()

<img src="/media/img/2014/11/parabola.png" alt="parabola" width="400">

把它和 `y = x` 画到一个图上面：

    :::python
    fig = pylab.figure()
    X = range(-100, 101)
    Y = [i**2 - 300 for i in X]

    ax = fig.add_subplot(1, 1, 1)

    ax.plot(X, Y)
    ax.plot(X, X)

    ax.spines['left'].set_position('center')
    ax.spines['bottom'].set_position('center')
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')
    ax.xaxis.set_ticks_position('bottom')
    ax.yaxis.set_ticks_position('left')
    pylab.axis([-100, 100, -1000, 1000])
    pylab.show()

<img src="/media/img/2014/11/parabola_and_line.png" alt="parabola_and_line" width="400">

画个统计图

    :::python
    import datetime
    import pylab
    from matplotlib.dates import DayLocator, DateFormatter, drange

    d1 = datetime.date(2014, 10, 1)
    d2 = datetime.date(2014, 11, 1)
    delta = datetime.timedelta(days=1)

    dates = drange(d1, d2, delta)
    Y = [110.92, 71.55, 38.54, 58.79, 29.11, 69.95, 96.76, 111.07, 151.88, 121.92, 143.47, 149.78, 98.65, 93.64, 88.23, 62.77, 64.05, 73.40, 72.12, 12.29, 17.36, 27.26, 29.62, 24.08, 22.95, 30.86, 21.21, 76.04, 82.15, 104.78, 55.37]

    fig, ax = pylab.subplots()
    ax.plot(dates, Y)
    ax.set_xlim( dates[0], dates[-1] )

    ax.xaxis.set_major_locator(DayLocator())
    ax.xaxis.set_major_formatter(DateFormatter('%Y-%m-%d'))
    fig.autofmt_xdate()

    pylab.ylabel('Players Total Online Time (hours)')
    pylab.show()

<img src="/media/img/2014/11/online_time_stats.png" alt="online_time_stats" width="400">

更多内容请阅读[matplotlib官方文档](http://matplotlib.org/contents.html)
