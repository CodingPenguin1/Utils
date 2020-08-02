# Utils

This is a directory containing all the short, but useful, little scripts I use on all my Linux systems nearly every day. I store this in my home directory, and have added `~/Utils/bin` to my PATH.

## backup

This is a modified version of the sample [Borg Backup script](https://borgbackup.readthedocs.io/en/stable/quickstart.html). This is a little personalized. You'll want to edit the `--exclude` lines in `src/backup` to match what you want to not backup.

Language: Bash

Dependencies: [Borg Backup](https://borgbackup.readthedocs.io/en/1.1-maint/installation.html)

Usage: `backup /PATH/TO/BORG/REPOSITORY`

## diskusage

This script provides a fast listing of disk usage. It automatically finds mounted partions of `/dev/sdXY`, anything mounted in `/mnt`, and the `/tmp` directory. There are a few options for styling the output.

Language: Python

Dependencies: [termcolor](https://pypi.org/project/termcolor2/)

Usage: `diskusage` (you may need to run it as root, depending on your setup)

Options (optional):

``` bash
-p, --polybar   Switch to vertical bars that more nicely fit on a polybar
-o, --oneLine   Print all output on one line (must have -p flag as well to work)
-n, --noNames   Do not print the names of drives
```

## mountsystem

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

## paleofetch

A rewrite of [neofetch](https://github.com/dylanaraps/neofetch) in C written by [sam-barr](https://github.com/sam-barr). More documentation available on his [github](https://github.com/sam-barr/paleofetch)

Language: C

Dependencies: libX11, libpci

Usage: `paleofetch`

## portscan

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

## sshsystem

SSH a system by providing a system name, and just a system name.

This requires you to have the following files:

`~/.SYSTEM_NAME_IP`  (Used to store the IP of SYSTEM_NAME. Replace SYSTEM_NAME with whatever you want)

`~/.ssh/SYSTEM_NAME_rsa`  (RSA key for the system. Learn how to set up an RSA key pair [here](https://www.digitalocean.com/community/tutorials/how-to-set-up-ssh-keys--2))

If you set up your RSA keys and filesystem structure like `mountsystem` requires, this will already be done.

Language: Python

Dependencies: None

Usage: `sshsystem SYSTEM_NAME`

## Other People's Programs

Here are some links to programs I really enjoy from other users:

[screenshot-actions](https://github.com/jrodal98/screenshot-actions)

[thefuck](https://github.com/nvbn/thefuck)

[paleofetch](https://github.com/sam-barr/paleofetch)

[x2x](https://www.youtube.com/watch?v=umC_zUPGrp4&list=WL&index=7&t=0s)

[xscreensaver](https://www.jwz.org/xscreensaver/)

[mlocate](https://wiki.archlinux.org/index.php/Mlocate)

[lxappearance](https://www.archlinux.org/packages/community/x86_64/lxappearance/)

[wallset](https://github.com/terroo/wallset)

[pscircle](https://github.com/tuxarch/pscircle)

## Fun Programs

Some programs that aren't really that useful but I like them so I put them here

[doge](https://github.com/thiderman/doge)

[fortune](https://wiki.archlinux.org/index.php/Fortune)

[cowsay](https://github.com/piuccio/cowsay)

[xcowsay](https://github.com/Tuczi/xcowsay)

[lolcat](https://github.com/busyloop/lolcat)

[sl](https://github.com/mtoyoda/sl)

[figlet](http://www.figlet.org/)

[toilet](http://caca.zoy.org/wiki/toilet)

[bullshit](https://github.com/fceschmidt/bullshit-arch/)

[cmatrix](https://github.com/abishekvashok/cmatrix)

[asciiquarium](https://github.com/cmatsuoka/asciiquarium)

[aafire](https://github.com/Softmuppen/aafire)

[tty-clock](https://github.com/xorg62/tty-clock)

`sudo visudo` (Add "Default insults")

[hollywood](https://github.com/dustinkirkland/hollywood)

[bb](https://aur.archlinux.org/packages/bb/)
