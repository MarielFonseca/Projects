package Tetris;

import javax.swing.JPanel;
import java.awt.Color;
import java.awt.Dimension;

public class GamePanel extends JPanel {

public static final int WIDTH = 445;
   public static final int HEIGHT = 629;

   public GamePanel() {

    // panel settings
    this.setPreferredSize(new Dimension(WIDTH, HEIGHT));  
    this.setBackground(Color.BLACK);
    this.setLayout(null);
   }
    
}
