#include "point.h"
#include <cmath>

point::point():x(0),y(0) {}
point::point(int x, int y):x(x),y(y) {}
point::point(const point & point2):x(point2.getX()),y(point2.getY()) {}  

int point::getX() const {
    return x;
}

int point::getY() const {
    return y;
}

void point::setX(int x) {
    this->x = x;
}

void point::setY(int y) {
    this->y = y;
}

double point::distance(const point & point2) const {
    return sqrt(pow(this->getX() - point2.getX(), 2) + 
                pow(this->getY() - point2.getY(), 2));
}