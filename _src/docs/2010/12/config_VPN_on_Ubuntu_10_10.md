在网上购买一个vpn，在iTouch上已经连接 上了  
但在Ubuntu下却很迷惑：  
不明白 服务器地址应该写到 Gateway 里面 还是 NT Domain 里。  
而且都尝试过也连接不上。  

Google了一下，才把问题搞定！  
下面把步骤记录一下：  

左键点击 网络图标 --> VPN Connection --> Configure VPN  
点击ADD  
选择PPTP --> Create...  

<span style="color:red;">GetWay: 输入vpn服务器地址</span>  
然后用户名密码，（其它不用填）  
点击 右下角高级(Advanced...)  

<span style="color:red;">选中 Use Point-to-Point Encryption (MPPE)</span> 和 Allow Stateful Encryption  
确定， 应用。  

这样就配置好了  

连接时，左键点击 网络图标 --> Vpn Connection --> XXX (刚才你配置的vpn的名字）  
连接成功后，风格状态图标上会多一个小锁  
在Vpn Connection 里有一个Disconnect VPN, 点击会断开VPN连接。  
