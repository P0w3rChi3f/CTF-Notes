# Big Scan Notes

1. I imedately used the hint and pulled up this [grep cheatsheet](https://ryanstutorials.net/linuxtutorial/cheatsheetgrep.php)  
2. The questions that need answered are:
    - What port does 34.76.1.22 have open?
        - query: `grep "34.76.1.22" bigscan.gnmap`
        - answer: `62078`
    - What port does 34.77.207.226 have open?
        - query: `grep "34.77.207.226" bigscan.gnmap`
        - answer: `8080`
    - How many hosts appear "Up" in the scan?
        - query: `grep "Status: Up" bigscan.gnmap | awk '{print $2}' | sort | uniq | wc -l`
        - answer: `26054`
    - How many hosts have a web port open?  (Let's just use TCP ports 80, 443, and 8080)
        - query: `grep Ports: bigscan.gnmap | grep -E "80/open|443/open|8080" | wc -l`
        - answer: `14372`
    - How many hosts with status Up have no (detected) open TCP ports?
        - hint: `echo $(("grep Something | wc -l" - "grep SomethingElse | wc -l"))`
        - query: `echo $(("grep "Up" bigscan.gnmap | wc -l" - "grep Ports: bigscan.gnmap | wc -l"))`
        - answer: `402`
    - What's the greatest number of TCP ports any one host has open?  
        - hint: `grep -E "(Jolly.*){5}" file.txt | wc -l`  
        - hint: `grep -E "(Jolly.*){6,}" file.txt | wc -l`  
        - hint: ``
        - query: `grep -E "(tcp.*){12,}" bigscan.gnmap | wc -l`
        - answer: `12`  
