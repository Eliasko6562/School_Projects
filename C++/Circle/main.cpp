#include <iostream>
using std::cout;
using std::endl;

#include "circle.h"

int main() {
    circle c(23);
    
    cout << c.circ() << endl;
    cout << c.area() << endl;
}