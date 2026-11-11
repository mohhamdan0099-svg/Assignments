// import java.util.Scanner;
import java.util.Random;

public class BankAcc {
  	// Scanner scanner = new Scanner(System.in); 
		Random random = new Random();
 		
	    // MEMBER VARIABLES
	    private double checkingBalance;
	    private double savingsBalance;

			private String accountNum;

	    private static int accounts;
	    private static double totalMoney; // refers to the sum of all bank account checking and savings balances

	    // CONSTRUCTOR
	    // Be sure to increment the number of accounts
      
	    BankAcc(double checkingBalance, double savingsBalance){
        this.checkingBalance = checkingBalance;
	    	this.savingsBalance = savingsBalance;
				this.accountNum = setAccountNum();
        allAccounts();
	    }

			private String setAccountNum(){
				String accountNum = "";
				for (int i = 0; i < 10; i++){
					accountNum += (random.nextInt(0, 10));
				}
				return accountNum;
			};

			public String getAccNum(){
				return accountNum;
			}
      
      public void allAccounts(){
        accounts++;
      }
	    // GETTERS
	    // for checking, savings, accounts, and totalMoney
	    public double getChecking() {
	    	return checkingBalance;
	    }
	    public double getSaving() {
	    	return savingsBalance;
	    }
	    public static int getAccounts() {
	    	return accounts;
	    }
	    public double getTotalmoney() {
	    	return totalMoney;
	    }
	    
      
	    // METHODS
	    // deposit
	    // - users should be able to deposit money into their checking or savings account
	    public double deposit(boolean checkingOrSaving, double money) {
        // true is checking, false is savings
        if (checkingOrSaving) {
          checkingBalance += money;
          return checkingBalance;
        }
        else{
          savingsBalance += money;
          return savingsBalance;
        }
	    }
	    
	    
	    // withdraw 
	    // - users should be able to withdraw money from their checking or savings account
	    // - do not allow them to withdraw money if there are insufficient funds
	    // - all deposits and withdrawals should affect totalMoney
      	public double withdraw(boolean checkingOrSaving, double money) {
          // true is checking, false is savings
        if (checkingOrSaving) {
          if (checkingBalance < money){
            System.out.println("insufficient funds in your Checking Account.");
            return checkingBalance;
          }else{
            checkingBalance -= money;
            return checkingBalance;
          }
        }
        else{
          if (savingsBalance < money){
            System.out.println("insufficient funds in your Savings Account.");
            return savingsBalance;
          }else{
            savingsBalance -= money;
            return savingsBalance;
          }
        }
	    }

	    // getBalance
	    // - display total balance for checking and savings of a particular bank account
      public double getBalance() {
        totalMoney = checkingBalance + savingsBalance;
	        return totalMoney;
	}

			// Ninja Bonus #1



}