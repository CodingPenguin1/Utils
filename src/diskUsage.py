#!/usr/bin/env python3
from termcolor import colored
import subprocess
import sys


class Drive:
    def __init__(self, name='drive', mountPoint='', displayName='DisplayName'):
        self.name = name
        self.displayName = name if displayName == 'DisplayName' else displayName

        # In bytes
        if mountPoint != '':
            self.mountPoint = mountPoint
        else:
            self.getMountPoint()
        self.getUsage()
        self.getCapacity()
        self.usagePercent = self.usage / self.capacity

    def getMountPoint(self):
        ps = subprocess.Popen(f'df | grep {self.name}', shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        output = ps.communicate()[0].decode('utf-8').strip().split('\n')
        output = [part.strip() for part in output[0].split(' ') if len(part.strip()) > 0]
        self.mountPoint = output[-1]

    def getUsage(self):
        ps = subprocess.Popen(f'df | grep {self.mountPoint}', shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        output = ps.communicate()[0].decode('utf-8').strip().split('\n')
        output = [part.strip() for part in output[0].split(' ') if len(part.strip()) > 0]
        self.usage = float(output[2]) * 2**10

    def getCapacity(self):
        ps = subprocess.Popen(f'df | grep {self.mountPoint}', shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        output = ps.communicate()[0].decode('utf-8').strip().split('\n')
        output = [part.strip() for part in output[0].split(' ') if len(part.strip()) > 0]
        self.capacity = (float(output[2]) + float(output[3])) * 2**10

    def printUsageBar(self, barWidth=50, green=0.75, yellow=0.9, style='htop', showNames=True, oneLine=False):
        if style == 'htop':
            numFillerChars = int(barWidth * self.usagePercent)
            if showNames:
                print(f'{self.displayName}\t[', end='')
            else:
                print('[', end='')

            if self.usagePercent < green:
                print(colored(numFillerChars * '|', 'green'), end='')
            elif self.usagePercent < yellow:
                print(colored(numFillerChars * '|', 'yellow'), end='')
            else:
                print(colored(numFillerChars * '|', 'red'), end='')

            print((barWidth - numFillerChars) * ' ', end='')
            print('] ', end='')

            print(f'{toHumanReadable(self.usage)} / {toHumanReadable(self.capacity)}', end='')

            if self.usagePercent < green:
                print('\t' + colored(str(round(100 * self.usagePercent, 1)), 'green') + '%')
            elif self.usagePercent < yellow:
                print('\t' + colored(str(round(100 * self.usagePercent, 1)), 'yellow') + '%')
            else:
                print('\t' + colored(str(round(100 * self.usagePercent, 1)), 'red') + '%')
        elif style == 'polybar':
            if showNames:
                print(self.displayName.strip() + ' ', end='')
            if oneLine:
                endChar = ''
                if showNames:
                    endChar = ' '
            else:
                endChar = '\n'
            if self.usagePercent < 0.125:
                print('▁', end=endChar)
            elif self.usagePercent < 0.25:
                print('▃', end=endChar)
            elif self.usagePercent < 0.375:
                print('▄', end=endChar)
            elif self.usagePercent < 0.5:
                print('▅', end=endChar)
            elif self.usagePercent < 0.625:
                print('▆', end=endChar)
            elif self.usagePercent < 0.75:
                print('▇', end=endChar)
            elif self.usagePercent < 0.875:
                print('█', end=endChar)


def toHumanReadable(size):
    if size < 2**10:
        return f'{round(size, 1)}B'
    elif size < 2**20:
        return f'{round(size / 2**10, 1)}K'
    elif size < 2**30:
        return f'{round(size / 2**20, 1)}M'
    elif size < 2**40:
        return f'{round(size / 2**30, 1)}G'
    elif size < 2**50:
        return f'{round(size / 2**40, 1)}T'


if __name__ == '__main__':
    # Get list of disks
    ps = subprocess.Popen(f'df', shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    drives = ps.communicate()[0].decode('utf-8').strip().split('\n')
    for i in range(len(drives)):
        newLine = drives[i].split(' ')
        while '' in newLine:
            newLine.remove('')
        drives[i] = newLine
    drives = drives[1:]

    # Parse out a list of drives to print
    goodDrives = []
    for drive in drives[1:]:
        if '/dev' in drive[0] or drive[5] == '/tmp':
            # Ignore loop partitions
            if drive[0][:9] != '/dev/loop':
                goodDrives.append(drive)

    # Get drive info
    drives = []
    for drive in goodDrives:
        # Get drive name
        name = drive[0]
        if '/' in drive[0]:
            name = drive[0][drive[0].rfind('/') + 1:]

        # Get drive mountpoint
        mountpoint = drive[5]
        if mountpoint == '/':
            mountpoint = '/dev/' + name

        # Generate drive display name
        displayName = mountpoint
        if displayName == '/dev/' + name:
            displayName = 'Boot'
        elif '/' in displayName:
            displayName = displayName[displayName.rfind('/') + 1:]

        drives.append(Drive(name, mountpoint, displayName))

    # Get longest display name
    longestName = 0
    for drive in drives:
        if len(drive.displayName) > longestName:
            longestName = len(drive.displayName)

    # Make all drives have the same dispay name length
    for drive in drives:
        drive.displayName += (longestName - len(drive.displayName)) * ' '

    # Assign default print options
    style = 'htop'
    noNames = False
    oneLine = False

    # Get print options from CLI args
    args = sys.argv[1:]
    for arg in args:
        if '-p' in arg:
            style = 'polybar'
        if '-n' in arg:
            noNames = True
        if '-o' in arg:
            oneLine = True

    # Print drive usage bars
    for drive in drives:
        drive.printUsageBar(style=style, showNames=(not noNames), oneLine=oneLine)
