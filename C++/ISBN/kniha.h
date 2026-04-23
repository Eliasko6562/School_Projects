#pragma once
#include <string>

class Kniha {
    private:
        std::string ISBN;
        std::string author;
        std::string bookName;
        
        // Helper function to validate ISBN format
        bool isValidISBN(const std::string& isbn) const;

    public:
        // Constructor without parameters (default values)
        Kniha();
        
        // Constructor with parameters
        Kniha(const std::string& isbn, const std::string& author, const std::string& bookName);
        
        // Copy constructor
        Kniha(const Kniha& other);
        
        // Getters
        std::string getISBN() const;
        std::string getAuthor() const;
        std::string getBookName() const;
        
        // Setters
        void setISBN(const std::string& isbn);
        void setAuthor(const std::string& author);
        void setBookName(const std::string& bookName);
        
        // Verify ISBN validity
        bool verifyISBN() const;
};