public class Gorilla extends Mammal {

    public void throwSomething() {
        System.out.println("The gorilla has thrown an object!");
        this.energy -= 5;
    }
    
    public void eatBananas() {
        System.out.println("The gorilla is eating bananas and looks very satisfied.");
        this.energy += 10;
    }

    public void climb() {
        System.out.println("The gorilla has climbed a tree!");
        this.energy -= 10;
    }
}