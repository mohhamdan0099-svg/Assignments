import java.util.ArrayList;
import java.util.Scanner;

class Item {
    public int index;
    public String name;
    public double price;

    public Item(int index, String name, double price) {
        this.index = index;
        this.name = name;
        this.price = price;
    }
}

class Order {
    public String customerName;
    public ArrayList<Item> items = new ArrayList<Item>();

    public Order(String customerName) {
        this.customerName = customerName;
    }
}

class CoffeeKiosk {
    public ArrayList<Item> menu = new ArrayList<Item>();
    public ArrayList<Order> orders = new ArrayList<Order>();

    public void addMenuItem(String name, double price) {
        Item item = new Item(menu.size(), name, price);
        menu.add(item);
    }

    public void displayMenu() {
        for (Item item : menu) {
            System.out.printf(
                "%d %s -- $%.2f%n",
                item.index,
                item.name,
                item.price
            );
        }
    }

    public void newOrder(Scanner scanner) {
        System.out.println("Please enter customer name:");
        String name = scanner.nextLine();
        Order order = new Order(name);

        displayMenu();
        System.out.println(
            "Please enter a menu item index or q to finish:"
        );
        String choice = scanner.nextLine();

        while (!choice.equals("q")) {
            int itemIndex = Integer.parseInt(choice);
            Item selectedItem = menu.get(itemIndex);
            order.items.add(selectedItem);

            System.out.println("Added: " + selectedItem.name);
            System.out.println(
                "Please enter a menu item index or q to finish:"
            );
            choice = scanner.nextLine();
        }

        orders.add(order);

        double total = 0.0;
        System.out.println("Order for " + order.customerName + ":");

        for (Item item : order.items) {
            System.out.printf(
                "%s - $%.2f%n",
                item.name,
                item.price
            );
            total += item.price;
        }

        System.out.printf("Total: $%.2f%n", total);
    }
}

public class CafeJavaApp {
    public static void main(String[] args) {
        CoffeeKiosk kiosk = new CoffeeKiosk();

        kiosk.addMenuItem("banana", 2.00);
        kiosk.addMenuItem("coffee", 1.50);
        kiosk.addMenuItem("latte", 4.50);
        kiosk.addMenuItem("cappuccino", 3.00);
        kiosk.addMenuItem("muffin", 4.00);

        Scanner scanner = new Scanner(System.in);

        System.out.println("Welcome to Cafe Java!");
        System.out.println(
            "Press Enter to create an order or q to exit:"
        );
        String command = scanner.nextLine();

        while (!command.equals("q")) {
            kiosk.newOrder(scanner);

            System.out.println(
                "Press Enter to create another order or q to exit:"
            );
            command = scanner.nextLine();
        }

        System.out.println("Goodbye!");
        scanner.close();
    }
}