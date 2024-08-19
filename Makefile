CXX = g++
CXXFLAGS = -std=c++11 -fPIC -shared
PYTHON = python3
LIBNAME = libthreebodyproblem
LIBFILE = $(LIBNAME).so
PYTHONFILE = threeBodyProblem.py

all: $(LIBFILE)

$(LIBFILE): gravity.cpp
	$(CXX) $(CXXFLAGS) -o $(LIBFILE) gravity.cpp

run: $(LIBFILE)
	$(PYTHON) $(PYTHONFILE)

clean:
	rm -f $(LIBFILE)

.PHONY: all run clean