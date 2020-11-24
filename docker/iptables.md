### 常见术语：
* DNAT：Destination Network Address Translation，目的网络地址转换，一种改变数据包目的 ip 地址的技术，比如可以使多台服务器共享一个ip地址连入Internet，并且继续服务
* SNAT：Source Network Address Translation，源网络地址转换，是一种改变数据包源ip地址的技术，比如可以使多台计算机分享一个Internet地址
* target：表示对匹配的数据包所做的操作

### 书写规则：
* iptables [-t table] command [match] [target/jump]：
    * -t：表示指定表名，包括：nat、mangle、filter
        * nat：用于网络地址转化，涉及：PREROUTING、OUTPUT、POSTROUTING
        * mangle：用于改变不同的包及包头的内容，涉及PREROUTING、POSTROUTING、OUTPUT、INPUT、FORWARD
        * filter：用于过滤包，涉及FORWARD、INPUT、OUTPUT 
    * command：相关指令
        * -A：在所选择的链末添加规则
            * `iptables -A INPUT`
        * -D：在所选择的链中删除规则，有两种方法删除规则，一是把规则完整的写出来，二是指定规则所在链中的序号
            * `iptables -D INPUT --dport 80 -j DEOP`
            * `iptables -D INPUT 1`
        * -R：在所选择的链中，找到指定规则并替换部分规则
            * `iptables -R INPUT 1 -s 192.168.0.1 -j DROP`
        * -I：在所选择的链中，找到指定规则并插入规则，会插入当前规则之前
            * `iptables -I INPUT 1--dport 80 -j ACCEPT`
        * -L：显示所选链的所有规则，若没有指定显示默认表的所有链的规则
            * -v：详细的verbose
            * -x：精确的exact
            * -n：
        * -F：清空所选链
            * `iptables -F INPUT`
        * -N：根据用户名指定新的链
            * `iptables -N allowed`
        * -X：删除指定的用户自定义链
            * `iptables -X allowed`
        * -E：对自定义链重命名
            * `iptables -E allowed disallowed`
    * match：匹配规则
        * 通用匹配：
            * -p：匹配协议
                * `iptables -A INPUT -p tcp`
            * -s：匹配源ip地址
                * `iptables -A INPUT -s 192.168.0.1`
            * -d：匹配目标ip地址
                * `iptables -A INPUT -d 192.168.0.1`
            * -i：匹配指定的网卡，流量将要进入此卡
                * `iptables -A INPUT -i eth0`
            * -o：匹配指定的网卡，流量从此卡流出
                * `iptables -A INPUT -o eth0`
        * 隐含匹配：
            * --sport：基于TCP的源端口来匹配包
                * `iptables -A INPUT -p tcp --sport 22`
                * `iptables -A INPUT -p tcp --sport :22` 表示从0到22端口
                * `iptables -A INPUT -p tcp --sport 22:` 表示从0到65535所有端口
                * `iptables -A INPUT -p tcp --sport 22:88` 连续的端口表示从22到88端口均可匹配
                * `iptables -A INPUT -p tcp --sport !22,23,25` 表示不匹配22,23,25端口
            * --dport：基于TCP的目的端口来匹配包
                * `iptables -A INPUT -p tcp --dport 22`
        * 显示匹配：
            * --limit：指定最大平均匹配速率，单位包括：/second /minute /hour /day, 可以有效的防止DOS攻击
                * `iptables -A INPUT -m limit --limit 3/hour`
            * --mac-source：基于包的MAC地址匹配包
                * `iptables -A INPUT -m mac --mac-source 00:00:00:00:00:01`
            * --source-port：远端口的多端口匹配
                * `iptables -A INPUT -m multiport --source-port 22,25,80`
            * --destination-port
            * --port
    * target/jump
        * jump:
            * `iptables -N tcp_packets` 新建一个 tcp_packets 的链
            * `iptables -A INPUT -p tcp -j tcp_packets` 当进入INPUT链的时候，匹配到此处时会跳入到 tcp_packets 链
        * target
            * ACCEPT：表示接受
            * DNAT：指定要写入IP头的地址
                * `iptables -t nat -A PREROUTING -p tcp -d 15.15.15.15 --dport 80 -j DNAT --to-destination 192.168.1.1-192.168.1.10`
                    把所有发往 15.15.15.15 的包都转发到一段LAN使用的私有地址中， 即192.168.1.1-192.168.1.10
            * SNAT：做源网络地址转换
                * `iptables -t nat -A POSTROUTING -p tcp -o eth0 -j SNAT --to-source 194.236.50.155-194.236.50.160:1024-32000`
            * DROP：丢弃
            * LOG
            * MARK
            * MASQUERADE：专门设计用于那些动态获取IP地址的连接
                * `iptables -t nat -A POSTROUTING -p tcp -j MASQUERADE --to-ports 1024-31000` 设置外出包能使用的端口
            * MIRROR：



