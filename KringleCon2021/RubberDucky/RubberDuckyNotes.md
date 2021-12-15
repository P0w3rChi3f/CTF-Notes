# USB Rubber Ducky Notes

1. Reviewed some of the hints the elf gave me.  
    - [Ducky Script](https://docs.hak5.org/hc/en-us/articles/360010555153-Ducky-Script-the-USB-Rubber-Ducky-language)
    - [Duck Encoder](https://docs.hak5.org/hc/en-us/articles/360010471234-Writing-your-first-USB-Rubber-Ducky-Payload)
    - [Ducky RE with Mallard](https://github.com/dagonis/Mallard)
    - [Mitre ATT&CK and Ducky](https://attack.mitre.org/techniques/T1098/004/)
2. I read the help file for the `Mallard Python3` script and decided to try: `python3 mallard.py --file /mnt/USBDEVICE/inject.bin`.  
3. The results showed many command lines, but there was one that was reversed base64 encoded.  The encoded string was `ickymcgoop@trollfun.jackfrosttower.com` emeded in it.
4. The answer was: `ickymcgoop`  
