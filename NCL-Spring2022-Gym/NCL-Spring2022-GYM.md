# Gymnasium Notes

## Exiftool

* Convert GPS to decimal
`exiftool.exe -c  "%.6f degrees" .\Downloads\Meta.jpg`  

## DNSSEC

[DNSSEC Blog](https://medium.com/@Nilabh/an-introduction-to-dnssec-96e53a469528)  

* RRSIG: Resource Record Signature
  * The RRSIG record contains the signed Record
* DNSKEY: DNS Public Key
  * DNSKEY is a record that holds the public key used to sign a Record or a DNS Zone
  * Zone Signing Key (ZSK): It is used to sign records in a DNS Zone
  * Key Signing Key (KSK): It is used to sign the Zone Signing Key (ZSK) and create a chain of trust with its upper level.  
  
## Training 17 Feb 2022

## Cryptography - Gym

### Crypto 1 (Easy)(80 points)  

Used KPE-Tools

1. Hex to ascii
2. Base64 to ascii
3. Binary to ascii
4. Binary to Base64 to ascii

### Crypto 2 (Easy)(25 points)

Uused KPE-Tools to decode ROT-13

### Crypto 3 (Easy)(25 points)  

Used http://rumkin.com/tools/cipher/atbash.php and the ***atbash*** decoder.  

### Crypto 4 (Easy)(25 points)

Used http://rumkin.com/tools/cipher/atbash.php and the ***morse*** decoder  

### Crypto 5 (Medium)(100 points)  

Used https://planetcalc.com/6947/ and decoded the ***Rail fence cipher***

* Example Encoded message: 	
Cair eruSA-0org sgaeudrpesr K-II98.ue cn seYQ3  
* Decoded message: Courage is grace under pressure SKY-AIQI-9380.  

### Crypto 6 (Medium)(50 points)  

Key: qizkwcgqbs
Message: Y ln xkv lubj swlzqvkht, A vmzb pjk bbua we ddgs ILQ-GQYU-8026  

Used http://rumkin.com/tools/cipher/atbash.php and the ***One Time Pad*** decoder  

### Stego 1 (Easy)(35 points)  

