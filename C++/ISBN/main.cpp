#include <iostream>
#include <string>
#include "kniha.h"

using std::cout;
using std::cin;
using std::getline;
using std::string;
using std::endl;

static string readLine(const string& prompt) {
    cout << prompt;
    string line;
    getline(cin, line);
    return line;
}

int main() {
    cout << "=== Ukázky výpisu ===" << endl << endl;

    // k1 default constructor
    Kniha k1;
    cout << "Objekt k1 vytvořen výchozím konstruktorem" << endl;
    cout << k1 << endl << endl;

    // k2 constructor with parameters
    Kniha k2("978-80-251-1583-1", "Jesse Liberty", "Naučte se C++ za 21 dní ");
    cout << "Objekt k2 vytvořen konstruktorem s parametry" << endl;
    cout << k2 << endl << endl;

    // k3 copy constructor
    Kniha k3 = k1;
    cout << "Objekt k3 vytvořen kopírovacím konstruktorem" << endl;
    cout << k3 << endl << endl;

    // k4(user input) = k1(changed with setters)
    cout << "Zadejte údaje o k4:" << endl;
    string isbn = readLine("ISBN: ");
    string author = readLine("Autor: ");
    string name = readLine("Název: ");

    Kniha k4;
    k4.setBook(isbn, author, name);
    cout << "Objekt k4 vytvořen z uživatelského vstupu" << endl;
    cout << k4 << endl << endl;

    cout << "Změníme k1 pomocí setterů a přiřadíme jej do k4." << endl;
    k1.setISBN("978-0-321-56384-2");
    k1.setAuthor("Bjarne Soustrup");
    k1.setBookName("The C++ Programming Language");
    k4 = k1;
    cout << "Objekt k4 po přiřazení z k1:" << endl;
    cout << k4 << endl;

    return 0;
}
