import java.util.ArrayList;
import java.util.Random;


public class TestPuzzleJava {
    
    public static void main(String[] args) {
        PuzzleJava generator = new PuzzleJava();
        ArrayList<Integer> randomRolls = generator.getTenRolls();
        System.out.println(randomRolls);
        
                //..
        // Write your other test cases here.
        //..
        System.out.println(generator.getRandomLetter());
        System.out.println(generator.generatePass());
        System.out.println(generator.getNewPass(7));
        
    }
}