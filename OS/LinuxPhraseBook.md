# Linux Phrasebook

Author: Scott Granneman
Publication Year: 2006

## Look Up Later

* Sam's Teach yourself regular expressions in 10 minutes by Ben Forta
  * what is a regular expressin by docs.kde
  * Regular expressions explained by castiglia
  * Wildcardsgone wrong by linux-mag
* KDE
* "Bourn again shell" where did that come from
* lsof command
* MS-DOS
* FIFO as | from ls -F options, and = as socket
* Linux hard vs soft links
* Why -i for warnings?
* Firmer tutorial on environment variables
* Origin of Man Page categories, the evolution of the man pages. Games?
* Man vs info
* IO Streams and file descriptors
* "Dog" as a text editor alternative to "Cat"
* Access control lists: the latest on this. Overlap with Cloud computing course? "An ACL Gui for Linux" recommended here
* Sticky bit and permissions on older linux systems
* Permissions as 000
* suid for exes, sgids
* History of the Sticky Bit, and how it actually works in the /tmp dir
* Linux Magazine article comparing different compression mechanisms
* Why does zip -P passwd even exist?
* Explore more consequences of -t for zip
* Linux Trivia
* List Difference between tar and zip (tricky = zip 0)
* History of tar, and its flag combinations. Revisit how the zvcf works
* Why did i have to manually install locate, and why did its installation take so long?
* Time command to figure out how long something takes
* Play around with grep -A, -B, -C for contexts
* Gentoo Wiki: Linux Memory Management
* tmpfs as a storage space, history
* Distrowatch's Linux distributions facts and figures
* apt vs apt-get vs dpkg
* Linux magazine: a very apropos apt
* sshfs
* Loopback interface
* How the internet really works, hops, traceroute
* mtr as a ping and traceroute alternative
* Wired equivalent privacy, essids
* ifup
* Routing tables
* Is samba relevant? Does it really help bridge linux and windows?
* wget vs curl


## Introduction

* Bash = "Bourn again shell"
* \# in examples means logged in as root

## Part 1: Getting Started

### Things to Know about your Command Line

* Everything is a File
  * Running processes, irs, disk drives, all of it!
* Maximum file lengths
  * Linux file names can be up to 255 chrs, but good practice is 80 chars
* Names are Case Sensitive (file, commands, all around)
* Special Characters to avoid in filenames
  * SAFE = numbers, letters, dots, underscores
  * No Nos
    * / (since its used to separate dirs)
    * Dash cannot come at the front of a file name (its interpreted as a flag)
    * {} [] * ? ' " must be escaped to use
  * Not wrong, but don't feel right
    * Characters you need to escape with \\
    * Surround spaces with quotes
* Wildcards
  * Asterisk = match a char 0 or more times
  * Question Mark = matches a single char
  * Brackets = single set of chars, or range of chars
    * rm libby1[12].txt = remove libby11 and libby12

### The Basics

* Good Example for all file types: ls -lF /dev
* List Files and Folders (ls)
  * Works with relative or absolute paths
  * Can combine with wildcards to narrow down results: "ls ~/*.txt" is just text files
  * Recursive LS: "ls -R"
  * LS Results as a column: "ls --format=single-column" or "ls -1"
  * LS Results as a comma separated list: "ls -m"
  * View hidden files with -a
  * Show file types: "ls -F" or "ls -classify". Star means executable, @ is symlink,  = is a socket
  * Color Codes (enable with ls --color)
    * Red = archive
    * Yellow = symlink
    * Use "dircolors --print-database" to see or set mappings for system
  * Permissions, Ownership, etc ("ls - l") for long
    * Order for permissions is Owner, Group, World
    * For a Dir, r=read from dir, w = add files to dir, x is run files from that folder
  * Reverse list (ls -r)
  * Sort files by extension (ls -X)
    * If a file has multiple extensions, then the last one is the one that counts
  * Sort files by date and time (ls -t)
  * Sort files by size (ls -S)
  * Express size in human readable terms: (ls -lSh)
