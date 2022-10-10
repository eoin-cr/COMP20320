# COMP20320
Scripts and files for computer networking

## Netmask
The linux package `ipcalc` will take IP address(es) and convert it to binary, and show the class, netmask, etc.

## Converting between binary and decimal
To convert from decimal to binary you can either use the `dec_to_bin.sh` script, or you can use the command
```
bc <<< "obase=2; 255"
```
where 255 is any decimal number.  Note that you cannot convert full ip addresses with this method (i.e. 255.255 does not work).  Also note that the result will not always be 8 bits long.

To convert from binary to decimal you can use the command
```
echo "$((2#11111111))"
```
where 11111111 is a binary number.  Once again note that full ip addresses will not work.
