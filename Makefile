# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 3.14

# Default target executed when no arguments are given to make.
default_target: all

.PHONY : default_target

# Allow only one "make -f Makefile2" at a time, but pass parallelism.
.NOTPARALLEL:


#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canonical targets will work.
.SUFFIXES:


# Remove some rules from gmake that .SUFFIXES does not remove.
SUFFIXES =

.SUFFIXES: .hpux_make_needs_suffix_list


# Suppress display of executed commands.
$(VERBOSE).SILENT:


# A target that is always out of date.
cmake_force:

.PHONY : cmake_force

#=============================================================================
# Set environment variables for the build.

# The shell in which to execute make rules.
SHELL = /bin/sh

# The CMake executable.
CMAKE_COMMAND = /home/chanceygardener/Applications/clion-2019.2/bin/cmake/linux/bin/cmake

# The command to remove a file.
RM = /home/chanceygardener/Applications/clion-2019.2/bin/cmake/linux/bin/cmake -E remove -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = /home/chanceygardener/repos/proto_embed

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /home/chanceygardener/repos/proto_embed

#=============================================================================
# Targets provided globally by CMake.

# Special rule for the target rebuild_cache
rebuild_cache:
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --cyan "Running CMake to regenerate build system..."
	/home/chanceygardener/Applications/clion-2019.2/bin/cmake/linux/bin/cmake -S$(CMAKE_SOURCE_DIR) -B$(CMAKE_BINARY_DIR)
.PHONY : rebuild_cache

# Special rule for the target rebuild_cache
rebuild_cache/fast: rebuild_cache

.PHONY : rebuild_cache/fast

# Special rule for the target edit_cache
edit_cache:
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --cyan "No interactive CMake dialog available..."
	/home/chanceygardener/Applications/clion-2019.2/bin/cmake/linux/bin/cmake -E echo No\ interactive\ CMake\ dialog\ available.
.PHONY : edit_cache

# Special rule for the target edit_cache
edit_cache/fast: edit_cache

.PHONY : edit_cache/fast

# The main all target
all: cmake_check_build_system
	$(CMAKE_COMMAND) -E cmake_progress_start /home/chanceygardener/repos/proto_embed/CMakeFiles /home/chanceygardener/repos/proto_embed/CMakeFiles/progress.marks
	$(MAKE) -f CMakeFiles/Makefile2 all
	$(CMAKE_COMMAND) -E cmake_progress_start /home/chanceygardener/repos/proto_embed/CMakeFiles 0
.PHONY : all

# The main clean target
clean:
	$(MAKE) -f CMakeFiles/Makefile2 clean
.PHONY : clean

# The main clean target
clean/fast: clean

.PHONY : clean/fast

# Prepare targets for installation.
preinstall: all
	$(MAKE) -f CMakeFiles/Makefile2 preinstall
.PHONY : preinstall

# Prepare targets for installation.
preinstall/fast:
	$(MAKE) -f CMakeFiles/Makefile2 preinstall
.PHONY : preinstall/fast

# clear depends
depend:
	$(CMAKE_COMMAND) -S$(CMAKE_SOURCE_DIR) -B$(CMAKE_BINARY_DIR) --check-build-system CMakeFiles/Makefile.cmake 1
.PHONY : depend

#=============================================================================
# Target rules for targets named probed

# Build rule for target.
probed: cmake_check_build_system
	$(MAKE) -f CMakeFiles/Makefile2 probed
.PHONY : probed

# fast build rule for target.
probed/fast:
	$(MAKE) -f CMakeFiles/probed.dir/build.make CMakeFiles/probed.dir/build
.PHONY : probed/fast

src/fake_task/fake_task.o: src/fake_task/fake_task.cc.o

.PHONY : src/fake_task/fake_task.o

# target to build an object file
src/fake_task/fake_task.cc.o:
	$(MAKE) -f CMakeFiles/probed.dir/build.make CMakeFiles/probed.dir/src/fake_task/fake_task.cc.o
.PHONY : src/fake_task/fake_task.cc.o

