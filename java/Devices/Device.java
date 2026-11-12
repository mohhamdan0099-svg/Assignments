public class Device {
    private int battery = 100;

    public Device(int battery) {
        this.battery = battery;
    }

    public int getBattery() {
        return battery;
    }

    public void setBattery(int battery) {
        this.battery = battery;
    }
}