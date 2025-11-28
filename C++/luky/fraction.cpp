#include "fraction.h"

#include <numeric>
#include <iostream>

using std::cout;
using std::endl;

void Fraction::swap(int &a, int &b) {
    int temp = a;
    a = b;
    b = temp;
}

Fraction::Fraction(): numerator(1), denominator(1) {}

Fraction::Fraction(int numerator, int denominator): numerator(numerator), denominator(1) {
    set_denominator(denominator);
}

Fraction::Fraction(const Fraction &f): numerator(f.get_numerator()), denominator(f.get_denominator()) {}

int Fraction::get_numerator() const {
    return numerator;
}

int Fraction::get_denominator() const {
    return denominator;
}

void Fraction::set_numerator(int numerator) {
    this->numerator = numerator;
}

void Fraction::set_denominator(int denominator) {
    if (denominator == 0) {
        cout << "Denominator cannot be zero. Setting to 1 instead." << endl;
        this->denominator = 1;
    }
    this->denominator = denominator;
}

void Fraction::set_fraction(int numerator, int denominator) {
    this->numerator = numerator;
    return set_denominator(denominator);
}

double Fraction::to_decimal(int numerator, int denominator) {
    if (denominator == 0) {
        cout << "Denominator cannot be zero." << endl;
        return 0.0;
    }
    return static_cast<double>(numerator) / denominator;
}

bool Fraction::flip() {
    if (numerator == 0) {
        cout << "Cannot flip a fraction with a numerator of zero." << endl;
        return false;
    }
    swap(numerator, denominator);
    return true;
}

void Fraction::shrink() {
    int divisor = std::gcd(numerator, denominator);
    numerator /= divisor;
    denominator /= divisor;
}

Fraction& Fraction::operator=(const Fraction &f) {
    if (this != &f) {
        numerator = f.numerator;
        denominator = f.denominator;
    }
    return *this;
}

Fraction Fraction::operator+(const Fraction &f) const {
    int new_numerator = numerator * f.denominator + f.numerator * denominator;
    int new_denominator = denominator * f.denominator;
    return Fraction(new_numerator, new_denominator);
}

Fraction Fraction::operator-(const Fraction &f) const {
    int new_numerator = numerator * f.denominator - f.numerator * denominator;
    int new_denominator = denominator * f.denominator;
    return Fraction(new_numerator, new_denominator);
}

Fraction Fraction::operator*(const Fraction &f) const {
    int new_numerator = numerator * f.numerator;
    int new_denominator = denominator * f.denominator;
    return Fraction(new_numerator, new_denominator);
}

Fraction Fraction::operator/(const Fraction &f) const {
    int new_numerator = numerator * f.denominator;
    int new_denominator = denominator * f.numerator;
    return Fraction(new_numerator, new_denominator);
}

Fraction& Fraction::operator+=(const Fraction &f) {
    *this = *this + f;
    return *this;
}

Fraction& Fraction::operator-=(const Fraction &f) {
    *this = *this - f;
    return *this;
}

Fraction& Fraction::operator*=(const Fraction &f) {
    *this = *this * f;
    return *this;
}

Fraction& Fraction::operator/=(const Fraction &f) {
    *this = *this / f;
    return *this;
}