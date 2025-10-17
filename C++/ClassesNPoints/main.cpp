#include <iostream>
#include "point.h"
#include <iomanip>

using std::cin;
using std::cout;
using std::endl;
using std::setprecision;

int main() {
    point point_1;
    point point_2(5, 20);

    cout << setprecision(2) << std::fixed << point_2.distance(point_1) << endl;
}