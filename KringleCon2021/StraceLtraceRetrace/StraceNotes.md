# Strace Ltrace Retrace Notes

1. Runing `./make_the_candy` produced `Unable to open configuration file.`  
2. Started with `ltrace ./make_the_candy` and noticed that is was trying to open a `registration.json` with `fopen("registration.json", "r")`  
3. I created the json using `touch registration.json` and ran `./make_the_candy` again.
4. This time it had a `Unregistered - Exiting.` message.
5. I tried to add some text to the json file and it didn't work.  It did produce a new library call `strstr` and showed my input.  I didn't think of anything then, but it helped out later.
6. After a couple days of reading about [ltrace](https://man7.org/linux/man-pages/man1/ltrace.1.html) and [strace](https://man7.org/linux/man-pages/man1/strace.1.html) and all the various system and library calls.
7. I finally read some of the chats and took the hint of looking for `strstr`.  Here is where I started having fun.
8. I added `1234567890` to the file; then ran `ltrace ./make_the_candy`; I found this line to be interesting `strstr("123456789\n", "Registration")`
9. Next thought was to add json formating; so I added the `{}` so now my json looks like:

    ```json
        {
        "1234567890"
        }
    ```

10. My `./make_the_candy` still fail; Now my `ltrace ./make_the_candy` has the following interesting lines:

    ```output
        getline(0x7fff55e2f680, 0x7fff55e2f688, 0x55e7322c8260, 0x7fff55e2f688) = 2
        strstr("{\n", "Registration")                             = nil
        getline(0x7fff55e2f680, 0x7fff55e2f688, 0x55e7322c8260, 0x7fff55e2f688) = 15
        strstr("  "1234567890"\n", "Registration")                = nil
        getline(0x7fff55e2f680, 0x7fff55e2f688, 0x55e7322c8260, 0x7fff55e2f688) = 2
        strstr("}\n", "Registration")                             = nil
        getline(0x7fff55e2f680, 0x7fff55e2f688, 0x55e7322c8260, 0x7fff55e2f688) = -1
    ```
