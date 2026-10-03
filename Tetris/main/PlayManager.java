package main;

import java.awt.BasicStroke;
import java.awt.Color;
import java.awt.Font;
import java.awt.Graphics2D;
import java.awt.RenderingHints;
import java.util.ArrayList;
import java.util.Random;

import mino.Block;
import mino.Mino;
import mino.Mino_Bar;
import mino.Mino_L1;
import mino.Mino_L2;
import mino.Mino_Square;
import mino.Mino_T;
import mino.Mino_Z1;
import mino.Mino_Z2;

public class PlayManager { // point of this class is to draw the play area

    // handles tetrominoes and handles game play action like deleting lines, adding scorrs, etc.
    final int WIDTH = 360;
    final int HEIGHT = 600;

    // these variabkes indicate the left, right, top and bottom of the frame
    public static int left_x;
    public static int right_x;
    public static int top_y;
    public static int bottomt_y;


    // mino
    Mino currentMino;
    final int MINO_START_X;
    final int MINO_START_Y;
    
    Mino nextMino;
    final int NEXTMINO_X;
    final int NEXTMINO_Y;
    public static ArrayList<Block> staticBlocks = new ArrayList<>(); // blocks that are already placed in the play area

    // others
    public static int dropInterval = 15;


    public PlayManager() {

        left_x = (GamePanel.WIDTH/2) - (WIDTH/2);
        right_x = left_x + WIDTH;
        top_y = 50;
        bottomt_y = top_y + HEIGHT;

        // starting positions, middle top of frame
        MINO_START_X = left_x + (WIDTH/2) - Block.SIZE;
        MINO_START_Y = top_y + Block.SIZE;


        NEXTMINO_X = right_x + 175;
        NEXTMINO_Y = top_y + 500;

        // set mino
        currentMino = pickMino();
        currentMino.setXY(MINO_START_X, MINO_START_Y);

        nextMino = pickMino();
        nextMino.setXY(NEXTMINO_X, NEXTMINO_Y); 
    }

    private Mino pickMino() {
        // pick random mino
        Mino mino = null;
        int random = new Random().nextInt(7); // up to 7 bc there are 7 minos

        switch (random) {
            case 0: mino = new Mino_L1(); break;
            case 1: mino = new Mino_L2(); break;
            case 2: mino = new Mino_Square(); break; 
            case 3: mino = new Mino_Bar(); break; 
            case 4: mino = new Mino_T(); break; 
            case 5: mino = new Mino_Z1(); break; 
            case 6: mino = new Mino_Z2(); break; 
        }
        return mino;
    }

    public void update() {

        // check if current mino is active
        if (currentMino.active == false) {
            staticBlocks.add(currentMino.block[0]);
            staticBlocks.add(currentMino.block[1]);
            staticBlocks.add(currentMino.block[2]);
            staticBlocks.add(currentMino.block[3]);

            currentMino.deactivating = false;

            // replace current mino with next mino
            currentMino = nextMino;
            currentMino.setXY(MINO_START_X, MINO_START_Y);
            nextMino = pickMino();
            nextMino.setXY(NEXTMINO_X, NEXTMINO_Y);

            checkDelete(); // when mino becomes innactive, check if line(s) can be deleted

        } else {
            currentMino.update();
        }
    }

    private void checkDelete() {

        int x = left_x;
        int y = top_y;
        int blockCount = 0;

        while (x < right_x && y < bottomt_y) {

            for (int i = 0; i < staticBlocks.size(); i++) {
                if (staticBlocks.get(i).x == x && staticBlocks.get(i).y == y) {
                    blockCount ++;
                }
            }

             x += Block.SIZE;

             if (x == right_x) {

                 if (blockCount == 12) {

                     for (int i = staticBlocks.size() - 1; i > -1; i--) {
                         // remove all block in current y line
                         if (staticBlocks.get(i).y == y) {
                             staticBlocks.remove(i);
                         }
                     }

                     for (int i = 0; i < staticBlocks.size(); i++) {
                         if (staticBlocks.get(i).y < y) {
                             staticBlocks.get(i).y += Block.SIZE;
                         }
                     }

                 }

                 blockCount = 0;
                 x = left_x;
                 y += Block.SIZE;
             }
        }
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

        // draw current mino
        if (currentMino != null) {
            currentMino.draw(g2);
        }   

        // draw next mino
        nextMino.draw(g2);

        for (int i = 0; i < staticBlocks.size(); i++) {
            staticBlocks.get(i).draw(g2); 
        }
        
        g2.setColor(Color.YELLOW);
        g2.setFont(g2.getFont().deriveFont(50f) );
        if (KeyHandler.pausePressed) {
            g2.drawString("PAUSED", left_x + 76, top_y + 300);
        }
    }   
}