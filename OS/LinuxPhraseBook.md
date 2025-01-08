# Linux Phrasebook

Author: Scott Granneman
Publication Year: 2006

## Look Up Later

* Sam's Teach yourself regular expressions in 10 minutes by Ben Forta
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
* Changing ownership: chmod
  * 

### Archiving and Compression

## Part 3: Finding Stuff

### Finding Stuff: easy

### The Find command

## Part 4: Your Environment

### Your Shell

### Monitoring System Resources

### Installing Software

## Part 5: Networking

### Connectivity

### Working on the Network

### Windows Networking