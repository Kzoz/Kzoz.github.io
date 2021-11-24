// declare pop and make it as a reference to soda using $
// Whatever changes will happen to the reference will also influence the original variable
#include <iostream>

int main() {
  
  int soda = 99;
  int &pop = soda;
  pop += 1;
  std::cout<<soda<<"\n";
  std::cout<<pop;
  
  
}