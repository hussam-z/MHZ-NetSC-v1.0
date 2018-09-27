#! /usr/bin/env python3

import scapy.all as scapy

##############################################
 
print("""



        __  __ _    _ ______     _   _      _    _____  _____ 
       |  \/  | |  | |___  /    | \ | |    | |  / ____|/ ____|
       | \  / | |__| |  / ______|  \| | ___| |_| (___ | |     
       | |\/| |  __  | / |______| . ` |/ _ | __|\___ \| |     
       | |  | | |  | |/ /__     | |\  |  __| |_ ____) | |____ 
       |_|  |_|_|  |_/_____|    |_| \_|\___|\__|_____/ \_____|

                          -- version 1.0 --                                           

			Welcome To MHZ-NetSC
			   created by : 
		  {*} Moammad Hussam Alzeyyat {*}
		      {*} bash_shabakate {*}

				FB :
	   https://www.facebook.com/muhammedhusam.alzeyyat.9
			     Github : 
		     https://github.com/hussam-z


Usage : 
	
	1- Enther Target IP / Target IP Range
	
.............................................................

""")

##############################################


ip = input("{+} Enther Target IP / Target IP Range => ")

def scan(ip):
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast/arp_request
    answered_list = scapy.srp(arp_request_broadcast, timeout=10)[0]
    

    print("\nIP\t\t\tMAC Address\n-------------------------------------------------------------")

    for answeres in answered_list:
        print(answeres[1].psrc+ "\t\t" + answeres[1].hwsrc)
        print("-------------------------------------------------------------")

scan(ip)
