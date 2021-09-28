#ifndef ball_h
#define ball_h
#include <GLUT/GLUT.h>


// The ball has the radius, color, and bounces between
// the maximum height and the xz plane.  Therefore its x and z coordinates
// are fixed. Using the lame bouncing algorithm, the ball bounces.
class Ball {
  double radius;
  GLfloat* color;
  double x;
  double y;
  double z;
public:
  Ball(double r, GLfloat* c, double y, double x, double z):
      radius(r), color(c), y(y), x(x), z(z) {
  }
  void update() {
    glPushMatrix();
    glMaterialfv(GL_FRONT, GL_AMBIENT_AND_DIFFUSE, color);
    glTranslated(x, y, z);
    glutSolidSphere(radius, 30, 30);
    glPopMatrix();
  }
};

#endif /* ball_h */
