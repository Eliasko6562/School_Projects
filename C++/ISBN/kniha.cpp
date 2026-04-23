#include "kniha.h"
#include <cctype>
#include <algorithm>

// Constructor without parameters (default values)
Kniha::Kniha(): ISBN(""), author("None"), bookName("None") {}

// Constructor with parameters
Kniha::Kniha(const std::string& isbn, const std::string& author, const std::string& bookName) {
    setISBN(isbn);
    setAuthor(author);
    setBookName(bookName);
}

// Copy constructor
Kniha::Kniha(const Kniha& other): ISBN(other.ISBN), author(other.author), bookName(other.bookName) {}

// Helper function to validate ISBN format
bool Kniha::isValidISBN(const std::string& isbn) const {
    // Remove hyphens and spaces
    std::string cleanISBN = isbn;
    cleanISBN.erase(std::remove_if(cleanISBN.begin(), cleanISBN.end(), 
                    [](char c) { return c == '-' || c == ' '; }), cleanISBN.end());
    
    // Check if it's ISBN-10 or ISBN-13
    if (cleanISBN.length() == 10) {
        // Validate ISBN-10: all characters must be digits except possibly last character (can be X)
        for (int i = 0; i < 9; i++) {
            if (!std::isdigit(cleanISBN[i])) return false;
        }
        if (!std::isdigit(cleanISBN[9]) && cleanISBN[9] != 'X') return false;
        
        // Validate checksum: sum of (digit * position) must be divisible by 11
        int sum = 0;
        for (int i = 0; i < 10; i++) {
            int digit = (cleanISBN[i] == 'X') ? 10 : (cleanISBN[i] - '0');
            sum += digit * (10 - i);
        }
        return sum % 11 == 0;
    } 
    else if (cleanISBN.length() == 13) {
        // Validate ISBN-13: all characters must be digits
        for (char c : cleanISBN) {
            if (!std::isdigit(c)) return false;
        }
        
        // Validate checksum: alternating sum weighted by 1,3,1,3... must be divisible by 10
        int sum = 0;
        for (int i = 0; i < 13; i++) {
            int digit = cleanISBN[i] - '0';
            int weight = (i % 2 == 0) ? 1 : 3;
            sum += digit * weight;
        }
        return sum % 10 == 0;
    }
    
    return false;
}

// Getters
std::string Kniha::getISBN() const {
    return ISBN;
}

std::string Kniha::getAuthor() const {
    return author;
}

std::string Kniha::getBookName() const {
    return bookName;
}

// Setters
void Kniha::setISBN(const std::string& isbn) {
    if (isValidISBN(isbn)) {
        ISBN = isbn;
    } else {
        ISBN = "";  // Invalid ISBN
    }
}

void Kniha::setAuthor(const std::string& authorName) {
    author = authorName;
}

void Kniha::setBookName(const std::string& name) {
    bookName = name;
}

// Verify ISBN validity
bool Kniha::verifyISBN() const {
    return !ISBN.empty() && isValidISBN(ISBN);
}
