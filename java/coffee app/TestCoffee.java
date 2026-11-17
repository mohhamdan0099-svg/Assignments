public class TestCoffee {
    public static void main(String[] args) {
        CoffeeKiosk kiosk = new CoffeeKiosk();

        // Add menu items
        kiosk.addMenuItem("banana", 2.00);
        kiosk.addMenuItem("coffee", 1.50);
        kiosk.addMenuItem("latte", 4.50);
        kiosk.addMenuItem("cappuccino", 3.00);
        kiosk.addMenuItem("muffin", 4.00);

        // Run the interactive order prompt
        kiosk.newOrder();
    }
}