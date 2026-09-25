package mino;

import java.awt.Color;

public class Mino_L1 extends Mino {
    
    public Mino_L1() {
        create(Color.ORANGE);
    }

    public void setXY(int x, int y) {
        // o (b1)
        // o (b0)
        // o o (b2, b3)

        block[0].x = x;
        block[0].y = y;
        block[1].x = block[0].x;
        block[1].y = block[0].y - Block.SIZE;
        block[2].x = block[0].x;
        block[2].y = block[0].y + Block.SIZE;
        block[3].x = block[0].x + Block.SIZE;
        block[3].y = block[0].y + Block.SIZE;


        
    }
}