src/fake_task/fake_task.i: src/fake_task/fake_task.cc.i

.PHONY : src/fake_task/fake_task.i

# target to preprocess a source file
src/fake_task/fake_task.cc.i:
	$(MAKE) -f CMakeFiles/probed.dir/build.make CMakeFiles/probed.dir/src/fake_task/fake_task.cc.i
.PHONY : src/fake_task/fake_task.cc.i

src/fake_task/fake_task.s: src/fake_task/fake_task.cc.s

.PHONY : src/fake_task/fake_task.s

# target to generate assembly for a file
src/fake_task/fake_task.cc.s:
	$(MAKE) -f CMakeFiles/probed.dir/build.make CMakeFiles/probed.dir/src/fake_task/fake_task.cc.s
.PHONY : src/fake_task/fake_task.cc.s

src/freqdist/freqdist.o: src/freqdist/freqdist.cc.o

.PHONY : src/freqdist/freqdist.o

# target to build an object file
src/freqdist/freqdist.cc.o:
	$(MAKE) -f CMakeFiles/probed.dir/build.make CMakeFiles/probed.dir/src/freqdist/freqdist.cc.o
.PHONY : src/freqdist/freqdist.cc.o

src/freqdist/freqdist.i: src/freqdist/freqdist.cc.i

.PHONY : src/freqdist/freqdist.i

# target to preprocess a source file
src/freqdist/freqdist.cc.i:
	$(MAKE) -f CMakeFiles/probed.dir/build.make CMakeFiles/probed.dir/src/freqdist/freqdist.cc.i
.PHONY : src/freqdist/freqdist.cc.i

src/freqdist/freqdist.s: src/freqdist/freqdist.cc.s

.PHONY : src/freqdist/freqdist.s

# target to generate assembly for a file
src/freqdist/freqdist.cc.s:
	$(MAKE) -f CMakeFiles/probed.dir/build.make CMakeFiles/probed.dir/src/freqdist/freqdist.cc.s
.PHONY : src/freqdist/freqdist.cc.s

src/main.o: src/main.cc.o

.PHONY : src/main.o

# target to build an object file
src/main.cc.o:
	$(MAKE) -f CMakeFiles/probed.dir/build.make CMakeFiles/probed.dir/src/main.cc.o
.PHONY : src/main.cc.o

src/main.i: src/main.cc.i

.PHONY : src/main.i

# target to preprocess a source file
src/main.cc.i:
	$(MAKE) -f CMakeFiles/probed.dir/build.make CMakeFiles/probed.dir/src/main.cc.i
.PHONY : src/main.cc.i

src/main.s: src/main.cc.s

.PHONY : src/main.s

# target to generate assembly for a file
src/main.cc.s:
	$(MAKE) -f CMakeFiles/probed.dir/build.make CMakeFiles/probed.dir/src/main.cc.s
.PHONY : src/main.cc.s

src/tokenize/tokenize.o: src/tokenize/tokenize.cc.o

.PHONY : src/tokenize/tokenize.o

# target to build an object file
src/tokenize/tokenize.cc.o:
	$(MAKE) -f CMakeFiles/probed.dir/build.make CMakeFiles/probed.dir/src/tokenize/tokenize.cc.o
.PHONY : src/tokenize/tokenize.cc.o

src/tokenize/tokenize.i: src/tokenize/tokenize.cc.i

.PHONY : src/tokenize/tokenize.i

# target to preprocess a source file
src/tokenize/tokenize.cc.i:
	$(MAKE) -f CMakeFiles/probed.dir/build.make CMakeFiles/probed.dir/src/tokenize/tokenize.cc.i
.PHONY : src/tokenize/tokenize.cc.i

src/tokenize/tokenize.s: src/tokenize/tokenize.cc.s

.PHONY : src/tokenize/tokenize.s

# target to generate assembly for a file
src/tokenize/tokenize.cc.s:
	$(MAKE) -f CMakeFiles/probed.dir/build.make CMakeFiles/probed.dir/src/tokenize/tokenize.cc.s
