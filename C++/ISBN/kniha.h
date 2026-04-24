#pragma once

#include <string>
#include <ostream>

#define AUTHOR_MIN_LENGTH 1
#define AUTHOR_MAX_LENGTH 100
#define BOOK_NAME_MIN_LENGTH 1
#define BOOK_NAME_MAX_LENGTH 200

using std::string;
class Kniha {
    private:
        string ISBN;
        string author;
        string bookName;
        
        // Helper functions to validate inputs
        bool isValidISBN(const string& isbn) const;
        bool isValidAuthor(const string& authorName) const;
        bool isValidBookName(const string& bookName) const;
        bool isValidText(const string& text, int minLength, int maxLength) const;

    public:
        // Constructor without parameters (default values)
        Kniha();
        
        // Constructor with parameters
        Kniha(const string& isbn, const string& author, const string& bookName);
        
        // Copy constructor
        Kniha(const Kniha& other);
        
        // Operator overloads
        Kniha& operator=(const Kniha& other);
        bool operator==(const Kniha& other) const;
        
        // Output operator
        friend std::ostream& operator<<(std::ostream& os, const Kniha& book);
        
        // Getters
        string getISBN() const;
        string getAuthor() const;
        string getBookName() const;
        
        // Setters
        void setISBN(const string& isbn);
        void setAuthor(const string& author);
        void setBookName(const string& bookName);
        void setBook(const string& isbn, const string& author, const string& bookName);

        // ISBN helpers
        string getISBNPrefix() const;
        string getISBNRegion() const;
        string getISBNPublisher() const;
        string getISBNEdition() const;
        string getISBNWithoutSeparators() const;
        int getISBNLength() const;
        
        // Verify ISBN validity
        bool verifyISBN() const;
};