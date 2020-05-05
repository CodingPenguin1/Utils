# Utils

This is a directory containing all the short, but useful, little scripts I use on all my Linux systems nearly every day. I store this in my home directory, and have added `~/Utils/bin` to my PATH.

## backup

----------------

This is a modified version of the sample [Borg Backup script](https://borgbackup.readthedocs.io/en/stable/quickstart.html). This is a little personalized. You'll want to edit the `--exclude` lines in `src/backup` to match what you want to not backup.

Language: Bash

Dependencies: [Borg Backup](https://borgbackup.readthedocs.io/en/1.1-maint/installation.html)

Usage: `backup /PATH/TO/BORG/REPOSITORY`

## mountsystem

----------------

This script is used to mount the home directory of a user on a remote system to a directory in the local user's home directory. For example, say the following properties are true:

``` bash
Local username: localuser
Remote username: remoteuser
Remote system name: sysname
```

Then
`/home/remoteuser` on `sysname` will be mounted to `/home/localuser/sysname` on the local system.

The command that ends up getting run is
`sshfs -o IdentityFile=/home/$(localuser)/.ssh/$(sysname)_rsa remoteuser@$(remoteip):/home/$(remoteuser) /home/$(localuser)/$(sysname)`

This requires you to have the following files:

`~/.SYSTEM_NAME_IP`  (Used to store the IP of SYSTEM_NAME. Replace SYSTEM_NAME with whatever you want)

`~/SYSTEM_NAME/`     (Directory to mount the remote system to. Needs to be in the home directory)

`~/.ssh/SYSTEM_NAME_rsa`  (RSA key for the system. Learn how to set up an RSA key pair [here](https://www.digitalocean.com/community/tutorials/how-to-set-up-ssh-keys--2))

Language: Python

Dependencies: [sshfs](https://github.com/libfuse/sshfs)

Usage: `mountsystem SYSTEM_NAME`

## portscan

----------------

This program was written by [tux2603](https://github.com/tux2603/QuickLittleUtils/blob/master/portCheck). It checks all ports within a range on a given system and outputs if they're open.

Language: Perl

Dependencies: None

Usage:

``` bash
portCheck -- checks which communication ports on a certain host are open

USAGE: portCheck [-ah] [-t port_timeout] [-u host_url] [ [starting_port] ending_port]

By default, this checks ports on localhost.  By passing a -u argument followed by
a url, you can specify what location to check.

By default, this will only display ports that are open.  By passing '-a' as a
command line argument, this will display output for all ports checked.

By default, this will check all ports from 0 to 65535.  If one integer is passed
as an argument, it will be used for the maximum port number to check (inclusive).
If two integers are passed, they will be used as the range of port numbers to be
checked (again, inclusive).

By default, this tries to connect to a port for 1000 ms before giving up.  By
passing a -t argument followed by an integer, you can specify how long of a
time out to use.  Note that if you are checking remote ports, you should allow for
sufficient communication time.

Passing -h as an argument will print out this help message.

-☃, the Unicode Snowman
```
