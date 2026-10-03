public class SongNode {

    String title;
    String artist;
    int duration;
    SongNode next;
    SongNode previous;

    public SongNode(String title, String artist, int duration) {
        this.title = title;
        this.artist = artist;
        this.duration = duration;
        this.next = null;
        this.previous = null;
    }


}
