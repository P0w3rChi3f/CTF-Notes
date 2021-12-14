# Yara Analysis Notes

1. Ran the application and received `yara_rule_135 ./the_critical_elf_app`  
2. Ran `cat yara_rules/rules.yar | grep -A15 yara_rule_135 | less`  

    ```received
    rule yara_rule_135 {
    meta:
        description = "binaries - file Sugar_in_the_machinery"
        author = "Sparkle Redberry"
        reference = "North Pole Malware Research Lab"
        date = "1955-04-21"
        hash = "19ecaadb2159b566c39c999b0f860b4d8fc2824eb648e275f57a6dbceaf9b488"
    strings:
        $s = "candycane"
    condition:
        $s
    }
    ```

3. Ran `xxd yara_rule_135 ./the_critical_elf_app yara_rule_135 ./the_critical_elf_app.hex`
4. Found a malicious statement and changed the e in cane to a 3 or.

    ```found
        00002000: 0100 0200 0000 0000 6361 6e64 7963 616e  ........candycan
        00002010: 6500 6e61 7567 6874 7920 7374 7269 6e67  e.naughty string
        00002020: 0000 0000 0000 0000 5468 6973 2069 7320  ........This is
        00002030: 6372 6974 6963 616c 2066 6f72 2074 6865  critical for the
        00002040: 2065 7865 6375 7469 6f6e 206f 6620 7468   execution of th
        00002050: 6973 2070 726f 6772 616d 2121 0000 0000  is program!!....
        00002060: 486f 6c69 6461 7948 6163 6b43 6861 6c6c  HolidayHackChall
        00002070: 656e 6765 7b4e 6f74 5265 616c 6c79 4146  enge{NotReallyAF
        00002080: 6c61 677d 0064 6173 7461 7264 6c79 2073  lag}.dastardly s
        00002090: 7472 696e 6700 0000 011b 033b 3c00 0000  tring......;<...
    ```
    * running strings also found `naughty string` and `dastardly string`
5. Ran `xxd -r the_critical_elf_app.hex the_critical_elf_app.back`
6. Tried to execute `./the_critical_elf_app.back` and received `yara_rule_1056 ./the_critical_elf_app.back`
7. Ran `cat yara_rules/rules.yar | grep -A15 yara_rule_1056 | less`

    ```received
    rule yara_rule_1056 {
    meta: 
            description = "binaries - file frosty.exe"
            author = "Sparkle Redberry"
            reference = "North Pole Malware Research Lab"
            date = "1955-04-21"
            hash = "b9b95f671e3d54318b3fd4db1ba3b813325fcef462070da163193d7acb5fcd03"
        strings:
            $s1 = {6c 6962 632e 736f 2e36}
            $hs2 = {726f 6772 616d 2121}
        condition:
            all of them
    }
    ```

8. Changed `6c 6962 632e 736f 2e36` to `6c 6962 632e 736f 2e30`

    ```received
    rule yara_rule_1732 {
    meta:
        description = "binaries - alwayz_winter.exe"
        author = "Santa"
        reference = "North Pole Malware Research Lab"
        date = "1955-04-22"
        hash = "c1e31a539898aab18f483d9e7b3c698ea45799e78bddc919a7dbebb1b40193a8"
    strings:
        $s1 = "This is critical for the execution of this program!!" fullword ascii
        $s2 = "__frame_dummy_init_array_entry" fullword ascii
        $s3 = ".note.gnu.property" fullword ascii
        $s4 = ".eh_frame_hdr" fullword ascii
        $s5 = "__FRAME_END__" fullword ascii
        $s6 = "__GNU_EH_FRAME_HDR" fullword ascii
        $s7 = "frame_dummy" fullword ascii
        $s8 = ".note.gnu.build-id" fullword ascii
        $s9 = "completed.8060" fullword ascii
        $s10 = "_IO_stdin_used" fullword ascii
        $s11 = ".note.ABI-tag" fullword ascii
        $s12 = "naughty string" fullword ascii
        $s13 = "dastardly string" fullword ascii
        $s14 = "__do_global_dtors_aux_fini_array_entry" fullword ascii
        $s15 = "__libc_start_main@@GLIBC_2.2.5" fullword ascii
        $s16 = "GLIBC_2.2.5" fullword ascii
        $s17 = "its_a_holly_jolly_variable" fullword ascii
        $s18 = "__cxa_finalize" fullword ascii
        $s19 = "HolidayHackChallenge{NotReallyAFlag}" fullword ascii
        $s20 = "__libc_csu_init" fullword ascii
    condition:
        uint32(1) == 0x02464c45 and filesize < 50KB and
        10 of them
    }
    ```
