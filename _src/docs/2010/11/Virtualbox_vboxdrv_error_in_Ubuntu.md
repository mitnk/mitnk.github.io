I installed virtualbox-ose from the "Ubuntu Software Center".  

When I start a OS after creating it, I got an error:  
Please install the virtualbox-ose-dkms package and execute 'modprobe vboxdrv'  

After googling, I solved this problem.

    sudo apt-get purge virtualbox-ose*
    sudo apt-get autoremove
    sudo apt-get clean
    sudo apt-get install build-essential
    sudo apt-get install virtualbox-ose

