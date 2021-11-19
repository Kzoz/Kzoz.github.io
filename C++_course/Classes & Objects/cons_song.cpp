#include "song.hpp"

// add the Song constructor here:



std::string Song::get_title() {

  return title;

}


Song::Song(std::string new_title, std::string new_artist){
  title = new_title;
  artist = new_artist;
}

std::string Song::get_artist() {

  return artist;

}