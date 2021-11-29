#include <iostream>
#include <string>
#include <algorithm>
#include <cstdlib>
#include "atm.hpp"

//add transfer
int main()
{
    atm moussa;
    atm mak;

    while (true)
    {
        int rslt = moussa.mainmenu();
        if (rslt==1)
        {
            moussa.deposit();
        }
        else if (rslt==2)
        {
            moussa.withdrawal();
        }
        else if (rslt ==3)
        {
            moussa.checkbalance();
        } 
        else if (rslt ==4)
        {
            moussa.transfer(mak);
        } 
        else if (rslt == 5)
        {
            moussa.exitprg();
        }
        else {
            std::cout<<"Incorrect input";
        }
    }
}