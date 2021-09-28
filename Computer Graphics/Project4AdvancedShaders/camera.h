#ifndef camera_H
#define camera_H

#include <GLUT/glut.h>

#include <vector>


//Creation of camera class
class Camera {
  double theta;      //X and Z positioning in the rendering
  double y;          //Y position
  double dTheta;     //Incrementation for camera changes
  double dy;         //Incrementation for camera changes
public:
  //Constructor for the camera
  Camera(): theta(0), y(3), dTheta(0.04), dy(1.0) {}
  //To find the position of the camera
  double getX() {
    return 10 * cos(theta);
}
  //To find the position of the camera
  double getY() {
    return y;
}

  //To find the position of the camera
  double getZ() {
    return 10 * sin(theta);
}

  //Moving the camera to the right
  void moveRight() {
    theta -= dTheta;
}
  //To move the camera to the left
  void moveLeft() {
   theta += dTheta;
}
  //To move the camera up
  void moveUp() {
    y += dy;
}
  //To move the camera down
  void moveDown() {
    y -= dy;
}
};


#endif /* camera_h */