* Directory Navigation and Manipulations
  * Print working directory (pwd)
  * Change Directory (cd)
    * To home {cd ~}
    * To Previous directory (cd -)
  * Touch
    * Change file to current time (touch file.txt). Updates the access and modification times
    * Change to specific time (touch -t [[CC]YY]MMDDhhmm[.ss])
    * Create new empty file
  * mkdir
    * Default permissions for mkdir = rwxr-xr-x
    * Make subdirectory or parent directories: mkdir -p dad/mom/test.txt
    * Use verbose flag to learn about what mkdir is doing
  * Copy cp src destination
    * Copy using wildcards
    * Copy verbosely: -v
    * Get a warning if you're going to overwrite a file with that name already: -i
    * Copy recursively: -R
    * Create archives/backups: -a. This copies out symlinks, copies attributes(owner, timestamp)
  * Move: mv
    * Can move locations of files
    * When moving a dir, go ahead and use mv ambiguiousName/ to indicate dir
    * -i for warning and -v for verbose still apply
    * Rename with mv too
  * Remove Files: rm
    * There's no trash can in Linux
    * Useful flags: wildcards, -v for verbose, -i for warning
  * Remove directory: rmdir
    * rmdir only works on empty dirs
    * rmdir -Rf, recursive force
  * Become another user: su username
    * su stands for switch user, not super user
    * Use whoami to verify that your user has switched
    * Switch users, and switch environment variables to them too: su -l
    * Become root with just: su
    * Get Root's environment variables with: su -

### Learning About Commands

* Man
  * Short for "manual"
  * Man entries have a format: Name, Synopsis, Desription, Options, Files, Author, Bugs, Copyright, See Also
  * To jump a page in the man entry, use "f", backwards is "b"
  * Search on a man page: "/+[searchterm]+enter". Jump forwards/backwards on search with "n" and "ctrl+n
  * Find a command based on keyword, or what it does: "man -k keyword"
    * The command "apropos keyword" also does this search for you
  * Find out what a command does: "man -f command", or --whatis
    * The command "whatis command" also does this
  * Force man to update its database: man -u
  * Man Page Categories
    * Cat 1: General commands (like ls, ch)
    * Cat 2: Low level system calls (like intro, chmod)
    * Cat 3: C Library Functions (beep, HTML parser)
    * Cat 4: Special files (like devices from /dev)
    * Cat 5: File formats
    * Cat 6: Games
    * Cat 7: Misc, like macro packages
    * Cat 8: System administration commands
  * Pull up a specific man page category (not the default lowest on): man [1-8] command
  * Print a Man page: man -
    * Needs extra pipiing to be readable
* Info
  * Info pages are intended to be easier to read
  * Organize their pages into nodes or subnodes
  * When jumping around, the screen may get wonky, so redraw with ctrl+l
  * n for next node, p for previous
  * Press u to jump to the parent of a node
  * Press [ or ] to go next or prev too
  * d for directory node
  * m for menu
  * i to search for titles, s to search for content
* Finding locations or details of files
  * whereis: flags are -b for only binaries, -s for only sources, -m for manpages
  * whatis: gets descriptions of commands. Can use -w flag for wildcards: whatis -w ls*
    * Can use regular expressions if you also use -r flag
  * apropos: find command based on what it does
  * which: find which version of a command will run

### Building Blocks

* Run Several Commands Sequentially with ;
  * Semi colon will run all commands, even if previous ones failed
  * Called Command stacking
  * Executes in sequential order, and waits on termination before proceeding
  * Wait using: "sleep"
  * Run commands only if the last one succeeded: &&
  * Run a command only if the previous one fails: ||
* Plug the output of one command into another command: $()
  * Called Command Substitution
