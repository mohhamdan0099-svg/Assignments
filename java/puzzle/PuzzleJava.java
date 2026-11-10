import java.util.Random;
import java.util.ArrayList;

public class PuzzleJava {
Random randMachine = new Random();
    public ArrayList<Integer> getTenRolls(){
        ArrayList<Integer> randomRolls = new ArrayList<Integer>();
        for (int i = 0; i < 10; i++){
        randomRolls.add(randMachine.nextInt(21));
        }
        return randomRolls;
        }

    public char getRandomLetter(){
        char[] alphabets = {'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'};
        int result = randMachine.nextInt(alphabets.length);
        return (alphabets[result]);  
    }
public String generatePass() {
    String chars = "abcdefghijklmnopqrstuvwxyz";
    String nums="123456789";
    String randomPass = "";
    Random randMachine = new Random();
    int randomNum = randMachine.nextInt(nums.length());
    randomPass += nums.charAt(randomNum);
    for (int i = 1; i < 8; i++) {
        int randomIndex = randMachine.nextInt(chars.length());
        randomPass += chars.charAt(randomIndex);
    }
    return randomPass;
}

    public ArrayList<String> getNewPass(int length){
        ArrayList<String> randWords = new ArrayList<String>();
        for (int i = 0; i < length; i++){
        randWords.add(generatePass());

        };
        return randWords;
    }

}