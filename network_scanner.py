#! /usr/bi/env python

import scapy.all as scapy
import argparse

def get_arguments():
    parser = argparse.ArgumentParser()
    parser.add("-t", "--target", Dest="target", help="target range/ip range")
    options = parser.parse_args()
    return options

def scan(ip):
    arp_request = scapy.ARP(pdst=ip)
    broad_cast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broad_cast/arp_request
    answered_list = scapy.srp(arp_request_broadcast, timeout=1)[0]

    print("IP\t\t\tMAC ADDRESS\n....................................")
    for element in answered_list:
        print(element[1].psrc, "\t\t" + element[1].hwsrc)


scan("[+] please mention subnet range here")

# useful comments/ commands
# arp_request_broadcast.show()
# print(arp_request_broadcast.summary())
# print(broad_cast.summary())
# print(arp_request.summary())
# scapy.ls(scapy.ARP())
