// This program generates a Sierpinski gasket with 10000 points.

#include <iostream>
#ifdef __APPLE_CC__
#include <GLUT/glut.h>
#else
#include <GL/glut.h>
#endif
#include <cstdlib>


// Here, we create a 3D class. It includes x and y coordinates to keep information organized.
// A midpoint function is included to help with centering.

struct Point3D {
    GLfloat x, y, z;
    Point3D(GLfloat x, GLfloat y, GLfloat z) : x(x), y(y), z(z) {}
    Point3D midpoint(Point3D p) { return Point3D((x + p.x) / 2, (y + p.y) / 2, (z + p.z) / 2); }
};

// Here, we create a 2D class. it includes x and y coordinates to keep information organized.
// A midpoint functino is included to help with centering.

struct Point {
    GLfloat x, y;
    Point(GLfloat x = 0, GLfloat y = 0) : x(x), y(y) {}
    Point midpoint(Point p) { return Point((x + p.x) / 2.0, (y + p.y) / 2.0); }
};

// Reshaping the view angle and projection of the graphic is important in order to view
// the rendering at an appropriate angle. This section of code ensures that the perspective
// is consistent if the window is reshaped.

void reshape(GLint w, GLint h) {
    glViewport(0, 0, w, h);
    glMatrixMode(GL_PROJECTION);
    glLoadIdentity();
    gluPerspective(100.0, GLfloat(w) / GLfloat(h), 10.0, 1500.0);
}

// Display requests are computed here.
void display3D() {
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT);
}

// Rendering of the next 500 points is done here.
void generateMorePoints() {

    // The tetrahedron has four vertices.  We also have to keep track of the
    // current point during the plotting.
    static Point3D vertices[4] = {
      Point3D(-250, -225, -200),
      Point3D(-150, -225, -700),
      Point3D(250, -225, -275),
      Point3D(0, 450, -500)
    };
    static Point3D lastPoint = vertices[0];
    
    // This section of code introduces shading to give even more perspective.
    // If points are displayed closer to the perspective camera, they will display brighter,
    // as if a light source is at the camera.
    glBegin(GL_POINTS);
    for (int i = 0; i <= 500; i++) {
        lastPoint = lastPoint.midpoint(vertices[rand() % 4]);
        GLfloat intensity = (700 + lastPoint.z) / 500.0;
        glColor3f(intensity, intensity, 0.25);
        glVertex3f(lastPoint.x, lastPoint.y, lastPoint.z);
    }
    glEnd();
    glFlush();
}

// Triangle is drawn with a termination point to ensure it doesn't render forever.
void display() {

    glClear(GL_COLOR_BUFFER_BIT);

    static Point vertices[] = { Point(0, 0), Point(200, 500), Point(500, 0) };

    // creating 100000 new points in the render
    static Point p = vertices[0];
    glBegin(GL_POINTS);
    for (int k = 0; k < 100000; k++) {
            p = p.midpoint(vertices[rand() % 3]);
            glVertex2f(p.x, p.y);
    }
    glEnd();
    glFlush();
}

void init3D() {
    glEnable(GL_DEPTH_TEST);
}

// setting color
void init() {

    // Setting a bright pink color for the background and yellow for rendering for a viewable
    // contrast.
    glClearColor(0.75, 0.0, 0.3, 0.75);
    glColor3f(0.8, 0.75, 0.3);

    // Viewing with origin on the bottom left
    glMatrixMode(GL_PROJECTION);
    glLoadIdentity();
    glOrtho(0.0, 500.0, 0.0, 700.0, 0.0, 1.0);
}

using namespace std;

// Initializing callbacks, GLUT, display settings, and the main rendering window.
int main(int argc, char** argv) {
    
    string answer;
    bool response = false;

    while (response == false) {

        cout << "input '2D' for 2D render and '3D' for 3D render" << endl;
        cin >> answer;

        if (answer == "2D") {
            glutInit(&argc, argv);
            glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB);
            glutInitWindowSize(700, 700);
            glutInitWindowPosition(40, 40);
            glutCreateWindow("Sierpinski Gasket");
            glutDisplayFunc(display);
            init();
            glutMainLoop();
            response = true;
        }
        else if (answer == "3D") {
            glutInit(&argc, argv);
            glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB | GLUT_DEPTH);
            glutInitWindowSize(500, 500);
            glutInitWindowPosition(0, 0);
            glutCreateWindow("Sierpinski Tetrahedron");
            glutDisplayFunc(display3D);
            glutReshapeFunc(reshape);
            glutIdleFunc(generateMorePoints);
            init3D();
            glutMainLoop();
            response = true;
        }
        else
        {
            cout << "Input could not be read, please try again." << endl;
        }
    }
}

