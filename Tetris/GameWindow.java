package Tetris;
import javax.swing.JFrame;


public class GameWindow {

   private JFrame window;

   public GameWindow() {

      window = new JFrame("Tetris");
      window.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
      window.setResizable(false);

      // add GamePanel to the window
      GamePanel panel = new GamePanel();
      window.add(panel);
      window.pack();

      window.setLocationRelativeTo(null);    
      window.setVisible(true);

   }

   public static void main(String[] args) {
    new GameWindow();
   }

}
