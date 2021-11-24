#include <string>

// add the Song class here:
class Song{
  std::string title;
  std::string artist;

  public:
  void add_title(std::string new_title);
  std::string get_title();
  void add_artist(std::string new_artist);
  std::string get_artist();
};