#Given an IP address and a mask, return whether or not it is a valid host IP address

import sys

def is_valid_ip(ip):
    octets = ip.split(".")
    if len(octets) != 4:
        return False
    for octet in octets:
        if not octet.isdigit():
            return False
        if int(octet) < 0 or int(octet) > 255:
            return False
    return True

def is_valid_mask(mask):
    octets = mask.split(".")
    if len(octets) != 4:
        return False
    for octet in octets:
        if not octet.isdigit():
            return False
        if int(octet) < 0 or int(octet) > 255:
            return False
    return True

def is_valid_host(ip, mask):
    ip_octets = ip.split(".")
    mask_octets = mask.split(".")
    for i in range(4):
        if int(ip_octets[i]) & int(mask_octets[i]) != int(ip_octets[i]):
            return False
    return True

def main():
    if len(sys.argv) != 3:
        print("Usage: ./valid_ip.py <ip> <mask>")
        sys.exit(1)
    ip = sys.argv[1]
    mask = sys.argv[2]
    if not is_valid_ip(ip):
        print("Invalid IP address")
        sys.exit(1)
    if not is_valid_mask(mask):
        print("Invalid mask")
        sys.exit(1)
    if is_valid_host(ip, mask):
        print("Valid host IP address")
    else:
        print("Invalid host IP address")