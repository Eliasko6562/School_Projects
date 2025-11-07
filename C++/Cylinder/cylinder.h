#pragma once
 
class cylinder {
private:
    float radius;
    float height;
public:
    cylinder();
    cylinder(float radius, float height);
    cylinder(const cylinder& c);
 
    ~cylinder();
 
    float getRadius() const;
    float getHeight() const;
 
    bool setRadius(float radius);
    bool setHeight(float height);
 
    float getVolume() const;
    float getSurface() const;
    float getBase() const;
    float getCasing() const;
 
    float getWaterHeight(float waterVolume) const;
};