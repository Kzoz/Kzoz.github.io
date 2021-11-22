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

int atm::mainmenu(){
    std::cout<<"Welcome to XYZ Bank! \n Select an option below. \n";
    std::cout<<"1. Deposit \n";
    std::cout<<"2. Withdrawal \n";
    std::cout<<"3. Balance \n";
    std::cout<<"4. Exit \n";
    int usr_option;
    std::cin>>usr_option;
    if (usr_option <=0 or usr_option >=5)
    {    
        std::cout<<"Incorrect choice, please try again! \n";
        exit(1);
        
    } else {
        return usr_option;
    }
    
}

void atm::checkbalance(){
    std::cout<<"BALANCE\n";
    atm::enterpasscode();
    std::cout <<"Your balance is: ¥"<<mybalance<<"\n";
    //atm::mainmenu();
    
  
}
void atm::withdrawal(){
    std::cout<<"WITHDRAWAL \n";
    atm::enterpasscode();
    int deduct;
    std::cout<<"Please select the withdrawal amount: \n ¥";
    std::cin>>deduct;
    mybalance-=deduct;
    std::cout<<"\nYou have withdrawn ¥ "<<deduct<<" from your account. \n";
    std::cout<<"\nYour new balance is ¥"<<mybalance<<".\n";
    //atm::mainmenu();
    
}

void atm::deposit(){
    std::cout<<"DEPOSIT\n";
    int new_balance;
    std::cout<<"Enter the sum: \n  ¥";
    std::cin>>new_balance;
    mybalance += new_balance;
    std::cout<<"\nYou have added ¥ "<<new_balance<<" to your account. \n";
    std::cout<<"\nYour new balance is ¥"<<mybalance<<".\n";
    //atm::mainmenu();
    
}

void atm::exitprg(){
    std::cout<<"\nThank you for using our service.\n";
    exit(1);
}

