public class BankTest {
  public static void main(String[] args) {

    BankAcc Moh = new BankAcc(0, 0);
    BankAcc Emil = new BankAcc(0, 0);
    BankAcc Sajeda = new BankAcc(0, 0);

    System.out.println(Moh.deposit(false, 100));
    System.out.println(Emil.deposit(true, 1000));
    System.out.println(Sajeda.deposit(false, 10));
    System.out.println(Sajeda.withdraw(false, 100));

    System.out.println(Emil.getAccNum());


    
  System.out.println(BankAcc.getAccounts());
    
  }
}