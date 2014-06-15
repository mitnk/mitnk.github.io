昨天在我闲置的的EPC小本上安装了Arch Linux  
对这个Linux发行版本有了一些认知  
值得一提的是  
Arch Linux的Wiki系统内容很全面，能学到很多东西  
本文是Arch Linux一个Wiki页[1]的简单总结  

基于源码的发行版
------------------------

**Arch Linux**

独立开发，仅支持i686/x84-64架构。开发焦点为简洁，最小化，代码优美。Arch安装后仅有最基本的系统，由用户决定以后的配置和软件环境。基本Rolling Release模式，软件包版本跟进快。


**Gentoo Linux**

软件包都是对源代码的编译安装。允许用户对系统进行深层定制。基于Rolling Release系统，软件包的版本跟进很快。官方支持x86, PPC, SPARC, Alpha, AMD64, ARM, MIPS, HP/PA, S/390等框架。和Arch Linux一样面向有经验的用户和开发者。


**Sorcerer / Lunar-Linux / Source Mage**

SLS 是三个关系很近的基本源码的发行版。SLS提供了软件包依赖检查、跟踪、删除、升级的工具集。不提供二进制软件包，但提供了让软件包方便回滚到早期安装版本的机制。


极简派
---------

**LFS**

LFS (Linux From Scratch) 非常简单，简单到只提供了一本指南书。它指导用户如何取得源代码来手动编译（通过make）一个最小的Linux系统。它提供了一个相当棒的具有教育意义的“如何安装和定制一个Linux基本操作系统”。


**CRUX**

Judd Vinet在创建Arch之前欣赏并使用CRUX系统。两者分享很多理念，如KISS。都是只提供一个基本的Linux系统，由用户决定下一步安装什么。


**Slackware**

和Arch一样焦点是优雅与精简。提供最Unix风格的Linux发行版。尽可能不修改上游软件包，倾向于只提供稳定版本的软件包。提供很少的shell脚本、配置及管理。


通用型Linux
----------------

**Debian**

Debian是一个比较大的项目和社区，拥有超过20,000个二进制软件包。倾向于只用免费软件包。注重稳定性，拥有严格测试。拥有非常棒的软件包管理工具apt-get。


**Fedora**

开发团队为Red Hat团队，被认为是测试版的RHEL。基于RPM模式的软件包，用YUM软件包管理工具。Fedora拒绝将MP3软件包等非免费软件进入官方仓库中。面向的用户为有经验的用户或开发者。Fedora的wiki系统是真正意义上的wiki。


**Frugalware**

早期版本基于Slackware，现在为独立开发。使用Arch的pacman软件包管理工具。


菜鸟友好型Linux
----------------------

**Ubuntu**

基于Debain，由Canonical公司赞助。提供大量的自动化配置工具，方便用户安装使用。每半年发布一个版本。


**Mandriva**

Mandriva（以前叫 Mandrake）创建于1998，目标是让GNU/Linux对所有人都变得好用。基于RPM软件包，提供urpmi软件包管理工具


**openSUSE**

基于RPM，提供很厉害的YaST2 GUI驱动配置工具及软件包安装，方便用户使用。面对用户为无经验的、希望有个友好界面的系统的人。


**PCLinuxOS**

基于Andriva，目标是让用户使用起来感觉简单。系统非常GUI化，对shell的依赖最小化。是低配置要求为256M内存。


BSD家族
------------

**FreeBSD**

来源于AT&T Unix。由于法律原因FreeBSD不能被叫为UNIX，但它是UNIX兼容的。FreeBSD的核心已经成为其它操作系统的一部分，如Mac OS X。


**NetBSD**

来源于Berkeley Software Distribution（BSD）。NetBSD的焦点是高质量的系统设计、稳定性及性能。


**OpenBSD**

由Theo de Raadt于1995年fork自NetBSD。很有兼容性的子系统，如OpenSSH就出自OpenBSD。 注重开源代码及高质量文档。焦点为系统安全与代码健壮性。

[1] [Arch Compared to Other Distributions](https://wiki.archlinux.org/index.php/Arch_Compared_to_Other_Distributions)