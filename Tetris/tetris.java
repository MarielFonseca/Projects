package Tetris;
import javax.swing.JFrame;

public class tetris {
   public static final int WIDTH = 445;
   public static final int HEIGHT = 629;

   private Board board;
   private Title title;
   private JFrame window;

   public tetris() {

    window = new JFrame("Tetris");
    window.setSize(WIDTH, HEIGHT);
    window.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
    window.setLocationRelativeTo(null);
    window.setResizable(false);

    board = new Board();
    title = new Title();

    window.addKeyListener(board);
    window.addKeyListener(title);
    window.add(title);
    window.setVisible(true);

   }

   public static void main(String[] args) {
    new tetris();
   }

}
