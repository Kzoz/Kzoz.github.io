class atm
{
    
private:
    int mybalance= 3000;
    int mypasscode = 1234;
    std::string customer;
    
public:
    int mainmenu();
    void checkbalance();
    void deposit();
    void withdrawal();
    int enterpasscode();
    void transfer(atm aite);
    void exitprg();
};


// 
//