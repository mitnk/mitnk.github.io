为了更好地学习英文，我用github来管理我的生词。

    $ tree en-words/
    en-words/
    └── 2011
        ├── april
        │   └── ultimate_pessimism.txt
        ├── october
        │   └── knowledge_and_decisions.txt
        └── september
            ├── justice12.txt
            ├── learned_optimism.txt
            ├── learned_optimism_dict.txt
            ├── longman.txt
            └── programming_erlang.txt

每遇到一个新词，我会查一下以前是不是遇到过。一般我会用grep命令查找，而且它工作的很好。

今天我想基于grep写个脚本程序放到local目录，这样就不用每次查看都要输入一长串命令了。我想给它起名为lookup，在我输入look后按了两次Tab键之后，发现系统有一个look命令。我就man了一下，发现这个命令太有用了。

它主要是在一个文本文件里输出包含某前缀的单词，最有用的时，当省略文件名参数时，它会默认查找 /usr/share/dict/words 这个字典文件。

比如你想不起一个单词的拼写，比如possiblity，但你可以想起前几个字母。这时你可以用look命令来查找

    $ look possi
    possibilism
    possibilist
    possibilitate
    possibility
    possible
    possibleness
    possibly

非常贴心，是不是？

在我决定用look写我的lookup命令后，我的lookup程序就成了这个样子：

    $ cat /usr/local/bin/lookup
    find ~/projects/en-words -name "*.txt" | xargs look $@

比如我想查以前是否记过democracy这个单词，就可以这样做：

    $ lookup democ

