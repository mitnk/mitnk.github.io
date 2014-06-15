Git Basic
=========

    git init
    .git

    git add .
    git add readme.txt

    git commit -m 'added readme file'

    (git commit -am 'added edited files.')

 ---------

    git log -3
    git log -3 -p
    git log -3 --stat

    git log --pretty=oneline
    git log --pretty=full
    git log --pretty=format:"%h - %an, %ar : %s"
    git log --pretty=format:"%h %s" --graph

    git log --since=1.weeks
    git log --author dc --pretty=oneline

    gitk

 ----------

修改最后一次提交

    touch a.txt
    git add a.txt
    git commit -m 'added a.txt'
    touch b.py
    git add b.py
    git ci --amend -m 'added txt and py together.'

最终只是产生一个提交

    git log

 --------------

取消已经暂存的文件

    touch hello.py
    touch test.py
    git add .
    git st

    git reset HEAD test.py
    git st

取消对文件的修改

    git ci -m 'commit something.'

    vim hello.py
    git checkout hello.py

这条命令有些危险

任何已经提交到 Git 的都可以被恢复。你可能失去的数据，仅限于没有提交过的。

 ---------------

远程仓库的使用

    git clone git://github.com/schacon/ticgit.git
    git remote -v

添加远程仓库

    mkdir hello
    cd hello
    git init
    git touch readme
    git add .
    git ci -m 'first init.'
    git remote add origin https://github.com/mitnk/hello.git
    git push origin master

远程仓库的删除

    git remote -v
    git remote rm origin
    git remote -v
    git remote add origin git@github.com:mitnk/helloapi.git

从远程仓库抓取数据

    git fetch origin master
    git pull origin master
    (git pull == git fetch & git merge)

 ----------------

Git 分支
=======

分支的新建与切换

    git st (Clean is better)
    git branch -v
    git branch dev
    git branch -v
    (Note we still at master branch)

    git checkout dev
    git branch -v
    (Now we are on dev branch)

 --------------

    Case Study

    git checkout -b iss53
    (Fixing bug)

现在你就接到了那个网站问题的紧急电话，需要马上修补

    git add .
    git ci -m 'WIP: work on iss53'
    (Commit current work)

    git checkout master
    (Now we back on master branch)

    vim index.html
    (Fixing bug)

    git ci -am 'fixed bug in index.html'

    (git push or something)

    (Then we back to iss53)
    git checkout iss53

    (Finally, we finished issue 53)
    git commit -am 'fixed issue 53'

将iss53合并到master分支

    git co master
    git merge iss53

    git br -v

我们已经不再需要iss53分支，所以删除它

    git br -d iss53

 --------------------

遇到冲突时的分支合并

    git merge iss53

    ( CONFLICT (content): Merge conflict in index.html)

    git st
    vim index.html
    (Editing conflict contents)

    git commit -am 'merged issue 53 branch'

 -----------

    git br merged
    git br --no-merged

 ------------

利用分支进行开发的工作流程

仅在 master 分支中保留完全稳定的代码，即已经发布或即将发布的代码。与此同时，他们还有一个名为 develop 或 next 的平行分支，专门用于后续的开发，或仅用于稳定性测试 — 当然并不是说一定要绝对稳定，不过一旦进入某种稳定状态，便可以把它合并到 master 里。这样，在确保这些已完成的特性分支（短期分支，比如之前的 iss53 分支）能够通过所有测试，并且不会引入更多错误之后，就可以并到主干分支中，等待下一次的发布。

你可以用这招维护不同层次的稳定性。某些大项目还会有个 proposed（建议）或 pu（proposed updates，建议更新）分支，它包含着那些可能还没有成熟到进入 next 或 master 的内容。这么做的目的是拥有不同层次的稳定性：当这些分支进入到更稳定的水平时，再把它们合并到更高层分支中去。再次说明下，使用多个长期分支的做法并非必需，不过一般来说，对于特大型项目或特复杂的项目，这么做确实更容易管理。

在任何规模的项目中都可以使用特性（Topic）分支。一个特性分支是指一个短期的，用来实现单一特性或与其相关工作的分支。可能你在以前的版本控制系统里从未做过类似这样的事情，因为通常创建与合并分支消耗太大。然而在 Git 中，一天之内建立、使用、合并再删除多个分支是常见的事。(上面的iss53分支就是Topic分支)
