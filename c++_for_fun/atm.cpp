#include <iostream>
#include "atm.hpp"
#include <cstdlib>

int atm::enterpasscode(){
    int enter_pass;
    int count = 3;
    std::cout<<"Please input your password: \n";
    for (int i = 0; i < count; i++)
    {      
        std::cin>>enter_pass;
        if (enter_pass != mypasscode)
        {
            if (i>=count-1)
            {
                std::cout<<"We cannot process your request at this time. \nFor more information, contact your financial institution. \n\n\n";
                exit(1);
            }
            std::cout<<"Incorrect password. Try again! \n";
        } else {
            break;
        }
        
    }
    
}

void atm::checkbalance(){
    std::cout<<"BALANCE\n";
    atm::enterpasscode();
    std::cout <<"Your balance is: ¥"<<mybalance<<"\n";
    
  
}

void atm::deposit(){
    std::cout<<"DEPOSIT\n";
    int new_balance;
    std::cout<<"Enter the sum: \n  ¥";
    std::cin>>new_balance;
    mybalance += new_balance;
    std::cout<<"\nYou have added ¥ "<<new_balance<<" to your account. \n";
    std::cout<<"\nYour new balance is ¥"<<mybalance<<".\n";
    
}