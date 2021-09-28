/*
Austin Johns
CST-310
*/
#include <GLUT/GLUT.h>
#include <cmath>
#include "camera.h"
#include "ball.h"
#include "cube.h"
#include "checkerboard.h"
#include "cylinder.h"

//Colors
GLfloat BLUE[] = {0, 0, 1}; //RGB: 0, 0, 255
GLfloat PURPLE[] = {1, 0, 1}; //RGB: 255, 0, 255
GLfloat RED[] = {1, 0, 0}; //RGB: 255, 0, 0

// Global variables
Checkerboard checkerboard(8, 8); //CREATES A 8 X 8 CHECKERBOARD
Camera camera; //CREATES A CAMERA

//Creation of ball class in simulation
Ball ball[] = {
  Ball(0.8, BLUE, 0.8, 4.5, 5)
};

//Creation of cube class in simulation
Cube cube[] = {
  Cube(1, RED, 0.53, 4.5, 1.4)
};

//Creation of cylinder class in simulation
Cylinder cylinder[] = {
  Cylinder(0.5,PURPLE, 0.1, 5, 2.7)
};

void init() {
  glEnable(GL_DEPTH_TEST); //Depth comparisons
  glLightfv(GL_LIGHT0, GL_DIFFUSE, WHITE); //Diffusion of RGB Lighting with shaders
  glLightfv(GL_LIGHT0, GL_SPECULAR, WHITE); //Lighting intensity
  glMaterialfv(GL_FRONT, GL_SPECULAR, WHITE); //Front intensity
  glMaterialf(GL_FRONT, GL_SHININESS, 30); //Definition of luster from front view
  glEnable(GL_LIGHTING); //Lighting
  glEnable(GL_LIGHT0);
  checkerboard.create(); //Checkerboard utilization
}

//Drawing all objects
void display() {
  glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT);
  glLoadIdentity();
  gluLookAt(camera.getX(), camera.getY(), camera.getZ(), checkerboard.centerx(), 0.0, checkerboard.centerz(), 0.0, 1.0, 0.0);  //Starting camera and checkerboard
  checkerboard.draw();
  for (int i = 0; i < sizeof ball / sizeof(Ball); i++) {
    ball[i].update();
  }
  for (int i = 0; i < sizeof cube / sizeof(Cube); i++) {
    cube[i].update();
  }
  for (int i = 0; i < sizeof cylinder / sizeof(Cylinder); i++) {
    cylinder[i].update();
  }
  glFlush();
  glutSwapBuffers();
}

//Setting the camera to fit the window
void reshape(GLint w, GLint h) {
  glViewport(0, 0, w, h);
  glMatrixMode(GL_PROJECTION); 
  glLoadIdentity();
  gluPerspective(40.0, GLfloat(w) / GLfloat(h), 1.0, 150.0);
  glMatrixMode(GL_MODELVIEW);
}

//Drawing the next frame based on user input
void timer(int v) {
  glutPostRedisplay();
  glutTimerFunc(1000/60, timer, v);
}

//Movement of camera based on input
void special(int key, int, int) {
  switch (key) 
{
    //Left keystroke
    case GLUT_KEY_LEFT:
      camera.moveLeft(); //Left keystroke
      break;
    //Right keystroke
    case GLUT_KEY_RIGHT: 
      camera.moveRight(); //Right keystroke
      break;
    //Up keystroke
    case GLUT_KEY_UP: 
      camera.moveUp(); //Up keystroke
      break;
    //Down keystroke
    case GLUT_KEY_DOWN:
      camera.moveDown(); //Down keystroke
      break;
  glutPostRedisplay();
}
}
//Entering main loop to utilize all predetermined functions
int main(int argc, char** argv) {
  glutInit(&argc, argv);
  glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH);  //Displays 3D depth
  glutInitWindowPosition(80, 80);
    //Window
  glutInitWindowSize(800, 600);
    //Window size
  glutCreateWindow("PROJECT 9: ADVANCED SHADERS");
    //Creation of window
  glutDisplayFunc(display);
    //Display of function
  glutReshapeFunc(reshape);
    //Reshape of function
  glutSpecialFunc(special);
    //Function for all camera input processing
  glutTimerFunc(100, timer, 0);
    //Timer
  init();
  glutMainLoop();
}
