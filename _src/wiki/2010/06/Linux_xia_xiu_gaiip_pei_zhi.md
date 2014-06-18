sudo ifconfig eth0 192.168.2.11 netmask 255.255.255.0 down
sudo ifconfig eth0 192.168.2.11 netmask 255.255.255.0

sudo route add default gw 192.168.2.1
sudo ifconfig eth0 192.168.2.11 netmask 255.255.255.0 up
这样应该OK。你试试。