import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

class Item {
    private int index;
    private String name;
    private double price;

    public Item(int index, String name, double price) {
        if (index < 0) {
            throw new IllegalArgumentException("Index cannot be negative.");
        }
        if (name == null || name.trim().isEmpty()) {
            throw new IllegalArgumentException("Item name cannot be empty.");
        }
        if (price < 0) {
            throw new IllegalArgumentException("Price cannot be negative.");
        }
        this.index = index;
        this.name = name;
        this.price = price;
    }

    public int getIndex() {
        return index;
    }

    public String getName() {
        return name;
    }

    public double getPrice() {
        return price;
    }

    public String formatMenuLine() {
        return String.format("%d %s -- $%.2f", index, name, price);
    }

    public String formatReceiptLine() {
        return String.format("%s - $%.2f", name, price);
    }
}

class Order {
    private String customerName;
    private final List<Item> items;

    public Order(String customerName) {
        this.customerName = (customerName == null || customerName.trim().isEmpty())
                ? "Guest"
                : customerName.trim();
        this.items = new ArrayList<>();
    }

    public String getCustomerName() {
        return customerName;
    }

    public void addItem(Item item) {
        if (item != null) {
            items.add(item);
        }
    }

    public double getOrderTotal() {
        double total = 0.0;
        for (Item item : items) {
            total += item.getPrice();
        }
        return total;
    }

    public void printReceipt() {
        System.out.println("Order for " + customerName + ":");
        for (Item item : items) {
            System.out.println(item.formatReceiptLine());
        }
        System.out.printf("Total: $%.2f%n", getOrderTotal());
    }
}

class CoffeeKiosk {
    private final List<Item> menu;
    private final List<Order> orders;

    public CoffeeKiosk() {
        this.menu = new ArrayList<>();
        this.orders = new ArrayList<>();
    }

    public void addMenuItem(String name, double price) {
        Item item = new Item(menu.size(), name, price);
        menu.add(item);
    }

    public void displayMenu() {
        for (Item item : menu) {
            System.out.println(item.formatMenuLine());
        }
    }

    public void run(Scanner scanner) {
        System.out.println("Welcome to Cafe Java!");
        System.out.println("Press Enter to create an order or q to exit:");
        String command = scanner.nextLine();

        while (!command.equals("q")) {
            newOrder(scanner);

            System.out.println("Press Enter to create another order or q to exit:");
            command = scanner.nextLine();
        }

        System.out.println("Goodbye!");
    }

    public void newOrder(Scanner scanner) {
        Order order = createOrderFromPrompt(scanner);
        displayMenu();
        collectOrderItems(scanner, order);
        orders.add(order);
        order.printReceipt();
    }

    private Order createOrderFromPrompt(Scanner scanner) {
        System.out.println("Please enter customer name:");
        String name = scanner.nextLine();
        return new Order(name);
    }

    private void collectOrderItems(Scanner scanner, Order order) {
        System.out.println("Please enter a menu item index or q to finish:");
        String choice = scanner.nextLine();

        while (!choice.equals("q")) {
            processItemChoice(choice, order);
            System.out.println("Please enter a menu item index or q to finish:");
            choice = scanner.nextLine();
        }
    }

    private void processItemChoice(String choice, Order order) {
        try {
            int itemIndex = Integer.parseInt(choice.trim());
            if (itemIndex < 0 || itemIndex >= menu.size()) {
                System.out.println("Invalid item index. Please choose a number from the menu.");
                return;
            }
            Item selectedItem = menu.get(itemIndex);
            order.addItem(selectedItem);
            System.out.println("Added: " + selectedItem.getName());
        } catch (NumberFormatException e) {
            System.out.println("Invalid input. Please enter a valid menu index or q to finish.");
        }
    }
}

public class CafeJavaApp {
    public static void main(String[] args) {
        CoffeeKiosk kiosk = initializeKiosk();

        try (Scanner scanner = new Scanner(System.in)) {
            kiosk.run(scanner);
        }
    }

    private static CoffeeKiosk initializeKiosk() {
        CoffeeKiosk kiosk = new CoffeeKiosk();
        kiosk.addMenuItem("banana", 2.00);
        kiosk.addMenuItem("coffee", 1.50);
        kiosk.addMenuItem("latte", 4.50);
        kiosk.addMenuItem("cappuccino", 3.00);
        kiosk.addMenuItem("muffin", 4.00);
        return kiosk;
    }
}