/*
Attributes, also known as member data, consist of information about an instance of the class.
Methods, also known as member functions, are functions that you can use with an instance of the class. 
We use a . before method names to distinguish them from regular functions.

Unless we have a mostly empty class, it’s common to split function declarations from definitions. 
We declare methods inside the class (in a header), then define the methods 
outside the class (in a .cpp file of the same name).

How can we define methods outside a class? We can do this using ClassName:: before the method name 
to indicate its class like this:

int City::get_population() {
  return population;
}
Unlike with regular functions, we need to include the header file in the .cpp file where 
we define the methods.

Note: We must declare a method inside the class if we want to define it outside.
*/
#include "song.hpp"

// add Song method definitions here:
void Song::add_title(std::string new_title){
  title = new_title;
}
std::string Song::get_title(){
  return title;
}

void Song::add_artist(std::string new_artist){
  artist = new_artist;
}
std::string Song::get_artist(){
  return artist;
}