# Objective: Level 3 - Control Room Terminals

## Q8 - SCALPEL: RESEARCH RECOVERY 7 POINTS

Access the Scalpel terminal found in control.wey-tech.com on the terminals tab, and follow the instructions found in the motd banner or the HELP file.

Submit the flag found from mounting john_sdb1.img and recovering files.

```Help file
Dr. John Reed had captured and was studying
a xeno-morph specimen before norehca was 
overrun. Investigate john's recovered drive-
file at /root/john_sdb1.img to find and 
recover (using scalpel) any research he may
have produced. 
```

Research is typically in spreadsheets, word docs, and PDFs.
ran `file john_sdb1.img` found a DOS/MBR Boot Sector and Fat formatted

john@norehca­research:~/$ xxd NW.flag 
00000000: 924e 5746 5354 4152 540a 4e65 7457 6172  .NWFSTART.NetWar
00000010: 737b 4e6f 7441 466c 6167 7d0a 9245 4f46  s{NotAFlag}..EOF
john@norehca­research:~/$ xxd Power.cell 
00000000: 8050 4353 5441 5254 0a50 6f77 6572 4365  .PCSTART.PowerCe
00000010: 6c6c 5b44 6570 6c65 7465 645d 0a80 454f  ll[Depleted]..EO
00000020: 46      
Truly fascinating creatures!

```Scalple Config

# Custom Scalpel Config File
#               Case    Size    Header          Footer
#Extensions Sensitive
#-----------------------------------------------
# NWF START
#-----------------------------------------------
        flag    y       64      \x92\x4e\x57\x46\x53\x54\x41\x52\x54    EOF
#
#-----------------------------------------------
# PC START
#-----------------------------------------------
        cell    y       64      \x80\x50\x43\x53\x54\x41\x52\x54        EO
#
```

## Q9 - DIG: CAN YOU DIG IT? 3 POINTS

```tasks
The Norehca (LV-425) DNS server is currently infected 
with a variant of the xeno-malware. Investigate the DNS
server using the dig tool and find a way to elevate to 
root, stop the malware and recover any PowerCells.
```


## Q13 - REGEX: (BB|[^B]{2}) 7 POINTS

```Notes
Dr. Reed don't need no stinkin passwords, he's 
got regular expressions! Prove you are Dr. Reed
by correctly solving eight Regex Challenges to 
get Dr. Reed's terminal access. Checkout the 
site https://pythex.org/ for testing regex. 
Python re.findall module used for validation.
```
