#include <iostream>
#include <vector>
int main() {

  std::vector<int> nums ={2, 4, 3, 6, 1, 9};

  int even_numbers = 0;
  int odd_numbers = 1;

  for (int i = 0; i < nums.size(); i++) {
    if (nums[i] % 2 == 0){
      even_numbers = even_numbers+nums[i];
    }
    else{
      odd_numbers = odd_numbers*nums[i];
    }
  }

  std::cout<<"Sum of even numbers is "<<even_numbers<<"\n";

  std::cout<<"Product of odd numbers is "<<odd_numbers<<"\n";

}