```text
192.168.65.3 物理网关 <- 宿主机 ->  

tcpdump抓包eth0

06:47:18.292498 IP 192.168.65.3.36551 > 192.168.65.1.domain: 27537+ A? www.baidu.com. (31)
06:47:18.292847 IP 192.168.65.3.55098 > 192.168.65.1.domain: 12420+ PTR? 1.65.168.192.in-addr.arpa. (43)
06:47:18.297045 IP 192.168.65.1.domain > 192.168.65.3.55098: 12420 NXDomain 0/0/0 (43)
06:47:18.297313 IP 192.168.65.3.34625 > 192.168.65.1.domain: 453+ PTR? 3.65.168.192.in-addr.arpa. (43)
06:47:18.298080 IP 192.168.65.1.domain > 192.168.65.3.36551: 27537 3/0/0 CNAME www.a.shifen.com., A 14.215.177.38, A 14.215.177.39 (90)
06:47:18.300283 IP 192.168.65.1.domain > 192.168.65.3.34625: 453 NXDomain 0/0/0 (43)
06:47:18.308955 IP 192.168.65.3 > 14.215.177.38: ICMP echo request, id 11, seq 0, length 64
06:47:18.309106 IP 192.168.65.3.40934 > 192.168.65.1.domain: 52815+ PTR? 38.177.215.14.in-addr.arpa. (44)
06:47:18.313090 IP 192.168.65.1.domain > 192.168.65.3.40934: 52815 NXDomain 0/0/0 (44)
06:47:18.327453 IP 14.215.177.38 > 192.168.65.3: ICMP echo reply, id 11, seq 0, length 64
06:47:23.564134 ARP, Request who-has 192.168.65.1 tell 192.168.65.3, length 28
06:47:23.564737 ARP, Reply 192.168.65.1 is-at f6:16:36:bc:f9:c6 (oui Unknown), length 28


tcpdump抓包虚拟网卡

06:50:03.780337 IP 172.19.0.2.46491 > 192.168.65.1.domain: 28994+ A? www.baidu.com. (31)
06:50:03.782503 IP 192.168.65.1.domain > 172.19.0.2.46491: 28994 3/0/0 CNAME www.a.shifen.com., A 14.215.177.38, A 14.215.177.39 (90)
06:50:03.783246 IP 172.19.0.2 > 14.215.177.38: ICMP echo request, id 13, seq 0, length 64
06:50:03.801048 IP 14.215.177.38 > 172.19.0.2: ICMP echo reply, id 13, seq 0, length 64
06:50:08.940297 ARP, Request who-has 172.19.0.2 tell 172.19.0.1, length 28
06:50:08.940521 ARP, Request who-has 172.19.0.1 tell 172.19.0.2, length 28
06:50:08.940529 ARP, Reply 172.19.0.1 is-at 02:42:a6:0f:bc:f3 (oui Unknown), length 28
06:50:08.940536 ARP, Reply 172.19.0.2 is-at 02:42:ac:13:00:02 (oui Unknown), length 28
```




