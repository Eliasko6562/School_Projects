#include <cuboid.h>

#include <iostream>
using std::cout;
using std::endl;

cuboid::cuboid(): s1(1), s2(1), h(1) {}

cuboid::~cuboid() {}

cuboid::cuboid(int s1, int s2, int h): s1(1), s2(1), h(1) {
    setS1(s1);
    setS2(s2);
    setH(h);
}

cuboid::cuboid(const cuboid &source): s1(source.getS1()), s2(source.getS2()), h(source.getH()) {}

float cuboid::surfaceArea() const {
    return 2 * (s1 * s2 + s1 * h + s2 * h);
}

float  cuboid::volume() const {
    return s1 * s2 * h;
}

float cuboid::getS1() const {
    return s1;
}

float cuboid::getS2() const {
    return s2;
}

float cuboid::getH() const {
    return h;
}

bool cuboid::setS1(int s1) {
    if (s1 > 0) {
        this->s1 = s1;
        return true;
    }
    return false;
}

bool cuboid::setS2(int s2) {
    if (s2 > 0) {
        this->s2 = s2;
        return true;
    }
    return false;
}

bool cuboid::setH(int h) {
    if (h > 0) {
        this->h = h;
        return true;
    }
    return false;
}

void cuboid::cuboidInfo() const {
    cout << "Side 1: " << getS1() << endl;
    cout << "Side 2: " << getS2() << endl;
    cout << "Height: " << getH() << endl;
    cout << "Surface Area: " << surfaceArea() << endl;
    cout << "Volume: " << volume() << endl;
}