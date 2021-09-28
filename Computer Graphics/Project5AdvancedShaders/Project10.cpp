//Austin Johns
//CST-310
//Project10AdvancedShaders

#define GL_SILENCE_DEPRECATION
#include <GLUT/GLUT.h>
#include <iostream>
#include"SOIL.h"
#include <vector>
#include <stdio.h>
#include <cmath>


using namespace std;


//Creates GLfloat variables for different colors
GLfloat WHITE[] = {1, 1, 1}; //code for white
GLfloat RED[] = {1, 0, 0}; //code for red
GLfloat GREEN[] = {0, 1, 0}; //code for green
GLfloat BLUE[] = {0, 0, 1}; //code for blue
GLfloat YELLOW[] = {1, 1, 0}; //code for yellow

//Defining pi
#define PI 3.14159265

//Camera control variables
float cam_height = 3, cam_position = 3.5, cam_depth = -10; //Variables for camera location
float cam_x = 0, cam_y = 0; //Variables for camera angle
float cam_pitch = 0, cam_yaw = 0, cam_roll_1 = 0, cam_roll_2 = 1, roll_angle = 0; //variables for camera angle

//Texture variables
GLuint sphere_texture, ObjectSquare_texture[6], ObjectCylinder_texture; //texture variables
int width, height; //Sets dimensions of textures
unsigned char * image; //pointer for image

//creation of checkerboard
class Checkerboard {
    
    //Creation of checkerboard class
    int displayListId; //List variable
    int width; //Width variable
    int depth; //Depth variable

public:
    
    //Creation of checkerboard constructor
    Checkerboard(int width, int depth): width(width), depth(depth) {}
    
    //Creation of object
    void create() {
        //GL List the size of 1
        displayListId = glGenLists(1);
        glNewList(displayListId, GL_COMPILE);
        
        //Sets lighting
        GLfloat lightPosition[] = {3.5, 3, 1, 1};
        //Placing light in scene
        glLightfv(GL_LIGHT0, GL_POSITION, lightPosition);
        
        //GL Quad for checkerboard
        glBegin(GL_QUADS);
        glNormal3d(0, 1, 0);
        
        //Looping for x position
        for (int x = 0; x < width - 1; x++) {
            //Looping for z position
            for (int z = 0; z < depth - 1; z++) {
                //Random color alternation
                glMaterialfv(GL_FRONT, GL_AMBIENT_AND_DIFFUSE, (x + z) % 2 == 0 ? BLUE : GREEN);
                //vertices of checkerboard
                glVertex3d(x, 0, z);
                glVertex3d(x + 1, 0, z);
                glVertex3d(x + 1, 0, z + 1);
                glVertex3d(x, 0, z + 1);
            }
        }
    glEnd(); //Stopping process
    glEndList(); //Stopping list additions
    }
    
    //Draw function for checkerboard
    void draw() {
        //Calling list above
        glCallList(displayListId);
    }
};

//Defines the ObjectCylinder Class
class ObjectCylinder {

    //Creates the private ObjectCylinder class variables
    GLfloat* color; //Variable for the ObjectCylinder color
    float height; //Variable for the ObjectCylinder height
    float radius; //Variable for the ObjectCylinder radius
    float x; //Variable for the ObjectCylinder x position
    float z; //Variable for the ObjectCylinder z position
    
public:
    
    //ObjectCylinder Constructor
    ObjectCylinder(GLfloat* c, float h, float r, float x, float z): color(c), height(h), radius(r), x(x), z(z) {}
    
