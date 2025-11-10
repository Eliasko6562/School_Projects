#pragma once

class cuboid {
private:
    int s1;
    int s2;
    int h;
public:
    cuboid();
    ~cuboid();
    cuboid(int s1, int s2, int h);
    cuboid(const cuboid &source);

    float surfaceArea() const;
    float volume() const;
    float getS1() const;
    float getS2() const;
    float getH() const;
    bool setS1(int s1);
    bool setS2(int s1);
    bool setH(int s1);
    void cuboidInfo() const;
};