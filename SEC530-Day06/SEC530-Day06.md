# SEC530-Day06  

## Level 1

1. NTP DoS - Monlist
2. 9 $9$7HMiVNcHwGuyyI$qe5Geds4Vvcij5fl6asR3wAvO7pDFt/iJddDM6gKaF2 - ***Cicos type 9 / SCRYPT***

    ``` Algorithim ID
        $1$ is MD5
        $2a$ is Blowfish
        $2y$ is Blowfish
        $5$ is SHA-256
        $6$ is SHA-512
    ```

3. Vlan Tagging Protocol - ***802.1q***  

4. Bogon Addresses  

    ``` Address List
        0.0.0.0/8
        10.0.0.0/8
        100.64.0.0/10
        127.0.0.0/8
        169.254.0.0/16
        172.16.0.0/12
        192.0.0.0/24
        192.0.2.0/24
        192.168.0.0/16
        198.18.0.0/15
        198.51.100.0/24
        203.0.113.0/24
        224.0.0.0/4
        240.0.0.0/4
    ```  

5. Protocol used by proxies allows additional security checks such as multiple antivirus engine scans, malware detonation, or custom analysis - ***ICAP***  

6. Technology automatically upgrades all connection attempts to HTTP to HTTPS and removes the end-user's capability of clicking through an invalid certificate  - ***HSTS***  

7. Windows File Classification Infrastructure (FCI) store file classifications - ***Alternate Data Streams (ADS)***  

8. Flexible Authentication Secure Tunneling (FAST) for Kerberos is commonly known as ***Kerberos armoring***  

9. Syslog UDP port ***514***  

10. DHCP Discover option for DHCP Fingerprinting ***55***  

## SEC530 - IPv6  

1. fe80:: is a ***Link-Local Address***  

2. IPv6 address of dtf.sec530.org is ***2604:a880:0:1010::5db:4001***  

    ``` notes
    Found with Brim looking at the "HTTP" requests.  I was able to find a "GET" request to "dualstack.sec530.org" in pcap 2

    Same results using wireshark display fileter "http.request.method==GET"

    tcpdump filter should work "tcpdump -r ipv6-2.pcap 'tcp[((tcp[12:1] & 0xf0) >> 2):4] = 0x47455420'"
    ```  

3. IPv6 address of an internet DNS server ***2001:4860:4860::8888*** in pcap 1.  

    ``` Query
    Wireshark filter "udp.dstport == 53"

    tcpdump -n -r ipv6-1.pcap 'udp dst port 53'
    ```  

4. alphanumeric model number of the printer ***Brother HL-2270DW series***

    mDNS message is a multicast UDP packet

    ```mDNS Notes
    IPv4 address 224.0.0.251
    IPv6 address ff02::fb
    UDP port 5353

    query used "ipv6.addr == ff02::fb" on pcap1
    ```  

5. Destination multicast address used by the multicast DNS traffic
    * See previous notes  
6. QUIC port and protocol ***UDP/443***
7. Version of Chrome is using QUIC.  Just followed the stream of the previous answer and came up with ***65.0.3325.181***  
8. Numeric ICMPv6 type used for the Neighbor Solicitation.  I used a wireshark filter of "icmpv6".  Drilled down in the packet (ICMP -> type -> ***135***)  
9. The Wireshark filter I used to find the number of chained IPv6 extension headers ***((((ipv6 ) && !(ipv6.nxt == 6)) && !(ipv6.nxt == 17)) ) && !(ipv6.nxt == 58)*** I then counted the extension headers  

    ``` Answers
    TCPDUMP command: 

    "tcpdump -nX -r ipv6-1.pcap greater 726 and ip6 and !'ip6[6:1]=0x06' and !'ip6[6:1]=0x3a' and !'ip6[6:1]=0x11' | head -1 | awk -F">" '{print $2}' | awk -F":" '{print $(NF)}' | sed 's/no next header//g' | tr ' ' '\n' | grep -v "=" | grep -v "(" | grep -v "Deprecated" | wc -w"

    Wireshark Filter: 

    "((((ipv6 ) && !(ipv6.nxt == 6)) && !(ipv6.nxt == 17)) ) && !(ipv6.nxt == 58)"
    ```  

10. Using the above Wireshark filter there was only one IPv6 source address of the packets with a large number of IPv6 extension headers ***fe80::dead:beef:530***  
11. Not Found yet
12. the Unique Local Address subnet used on the network where this PCAP2 file was captured ***fdfe:9e87:9d56:1000::/64***  
13. The MAC address of the IPv6 router interface used on the network where this PCAP2 file was captured ***00:2a:e3:cc:a2:2d*** found with Wireshark filter "ipv6.addr == ff02::2"  
14. The Global Unique Address subnet used on the network where this PCAP2 file was captured.  I used Wireshark filter "((!(ipv6.src == ::)) && !(ipv6.src == fe80::52:3121:2ec1:f012)) && !(ipv6.src == fe80::1810:ac41:8f4e:66a8) && !(icmpv6) && !(mdns) && !(llmnr)"  ***2001:470:1f11:78e::/64***

## Sec530 Router  

1. SNMP RW community string on 10.5.30.100 is ***4changes***  

    ```Metasploit  
        use auxiliary/scanner/snmp/snmp_login
        set RHOSTS 10.5.30.100
        run
    ```  

2. Version of Cisco IOS is running on 10.5.30.100 is ***C7200-ADVIPSERVICESK9-M***  

    ```Metasploit
        use auxiliary/scanner/snmp/snmp_enum
        set rhosts 10.5.30.100
        run
    ```  

3. Sebastian's password on 10.5.30.100 is ***ncc1701d*** the hash was ***$1$qYUc$28Z6ORC0/46hBlztdSP5K.***

    ```Nmap
    sudo nmap -sU -p 161 --script snmp-ios-config --script-args creds.snmp=:4changes 10.5.30.100

    cd /opt/john/run
    ./john /home/student/Desktop/RouterCFG.txt
    ```  

4. Tyrell's password on 10.5.30.100 is ***MoreHumanThanHuman*** by using an online Cisco password 7 cracker.
