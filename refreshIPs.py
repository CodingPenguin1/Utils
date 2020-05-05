#!/home/rjslater/anaconda3/bin/python

from os import remove, system, popen

try:
    remove('/home/rjslater/Julien/JARVIS_IP')
except:
    pass

if __name__ == '__main__':
    # Get current IP and save to Julien
    # Mount Julien
    with open('/home/rjslater/.Julien_IP', 'r') as f:
        julienIP = f.read().strip()
    system('sshfs -o IdentityFile=/home/rjslater/.ssh/Julien_rsa kowalski@{}:/mnt/gloria/kowalski /home/rjslater/Julien'.format(julienIP))

    # Get Current IP
    jarvis_IP = popen('ip addr show wlp2s0').read().split('inet ')[1].split('/')[0]
    print('IP: {}'.format(jarvis_IP))

    # Write IP file to Julien
    with open('/home/rjslater/Julien/JARVIS_IP', 'w') as f:
        f.write(jarvis_IP)

    # Try to read FRIDAY IP from Julien
    try:
        with open('/home/rjslater/Julien/FRIDAY_IP', 'r') as f:
            fridayIP = f.read().strip()
        with open('/home/rjslater/.FRIDAY_IP', 'w') as f:
            f.write(fridayIP)
    except:
        print('Failed to get JARVIS\' IP')

    # Try to unmount Julien (may be busy from backup, etc)
    try:
        system('sudo umount /home/rjslater/Julien')
    except:
        print('Failed to unmount Julien')
