public class CafeJava {
    public static void main(String[] args) {
        // APP VARIABLES
        // Lines of text that will appear in the app. 
        String generalGreeting = "Welcome to Cafe Java, ";
        String pendingMessage = ", your order will be ready shortly";
        String readyMessage = ", your order is ready";
        String displayTotalMessage = "Your total is $";
        
        // Menu variables (price added for drip coffee, latte, and cappuccino)
        double mochaPrice = 4.5;
        double dripCoffeePrice = 6.5;
        double lattePrice = 5.5;
        double cappuccinoPrice = 3.5;
    
        // Customer name variables
        String customer1 = "Shatha"; // Kept Shatha or you can use Sali
        String customer2 = "Ahmad";
        String customer3 = "Sali";
        String customer4 = "Adam";

        // Order completions (booleans)
        boolean isReadyOrder1 = false;
        boolean isReadyOrder2 = true;
        boolean isReadyOrder3 = false;
        boolean isReadyOrder4 = true;
    
        // APP INTERACTION SIMULATION
        // 1. Display general greeting for customer 1
        System.out.println(generalGreeting + customer1); 

        // 2. Sali ordered a coffee. Print status message.
        // Assuming Sali is customer3 and ordered a drip coffee
        System.out.println(customer3 + pendingMessage);

        // 3. Ahmad ordered a cappuccino. Use an if statement to check order status and print total.
        if (isReadyOrder2) {
            System.out.println(customer2 + readyMessage);
            System.out.println(displayTotalMessage + cappuccinoPrice);
        } else {
            System.out.println(customer2 + pendingMessage);
        }

        // 4. Sali just ordered 2 lattes. Print total message and order status.
        System.out.println(customer3 + displayTotalMessage + (lattePrice * 2));
        if (isReadyOrder3) {
            System.out.println(customer3 + readyMessage);
        } else {
            System.out.println(customer3 + pendingMessage);
        }

        // 5. Adam just realized he was charged for a coffee but had ordered a latte. 
        // Print total message with the new calculated total (what he owes for the difference).
        System.out.println(customer4 + ", " + displayTotalMessage + (lattePrice - dripCoffeePrice)); // or difference calculation
    }
}