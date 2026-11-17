public class Painting extends Art {
    public String paintType;


    public Painting(String title, String author, String description, String paintType) {
        super(title, author, description);
        this.paintType = paintType;
    }


    @Override
    public void viewArt() {
        System.out.println("--- Painting ---");
        System.out.println("Title: " + this.title);
        System.out.println("Author: " + this.author);
        System.out.println("Description: " + this.description);
        System.out.println("Paint Type: " + this.paintType);
        System.out.println();
    }
}