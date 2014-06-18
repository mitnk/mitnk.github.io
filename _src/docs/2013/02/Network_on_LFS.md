To connect to a wireless network on LFS, we should read some content from BLFS.

First, we need install Net-tools, which contains the `ifconfig` program.

Install Wireless Tools for `iwconfig` program.

Install libnl and openssl for wpa_supplicant.

Install wpa_supplicant.

Config wpa_supplicant:

wpa_passphrase SSID SECRET_PASSWORD > /etc/wpa_supplicant.conf

Using the following command to connect:

    wpa_supplicant -B -c/etc/wpa_supplicant.conf -iwlan0 -Dnl80211,wext
    sleep 2 # let it settle
    dhcpcd

If you cannot see the wireless interface with `iwconfig` after rebooting, you may need to
recompile your Kernel with proper wireless device driver. Use `lspci | grep -i net` to check
which wireless device you are using.