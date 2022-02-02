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
  