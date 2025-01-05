# Linux Phrasebook

Author: Scott Granneman
Publication Year: 2006

## Look Up Later

* KDE
* "Bourn again shell" where did that come from
* lsof command
* MS-DOS
* FIFO as | from ls -F options, and = as socket
* Linux hard vs soft links

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



### Learning About Commands

### Building Blocks

## Part 2: Working With Files

### Viewing Files

### Printing and Managing Print Jobs

### Ownerships and Permissions

### Archiving and Compression

## Part 3: Finding Stuff

### Finding Stuff: easy

### The Find command

## Part 4: Your Environment

### Your Shell

### Monitoring System Resources

### Installing Software

## Part 4: Networking

### Connectivity

### Working on the Network

### Windows Networking