.PHONY : src/tokenize/tokenize.cc.s

src/utils/utils.o: src/utils/utils.cc.o

.PHONY : src/utils/utils.o

# target to build an object file
src/utils/utils.cc.o:
	$(MAKE) -f CMakeFiles/probed.dir/build.make CMakeFiles/probed.dir/src/utils/utils.cc.o
.PHONY : src/utils/utils.cc.o

src/utils/utils.i: src/utils/utils.cc.i

.PHONY : src/utils/utils.i

# target to preprocess a source file
src/utils/utils.cc.i:
	$(MAKE) -f CMakeFiles/probed.dir/build.make CMakeFiles/probed.dir/src/utils/utils.cc.i
.PHONY : src/utils/utils.cc.i

src/utils/utils.s: src/utils/utils.cc.s

.PHONY : src/utils/utils.s

# target to generate assembly for a file
src/utils/utils.cc.s:
	$(MAKE) -f CMakeFiles/probed.dir/build.make CMakeFiles/probed.dir/src/utils/utils.cc.s
.PHONY : src/utils/utils.cc.s

src/wordembedder/wordembedder.o: src/wordembedder/wordembedder.cc.o

.PHONY : src/wordembedder/wordembedder.o

# target to build an object file
src/wordembedder/wordembedder.cc.o:
	$(MAKE) -f CMakeFiles/probed.dir/build.make CMakeFiles/probed.dir/src/wordembedder/wordembedder.cc.o
.PHONY : src/wordembedder/wordembedder.cc.o

src/wordembedder/wordembedder.i: src/wordembedder/wordembedder.cc.i

.PHONY : src/wordembedder/wordembedder.i

# target to preprocess a source file
src/wordembedder/wordembedder.cc.i:
	$(MAKE) -f CMakeFiles/probed.dir/build.make CMakeFiles/probed.dir/src/wordembedder/wordembedder.cc.i
.PHONY : src/wordembedder/wordembedder.cc.i

src/wordembedder/wordembedder.s: src/wordembedder/wordembedder.cc.s

.PHONY : src/wordembedder/wordembedder.s

# target to generate assembly for a file
src/wordembedder/wordembedder.cc.s:
	$(MAKE) -f CMakeFiles/probed.dir/build.make CMakeFiles/probed.dir/src/wordembedder/wordembedder.cc.s
.PHONY : src/wordembedder/wordembedder.cc.s

# Help Target
help:
	@echo "The following are some of the valid targets for this Makefile:"
	@echo "... all (the default if no target is provided)"
	@echo "... clean"
	@echo "... depend"
	@echo "... rebuild_cache"
	@echo "... probed"
	@echo "... edit_cache"
	@echo "... src/fake_task/fake_task.o"
	@echo "... src/fake_task/fake_task.i"
	@echo "... src/fake_task/fake_task.s"
	@echo "... src/freqdist/freqdist.o"
	@echo "... src/freqdist/freqdist.i"
	@echo "... src/freqdist/freqdist.s"
	@echo "... src/main.o"
	@echo "... src/main.i"
	@echo "... src/main.s"
	@echo "... src/tokenize/tokenize.o"
	@echo "... src/tokenize/tokenize.i"
	@echo "... src/tokenize/tokenize.s"
	@echo "... src/utils/utils.o"
	@echo "... src/utils/utils.i"
	@echo "... src/utils/utils.s"
	@echo "... src/wordembedder/wordembedder.o"
	@echo "... src/wordembedder/wordembedder.i"
	@echo "... src/wordembedder/wordembedder.s"
.PHONY : help



#=============================================================================
# Special targets to cleanup operation of make.

# Special rule to run CMake to check the build system integrity.
# No rule that depends on this can have commands that come from listfiles
# because they might be regenerated.
cmake_check_build_system:
	$(CMAKE_COMMAND) -S$(CMAKE_SOURCE_DIR) -B$(CMAKE_BINARY_DIR) --check-build-system CMakeFiles/Makefile.cmake 0
.PHONY : cmake_check_build_system

