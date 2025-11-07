#include <iostream>
using std::cin;
using std::cout;
using std::endl;
 
#include "cylinder.h"
 
#define WATER_VOLUME 10.f
 
int main() {
    cylinder c1;
    cylinder c2(5.6f, 5.2f);
    cylinder c3(c2);
 
    float r;
    float h;
    float w;
 
    cout << "Cylinder radius (cm): ";
    cin >> r;
    cout << "Cylinder height (cm): ";
    cin >> h;
    cout << "Water volume (dl): ";
    cin >> w;
 
    c1.setRadius(r);
    c1.setHeight(h);
 
    cout << "\n";
 
    cout << "Cylinder volume: " << c1.getVolume() << "cm3" << endl;
    cout << "Cylinder surface: " << c1.getSurface() << "cm2" << endl;
    cout << "Cylinder base: " << c1.getBase() << "cm2" << endl;
    cout << "Cylinder casing: " << c1.getCasing() << "cm2" << endl;
 
    float waterHeight = c1.getWaterHeight(w);
    if (waterHeight >= 0.f) {
        cout << "Cylinder water height: " << waterHeight << "cm" << endl;
    } else {
        cout << "Water doesn't fit in the cylinder" << endl;
    }
}