public class Phone extends Device {

    public Phone(int battery) {
        super(battery);
    }

    public void mkCall(){
        int result = getBattery() - 5;
        setBattery(result);
        System.out.println("you make a call.");
        System.out.println("Battery Remaining:" + result ); 
    }

    public void playGame(){
        int result = getBattery() - 20;
        setBattery(result);
        System.out.println("you play a game.");
        System.out.println("Battery Remaining:" + result ); 
    }

    public void chargeBattery(){
        int result = getBattery() + 50;
        setBattery(result);
        System.out.println("you have charged your phone.");
        System.out.println("Battery Remaining:" + result );
    }
}