    //Creates the "draw" function to draw the ObjectCylinder
    void draw() {
        
        //Enables Textures
        glEnable(GL_TEXTURE_2D);
        //Binds the ObjectCylinder texture to the drawing texture
        glBindTexture(GL_TEXTURE_2D, ObjectCylinder_texture);
        //Sets up Texture Parameters
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR);
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR);
        
        //Pushes onto the matrix stack
        glPushMatrix();
            //Sets the color to yellow
            glMaterialfv(GL_FRONT, GL_AMBIENT_AND_DIFFUSE, color);
            //Creates a quadratic object
            GLUquadricObj* ObjectCylinder;
            ObjectCylinder = gluNewQuadric();
            gluQuadricTexture(ObjectCylinder, GL_TRUE);
            //Moves the ObjectCylinder to the correct location
            glTranslated(x, 2, z);
            //Rotates the ObjectCylinder to the correct orientation
            glRotatef(90, 1, 0, 0);
            //Creates the ObjectCylinder
            gluCylinder(ObjectCylinder, radius, radius, height, 32, 32);
            glDisable(GL_TEXTURE_2D);
        //Pops off the matrix stack
        glPopMatrix();
    }
};


//Defines the ObjectSquare class
class ObjectSquare {

    //Creates the ObjectSquare class
    GLfloat* color; //Variable for ObjectSquare color
    float length; //Variable for ObjectSquare length
    float x; //Variable for ObjectSquare x position
    float z; //Variable for ObjectSquare z position
    
public:
    
    //ObjectSquare Constructor
    ObjectSquare(GLfloat* c, float l, float x, float z): color(c), length(l), x(x), z(z) {}
    
    //Draw function
    void draw() {
        //Enables Texturing
        glEnable(GL_TEXTURE_2D);
        //Pushes to stack
        glPushMatrix();
            //Moves ObjectSquare to correct location
            glTranslated(x, 1, z);
            //Sets texture to ObjectSquare texture[0]
            glBindTexture(GL_TEXTURE_2D, ObjectSquare_texture[0]);
            //GL Quads for the top of ObjectSquare
            glBegin(GL_QUADS);
                //Sets Texture Coordinates and drawing Coordinates
                glTexCoord2f(0, 0); glVertex3d(length / 2, length / 2, length / 2); //First
                glTexCoord2f(1, 0); glVertex3d(-length / 2, length / 2, length / 2); //Second
                glTexCoord2f(1, 1); glVertex3d(-length / 2, length / 2, -length / 2); //Third
                glTexCoord2f(0, 1); glVertex3d(length / 2, length / 2, -length / 2); //Fourth
            glEnd(); //Stops drawing
            //Sets the texture to ObjectSquare texture[1]
            glBindTexture(GL_TEXTURE_2D, ObjectSquare_texture[1]);
            //Draws GL Quads for left of ObjectSquare
            glBegin(GL_QUADS);
                //Setting Texture Coordinates and drawing coordinates
                glTexCoord2f(0, 0); glVertex3d(length / 2, length / 2, length / 2); //First
                glTexCoord2f(1, 0); glVertex3d(length / 2, length / 2, -length / 2); //Second
                glTexCoord2f(1, 1); glVertex3d(length / 2, -length / 2, -length / 2); //Third
                glTexCoord2f(0, 1); glVertex3d(length / 2, -length / 2, length / 2); //Fourth
            glEnd(); //Stops drawing
            //Sets texture to ObjectSquare texture[2]
            glBindTexture(GL_TEXTURE_2D, ObjectSquare_texture[2]);
            //Draws GL Quads for right of ObjectSquare
            glBegin(GL_QUADS);
                //Sets Texture Coordinates and drawing coordinates
                glTexCoord2f(1, 0); glVertex3d(-length / 2, length / 2, length / 2); //First
                glTexCoord2f(0, 0); glVertex3d(-length / 2, length / 2, -length / 2); //Second
                glTexCoord2f(0, 1); glVertex3d(-length / 2, -length / 2, -length / 2); //Third
                glTexCoord2f(1, 1); glVertex3d(-length / 2, -length / 2, length / 2); //Fourth
            glEnd(); //Stops drawing
            //Sets texture to ObjectSquare texture[3]
            glBindTexture(GL_TEXTURE_2D, ObjectSquare_texture[3]);
            //Draws GL Quads for back of ObjectSquare
            glBegin(GL_QUADS);
                //Sets Texture Coordinates and drawing coordinates
                glTexCoord2f(1, 0); glVertex3d(length / 2, length / 2, length / 2); //First
                glTexCoord2f(0, 0); glVertex3d(-length / 2, length / 2, length / 2); //Second
                glTexCoord2f(0, 1); glVertex3d(-length / 2, -length / 2, length / 2); //Third
                glTexCoord2f(1, 1); glVertex3d(length / 2, -length / 2, length / 2); //Fourth
            glEnd(); //Stops drawing
            //Sets the texture to ObjectSquare texture[4]
            glBindTexture(GL_TEXTURE_2D, ObjectSquare_texture[4]);
            //Draws GL Quads for front of ObjectSquare
            glBegin(GL_QUADS);
                //Sets Texture Coordinates and drawing coordinates
                glTexCoord2f(0, 0); glVertex3d(length / 2, length / 2, -length / 2); //First
                glTexCoord2f(1, 0); glVertex3d(-length / 2, length / 2, -length / 2); //Second
                glTexCoord2f(1, 1); glVertex3d(-length / 2, -length / 2, -length / 2); //Third
                glTexCoord2f(0, 1); glVertex3d(length / 2, -length / 2, -length / 2); //Fourth
            glEnd(); //Stops drawing
            //Sets the texture to ObjectSquare[5]
            glBindTexture(GL_TEXTURE_2D, ObjectSquare_texture[5]);
            //Draws GL Quads for bottom of ObjectSquare
            glBegin(GL_QUADS);
                //Sets Texture Coordinates and drawing coordinates
                glTexCoord2f(0, 1); glVertex3d(length / 2, -length / 2, length / 2); //First
                glTexCoord2f(1, 1); glVertex3d(-length / 2, -length / 2, length / 2); //Second
                glTexCoord2f(1, 0); glVertex3d(-length / 2, -length / 2, -length / 2); //Third
                glTexCoord2f(0, 0); glVertex3d(length / 2, -length / 2, -length / 2); //Fourth
            glEnd(); //Stops drawing
            glBindTexture(GL_TEXTURE_2D, 0);
            //Disables 2D Texturing
            glDisable(GL_TEXTURE_2D);
        //Pops off the stack
        glPopMatrix();
        //Sets up the lighting in the scene for SquareObject
        glMaterialfv(GL_FRONT, GL_AMBIENT_AND_DIFFUSE, color);
    }
};

