首先安装g++，可以用这个命令安装

    sudo apt-get install build-essential

在build-essential包里含有 dpkg-dev fakeroot g++ g++-4.4 libalgorithm-diff-perl libalgorithm-merge-perl libdpkg-perl libstdc++6-4.4-dev patch 这几个程序

安装完成后，编译并运行C++程序
tmp.cpp


    :::c
    #include <iostream>
    using namespace std;
    int main()
    {
        cout << "Hello Ubuntu!" << endl;
        return 0;
    }


编译：

    g++ tmp.cpp

成功后，会生成 a.out 程序
执行：

    ./a.out
