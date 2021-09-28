//Project 8: Simple Animation
//Created by Austin Johns
//For class CST-310
//Include statement for GLUT
#define GL_SILENCE_DEPRECATION
# include <GLUT/glut.h>

using namespace std;
//creation of shape
GLfloat vertices[][3] = {
  { -1.0, -1.0, -1.0 },
  {  1.0, -1.0, -1.0 },
  {  1.0,  1.0, -1.0 },
  { -1.0,  1.0, -1.0 },
  { -1.0, -1.0,  1.0 },
  {  1.0, -1.0,  1.0 },
  {  1.0,  1.0,  1.0 },
  { -1.0,  1.0,  1.0 } };

GLfloat normals[][3] = {
  { -1.0, -1.0, -1.0 },
  {  1.0, -1.0, -1.0 },
  {  1.0,  1.0, -1.0 },
  { -1.0,  1.0, -1.0 },
  { -1.0, -1.0,  1.0 },
  {  1.0, -1.0,  1.0 },
  {  1.0,  1.0,  1.0 },
  { -1.0,  1.0,  1.0 } };
//coloring the shape
GLfloat colors[][3] = {
  { 1.0, 0.0, 0.0 },
  { 1.0, 1.0, 0.0 },
  { 1.0, 1.0, 1.0 },
  { 0.0, 1.0, 1.0 },
  { 0.0, 0.0, 1.0 } };
//Setting the shape to rotate on an axis
static GLint axis = 2;
static GLfloat theta[3] = { 0.0, 0.0, 0.0 };
//creation of functions
int main ( int argc, char *argv[] );
//initiates color
void colorpoly ( );
//setup for display of animatoin
void display ( );
//setup for mouse click interaction
void mouse ( int btn, int state, int x, int y );
//reshaping rendering
void myReshape ( int w, int h );
//3D functionality
void polygon ( int a, int b, int c, int d );
//Function to move cube three-dimensionally
void spinpoly ( );

int main ( int argc, char *argv[] )
{
  glutInit ( &argc, argv );
//    display setup
  glutInitDisplayMode ( GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH );
//    setting window size
  glutInitWindowSize ( 500, 500 );
//    normal window position
  glutInitWindowPosition ( 0, 0 );
//    window name
  glutCreateWindow ( "Project 8: Simple Animation" );
//    use of reshape function
  glutReshapeFunc ( myReshape );
  glutDisplayFunc ( display );
  glutIdleFunc ( spinpoly );
  glutMouseFunc ( mouse );
  glEnable ( GL_DEPTH_TEST );
  glutMainLoop ( );
  return 0;
}
//This function creates all attributes of the cube and the axes it rotates on.
void colorpoly ( )
{
    polygon ( 0, 3, 2, 1 );
    polygon ( 2, 3, 7, 6 );
    polygon ( 0, 4, 7, 3 );
    polygon ( 1, 2, 6, 5 );
    polygon ( 4, 5, 6, 7 );
    polygon ( 0, 1, 5, 4 );
  return;
}
//Generation of graphical output for the polygon interaction
void display ( )
{
  glClear ( GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT );
  glLoadIdentity ( );
//  creating axes for roataion of the shape
  glRotatef ( theta[0], 1.0, 0.0, 0.0 );
  glRotatef ( theta[1], 0.0, 1.0, 0.0 );
  glRotatef ( theta[2], 0.0, 0.0, 1.0 );
  colorpoly ( );
//buffer clear
  glFlush ( );
//switching between buffers to create a smooth animation
  glutSwapBuffers ( );

  return;
}
//creation of the mouse input
//this is very important because it's what creates the animation of the shape
void mouse ( int btn, int state, int x, int y )
{
  if ( btn == GLUT_LEFT_BUTTON && state == GLUT_DOWN )
  {
    axis = axis + 1;
  }
  if ( btn == GLUT_MIDDLE_BUTTON && state == GLUT_DOWN )
  {
    axis = axis + 1;
  }
  if ( btn == GLUT_RIGHT_BUTTON && state == GLUT_DOWN )
  {
    axis = axis + 1;
  }
//utilization of all axes
  axis = axis % 3;
  return;
}
//creation of window mapping to ensure object and animation is clear at any size
void myReshape ( int w, int h )
{
  glViewport ( 0, 0, w, h );
  glMatrixMode ( GL_PROJECTION );
  glLoadIdentity ( );

  if ( w <= h )
  {
    glOrtho (
      -2.0, 2.0,
      -2.0 * ( GLfloat ) h / ( GLfloat ) w, 2.0 * ( GLfloat ) h / ( GLfloat ) w,
      -10.0, 10.0 );
  }
  else
  {
    glOrtho (
      -2.0 * ( GLfloat ) h / ( GLfloat ) w, 2.0 * ( GLfloat ) h / ( GLfloat ) w,
      -2.0, 2.0,
      -10.0, 10.0 );
  }

  glMatrixMode ( GL_MODELVIEW );

  return;
}
//definition of all colors and verticies of the animation
void polygon ( int a, int b, int c, int d )
{
  glBegin ( GL_POLYGON );

  glColor3fv ( colors[a] );
  glNormal3fv ( normals[a] );
  glVertex3fv ( vertices[a] );

  glColor3fv ( colors[b] );
  glNormal3fv ( normals[b] );
  glVertex3fv ( vertices[b] );

  glColor3fv ( colors[c] );
  glNormal3fv ( normals[c] );
  glVertex3fv ( vertices[c] );

  glColor3fv ( colors[d] );
  glNormal3fv ( normals[d] );
  glVertex3fv ( vertices[d] );

  glEnd ( );

  return;
}
//creation of animation
void spinpoly ( )
{
//    rotation speed
  theta[axis] = theta[axis] + 2;
//    range of rotation
  if ( 360.0 < theta[axis] )
  {
    theta[axis] = theta[axis] - 360.0;
  }
  glutPostRedisplay ( );
  return;
}
