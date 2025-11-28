#include <iostream>
#include <string>

using std::cout;
using std::endl;

class Person {
public:
    int name;
private:
    int age;

public:
    Person(int name, int age): name(name), age(1) {
        set_age(age);
    }

    ~Person() {

    }

    int get_age() {
        return age;
    }

    void set_age(int age) {
        if (age <= 0) {
            cout << "Nesmi" << endl;
            return;
        }
        this->age = age;
    }

    void birthday() {
        age++;
    }
};

void print_num(int num) {
    std::printf("%d\n", num);
}

void print_num(float num) {
    std::printf("%f\n", num);
}

int main() {
    Person osoba1(5, 5);

    cout << osoba1.get_age() << endl;
}
