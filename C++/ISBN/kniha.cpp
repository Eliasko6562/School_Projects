#include "kniha.h"
#include <cctype>
#include <algorithm>

// Constructor without parameters (default values)
Kniha::Kniha(): ISBN("978-0-321-56384-2"), author("Bjarne Soustrup"), bookName("The C++ Programming Language") {}

// Constructor with parameters
Kniha::Kniha(const std::string& isbn, const std::string& author, const std::string& bookName)
    : ISBN(""), author("None"), bookName("None") {
    if (isValidISBN(isbn) &&
        isValidAuthor(author) &&
        isValidBookName(bookName)) {
        this->ISBN = isbn;
        this->author = author;
        this->bookName = bookName;
    }
}

// Copy constructor
Kniha::Kniha(const Kniha& other): ISBN(other.ISBN), author(other.author), bookName(other.bookName) {}

Kniha& Kniha::operator=(const Kniha& other) {
    if (this != &other) {
        ISBN = other.ISBN;
        author = other.author;
        bookName = other.bookName;
    }
    return *this;
}

bool Kniha::operator==(const Kniha& other) const {
    return ISBN == other.ISBN &&
           author == other.author &&
           bookName == other.bookName;
}

std::ostream& operator<<(std::ostream& os, const Kniha& book) {
    os << "ISBN: " << book.ISBN << "\n";
    os << "Prefix: " << book.getISBNPrefix() << "\n";
    os << "Region: " << book.getISBNRegion() << "\n";
    os << "Publisher: " << book.getISBNPublisher() << "\n";
    os << "Edition: " << book.getISBNEdition() << "\n";
    os << "ISBN bez oddělovačů: " << book.getISBNWithoutSeparators() << "\n";
    os << "Délka ISBN bez oddělovačů: " << book.getISBNLength() << "\n";
    os << "Autor: " << book.author << "\n";
    os << "Název knihy: " << book.bookName;
    return os;
}

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

bool Kniha::isValidText(const std::string& text, int minLength, int maxLength) const {
    return static_cast<int>(text.length()) >= minLength &&
           static_cast<int>(text.length()) <= maxLength;
}

//Pomocne metody pro validaci autora a názvu knihy
bool Kniha::isValidAuthor(const std::string& authorName) const {
    return isValidText(authorName, AUTHOR_MIN_LENGTH, AUTHOR_MAX_LENGTH);
}

bool Kniha::isValidBookName(const std::string& bookName) const {
    return isValidText(bookName, BOOK_NAME_MIN_LENGTH, BOOK_NAME_MAX_LENGTH);
}

static std::string getISBNPart(const std::string& isbn, int targetIndex) {
    std::string current;
    int currentIndex = 0;
    for (char c : isbn) {
        if (c == '-' || c == ' ') {
            if (!current.empty()) {
                if (currentIndex == targetIndex) {
                    return current;
                }
                current.clear();
                currentIndex++;
            }
        } else {
            current.push_back(c);
        }
    }
    if (!current.empty() && currentIndex == targetIndex) {
        return current;
    }
    return "";
}

static int countISBNParts(const std::string& isbn) {
    std::string current;
    int count = 0;
    for (char c : isbn) {
        if (c == '-' || c == ' ') {
            if (!current.empty()) {
                count++;
                current.clear();
            }
        } else {
            current.push_back(c);
        }
    }
    if (!current.empty()) {
        count++;
    }
    return count;
}

std::string Kniha::getISBNWithoutSeparators() const {
    if (!verifyISBN()) return "";
    std::string clean = ISBN;
    clean.erase(std::remove_if(clean.begin(), clean.end(),
                               [](char c) { return c == '-' || c == ' '; }), clean.end());
    return clean;
}

int Kniha::getISBNLength() const {
    return static_cast<int>(getISBNWithoutSeparators().length());
}

std::string Kniha::getISBNPrefix() const {
    if (!verifyISBN()) return "";
    if (getISBNLength() == 13) {
        int partCount = countISBNParts(ISBN);
        if (partCount >= 5) {
            return getISBNPart(ISBN, 0);
        }
        return getISBNWithoutSeparators().substr(0, 3);
    }
    return "";
}

std::string Kniha::getISBNRegion() const {
    if (!verifyISBN()) return "";
    int partCount = countISBNParts(ISBN);
    if (getISBNLength() == 13 && partCount >= 5) {
        return getISBNPart(ISBN, 1);
    }
    if (getISBNLength() == 10 && partCount >= 4) {
        return getISBNPart(ISBN, 0);
    }
    return "";
}

std::string Kniha::getISBNPublisher() const {
    if (!verifyISBN()) return "";
    int partCount = countISBNParts(ISBN);
    if (getISBNLength() == 13 && partCount >= 5) {
        return getISBNPart(ISBN, 2);
    }
    if (getISBNLength() == 10 && partCount >= 4) {
        return getISBNPart(ISBN, 1);
    }
    return "";
}

std::string Kniha::getISBNEdition() const {
    if (!verifyISBN()) return "";
    int partCount = countISBNParts(ISBN);
    if (getISBNLength() == 13 && partCount >= 5) {
        return getISBNPart(ISBN, 3);
    }
    if (getISBNLength() == 10 && partCount >= 4) {
        return getISBNPart(ISBN, 2);
    }
    return "";
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
    }
}

void Kniha::setAuthor(const std::string& authorName) {
    if (isValidAuthor(authorName)) {
        author = authorName;
    }
}

void Kniha::setBookName(const std::string& name) {
    if (isValidBookName(name)) {
        bookName = name;
    }
}

void Kniha::setBook(const std::string& isbn, const std::string& authorName, const std::string& name) {
    if (isValidISBN(isbn) &&
        isValidText(authorName, AUTHOR_MIN_LENGTH, AUTHOR_MAX_LENGTH) &&
        isValidText(name, BOOK_NAME_MIN_LENGTH, BOOK_NAME_MAX_LENGTH)) {
        ISBN = isbn;
        author = authorName;
        bookName = name;
    }
}

// Verify ISBN validity
bool Kniha::verifyISBN() const {
    return !ISBN.empty() && isValidISBN(ISBN);
}
