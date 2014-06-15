归并排序（Merge Sort）是一个基于比较的复杂度为O(n log n)的排序算法。大多数实现都是[稳定的](http://en.wikipedia.org/wiki/Sorting_algorithm#Stability)。它是一个[分治法算法](http://en.wikipedia.org/wiki/Divide_and_conquer_algorithm)。是1945年由[约翰·冯·诺伊曼](http://en.wikipedia.org/wiki/John_von_Neumann)发明的。
归并排序（Merge Sort）的步骤是这样的：

1. 如果列表的长度为0或1，它已经是排序好的了。否则：
2. 把这个待排序的列表分成两个子列表，各含一半元素。
3. 对每个子列表分别用`归并排序`进行递归排序。
4. 合并两个已排序好的子列表，生成一个排序好的列表。

归并排序融合了两个主要思想

1. 列表越小需要的步骤越少。
2. 对<span class="cb">两个已经排序好的列表</span>排序比对<span class="cb">两个未排序好的列表</span>排序需要较少的步骤（因为对已经排序好的列表，每个我们都只需遍历一次）。

根据上面的思想，归并排序的主体用C语言表示是这样的：

    :::c
    void merge_sort(int a[], int left, int right)
    {
        if (left >= right)
            return;
        int mid = (left + right) / 2;
        merge_sort(a, left, mid);
        merge_sort(a, mid + 1, right);
        merge(a, left, mid, right);
    }

归并排序有两个细节：

1. 对子列表进行排序
2. 对两个已经排序好的列表进行合并

![Merge sort 1](/media/images/article/300px-Merge_sort_algorithm_diagram.svg.png)

对于 `1.` 来说，上面函数中的 `if (left >= right) return;` 语句已经完成了，也就是说当列表元素个数为1或0时，列表自然是排序好的。所以焦点到了 `2.` 合并 `merge()` 这个动作

![Merge sort 1](/media/images/article/Merge-sort-example-300px.gif)

a) ** `merge()` 实现之简单明了版本**

实现 `merge()` 直接明了的方法是：先将要合并的两个列表内容复制到一个辅助列表里，然后用两个指针`i` 和 `j`寻找最小的元素依次复制回原列表，如下图：

![merge](/media/images/article/merge1.gif)

当其中一个指针到达一半的终点时，可以将另一半的剩余元素，直接复制回原列表对应位置即可。实事上，当剩余的是右面一半时，不用执行此操作，里面的元素已经各就各位了。C语言实现如下（为了这个实现，我们需要在上面代码里给函数 `merge_sort()` 和 `merge()` 增加一个 `b[]` 参数）：

    :::c
    void merge(int a[], int b[], int left, int mid, int right)
    {
        int i, j, k;
        for (i=left; i<=right; ++i)
            b[i] = a[i];

        i = k = left;
        j = mid + 1;
        while (i <= mid && j <= right)
            if (b[i] > b[j])
                a[k++] = b[j++];
            else
                a[k++] = b[i++];

        while (i <= mid)
            a[k++] = b[i++];
    }

b) ** `merge()` 高效一些的实现**

实际上，我们并不需要将第二半列表放到 `b[]` 辅助列表里。这样我们会节省一半的额外内存，并且节省一半复制元素到辅助列表的时间。如下图

![merge 2](/media/images/article/merge1b.gif)

这里的关键点是复制时的结束点： 当 `k` 追上 `j` 时。也就是说当且仅当`k`追上`j`时，`b[]`中的元素才全部复制回了`a[]`。

    :::c
    void merge(int a[], int b[], int left, int mid, int right)
    {
        int i, j, k;
        k = 0;
        for (j=left; j<=mid; ++j)
            b[k++] = a[j++];

        i = 0; k = left;
        while (k < j && j <= right)
            if (b[i] <= a[j])
                a[k++] = b[i++];
            else
                a[k++] = a[j++];

        while (k < j)
            a[k++] = b[i++];
    }


** 复杂度分析 **

当一个算法含有函数递归调用时，其运行时间常常以一个递推关系式。对于归并排序算法，一种情况是最简单的情况，即当列表元素只有一个时不用做任何操作，只需要常数时间 `Θ(1)`； 除此种情况外，我们将它的运行时间分解开来：

**分 (Divide):** 在 这一步，我们只需要计算拆分的中点。所以这步的时间为 `Θ(1)`。

**治 (Conquer):** 我们递归地解决两个子问题，运行时间为 `2T(n/2)`。

**并 (Combine):** 也就是 `merge()` 函数的运行时间，可以很容易看出，时间为 `Θ(n)`。

得到以下关系式

![recurrence equation1](/media/images/article/recurrence_equation1.png)

也可以写成这样 (*c* 为常数时间，即处理元素数量为1时的时间)：

![recurrence equation2](/media/images/article/recurrence_equation2.png)

可以将上面的关系式表示成如下图例：

![recurrence tree1](/media/images/article/recurrence_tree1.png)  
![recurrence tree2](/media/images/article/recurrence_tree2.png)

从图(a) 到 图(d)是递归树的依次展开过程。图(d)是已经完全展开的树，共有 `lgn + 1`层，共花费时间 `cn lgn + cn`，即 `Θ(nlgn)`。

参考及图片来源:   
[Wikipedia](http://en.wikipedia.org/wiki/Merge_sort)  
[inf.fh-flensburg.de](http://www.inf.fh-flensburg.de/lang/algorithmen/sortieren/merge/mergen.htm)  
[Introduction to Algorithms](http://www.amazon.com/Introduction-Algorithms-Thomas-H-Cormen/dp/0262033844)
