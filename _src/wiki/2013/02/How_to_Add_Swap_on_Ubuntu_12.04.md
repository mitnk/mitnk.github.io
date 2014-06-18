About Linux Swapping
--------------------

Linux RAM is composed of chunks of memory called pages. To free up pages of RAM, a “linux swap” can occur and a page of memory is copied from the RAM to preconfigured space on the hard disk. Linux swaps allow a system to harness more memory than was originally physically available. 

However, swapping does have disadvantages. Because hard disks have a much slower memory than RAM, virtual private server performance may slow down considerably. Additionally, swap thrashing can begin to take place if the system gets swamped from too many files being swapped in and out.

Check for Swap Space
--------------------

Before we proceed to set up a swap file, we need to check if any swap files have been enabled on the VPS by looking at the summary of swap usage.

    swapon -s

An empty list will confirm that you have no swap files enabled:

    Filename				Type		Size	Used	Priority

Check the File System
---------------------

After we know that we do not have a swap file enabled on the virtual server, we can check how much space we have on the server with the df command. The swap file will take 512MB— since we are only using up about 8% of the /dev/sda, we can proceed.

    df

    Filesystem     1K-blocks    Used Available Use% Mounted on
    /dev/sda        20907056 1437188  18421292   8% /
    udev              121588       4    121584   1% /dev
    tmpfs              49752     208     49544   1% /run
    none                5120       0      5120   0% /run/lock
    none              124372       0    124372   0% /run/shm

Create and Enable the Swap File
-------------------------------

Now it’s time to create the swap file itself using the dd command :

    sudo dd if=/dev/zero of=/swapfile bs=1024 count=512k

“of=/swapfile” designates the file’s name. In this case the name is swapfile. 

Subsequently we are going to prepare the swap file by creating a linux swap area:
sudo mkswap /swapfile

The results display:

    Setting up swapspace version 1, size = 262140 KiB
    no label, UUID=103c4545-5fc5-47f3-a8b3-dfbdb64fd7eb

Finish up by activating the swap file:

    sudo swapon /swapfile

You will then be able to see the new swap file when you view the swap summary.

    swapon -s

    Filename				Type		Size	Used	Priority
    /swapfile                               file		262140	0	-1

This file will last on the virtual private server until the machine reboots. You can ensure that the swap is permanent by adding it to the fstab file.

Open up the file:

    sudo nano /etc/fstab

Paste in the following line:

    /swapfile       none    swap    sw      0       0 


To prevent the file from being world-readable, you should set up the correct permissions on the swap file:

    sudo chown root:root /swapfile 
    sudo chmod 0600 /swapfile

From [Digital Ocean](https://www.digitalocean.com/community/articles/how-to-add-swap-on-ubuntu-12-04)
