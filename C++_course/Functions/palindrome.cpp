#include <iostream>
#include <algorithm>
#include <string>

bool is_palindrome(std::string text){
    std::string revs = text;
    std::reverse(revs.begin(), revs.end());
    if (text == revs)
    {
        return true;
    } else
    {
        return false;
    }
}

int main(int argc, char const *argv[])
{
    std::cout<< is_palindrome("madam") << "\n";
    std::cout<< is_palindrome("ada") << "\n";
    std::cout<< is_palindrome("lovelace") << "\n";
    return 0;
}
