#ifndef cylinder_h
#define cylinder_h
#include <GLUT/GLUT.h>

class Cylinder {
  double radius; //Radius
  GLfloat* color; //Color declaration
  double x; //X variable
  double y; //Y variable
  double z; //Z variable
public:
  //Cylinder setup with parameters
  Cylinder(double r, GLfloat* c, double y, double x, double z):
      radius(r), color(c), y(y), x(x), z(z) {
 }
 void update() {
   GLUquadricObj *quadratic; //Quadratic utilization
   quadratic = gluNewQuadric(); //New quadratic implementation
   glPushMatrix(); //Pushing object to the stack
   glMaterialfv(GL_FRONT, GL_AMBIENT_AND_DIFFUSE, color); //Declaring object
   glTranslated(x, y, z); //Translation of object for coordinates
   glRotatef(270,1,0,0); //Rotation of cylinder to make it vertical
   gluCylinder(quadratic,radius,radius,1,15,15);
   glPushMatrix(); //Pushing to stack
   gluDisk(quadratic, 0, radius, 15, 4);
   glPopMatrix(); //Popping the stack
  }
};

#endif /* cylinder_h */
