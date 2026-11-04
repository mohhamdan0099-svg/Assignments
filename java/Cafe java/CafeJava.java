public class CafeJava {
    public static void main(String[] args) {
        // APP VARIABLES
        // Lines of text that will appear in the app. 
        String generalGreeting = "Welcome to Cafe Java, ";
        String pendingMessage = ", your order will be ready shortly";
        String readyMessage = ", your order is ready";
        String displayTotalMessage = "Your total is $";
        String wrongOrder = ", Sorry, this is not your order, ";
        
        
        double mochaPrice = 4.5;
        double dripCoffee = 6.5;
        double latte = 5.5;
        double cappuccino = 3.5;
    
        
        String customer1 = "Sali";
        String customer2 = "Ahmad";
        String customer3 = "Adam";

    
        
        boolean isReadyOrder1 = true;
        boolean isReadyOrder2 = true;
        boolean isReadyOrder3 = true;
    
        
        System.out.println(generalGreeting + customer1); 

        System.out.println(customer1 + pendingMessage);

        if (isReadyOrder2){
            System.out.println(customer2 + readyMessage);
            System.out.println(displayTotalMessage + cappuccino);
            }
            

        
        
        if (isReadyOrder1){
            System.out.println(customer1 + readyMessage);
            System.out.println(customer1 + displayTotalMessage + (latte + latte));
            }
        

        System.out.println(customer3 + wrongOrder + displayTotalMessage + (dripCoffee - latte));
        
    }
}