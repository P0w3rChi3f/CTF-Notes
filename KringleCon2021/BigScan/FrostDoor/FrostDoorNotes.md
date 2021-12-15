# Frost Door Notes

1. Started with a scan: `iwlist scan` and returned the following results:  

    ```results
        wlan0     Scan completed :
          Cell 01 - Address: 02:4A:46:68:69:21
                    Frequency:5.2 GHz (Channel 40)
                    Quality=48/70  Signal level=-62 dBm  
                    Encryption key:off
                    Bit Rates:400 Mb/s
                    ESSID:"FROST-Nidus-Setup"
    ```

2. Connected to wifi with `iwconfig wlan0 essid FROST-Nidus-Setup`  
3. Received notice of: `** New network connection to Nidus Thermostat detected! Visit http://nidus-setup:8080/ to complete setup (The setup is compatible with the 'curl' utility)`
4. I first attempted `curl http://nidus-setup:8080` and received an API url of `http://nidus-setup:8080/apidoc` to change the temperature.  
5. I then used `curl http://nidus-setup:8080/apidoc` went to a screen and saw these urls `curl -XGET http://nidus-setup:8080/api/cooler` and `curl -XPOST -H 'Content-Type: application/json' --data-binary '{"temperature": -40}' http://nidus-setup:8080/api/cooler`  
6. I ended up getting my achievment by this command `curl -XPOST -H 'Content-Type: application/json' --data-binary '{"temperature": 40}' http://nidus-setup:8080/api/cooler`  
