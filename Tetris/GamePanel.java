package Tetris;

import javax.swing.JPanel;
import java.awt.Color;
import java.awt.Dimension;
import java.awt.Graphics;

public class GamePanel extends JPanel implements Runnable{

    public static final int WIDTH = 445;
    public static final int HEIGHT = 629;
    final int FPS = 60;
    Thread thread; 

   public GamePanel() {
        // panel settings
        this.setPreferredSize(new Dimension(WIDTH, HEIGHT));  
        this.setBackground(Color.BLACK);
        this.setLayout(null);
   }

   public void launchGame() { // launch by activating thread
        thread = new Thread(this);
        thread.start(); // starting will call the run method 
   }

   @Override
   public void run() {
        // game loop: updates and draws 
        // update object positions (x, y), score, etc.
        double drawInterval = 1000000000/FPS;
        double delta = 0;
        long lastTime = System.nanoTime();
        long currentTime;

        while (thread != null) {
            currentTime = System.nanoTime();
            
            delta += (currentTime - lastTime) / drawInterval;
            lastTime = currentTime;

            if (delta >= 1) {
                update();
                repaint();
                delta--;
            }
        }
        throw new UnsupportedOperationException("Unimplemented method 'run'");
   }

   public void update() {

   }

   public void paintComponent(Graphics g) {
    super.paintComponent(g);
   }

   
    
}
