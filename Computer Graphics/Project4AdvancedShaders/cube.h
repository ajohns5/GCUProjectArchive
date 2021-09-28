#ifndef cube_h
#define cube_h
#include <GLUT/GLUT.h>


// Creation of ball class.  The ball has the radius, color, and bounces  between
// the maximum height and the xz plane.It's x and z coordinates
// are fixed.  Using the lame bouncing algorithm, the ball bounces.
class Cube {
  double diameter;
  GLfloat* color;
  double x;
  double y;
  double z;
public:
  Cube(double d, GLfloat* c, double y, double x, double z):
      diameter(d), color(c), y(y), x(x), z(z) {
  }
    //Upadting position in the rendering
  void update() {
    glPushMatrix();
    glMaterialfv(GL_FRONT, GL_AMBIENT_AND_DIFFUSE, color);
    glTranslated(x, y, z);
    glutSolidCube(diameter);
    glPopMatrix();
  }
};

#endif /* cube_h */
