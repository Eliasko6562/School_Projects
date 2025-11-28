#pragma once

class Fraction{
    private:
        int numerator;
        int denominator;

        void swap(int &a, int &b);
    public:
        Fraction();
        ~Fraction() = default;

        Fraction(int numerator, int denominator);
        Fraction(const Fraction &f);

        int get_numerator() const;
        int get_denominator() const;

        void set_numerator(int numerator);
        void set_denominator(int denominator);
        void set_fraction(int numerator, int denominator);

        double to_decimal(int numerator, int denominator);

        bool flip();
        void shrink();

        Fraction& operator=(const Fraction &f);

        Fraction operator+(const Fraction &f) const;
        Fraction operator-(const Fraction &f) const;
        Fraction operator*(const Fraction &f) const;
        Fraction operator/(const Fraction &f) const;
        
        Fraction& operator+=(const Fraction &f);
        Fraction& operator-=(const Fraction &f);
        Fraction& operator*=(const Fraction &f);
        Fraction& operator/=(const Fraction &f);
};



