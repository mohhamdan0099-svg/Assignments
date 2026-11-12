public class TestDevice {
    public static void main(String [ ]args){
        Phone bashphone = new Phone(100);
        bashphone.mkCall();
        bashphone.mkCall();
        bashphone.mkCall();
        
        bashphone.playGame();
        bashphone.playGame();
        bashphone.chargeBattery();
        
    }
}