public class Bat extends Mammal {

    // Constructor setting initial energy to 300
    public Bat() {
        this.energy = 300;
    }

    public void fly() {
        System.out.println("The bat is now airborne!");
        this.energy -= 50;
    }

    public void eatHumans() {
        System.out.println("The bat has fed on humans and is quite satisfied.");
        this.energy += 25;
    }

    public void attackTown() {
        System.out.println("The bat is attacking a town!");
        this.energy -= 100;
    }
}