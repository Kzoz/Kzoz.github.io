#include <iostream>

int main() {
  
  int power = 9000;
  int &pow = power;
  
  // Print power
  std::cout << &power << "\n";
  std::cout <<pow<<"\n";
  std::cout <<&pow<<"\n";
  
  // Print &power
  
  
}
// notice that the variable power and its reference pow are stored in the same address