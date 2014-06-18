近段时间我花了一些时间，按LFS-7.2的指南成功地打造出了自己的LFS系统。

LFS (Linux From Scratch) [1] 是一个教你如何全部从源代码一步步打造你自己的Linux系统的开源项目。由Gerard Beekmans创建于1999年。参过LFS你可以学到： 1) Linux内部是如何工作的 2) 只安装自己需要的软件或服务 3) LFS非常灵活 4) 系统更加安全，因为每一个软件都是你从源码编译出来的。

安装其它的大多数Linux发行版只需要一个小时左右，而按这本书创建出一个LFS则要久很多：第一次做的话，大概要花24小时左右（可不包括吃饭睡觉）

首先你得有个**宿主Linux系统**

我的主机是EPC 1015pw，双核（四线程）上网本（这款相对老点的本本应该是上网本中的战斗机），系统用的是Arch Linux + Xfce4。

一个**空分区**

大小10G即可。

准备安装系统所**需要的所有源码包**

这个可以从LFS镜像站点 [2] 打包下载下来，近300M。放到上面的空分区里

然后需要从这些源码**打造一个工具箱**

这个工具箱是将来用来创建LFS系统的工具。这个过程很长，需要编译29个软件包。不同性能的机器的编译时间是不一样的，所以书中各个软件包标有一个相对时间单位 (SBU) ，即在你自己机器上编译Binutils-2.22 的时间。在我的EPC上1SBU等于8分钟。

在工具箱完成后，通过Chroot进入到了**打造真正的LFS系统**

在这个过程中因为需要编译更多的包（59个），而且要执行测试，所以编译过程花的时间会更多，至少需要你宅一整天。

系统完成后需要**配置启动脚本**

这个过程比较乱，有些内容可以先不做，比如我没有去配置网络。但最基本的LFS-Bootscripts包还是需要安装的，Sysvinit用到的/etc/inittab也是需要创建的。

启动脚本搞好后就到了**编译Linux Kernel**了

编译之前需要通过 `make menuconfig` 配置内核的编译选项，比如网卡驱动（用`lspci | grep -i net`来查看自己系统的硬件信息）、文件系统（如用ext4的话，记得选中它，kernel默认没选ext4）。编译过程比较长，大概6个SBU。

最后就到**通过GRUB重启系统**了！

这一步我没有做LFS 7.2书中的相关内容，我直接用的宿主系统Arch Linux中的GRUB来启动这个LFS系统。也就是我的EPC安装了多系统（实际上是三系统，还装有一个Windows XP）。按照Arch的GRUB Wiki页面 [3]，这里很好配置。

好了重启吧！

![mitnk lfs](/images/2013/02/mitnk-lfs.jpg)

[1] <http://www.linuxfromscratch.org/>  
[2] <http://linuxfromscratch.pl/pub/LFS/lfs-packages/>  
[3] <https://wiki.archlinux.org/index.php/Grub#With_GNU.2FLinux> 