#ifndef POINT_POINT_H
#define POINT_POINT_H

class point {
private:
    int x;
    int y;
public:
    point(int x, int y);
    point();
    point(const point &);
    int getX() const;
    int getY() const;
    void setX(int x);
    void setY(int y);
    double distance(const point& point2) const;
};

#endif //POINT_POINT_H