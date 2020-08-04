CXX := g++
CFLAGS := -std=c++98 -Wall -Wextra -Wpedantic -Iinclude

all: bin/exe

clean:
	rm -f obj/* bin/*

#########
## obj ##
#########

obj/main.o: src/main.cpp
	$(CXX) $(CFLAGS) -c -o obj/main.o src/main.cpp


#########
## bin ##
#########

bin/exe: obj/main.o
	$(CXX) $(CFLAGS) -o bin/exe obj/main.o
