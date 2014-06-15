用惯了 svn info 命令之后
会期待 git 也有这样的功能
可惜没有。

不过已经<a href="http://inquirylabs.com/blog2009/2008/06/12/git-info-kinda-like-svn-info/">有人写了个git-info 脚本</a>实现了类似的功能：

    :::bash
    #!/bin/bash

    # author: Duane Johnson
    # email: duane.johnson@gmail.com
    # date: 2008 Jun 12
    # license: MIT
    # 
    # Based on discussion at http://kerneltrap.org/mailarchive/git/2007/11/12/406496

    pushd . >/dev/null

    # Find base of git directory
    while [ ! -d .git ] && [ ! `pwd` = "/" ]; do cd ..; done

    # Show various information about this git directory
    if [ -d .git ]; then
      echo "== Remote URL: `git remote -v`"

      echo "== Remote Branches: "
      git branch -r
      echo

      echo "== Local Branches:"
      git branch
      echo

      echo "== Configuration (.git/config)"
      cat .git/config
      echo

      echo "== Most Recent Commit"
      git log --max-count=1
      echo

      echo "Type 'git log' for more commits, or 'git show' for full commit details."
    else
      echo "Not a git repository."
    fi

    popd >/dev/null


输出大概是这样：

    == Remote URL: origin git@github.com:canadaduane/my-project.git
    == Remote Branches:
      origin/work
      trunk
      trunk@1309
      trunk@2570
      trunk@8

    == Local Branches:
      master
    * work

    == Configuration (.git/config)
    [core]
      repositoryformatversion = 0
      filemode = true
      bare = false
      logallrefupdates = true
    [svn-remote "svn"]
      url = svn+ssh://svn.my-project.com/srv/svn
      fetch = my-project/trunk:refs/remotes/trunk
    [remote "origin"]
      url = git@github.com:canadaduane/my-project.git
      fetch = refs/heads/*:refs/remotes/origin/*
    [github]
      user = canadaduane
      repo = my-project

    == Most Recent Commit
    commit b47dce8b4102faf1cedc8aa3554cb58d76e0cbc1
    Author: Duane Johnson <duane.johnson@gmail.com>
    Date:   Wed Jun 11 17:00:33 2008 -0600

        Added changes to database schema that will allow decentralization from content pointers table

    type 'git log' for more, or 'git show' for full commit details.

所以你也可以用 `git info` 命令了。