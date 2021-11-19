#include <iostream>
#include "song.hpp"

int main() {

Song electric_relaxation;

electric_relaxation.add_title("Electric Relaxation");

std::cout<<electric_relaxation.get_title();

}