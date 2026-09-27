package mino;

import java.awt.Color;

public class Mino_T extends Mino {
    
    public Mino_T() {
        create(Color.MAGENTA);
    }
    
    public void setXY(int x, int y) {

        block[0].x = x;
        block[0].y = y;
        block[1].x = block[0].x;
        block[1].y = block[0].y - Block.SIZE;
        block[2].x = block[0].x - Block.SIZE;
        block[2].y = block[0].y;
        block[3].x = block[0].x + Block.SIZE;
        block[3].y = block[0].y;
    }

    public void getDirection1() {

        block[0].x = block[0].x;
        block[0].y = block[0].y;
        block[1].x = block[0].x;
        block[1].y = block[0].y - Block.SIZE;
        block[2].x = block[0].x - Block.SIZE;
        block[2].y = block[0].y;
        block[3].x = block[0].x + Block.SIZE;
        block[3].y = block[0].y;

        updateXY(1);
    }

    public void getDirection2() {
        block[0].x = block[0].x;
        block[0].y = block[0].y;
        block[1].x = block[0].x + Block.SIZE;
        block[1].y = block[0].y;
        block[2].x = block[0].x;
        block[2].y = block[0].y - Block.SIZE;
        block[3].x = block[0].x;
        block[3].y = block[0].y + Block.SIZE;

        updateXY(2);
    }

    public void getDirection3() {

        block[0].x = block[0].x;
        block[0].y = block[0].y;
        block[1].x = block[0].x;
        block[1].y = block[0].y + Block.SIZE;
        block[2].x = block[0].x + Block.SIZE;
        block[2].y = block[0].y;
        block[3].x = block[0].x - Block.SIZE;
        block[3].y = block[0].y;

        updateXY(3);
    }
    
    public void getDirection4() {

        block[0].x = block[0].x;
        block[0].y = block[0].y;
        block[1].x = block[0].x - Block.SIZE;
        block[1].y = block[0].y;
        block[2].x = block[0].x;
        block[2].y = block[0].y + Block.SIZE;
        block[3].x = block[0].x ;
        block[3].y = block[0].y - Block.SIZE;

        updateXY(4);
    }
}