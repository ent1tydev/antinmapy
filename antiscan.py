#!/usr/bin/python3
import os, sys
print('SHIFT AntiScan v0.1 by https://t.me/freeshift')

class iptables:
    def enable():
        os.system("iptables -A INPUT -i _NDM_INPUT  -p tcp --dport 0 -j DROP")
        os.system("iptables -A INPUT -i _NDM_INPUT  -p udp --dport 0 -j DROP")
        os.system("iptables -A INPUT -i _NDM_INPUT  -p tcp --sport 0 -j DROP")
        os.system("iptables -A INPUT -i _NDM_INPUT  -p udp --sport 0 -j DROP")
        os.system("iptables -A INPUT -p icmp -m icmp --icmp-type 17 -j DROP")
        os.system("iptables -A INPUT -p icmp -m icmp --icmp-type 13 -j DROP")
        os.system("iptables -A INPUT -i _NDM_INPUT -p tcp ! --syn -m conntrack --ctstate NEW -j DROP")
        os.system("iptables -A INPUT -i _NDM_INPUT -p tcp --tcp-flags FIN,SYN,RST,PSH,ACK,URG NONE -j DROP")
        os.system("iptables -A INPUT -i _NDM_INPUT -p tcp --tcp-flags FIN,SYN FIN,SYN -j DROP")
        os.system("iptables -A INPUT -i _NDM_INPUT -p tcp --tcp-flags SYN,RST SYN,RST -j DROP")
        os.system("iptables -A INPUT -i _NDM_INPUT -p tcp --tcp-flags SYN,FIN SYN,FIN -j DROP")
        os.system("iptables -A INPUT -i _NDM_INPUT -p tcp --tcp-flags FIN,RST FIN,RST -j DROP")
        os.system("iptables -A INPUT -i _NDM_INPUT -p tcp --tcp-flags FIN,ACK FIN -j DROP")
        os.system("iptables -A INPUT -i _NDM_INPUT -p tcp --tcp-flags ACK,URG URG -j DROP")
        os.system("iptables -A INPUT -i _NDM_INPUT -p tcp --tcp-flags ACK,FIN FIN -j DROP")
        os.system("iptables -A INPUT -i _NDM_INPUT -p tcp --tcp-flags ACK,PSH PSH -j DROP")
        os.system("iptables -A INPUT -i _NDM_INPUT -p tcp --tcp-flags ALL ALL -j DROP")
        os.system("iptables -A INPUT -i _NDM_INPUT -p tcp --tcp-flags ALL NONE -j DROP")
        os.system("iptables -A INPUT -i _NDM_INPUT -p tcp --tcp-flags ALL FIN,PSH,URG -j DROP")
        os.system("iptables -A INPUT -i _NDM_INPUT -p tcp --tcp-flags ALL SYN,FIN,PSH,URG -j DROP")
        os.system("iptables -A INPUT -i _NDM_INPUT -p tcp --tcp-flags ALL SYN,RST,ACK,FIN,URG -j DROP")
        os.system("iptables -A INPUT -i _NDM_INPUT  -p tcp --dport 0 -j DROP")
        os.system("iptables -A INPUT -i _NDM_INPUT  -p udp --dport 0 -j DROP")
        os.system("iptables -A INPUT -i _NDM_INPUT  -p tcp --sport 0 -j DROP")
        os.system("iptables -A INPUT -i _NDM_INPUT  -p udp --sport 0 -j DROP")
    def disable():
        os.system("iptables -D INPUT -i _NDM_INPUT  -p tcp --dport 0 -j DROP")
        os.system("iptables -D INPUT -i _NDM_INPUT  -p udp --dport 0 -j DROP")
        os.system("iptables -D INPUT -i _NDM_INPUT  -p tcp --sport 0 -j DROP")
        os.system("iptables -D INPUT -i _NDM_INPUT  -p udp --sport 0 -j DROP")
        os.system("iptables -D INPUT -p icmp -m icmp --icmp-type 17 -j DROP")
        os.system("iptables -D INPUT -p icmp -m icmp --icmp-type 13 -j DROP")
        os.system("iptables -D INPUT -i _NDM_INPUT -p tcp ! --syn -m conntrack --ctstate NEW -j DROP")
        os.system("iptables -D INPUT -i _NDM_INPUT -p tcp --tcp-flags FIN,SYN,RST,PSH,ACK,URG NONE -j DROP")
        os.system("iptables -D INPUT -i _NDM_INPUT -p tcp --tcp-flags FIN,SYN FIN,SYN -j DROP")
        os.system("iptables -D INPUT -i _NDM_INPUT -p tcp --tcp-flags SYN,RST SYN,RST -j DROP")
        os.system("iptables -D INPUT -i _NDM_INPUT -p tcp --tcp-flags SYN,FIN SYN,FIN -j DROP")
        os.system("iptables -D INPUT -i _NDM_INPUT -p tcp --tcp-flags FIN,RST FIN,RST -j DROP")
        os.system("iptables -D INPUT -i _NDM_INPUT -p tcp --tcp-flags FIN,ACK FIN -j DROP")
        os.system("iptables -D INPUT -i _NDM_INPUT -p tcp --tcp-flags ACK,URG URG -j DROP")
        os.system("iptables -D INPUT -i _NDM_INPUT -p tcp --tcp-flags ACK,FIN FIN -j DROP")
        os.system("iptables -D INPUT -i _NDM_INPUT -p tcp --tcp-flags ACK,PSH PSH -j DROP")
        os.system("iptables -D INPUT -i _NDM_INPUT -p tcp --tcp-flags ALL ALL -j DROP")
        os.system("iptables -D INPUT -i _NDM_INPUT -p tcp --tcp-flags ALL NONE -j DROP")
        os.system("iptables -D INPUT -i _NDM_INPUT -p tcp --tcp-flags ALL FIN,PSH,URG -j DROP")
        os.system("iptables -D INPUT -i _NDM_INPUT -p tcp --tcp-flags ALL SYN,FIN,PSH,URG -j DROP")
        os.system("iptables -D INPUT -i _NDM_INPUT -p tcp --tcp-flags ALL SYN,RST,ACK,FIN,URG -j DROP")
        os.system("iptables -D INPUT -i _NDM_INPUT  -p tcp --dport 0 -j DROP")
        os.system("iptables -D INPUT -i _NDM_INPUT  -p udp --dport 0 -j DROP")
        os.system("iptables -D INPUT -i _NDM_INPUT  -p tcp --sport 0 -j DROP")
        os.system("iptables -D INPUT -i _NDM_INPUT  -p udp --sport 0 -j DROP")

try:
    if sys.argv[1] == 'enable':
        print('[*]Enabling rules')
        iptables.enable()
        print('[+]Rules enabled, Anti nmap Scanning enabled')
    elif sys.argv[1] == 'disable':
        print('[*]Disabling rules')
        iptables.disable()
        print('[+]Rules disabled, Anti nmap Scanning disabled')
except:
    print(f'\r\nUsage: {sys.argv[0]} enable/disable')
