#include "circle.h"

#include <cmath>
using std::pow;

circle::circle(int radius): radius(radius) {}

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