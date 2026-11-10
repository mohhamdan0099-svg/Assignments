import java.util.HashMap;
import java.util.Set;

public class Hashmatique {
    public static void main(String[] args) {
        HashMap<String, String> trackList  = new HashMap <String, String>();
        trackList .put("Track1", "asd");
        trackList .put("Track2", "qwe");
        trackList .put("Track3", "rty");
        trackList .put("Track4", "poi");
        

        String singleTrack = trackList.get("Track2");
        System.out.println("Track2 Lyrics: " + singleTrack);

        Set<String> Lyrics = trackList .keySet();
        for(String Track : Lyrics) {
            System.out.println(Track + ": " + trackList.get(Track));    
        }
    }
}