#include <iostream>

int main(int argc, char const *argv[])
{
    for (int i = 0; i < 3; i++)
    {   
        if (i < 2)
        {
            std::cout<<"not yet";
            break;
        } else{

            std::cout<<"okay";
        }
        
    }
    
    return 0;
}