* Input/Output Streams
  * 3 Streams: standardin, standard out, and standard error
  * Each has a file descriptor (0), (1), (2)
  * Using output of one command as input for next: |
    * Redirects Stdout to become stdin for the next command
    * Example: ls | grep myThing
  * Redirect Command output to a file:  >
    * Prevent rewriting over a file with > by doing: set -o noclobber (turn off with set +o noclobber)
    * And if you want to rewrite anyway after that, do it with >|
  * Append content to a file: >>
  * Use file as input to a command: <

## Part 2: Working With Files

### Viewing Files

* Cat to view contents of a file in stdout
  * Can use "less" to view it one bit at a time
    * Can use -N flag to add numbers to less
    * Switch from less to vim by pressing v
    * Set editor to vim with "export EDITOR=vim"
  * Can also concatonate 2 files together to stdout: cat file1 file2
  * Save to a file: cat file1 file2 > file3
  * Cannot have output file also be input file
  * Can number the lines in the output with -n flag: cat -n
  * Concatenate and print files in reverse: tac
* View first 10 lines in stdout: head
  * Can view multiple files at once: head file1 file2
  * Can set specific number of lines to show: head -n 3 file1 file2
  * Can see the first X bytes of a file too: head -c
* View Last 10 lines of a file: tail
  * -n flag to specify number of lines to show
  * Can include several files
  * Tail is great for constantly updated files: tail -f --pid=PID

### Printing and Managing Print Jobs

* lpstat = line printer stat
* lpr = print files to default printer
* lpr -P = specify which printer to print to
* lpq = list print jobs
* lprm = cancel current print job
* lprm - = cancel all print jobs

### Ownerships and Permissions

* Change Group owning file or directories: chgrp
  * By default, you are the file owner and group for any file you make
  * Syntax: chgrp groupName file. Can also use group's id
  * Find group id from /etc/group
  * You can only change group if you are a member of that group
  * Use chgrp -R to change permissions on a dir recursively
  * Use the -v flag for chgrp to see what it is doing
    * -v will report on stuff that did and did not need any changes
  * -c can be used just to get info on the changes
* Change owner of file or directories: chown
  * Find a user's id by checking in /etc/passwd
    * First val = user's id, second val is the main group associated with the user
  * chown can change both user and group at once: chown user:group file
  * chown can change group: chown :group file. There' literally no reason to use chgrp since chown does it all
* Linux Permissions
  * Access Control Lists (ACLs)
  * Abbreviations for Users: u=users, g=group, o=others/everyone else
  * Abbreviations for Permissions: r=read, w=write, x=executable
* Changing ownership: chmod [ugo][+-=][rwx]
  * chmod has numeric and alphabetic options for changing permissions
  * To remove all permissions from a thing, chmod o= file.txt
  * Numeric: chmod[0-7][0-7][0-7]
    * Binary represents the permissions
    * 400 = owner can read, nothing else allowed (100 u 000 g 000 o)
    * 644 = owner and group can read, owner can write and execute (110 100 100)
    * 777 = all read write and execute
    * 000 = no one can do anything, except root
  * Change Permissions recursively -R flag
  * chmod u[+-]sSUID = only a property for executables
    * In ls -l, you may see "s" instead of x in permissions
  * chmod g[+-=]s  GUID = 
  * Sticky Bit: chmod [+-]t
    * Old OS Days: sticky bit indicated that the exe would be used constantly, so keep it in swap space
    * Modern: OS ignores sticky bit on files
    * Uses it on dirs though
    * Example: /tmp directory
    * Useful on a server, not super useful on a single workstation

### Archiving and Compression

* There is a difference between archive and Compression
  * Archive = Take 10 files, combine them into 1, size is the same
  * Compress = Affets the resulting size. Usually smaller, but could be bigger
    * If you compress a compressed file, then it adds extra overhead and makes it bigger
    * Zip is most common compression format. Zip can also achive
    * gzip is a replacement for Unix "compress"
    * bzip2 is newer, meant to replace gzip. Creates smaller files, but works slower
