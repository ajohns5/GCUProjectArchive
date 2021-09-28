#ifndef checkerboard_h
#define checkerboard_h
#include <GLUT/GLUT.h>


//Creation of the Checkboard class, each square on the checkerboard is 1x1, and the colors are predefined.
//Colors
GLfloat WHITE[] = {1, 1, 1};
//RGB: 255, 255, 255
GLfloat YELLOW[] = {1, 1, 0};
//RGB: 255, 0, 0
//Creation of the checkerboard class
class Checkerboard {
    //displaying the list ID
  int displayListId;
    //Creation of width
  int width;
    //Creation of depth
  int depth;
public:
  //Constructor for the checkerboard
  Checkerboard(int width, int depth): width(width), depth(depth) {}
  //Creation of width by division of 2
  double centerx() {
    return width / 2;
} 
  //Depth divided by 2 for center of z
  double centerz() {
    return depth / 2;
}
  //CFunction for creation of checkerboard
  void create() {
    displayListId = glGenLists(1); //Empty display lists
    glNewList(displayListId, GL_COMPILE); //Create or replace display lists
    GLfloat lightPosition[] = {4, 3, 7, 1}; //Lighting position for shaders
    glLightfv(GL_LIGHT0, GL_POSITION, lightPosition); //Lighting creation for board
    glBegin(GL_QUADS); //points for quads
    glNormal3d(0, 1, 0); //Creation of normal vector
    //Creation of pattern for the checkerboard
    for (int x = 0; x < width - 1; x++) {
      for (int z = 0; z < depth - 1; z++) {
        glMaterialfv(GL_FRONT, GL_AMBIENT_AND_DIFFUSE, (x + z) % 2 == 0 ? YELLOW : WHITE);
        glVertex3d(x, 0, z);
        glVertex3d(x+1, 0, z);
        glVertex3d(x+1, 0, z+1);
        glVertex3d(x, 0, z+1);
      }
    }
    glEnd();
    glEndList();
  }
  //Implementation of checkerboard
  void draw() {
    glCallList(displayListId);
  }
};

#endif /* checkerboard_h */

