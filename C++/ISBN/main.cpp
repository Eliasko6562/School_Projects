#include <iostream>
#include "kniha.h"

using namespace std;

int main() {
    cout << "=== ISBN Book Class Demo ===" << endl << endl;
    
    // Test 1: Default constructor
    cout << "Test 1: Default Constructor" << endl;
    Kniha book1;
    cout << "ISBN: " << book1.getISBN() << endl;
    cout << "Author: " << book1.getAuthor() << endl;
    cout << "Book Name: " << book1.getBookName() << endl;
    cout << "ISBN valid: " << (book1.verifyISBN() ? "Yes" : "No") << endl << endl;
    
    // Test 2: Constructor with valid ISBN-10
    cout << "Test 2: Constructor with valid ISBN-10" << endl;
    Kniha book2("0-306-40615-2", "Isaac Asimov", "Foundation");
    cout << "ISBN: " << book2.getISBN() << endl;
    cout << "Author: " << book2.getAuthor() << endl;
    cout << "Book Name: " << book2.getBookName() << endl;
    cout << "ISBN valid: " << (book2.verifyISBN() ? "Yes" : "No") << endl << endl;
    
    // Test 3: Constructor with valid ISBN-13
    cout << "Test 3: Constructor with valid ISBN-13" << endl;
    Kniha book3("978-0-306-40615-7", "J.R.R. Tolkien", "The Lord of the Rings");
    cout << "ISBN: " << book3.getISBN() << endl;
    cout << "Author: " << book3.getAuthor() << endl;
    cout << "Book Name: " << book3.getBookName() << endl;
    cout << "ISBN valid: " << (book3.verifyISBN() ? "Yes" : "No") << endl << endl;
    
    // Test 4: Constructor with invalid ISBN
    cout << "Test 4: Constructor with invalid ISBN" << endl;
    Kniha book4("123-456-789", "Unknown Author", "Invalid Book");
    cout << "ISBN: " << book4.getISBN() << endl;
    cout << "Author: " << book4.getAuthor() << endl;
    cout << "Book Name: " << book4.getBookName() << endl;
    cout << "ISBN valid: " << (book4.verifyISBN() ? "Yes" : "No") << endl << endl;
    
    // Test 5: Copy constructor
    cout << "Test 5: Copy Constructor" << endl;
    Kniha book5 = book2;
    cout << "Copied ISBN: " << book5.getISBN() << endl;
    cout << "Copied Author: " << book5.getAuthor() << endl;
    cout << "Copied Book Name: " << book5.getBookName() << endl << endl;
    
    // Test 6: Setters
    cout << "Test 6: Using Setters" << endl;
    book1.setISBN("0-306-40615-2");
    book1.setAuthor("C.S. Lewis");
    book1.setBookName("The Chronicles of Narnia");
    cout << "Updated ISBN: " << book1.getISBN() << endl;
    cout << "Updated Author: " << book1.getAuthor() << endl;
    cout << "Updated Book Name: " << book1.getBookName() << endl;
    cout << "ISBN valid: " << (book1.verifyISBN() ? "Yes" : "No") << endl;
    
    return 0;
}
