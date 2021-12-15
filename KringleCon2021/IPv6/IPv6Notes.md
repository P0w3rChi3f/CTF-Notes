# IPv6 Notes

1. Based on the notes I am thinking of running an IPv6 Nmap scan.  I ended up running an `ip a` and noticed I had an IPv4 address.  So I did an `nmap` against it.  It returned 0 results.
2. After a quick search of nmap IPv6 scripts; I found the following very interesting:

    ```nmap
    dns-ip6-arpa-scan - nmap --script dns-ip6-arpa-scan --script-args='prefix=2001:0DB8::/48'
    ipv6-multicast-mld-list - nmap --script=ipv6-multicast-mld-list
    ipv6-node-info - nmap -6 <target>
    targets-ipv6-multicast-echo - ./nmap -6 --script=targets-ipv6-multicast-echo.nse --script-args 'newtargets,interface=eth0' -sL
    targets-ipv6-multicast-mld - nmap -6 --script=targets-ipv6-multicast-mld.nse --script-args 'newtargets,interface=eth0'
    targets-ipv6-multicast-slaac - nmap -6 --script targets-ipv6-multicast-slaac --script-args 'newtargets,interface=eth0' -sP
    ```  

3. I started with `dns-ip6-arpa-scan` my command was `nmap --script dns-ip6-arpa-scan --script-args='prefix=260:6000::/48`; the scan ended up timing out.  
4. The next one that I ran: `nmap --script=ipv6-multicast-mld-list` failed immediately  
5. I then ran `nmap -6 --script=targets-ipv6-multicast-echo.nse --script-args 'newtargets,interface=eth0' -sL`.  It too failed immediately.
6. Next was `nmap -6 --script=targets-ipv6-multicast-mld.nse --script-args 'newtargets,interface=eth0'` - Failed
7. Next was `nmap -6 --script targets-ipv6-multicast-slaac --script-args 'newtargets,interface=eth0'` - Failed
8. Next I reviewed the [Hand out](https://gist.github.com/chriselgee/c1c69756e527f649d0a95b6f20337c2f) provided by the elf.
9. After the review I ran `ping6 ff02::1 -c2` and `ping6 ff02::2 -c2` and found the following IPv6 addresses:

    ```Addresses
        fe80::42:c0ff:fea8:a003%eth0
        fe80::42:95ff:fe57:ead5%eth0
        fe80::42:c0ff:fea8:a002%eth0
    ```

10. Now that I have the some IPs; I will start with the curl command and start with `curl http://[fe80::42:c0ff:fea8:a003]:8080/ --interface eth0` Received a failed to connect.
11. Next I tried `curl http://[fe80::42:c0ff:fea8:a002]:8080/ --interface eth0` - Failed to connect
12. Next was `curl http://[fe80::42:95ff:fe57:ead5]:8080/ --interface eth0` - Failed to connect
13. I moved onto `netcat` and started with `nc -6 fe80::42:c0ff:fea8:a003%eth0 23` - failed to connect.
14. After a moment of clairity, I realized I still had one more script to run.  I failed to do this earlier because I need an IP address to run it against.  I am going to attempt to run `nmap -6 -Pn fe80::42:c0ff:fea8:a003` - failed with an `22 - invalid error`
15. Next attemp was `nmap -6 -Pn fe80::42:95ff:fe57:ead5` - failed with `22 - Invalid argument`
16. After some research, I found that I needed to add the interface on the end of the IP; so now  `nmap -6 -sV fe80::42:95ff:fe57:ead5%eth0` works.  I found ports `22 and 3000` open and I received what appears to be an `HTTP Header`
17. I continued on with `nmap -6 -sV fe80::42:c0ff:fea8:a003%eth0` and did not receive any intersting things back.
18. Next I did `nmap -6 -sV fe80::42:c0ff:fea8:a002%eth0`.   This scan came back with open ports of `80` and `9000` labed `Listener`.  It also appears to have `http`.
19. I am attempting the curl command again this time it will be `curl http://[fe80::42:c0ff:fea8:a002]:80/ --interface eth0`.  It returned:

    ```Return
        <html>
        <head><title>Candy Stripter v6</title></head>
        <body>
        <marquee>Connec to the the other open TCP poort to get the striper's activation phrase!</marquee>
        </body>
        /html>
    ```

20. So I followed instructions.  I started with curl: `curl http://[fe80::42:c0ff:fea8:a002]:9000/ --interface eth0` and received `PieceOnEarth`  
21. I used that to `engage the candy striper` and it work.  I am still courious about the other IP and what is there.
22. I started with another curl command `curl http://[fe80::42:c0ff:fea8:a002]:3000/ --interface eth0` and failed to connect.
23. I am assuming `port 22` will fail as well, but I checked anyway: `curl http://[fe80::42:c0ff:fea8:a002]:22/ --interface eth0` - It failed too.
24. Next I will try the same IP with Netcat. `nc -6 fe80::42:c0ff:fea8:a002%eth0 22` and `nc -6 fe80::42:c0ff:fea8:a002%eth0 3000` - Connection Refused on both and nothing else I tried work.  
