package Tetris;

import java.awt.BasicStroke;
import java.awt.Color;
import java.awt.Font;
import java.awt.Graphics2D;
import java.awt.RenderingHints;

public class PlayManager { // point of this class is to draw the play area

    // handles tetrominoes and handles game play action like deleting lines, adding scorrs, etc.
    final int WIDTH = 360;
    final int HEIGHT = 600;

    // these variabkes indicate the left, right, top and bottom of the frame
    public static int left_x;
    public static int right_x;
    public static int top_y;
    public static int bottomt_y;

    public PlayManager() {

        left_x = (GamePanel.WIDTH/2) - (WIDTH/2);
        right_x = left_x + WIDTH;
        top_y = 50;
        bottomt_y = top_y + HEIGHT;
    }

    public void update() {

    }

    public void draw(Graphics2D g2) {
        // draw play area frame
        g2.setColor(Color.WHITE);
        g2.setStroke(new BasicStroke(4f));
        g2.drawRect(left_x - 4, top_y - 4, WIDTH + 8, HEIGHT + 8);

        // draw next-mino frame
        int x = right_x + 100;
        int y = bottomt_y - 200;
        g2.drawRect(x, y, 200, 200);
        g2.setFont(new Font("Arial", Font.PLAIN, 30));
        g2.setRenderingHint(RenderingHints.KEY_TEXT_ANTIALIASING, RenderingHints.VALUE_TEXT_ANTIALIAS_ON);
        g2.drawString("NEXT", x+60, y+60);
        g2.setColor(Color.WHITE);

        
    }

    
}
