import java.util.ArrayList;

public class CoffeeKiosk {
    private ArrayList<Item> menu;
    private ArrayList<Order> orders;

    // Constructor - initializes menu and orders to empty arrays
    public CoffeeKiosk() {
        this.menu = new ArrayList<Item>();
        this.orders = new ArrayList<Order>();
    }

    // Method to add a menu item
    public void addMenuItem(String name, double price) {
        Item newItem = new Item(name, price);
        int currentIndex = this.menu.size();
        newItem.setIndex(currentIndex);
        this.menu.add(newItem);
    }

    // Method to display the menu
    public void displayMenu() {
        for (Item item : this.menu) {
            System.out.println(item.getIndex() + " " + item.getName() + " -- $" + item.getPrice());
        }
    }

    // Method to create a new order interactively from the terminal
    public void newOrder() {
        // Shows the user a message prompt and sets their input to a variable
        System.out.println("Please enter customer name for new order:");
        String name = System.console().readLine();
        
        // Create a new order with the given input string
        Order order = new Order(name);
        
        // Show the user the menu, so they can choose items to add
        displayMenu();
        
        // Prompts the user to enter an item number
        System.out.println("Please enter a menu item index or q to quit:");
        String itemNumber = System.console().readLine();
        
        // Write a while loop to collect all user's order items
        while (!itemNumber.equals("q")) {
            try {
                // Parse the string input to an integer index
                int index = Integer.parseInt(itemNumber);
                
                // Check if the index is valid within menu bounds
                if (index >= 0 && index < menu.size()) {
                    Item selectedItem = menu.get(index);
                    order.addItem(selectedItem);
                    System.out.println("Added: " + selectedItem.getName());
                } else {
                    System.out.println("Invalid menu index. Please try again.");
                }
            } catch (NumberFormatException e) {
                System.out.println("Invalid input. Please enter a valid number index or 'q'.");
            }
            
            // Ask them to enter a new item index or q again, and take their input
            System.out.println("Please enter a menu item index or q to quit:");
            itemNumber = System.console().readLine();
        }
        
        // After collecting their order, add it to orders array and print details
        this.orders.add(order);
        System.out.println("\n--- Order Summary ---");
        order.display();
    }
}