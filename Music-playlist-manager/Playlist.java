import java.util.List;

public class Playlist {

    SongNode firstSong; // head
    SongNode lastSong; // tail
    SongNode currentSong; // current pointer
    int size; // optional?

    public Playlist(List<SongNode> songs) {
        firstSong = songs.getFirst();
        lastSong = songs.getLast();

    }

    public void addSongs(SongNode song) { // adds to the end automatically

    }

    public void addToStart(SongNode song) {

    }

    public void addRandomly(SongNode song) { // target is random

    }

    public void removeSong(SongNode song) { // find song by title, rewire neighbours

        // special cases: removing the head, tail, only node and song currently playing
    }

    public void playNext() { // DECIDE WHAT HAPPENS AT THE ENDS: STOP OR LOOP?

    }

    public void playPrevious() { // DECIDE WHAT HAPPENS AT THE ENDS: STOP OR LOOP?

    }

    public void find(String title) {

    }

    public void display() {
        // print all songs, whole playlist, from head to toe
        // mark the current one
    }


    // extra features for later
    // shuffle
    // repeat mode
    // total playlist duration
    // test edge cases



}
