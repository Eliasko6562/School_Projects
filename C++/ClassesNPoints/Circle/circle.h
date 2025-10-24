#pragma once
class circle {
private:
    int radius;

public:
    circle();
    ~circle();
    circle(int radius);
    circle(const circle &source);

    float circ() const;
    float area() const;
    float getRadius() const; 
    bool setRadius(int r); 
    void circleInfo() const;
};