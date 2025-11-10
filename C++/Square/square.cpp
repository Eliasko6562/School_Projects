#include <square.h>

#include <iostream>
using std::cout;
using std::endl;

#include <cmath>
using std::pow;

square::square(): side(1) {}

square::square(int side): side(1) {
    setSide(side);
}

square::square(const square &source): side(source.getSide()) {}

square::~square() {}

float square::perimeter() const {
    return 4 * side;
}

float square::area() const {
    return pow(side, 2);
}

float square::getSide() const {
    return side;
}

bool square::setSide(int s) {
    if (s > 0) {
        side = s;
        return true;
    }
    return false;
}

void square::squareInfo() const {
    cout << "Side Length: " << getSide() << endl;
    cout << "Perimeter: " << perimeter() << endl;
    cout << "Area: " << area() << endl;
}