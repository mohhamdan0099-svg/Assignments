public class TestOrder {
    public static void main(String[] args) {

        Item item1 = new Item("drip coffee", 1.50);
        Item item2 = new Item("cappuccino", 3.50);
        Item item3 = new Item("latte", 4.00);
        Item item4 = new Item("mocha", 4.50);


        Order order1 = new Order();
        Order order2 = new Order();


        Order order3 = new Order("Cindhuri");
        Order order4 = new Order("Sam");
        Order order5 = new Order("Jimmy");


        order1.addItem(item1);
        order1.addItem(item2);

        order2.addItem(item3);
        order2.addItem(item4);

        order3.addItem(item1);
        order3.addItem(item2);

        order4.addItem(item2);
        order4.addItem(item3);

        order5.addItem(item1);
        order5.addItem(item4);


        order3.setReady(true);
        order5.setReady(true);

        System.out.println(order3.getStatusMessage()); 
        System.out.println(order1.getStatusMessage()); 

        System.out.println("Order 1 Total: $" + order1.getOrderTotal());


        order1.display();
        System.out.println();
        order2.display();
        System.out.println();
        order3.display();
        System.out.println();
        order4.display();
        System.out.println();
        order5.display();
    }
}

