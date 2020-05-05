#!/usr/bin/env python
import sys
from os import system
from pathlib import Path


if __name__ == '__main__':
    SYSTEM_NAME = sys.argv[1]  # Get name of system from CLI arg
    HOME_DIR = str(Path.home())  # Get home directory (I store my IP files in ~/)
    REMOTE_USERNAME = sys.argv[2] if len(sys.argv) >= 3 else HOME_DIR[1:][HOME_DIR[1:].find('/') + 1:]

    # Get system IP and RSA key file
    with open(f'{HOME_DIR}/.{SYSTEM_NAME}_IP') as ipFile:
        # Get IP
        ip = ipFile.readline().strip()

        # Get RSA key
        identityFile = f'{HOME_DIR}/.ssh/{SYSTEM_NAME}_rsa'

    # Mount system
    system(f'sshfs -o IdentityFile={identityFile} {REMOTE_USERNAME}@{ip}:/home/{REMOTE_USERNAME} {HOME_DIR}/{SYSTEM_NAME}')
