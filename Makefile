CXX = g++
CXXFLAGS = -std=c++11 -fPIC -shared
PYTHON = python3
LIBNAME = libthreebodyproblem

ifeq ($(OS),Windows_NT)
    LIBFILE = $(LIBNAME).dll
else
    UNAME_S := $(shell uname -s)
    ifeq ($(UNAME_S),Linux)
        LIBFILE = $(LIBNAME).so
    endif
    ifeq ($(UNAME_S),Darwin)
        LIBFILE = $(LIBNAME).dylib
    endif
endif

PYTHONFILE = threeBodyProblem.py

all: $(LIBFILE)

$(LIBFILE): gravity.cpp
	$(CXX) $(CXXFLAGS) -o $(LIBFILE) gravity.cpp

run: $(LIBFILE)
	$(PYTHON) $(PYTHONFILE)

clean:
	rm -f $(LIBFILE)

.PHONY: all run clean