//Defines the ObjectBall Class
class ObjectBall {
    
    //Creates private ObjectBall class variables
    double radius; //Variable for the ObjectBall radius
    GLfloat* color; //Variable for the ObjectBall color
    double x; //Variable for the ObjectBall x position
    double z; //Variable for the ObjectBall z position

public:
    
    //ObjectBall Constructor
    ObjectBall(double r, GLfloat* c, double x, double z): radius(r), color(c), x(x), z(z) {}
    
    //Creates the "draw" function to draw the ObjectBall
    void draw() {
        glEnable(GL_TEXTURE_2D); //Enables 2D textures
        glBindTexture(GL_TEXTURE_2D, sphere_texture); //Binds the sphere texture to use
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR); //Sets up texture parameters
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR); //Sets up texture parameters
        
        //Pushes onto the matrix stack
        glPushMatrix();
            //Picks the color to green
            glMaterialfv(GL_FRONT, GL_AMBIENT_AND_DIFFUSE, color);
            
            //Creates a quadric object
            GLUquadricObj * sphere;
            sphere = gluNewQuadric();
            //Makes the object texture-able
            gluQuadricTexture(sphere, GL_TRUE);
            
            //Translates the ObjectBall to the correct location
            glTranslated(x, 1, z);
            //Rotates the ObjectBall correctly
            glRotatef(90, 1.0, 0.0, 0.0);
            
            //Creates the sphere
            gluSphere(sphere, radius, 60, 60);
            
            //Disables 2D textures
            glDisable(GL_TEXTURE_2D);
        //Pops off the matrix stack
        glPopMatrix();
    }
};

