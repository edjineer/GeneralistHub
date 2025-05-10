# Professional CMake 

Author: Craig Scott, 2018

## Topics or Exercises to Revisit Later

* Ask the expert: Ninja looks like a single-configuration tool, how do we use it as multi with debug/release?
  * Answer, we re-run cmake. if ninja were a multi-configuration tool, we wouldn't have to re-run
* How to check a system's default generator?
* Static libraries vs dynamic linked or shared libraries
* Linking non-target libraries
* Test on what is a public, private interface
* Test on static, shared, module

## Part 1: Fundamentals

### 1. Intro

* CMake is a suite of tools that cover setting up a build, to producing packages ready for distribution
* Supports range of platforms, tools, and languages

### 2. Setting up a project

* Intro
  * CMakeLists.txt defines what should be built, and how, what tests, what packages to create
  * Projects have both a source and binary directory
  * Binary Dir aka Build dir = where everything produced by CMake is created
  * CMakeCache is used to store info for reuse or subsequent runs
  * Where build directory is in relation to source: either in-source build or out-of-source build
  * Directory Structure Details
    * In-Source Builds
      * Discouraged
      * Where source and build directories are the same
      * Makes version control harder to parse out binaries from sources
      * Difficult to clear out for a new run
    * Out-of-source builds
      * Source and build directories are different, but still under same project root
* Generating Project Files (-G)
  * Pick a project file generator
  * Examples: VS 14/15, XCode, Ninja, Unix Makefile, MSYS Makefiles
  * Some are multi-config (debug, release). Allow a different build config without having to re-run cmake
  * If no -G passed in, it will pick default generator type based on host platform
  * Project file creation involves A.Configuring, and B. generating
* Running the Build Tool
  * --build flag points to build directory
  * --config flag specifies which debug/release to build
  * -- targat to specify target to build
* Recommended Practices
  * Ninja known for efficient builds

### 3. Minimal Project

* Intro
  * Command names in a CMakeLists.txt are case insensitive: ex= AdD_eXeCUTABLE. Typical convention is all lowercase
* Managing CMake Versions
  * Cmake provides policy mechanisms to say "behave like X.Y.Z" through minimum required version
  * Enfoces to match CMake behavior to the specified one
  * VERSION keyword is required
  * 3.2 is the oldest version to consider. Choose most recent you can
* Project() Command
  * Include name, version, and Languages used (C, CXX, Fortran, Java)
* Building a basic Executable
  * add_executable( targetName src1 src2)
* Commenting
  * Use pound for comments #
* Recommended Practices
  * Ensure that every project has required_minimum set first

### 4. Building of Simple Targets

* Executables
  * `add_executable(targetNam, [optional keywords for win32, macosx bundle], [EXCLUDE FROM ALL] source [more sources])`
  * EXCLUDE_FROM_ALL useful to define only a few that NEED to be built
* Defining Libraries
  * `add_library(targetName [STatic, shared, modules] [exclude_from_all] source[s])`
  * STATIC: static library or archive (.a); 
    * does not need any .so or .dll files at runtime. * Self Contained executable
    * Resolved at compile time, so they don't have overhead of linking. Might be larger than shared libraries
  * SHARED: Shared or dynamically linked library (.so)
    * Loaded into memory, linked to an executable at runtime instead of compile time
    * Multiple programs can share a same library
    * Smaller executable size since it is not embedded
    * Does not require recompiling the programs that use it if you update the so
    * so = shared object, dll = dynamic link library
  * MODULE: Like a shared library, but loaded dynamically at run time instead of being linked directly to a library or executable
  * BUILD_SHARED_LIBS sets the default for add_libraries that are not specified
  * At command line, can set by `cmake -DBUILD_SHARED_LIBS=YES /path/to/source`
  * In cmakelists.txt, can set with `set(BUILD_SHARED_LIBS YES)`
* Linking Targets
  * Simple: Lib A needs Lib B, so A is linked to B
  * PRIVATE
    * Lib A uses lib B in internal implementation
  * PUBLIC
    * Lib A uses lib B internally, but also in its interface. A cannot be used without B, so B is dependency of anything that depends on A
  * INTERFACE
    * In order to use libA, parts of lib B need to be used
    * A doesnt need B internally, only uses B in interface
  * `target_link_libraries(targetname P/P/I item1 item2 P/P/I item3)`
* Linking non-targets
  * Link a full path to a library file
  * Link a Plain Library Name
  * Link a flag
* Old-style Cmake
  * Pre 2.8.11
  * Didn't have the interface keyword
* Recommended Practices
  * Target names don'e need to be related to project names, and shouldn't have same names for proj name and executable name
  * Don't start or end names with lib, it gets added automatically on some platforms
  * Avoid prematurely specifying STATIC or SHARED as a keyword until you know you need it
  * Always specify PRIVATE,PUBLIC, INTERFACE. Old style assumed all were public

### 5. Variables

* Variable Basics
* Env Variables
* Cache Variables
* Manipulating Cache Variables
* Debugging Variables and Diagnostics
* String Handling
* Lists
* Math
* Recommended Practices

### 6. Flow Control

### Using Subdirectories

### Functions and Macros

### Properties

### Generator Expressions

### Modules

### Policies

## Part 2: Builds in Depth

## Part 3: The Bigger Picture
