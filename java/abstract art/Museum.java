import java.util.ArrayList;
import java.util.Collections;

public class Museum {
    public static void main(String[] args) {
        
        Painting p1 = new Painting("Starry Night", "Vincent van Gogh", "A brilliant nocturnal post-impressionist masterpiece.", "Oil");
        Painting p2 = new Painting("The Persistence of Memory", "Salvador Dalí", "Surrealist painting featuring melting pocket watches.", "Oil");
        Painting p3 = new Painting("Water Lilies", "Claude Monet", "A serene depiction of the artist's flower garden in Giverny.", "Oil");

        
        Sculpture s1 = new Sculpture("David", "Michelangelo", "A masterwork of Renaissance sculpture representing the biblical hero.", "Marble");
        Sculpture s2 = new Sculpture("The Thinker", "Auguste Rodin", "A bronze sculpture of a man in sober meditation.", "Bronze");

        p1.viewArt();
        p2.viewArt();
        p3.viewArt();
        s1.viewArt();
        s2.viewArt();

    }
}