* Archive and Compress with Zip
  * Example: zip [name of dest] [list of files]
  * When here are lost of files, better to zip a dir: zip [name of zipped file][dir name]
  * Adjust level of Compression: zip [0-9], where 0 is no compression at all, 1 is compress quickly. Default is 6
    * Can use -9 all the time. Can do this in .bashrc file: "alias zip=zip -9"
  * Password Protect zip archives: -P(never use), or -e
    * -P is trash, it shows your passwd in plain text on command line history. zip -P 1234 new.zip file.txt
    * -e encrypts the zip and uses a passwd
  * Unzip
    * Can add -v verbose flag
    * List files in zip without unzipping it
    * Test an unzip in case it is corrupted: unzip -t
      * Should use -t for every unzip
* Gzip
  * Difference between zip and gzip: zip leaves the original files behind, gzip replaces it
  * You can get the zipped output and leave the OG behind with: zip -c myZip.txt < file.gz
  * gzip does not work recursively by default, need to use -r for a dir
  * Can use levels 0-9 for adjusting compression too, default is 6
  * Unzip with gunzip: replaces original gzip file unless you use gunzip -c thing.gz > file.txt
    * Instead of gunzip, you could also use "gzip -d" for decompress
  * Can test with -t
* Bzip2
  * Very similar behavior to gzip. Replaces original files, has similar flags
  * Bunzip2 or bzip2 -d to unzip
* Archive files with tar -cf
  * tar does not compress, it only archives
  * Create flag: -c
  * File flag: -f
  * Size of the tarball will be the sum of the file sizes, plus a bit for overhead
  * Tar leaves the original files behind (like zip)
* Archive and Compress with tar -zcvf
  * verbose, gzip, create, files
  * Test untar with tar -zvtf
    * -f needs to be last because you specify the name of the tar.gz file
* Untar and uncompress tar -zxcf
  * x = extract
  * If untaring a bzip, then -jxvf

## Part 3: Finding Stuff

### Finding Stuff: easy

* locate
  * Searches DB of filenames and dirs
  * slocate = secure locate, probably symlinked with locate
  * Search while ignoring case: locate -i
  * Show first n results: locate -n 25 keyword
  * locate updates its DB regularly, but will miss recently added files. Run updatedb to update the db for locate to search in
* grep
  * Grep has several versions
    * grep for basic regular expressions
    * egrep for extended regular expressions
    * fgrep for fixed strings. Allows multiple search terms
    * grep -P for perl regular expressions
  * Big difference between sinlge (good) quotes and double for regex. Double quotes means you're using shell vars
  * Search recursively = grep -R, which follows symlinks
  * Ignore case: grep -i
  * Search for whole words only: grep -w
  * Show line numbers: grep -n
  * Search output of other commands: ls -l | grep thing
  * Search with context: -A = after context, -B= before context, -C= both contexts
  * Show lines where word does not appear: grep -v
  * Get List of results: grep -l

### The Find command

* Find
  * grep looks in files, locate looks based on a DB, and find looks live
  * find -name
    * Automatically recursive
    * Looks for exact matches, so you need wildcards and quotes
  * find -print; on by default
  * find -user: find files by ownership
    * To find files not owned by someone: find ! -user scott
  * find -group
  * find -size +10M
    * Default is bytes, so specify your units
    * b=blocks of bytes (default), c=bytes, k=kilobytes, M=Megabytes, G=gigabytes
    * Default searches for exact match; add + or - for more/less than given size
  * find -type
    * f=file, d=dir, l=symlink, b=block,c=char,p=fifo, s=socket
  * find -a; show results if expressions are true, AND
    * Combine multiple flags together: find -name *myFile* -a -type f
  * find -o; show results if either condition is true
  * find -exec: execute a command on every found file
  * find -fprint; print find results to a file
* Count results with: wc -l

## Part 4: Your Environment

### Your Shell

