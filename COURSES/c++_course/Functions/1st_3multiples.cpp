#include <iostream>
#include <vector>

std::vector<int> first_three_multiples(int num) {
    std::vector<int> lst;
    for (int i = num; i<= num*3; i++){
        if (i%num == 0){
            lst.push_back(i);
        }
    }
    return lst;

}
int main()
{
    for (int element:first_three_multiples(8)) {
        std::cout<< element << "\n";
    }
    
}