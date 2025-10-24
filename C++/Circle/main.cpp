#include <iostream>
using std::cout;
using std::endl;

#include "circle.h"

int main() {
    circle c(10);
    
    cout << c.getRadius() << endl;
    cout << c.circ() << endl;
    cout << c.area() << endl;
    cout << c.setRadius(20) << endl;
    cout << c.getRadius() << endl;
    cout << c.circ() << endl;
    cout << c.area() << endl;
}