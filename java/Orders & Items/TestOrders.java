import java.util.ArrayList;
public class TestOrders {
    public static void main(String[] args) {

        Item item1 = new Item();
        item1.name = "mocha";
        item1.price = 4.5;

        Item item2 = new Item();
        item2.name = "latte";
        item2.price = 5.0;

        Item item3 = new Item();
        item3.name = "drip coffee";
        item3.price = 3.5;

        Item item4 = new Item();
        item4.name = "cappuccino";
        item4.price = 4.5;




        Order order1 = new Order();
        order1.name = "Rami";

        Order order2 = new Order();
        order2.name = "Jimmy";

        Order order3 = new Order();
        order3.name = "Noah";

        Order order4 = new Order();
        order4.name = "Sam";
        
    

        System.out.println(order1);

        System.out.println(order1.total);

        order2.items.add(item1);
        order2.total += item1.price;

        order3.items.add(item4);
        order3.total += item4.price;


        order4.items.add(item2);
        order4.total += item2.price;

        order1.ready = true;

        
        order4.items.add(item2);
        order4.items.add(item2);
        order4.total += (item2.price * 2);

        order2.ready = true;

        
        System.out.printf("Order 2 Total: %s\n", order2.total);
        System.out.printf("Order 2 Ready: %s\n", order2.ready);
        System.out.printf("Order 4 Total: %s\n", order4.total);
    }
}