//Creates checkerboard object
Checkerboard checkerboard(8, 8);
//Creates ObjectBall object
ObjectBall ObjectBall(1, WHITE, 1, 3.5);
//Creates ObjectSquare object
ObjectSquare ObjectSquare(WHITE, 2, 3.5, 3.5);
//Creates ObjectCylinder object
ObjectCylinder ObjectCylinder(WHITE, 2, 1, 6, 3.5);

//Initializing GL variables
void init() {
    glEnable(GL_DEPTH_TEST); //Scene Depth
    glLightfv(GL_LIGHT0, GL_DIFFUSE, WHITE); //Lighting diffusion
    glLightfv(GL_LIGHT0, GL_SPECULAR, WHITE); //Lighting specular
    glMaterialfv(GL_FRONT, GL_SPECULAR, WHITE); //While lighting specular
    glMaterialf(GL_FRONT, GL_SHININESS, 30); //Lighting shine
    glEnable(GL_LIGHTING); //Initializing lighting in the scene
    glEnable(GL_LIGHT0); //Initializing lighting in the scene
    checkerboard.create(); //Creation of checkerboard in scene
    glEnable(GL_TEXTURE_2D);
}

//Loading files
GLuint load(const char * filename) {
    //Creates a GLuint for filename
    GLuint id = SOIL_load_OGL_texture(filename, SOIL_LOAD_AUTO, SOIL_CREATE_NEW_ID, SOIL_FLAG_MIPMAPS);
    //Enabling textures
    glEnable(GL_TEXTURE_2D);
    //Connecting texture to points
    glBindTexture(GL_TEXTURE_2D, id);
    //Texture parameters
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR);
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR);
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT);
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT);
    //Unbinding textures
    glBindTexture(GL_TEXTURE_2D, 0);
    //Return for drawing purpose
    return id;
}

//Scene display
void display() {
    //Buffer color/depth
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT);
    //Identity matrix
    glLoadIdentity();
    //Putting functions to use
    gluLookAt(cam_position, cam_height, cam_depth, cam_position + cam_x, cam_height + cam_y, 3.5, cam_roll_1, 1.0 + cam_roll_2, 0.0);
    //Drawing all objects
    checkerboard.draw();
    ObjectBall.draw();
    ObjectSquare.draw();
    ObjectCylinder.draw();
    //Flushing scene
    glFlush();
    //Swapping buffers
    glutSwapBuffers();
    //Calling function for redisplay
    glutPostRedisplay();
}

//Function to load textures
void initTex() {
    //Loads the sphere texture
    sphere_texture = load("Bump-Map.jpg");
    //Loads the texture for each side of the ObjectSquare
    ObjectSquare_texture[0] = load("posy.jpg"); //Positive y face
    ObjectSquare_texture[1] = load("negx.jpg"); //Negative x face
    ObjectSquare_texture[2] = load("posx.jpg"); //Positive x face
    ObjectSquare_texture[3] = load("negz.jpg"); //Negative z face
    ObjectSquare_texture[4] = load("posz.jpg"); //Positive z face
    ObjectSquare_texture[5] = load("negy.jpg"); //Negative y face
    //Loads the ObjectCylinder texture
    ObjectCylinder_texture = load("Bump-Picture.jpg");
}

//Function to reshape
void reshape(GLint w, GLint h) {
    glViewport(0, 0, w, h); //Viewpoint
    glMatrixMode(GL_PROJECTION); //Projection
    glLoadIdentity(); //Loading identity matrix
    gluPerspective(40.0, GLfloat(w) / GLfloat(h), 1.0, 150.0); //Perspective
    glMatrixMode(GL_MODELVIEW); //Modelview matrix
}

