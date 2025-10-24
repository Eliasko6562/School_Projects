#ifndef CIRCLE_H
#define CIRCLE_H

class circle {
private:
    int radius;
public:
    circle(int radius);
    float circ() const;
    float area() const;
    float getRadius() const; 
    bool setRadius(int r); 
};

#endif // CIRCLE_H