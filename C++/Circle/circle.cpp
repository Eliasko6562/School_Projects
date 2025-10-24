#include "circle.h"

#include <cmath>
using std::pow;

#include <iostream>
using std::cout;
using std::endl;

circle::circle(): radius(1) {}

circle::circle(int radius): radius(1) {
    setRadius(radius);
}

circle::circle(const circle &source): radius(source.getRadius()) {}

circle::~circle() {}

float circle::circ() const {
    return 2 * M_PI * radius;
}

float circle::area() const {
    return M_PI * pow(radius, 2);
}

float circle::getRadius() const {
    return radius;
}

bool circle::setRadius(int r) {
    if (r > 0) {
        radius = r;
        return true;
    }
    return false;
}

void circle::circleInfo() const {
    cout << "Radius: " << getRadius() << endl;
    cout << "Circumference: " << circ() << endl;
    cout << "Area: " << area() << endl;
}