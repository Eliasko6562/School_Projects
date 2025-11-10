#pragma once

class square {
private:
    int side;
public:
    square();
    ~square();
    square(int side);
    square(const square &source);

    float perimeter() const;
    float area() const;
    float getSide() const;
    bool setSide(int s);
    void squareInfo() const;
};