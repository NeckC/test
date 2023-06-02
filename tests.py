############0.1##############
#!/usr/bin/env python3

import os

config = []
# 获取参数并添加到config列表中
config.append("net add time zone " + input("请输入时区："))
config.append("net add time ntp server " + input("请输入NTP服务器IP地址：") + " iburst")
config.append("net add time ntp source " + input("请输入NTP源接口："))
config.append("net add snmp-server listening-address " + input("请输入SNMP监听地址：") + " vrf " + input("请输入VRF名称："))
config.append("net add snmp-server listening-address localhost")
config.append("net add snmp-server readonly-community " + input("请输入SNMP只读community：") + " access " + input("请输入允许访问的IP地址：") + "/32")
config.append("net add interface peerlink.4094,swp49-56 ipv6 nd ra-interval 10")
config.append("net del interface peerlink.4094,swp49-56 ipv6 nd suppress-ra")
config.append("net add vrf " + input("请输入VRF名称：") + ",POD1 vrf-table auto")
config.append("net add bridge bridge vids " + input("请输入Bridge VLAN ID："))
config.append("net add bridge bridge vlan-aware")
config.append("net add bridge stp treeprio 4096")
config.append("net add interface eth0 ip address " + input("请输入IP地址：") + "/24")
config.append("net add interface eth0 ip gateway " + input("请输入网关IP地址："))
config.append("net add interface eth0 vrf " + input("请输入VRF名称："))

config.append("net add interface swp1-54")
config.append("net add interface swp49-54 link down")

config.append("net add loopback lo clag vxlan-anycast-ip " + input("请输入VXLAN anycast IP地址："))
config.append("net add loopback lo ip address " + input("请输入IP地址：") + "/32")
config.append("net add loopback lo vxlan local-tunnelip " + input("请输入VXLAN本地隧道IP地址："))

config.append("net add hostname " + input("请输入主机名："))

config.append("net add bri bri ports peerlink")

config.append("net add bond peerlink bond slaves swp47,swp48")
config.append("net add interface peerlink.4094 clag backup-ip " + input("请输入CLAG备份IP地址：") + " vrf " + input("请输入VRF名称："))
config.append("net add interface peerlink.4094 clag peer-ip linklocal")
config.append("net add interface peerlink.4094 clag sys-mac " + input("请输入CLAG系统MAC地址："))


config.append("net commit")

# 获取文件名并输出配置脚本到文件
filename = input("请输入输出文件名：")
filepath = "/"+filename+".txt"
with open(filepath, "w") as f:
    for command in config:
        f.write(command + "\n")

# 在终端输出配置脚本
for command in config:
    print(command)


#运行示例：
#请输入时区：Asia/Shanghai
#请输入NTP服务器IP地址：10.123.209.1
#请输入NTP源接口：eth0
#请输入SNMP监听地址：10.123.200.46
#请输入VRF名称：mgmt
#请输入SNMP只读community：dcz%zjfz2022
#请输入允许访问的IP地址：10.123.209.1
#请输入允许访问的IP地址：10.22.32.250
#请输入VRF名称：mgmt
#请输入Bridge VLAN ID：1101
#请输入IP地址：10.123.200.46
#请输入网关IP地址：10.123.200.254
#请输入VRF名称：mgmt
#请输入VXLAN anycast IP地址：10.122.200.121
#请输入IP地址：10.122.200.46
#请输入VXLAN本地隧道IP地址：10.122.200.46
#请输入主机名：DCZ-LEAF20-2
#请输入CLAG备份IP地址：10.123.200.45
#请输入VRF名称：mgmt
#请输入CLAG系统MAC地址：44:38:39:FF:11:20