//Handling keys
void KeyInput(int key, int, int) {
    //shift, alt, and ctrl handling
    int mod;
    
    //Switch case
    switch (key) {
        
        //Left input
        case GLUT_KEY_LEFT: {
            //Mod shift
            mod = glutGetModifiers();
            //Checking if control
            if (mod == GLUT_ACTIVE_CTRL) {
                //Update yaw
                cam_yaw += 2 * PI / 180;
                cam_x = tan(cam_yaw);
            }
            //Input is left
            else {
                //Moves  camera left
                cam_position += 1;
            }
            break;
        }
        
        //Right key handling
        case GLUT_KEY_RIGHT: {
            //Mod set
            mod = glutGetModifiers();
            //Check if mod is control
            if (mod == GLUT_ACTIVE_CTRL) {
                //Update yaw
                cam_yaw -= 2 * PI / 180;
                cam_x = tan(cam_yaw);
            }
            //Right input
            else {
                //Moves camera right
                cam_position -= 1;
            }
            break;
        }
        
        //Up key handling
        case GLUT_KEY_UP: {
            //Mod set
            mod = glutGetModifiers();
            //Checks if shift
            if (mod == GLUT_ACTIVE_SHIFT) {
                //Zooms in
                cam_depth += 1;
            }
            //Checks if control
            else if (mod == GLUT_ACTIVE_CTRL) {
                //Update pitch
                cam_pitch -= 2 * PI / 180;
                cam_y = tan(cam_pitch);
            }
            //Up input
            else {
                //Moves camera up
                cam_height += 1;
            }
            break;
        }
        
        //Down key handling
        case GLUT_KEY_DOWN: {
            //Mod Set
            mod = glutGetModifiers();
            //Check if shift
            if (mod == GLUT_ACTIVE_SHIFT) {
                //Zooms out
                cam_depth -= 1;
            }
            //Check if control
            else if (mod == GLUT_ACTIVE_CTRL) {
                //Update pitch
                cam_pitch += 2 * PI / 180;
                cam_y = tan(cam_pitch);
            }
            else {
                //Move camera
                cam_height -= 1;
            }
            break;
        }
    }
    //Call to redisplay
    glutPostRedisplay();
}

//Function to handle keys
void key_control(unsigned char key, int, int) {
    
    //Case handling input
    switch (key) {
        
        //if the input is "<"
        case ',': {
            //Updates roll
            roll_angle += 2 * PI / 180;
            cam_roll_1 = 2 * sin(roll_angle);
            cam_roll_2 = 2 * cos(roll_angle);
            break;
        }
        
        //if the input is ">"
        case '.': {
            //Updates roll
            roll_angle -= 2 * PI / 180;
            cam_roll_1 = 2 * sin(roll_angle);
            cam_roll_2 = 2 * cos(roll_angle);
            break;
        }
        
        //if the input is "e"
        case 'e': {
            //Exits code
            exit(0);
        }
        
        //if the input esc
        case 27: {
            //Exit program
            exit(0);
        }
        
        //if the input is "r"
        case 'r': {
            //Resets to restart the program
            cam_height = 3, cam_position = 3.5, cam_depth = -10;
            cam_x = 0, cam_y = 0;
            cam_pitch = 0, cam_yaw = 0, cam_roll_1 = 0, cam_roll_2 = 1, roll_angle = 0;
        }
    }
    //Call to redisplay
    glutPostRedisplay();
}

//Glut loop
int main(int argc, char** argv) {
    glutInit(&argc, argv); //Initialize GLUT
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH); //initial display modes for Depth, Double, and RGB
    glutInitWindowPosition(80, 80); //window position
    glutInitWindowSize(800, 600); //window size
    glutCreateWindow("Project 10"); //Window name
    init(); //Introducing the objects in the scene
    initTex(); //Introducing the textures in the scene
    glutDisplayFunc(display); //Display Function
    glutReshapeFunc(reshape); //Window reshape
    glutSpecialFunc(KeyInput); //Keyboard input
    glutKeyboardFunc(key_control); //Keyboard input
    glutMainLoop(); //GLUT Loop
}
