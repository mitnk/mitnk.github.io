虽然插入排序在处理数据很大时效率不是很好，但它仍然有些优点：

- 非常容易实现，代码量非常小
- 当数据量很小时，效率很高
- 当需排序的数据多数已经是排好的时，效率很好
- 实践上，比其它N^2排序算法（如选择排序、冒泡排序）效率要好
- 排序是[稳定的](http://en.wikipedia.org/wiki/Stable_sort#Stability)
- 所需额外内存空间是固定且很小([In-place algorithm](http://en.wikipedia.org/wiki/In-place_algorithm))
- [Online algorithm](http://en.wikipedia.org/wiki/Online_algorithm)

![Insertion Sort](/media/images/article/Insertion-sort-example-300px.gif)

这是个非常简单的算法啦，下面是思路

- 从第2个元素开始从左向右遍历
- 用一个变量记住当前元素（它可能会被前面小于它的元素覆盖而不可得）
- 从右向左进行内层遍历，如果元素比当前元素大就右移一位
- 将当前元素插入到最后被移动的元素位置，结束内层遍历

用C语言表达如下：

    :::c
    void insertion_sort(int a[], const int size)
    {
        int i, j, key;
        for (j = 1; j < size; ++j)
        {
            key = a[j];
            i = j - 1;
            while (i >= 0 && a[i] > key)
            {
                a[i + 1] = a[i];
                i -= 1;
            }
            a[i + 1] = key;
        }
    }


参考: [wikipedia: Insertion Sort](http://en.wikipedia.org/wiki/Insertion_sort)