* History
  * .bash_history file is present in home dir, holds last 500 lines
  * !! = run last command again, referencing history file
  * ![##] = Run previous command using numbers
    * Uses line num from history file
  * ![string]
    * Runs most recent run matching chars from command
* Alias
  * Stored in .bash_rc or .bash_aliases
  * "alias" shows all aliases for machine
  * Create new temporary alias: alias newterm='[command]'
  * Make it permanent by adding it to the bashrc/bashalias, and then reloas with " . .bash_alias"
  * Remove an alias: unalias, works temporary unless you modify the bashrc

### Monitoring System Resources

* ps = Snapshot of current processes
  * ps aux; a=all users, u=user oriented, x= without controlling terminal screens
  * STAT column: R=running, S=sleping, T=stopped, Z=zombie
  * View process tree: ps axjf
    * Shows which processes have spawned others
    * Shows parent id
  * View processes owned by a specific user: ps U [username]
  * End a running process: kill [PID]
    * Can modify the timing and intensity of the kill
    * -15 = terminate gracefully, default
    * -9 = die now
    * -1 = shut down
* top = Dynamic list of running processes
  * can kill a program from top: press k, then enter the pid
* lsof = List open files
  * Thousands of results
  * lsof -u = Files from a particular user
  * lsof [file] = See who is using a specific file
  * lsof -c = list processes for a specific program
* free = show memory
  * -k is default, kilobytes
  * -b id bytes
  * -m is megabytes
* df = File system disk usage
  * -h for human readable
  * tmpfs
* du = File space used by a directory
  * cd into dir, then run du
  * Last line gives overall total
  * -s flag for the total space

### Installing Software

* Intro
  * Deb (ububtu) and RPM (red hat) packages dominate the SW world
* RPM
  * rpm -ihv or -Uhv [package]
  * -e for remove
  * yum install for distributions
  * apt handles this for debian
* Debian
  * dpkg -i = install
  * apt is like a wrapper around dpkg
  * dpkg -r [package] = remove
  * apt-get install [package]
    * apt handles dependency installation
  * apt-get update
    * looks to apt servers, found at /etc/apt/sources.list
  * apt-get remove
  * apt-get --purge remove [pkg], removes configuration files too
  * apt-get upgrade = runs upgrade for packages, use with caution
  * apt-cache search = lists pkgs available
  * apt-get clean
    * deb files are left in /var/cache/apt/archives after install
    * takes up space, so this cleans it
  * apt-get -f install = fix broken dependencies

## Part 5: Networking

### Connectivity

* ifconfig
  * Stands for interface configuration
  * -a for all
  * ath0 is a wireless card
    * Wireless PCMCIA card
    * eth1 would be a secondary interface
    * Could also show up as wlan0 for a wireless card
  * eth0 is a ethernet card
    * Plug in physical cables
  * lo is a loopback interface
    * allows machine to refer to itself, 127.0.0.1
  * Configure a network interface
    * To change ip adddr for an ethernet card eth0, ifconfig eth0 [new addr]
* iwconfig = View staus of wireless network interfaces
  * Can also configure them too
  * ESSID: extended service set identifier
* ping = Verify that the computer is running and accepting requests
  * ping -c  = stop after x replies
* traceroute = Trace the route packets take between two hosts
  * *** indicates a 5 s timeout at the hop
  * Can increase hops tried with -m
  * mtr is better alternative to traceroute
* host
  * Performs DNS lookups
* dhclient
  * Grab a new address using DHCP
* ifup
  * Make a network connection active
  * Note that its silent, use with ifconfig to see differences
* ifdown = bring network connection down
* route
  * Display IP routing table
* Troubleshooting network problems

### Working on the Network

* ssh
  * Avoid a password  with ssh-keygen -t dsa
* sftp
  * Securely transfer files between machines
* scp = Securely copy files between hosts
* rsync -v = Securely transfer and back up files  
* wget = download files or websites non-interactively
* curl = doenload sequential files and internet resources

### Windows Networking

* Samba
* Windows workgroup
* samba shares
* Samba bridges linux and windows environments
