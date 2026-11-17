public class Sculpture extends Art {
    public String material;

    // Constructor
    public Sculpture(String title, String author, String description, String material) {
        super(title, author, description);
        this.material = material;
    }

    
    @Override
    public void viewArt() {
        System.out.println("--- Sculpture ---");
        System.out.println("Title: " + this.title);
        System.out.println("Author: " + this.author);
        System.out.println("Description: " + this.description);
        System.out.println("Material: " + this.material);
        System.out.println();

        
    }
}