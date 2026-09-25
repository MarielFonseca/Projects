package mino;

import java.awt.Color;
import java.awt.Graphics2D;

import main.KeyHandler;
import main.PlayManager;

public class Mino { // super class for all tetrominoes, so all shapes will extend this class

    public Block block[] = new Block[4]; // each tetromino has 4 blocks
    public Block tempBlock[] = new Block[4];
    public int autoDropCounter = 0;
    public int direction = 1; // there are four directions 1-4

    public void create(Color color) {
        block[0] = new Block(color);
        block[1] = new Block(color); 
        block[2] = new Block(color); 
        block[3] = new Block(color); 

        tempBlock[0] = new Block(color);
        tempBlock[1] = new Block(color);
        tempBlock[2] = new Block(color);
        tempBlock[3] = new Block(color);
    }

    // used by daugther classes
    // TODO: implement direction change
    public void setXY(int x, int y) {    }
    public void getDirection1() {}
    public void getDirection2() {}
    public void getDirection3() {}
    public void getDirection4() {}
    public void updateXY(int direction) {    }
    
    public void update() {    
        autoDropCounter ++; // counter increases in every frame,
        if (autoDropCounter == PlayManager.dropInterval) {
            // mino goes down
            block[0].y += Block.SIZE;
            block[1].y += Block.SIZE;
            block[2].y += Block.SIZE;
            block[3].y += Block.SIZE;
            autoDropCounter = 0; // reset

            // move the mino
            if (KeyHandler.downPressed) {

                block[0].y += Block.SIZE;
                block[1].y += Block.SIZE;
                block[2].y += Block.SIZE;
                block[3].y += Block.SIZE;
                
                autoDropCounter = 0;

                KeyHandler.downPressed = false;

            }
            if (KeyHandler.upPressed) {
                
            }
            if (KeyHandler.leftPressed) {

                block[0].x -= Block.SIZE;
                block[1].x -= Block.SIZE;
                block[2].x -= Block.SIZE;
                block[3].x -= Block.SIZE;
                
                KeyHandler.leftPressed = false;
                
            }
            if (KeyHandler.rightPressed) {
                block[0].x += Block.SIZE;
                block[1].x += Block.SIZE;
                block[2].x += Block.SIZE;
                block[3].x += Block.SIZE;
                
                KeyHandler.rightPressed = false;
            }


        }
    }

    public void draw(Graphics2D g2) {

        int margin = 2;
        g2.setColor(block[0].color);
        g2.fillRect(block[0].x + margin, block[0].y + margin, Block.SIZE - (margin*2), Block.SIZE - (margin*2));
        g2.fillRect(block[1].x + margin, block[1].y + margin, Block.SIZE - (margin*2), Block.SIZE - (margin*2));
        g2.fillRect(block[2].x + margin, block[2].y + margin, Block.SIZE - (margin*2), Block.SIZE - (margin*2));
        g2.fillRect(block[3].x + margin, block[3].y + margin, Block.SIZE - (margin*2), Block.SIZE - (margin*2));
    }
    
}
