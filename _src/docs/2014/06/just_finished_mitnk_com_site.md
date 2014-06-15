Hello <a href="http://twitter.com/mitnk">@mitnk</a>,

We have **great** job to do!

这是一个测试中文

    :::bash
    grep -i 'good' | wc -l


python 测试

    :::python
    if __name__ == '__main__':
        import sys
        if len(sys.argv) < 2:
            print("Usage: mc.py create <title name>")
            exit(1)
        if sys.argv[1].lower() == 'create':
            title = ' '.join(sys.argv[2:])
            create(title)
        elif sys.argv[1].lower() == 'compile':
            title = ' '.join(sys.argv[2:])
            compile(title)
        else:
            raise NotImplementedError()

这是一个C代码测试

    :::c
    include <stdio.h>

    int main()
    {
        printf("Hello world!");
        return 0;
    }

BR,
Anna
