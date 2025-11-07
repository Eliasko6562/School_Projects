#include <cmath>
#include <iostream>
using std::cout;
using std::endl;
 
#include "cylinder.h"
 
cylinder::cylinder(): radius(1.f), height(1.f) {}
cylinder::cylinder(float radius, float height): radius(1.f), height(1.f) {
    this->setRadius(radius);
    this->setHeight(height);
}
cylinder::cylinder(const cylinder& c): radius(c.getRadius()), height(c.getHeight()) {}
 
cylinder::~cylinder() {}
 
float cylinder::getRadius() const {
    return radius;
}
 
float cylinder::getHeight() const {
    return height;
}
 
bool cylinder::setRadius(float radius) {
    if (radius <= 0.f) {
        cout << "error: radius has to be more than zero" << endl;
        return false;
    }
    this->radius = radius;
    return true;
}
 
bool cylinder::setHeight(float height) {
    if (height <= 0.f) {
        cout << "error: height has to be more than zero" << endl;
        return false;
    }
    this->height = height;
    return true;
}
 
float cylinder::getVolume() const {
    return getBase() * height;
}
 
float cylinder::getSurface() const {
    return getBase() + getCasing();
}
 
float cylinder::getBase() const {
    return M_PI * radius * radius;
}
 
float cylinder::getCasing() const {
    return 2 * M_PI * radius * height;
}
 
float cylinder::getWaterHeight(float waterVolume) const {
    float h = (waterVolume * 100.f) / getBase();
    if (h > height) {
        return -1.f;
    }
    return h;
}