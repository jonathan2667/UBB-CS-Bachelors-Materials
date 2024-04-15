#include "Set.h"
#include "SetIterator.h"


Set::Set() {
	this->head = nullptr;
	length = 0;
}

//adds an element to the set
//returns true if the element was added, false otherwise (if the element was already in the set and it was not added)
//BC = Theta(1) - daca e primul elemetn adaugat
//WC = Theta(n) - daca elementul nu exista deja in set
//TC = O(n)
bool Set::add(TElem elem) {
    // Verificam daca elementul exista deja in set
    Node* current = head;
    while (current != nullptr) {
        if (current->data == elem) {
            return false; // Elementul exista deja in set si nu poate fi adaugat
        }
        current = current->next;
    }

    // Adaugam elementul in set
    // Cream un nou nod
    Node* newNode = new Node;
    newNode->data = elem;
    newNode->next = head;
    head = newNode; 


    length++;

    return true; // am adaugat nod
}


//removes an element from the set
//returns true if e was removed, false otherwise
//BC = Theta(1) - daca e primul elemetn adaugat
//WC = Theta(n) - daca elementul nu exista deja in set
//TC = O(n)
bool Set::remove(TElem elem) {
    Node* current = head;
    Node* prev = nullptr;

    // gasim elementul de sters
    while (current != nullptr) {
        if (current->data == elem) {
            // l-am gasit, il stergem
            if (prev == nullptr) {
                // elementul e la inceput
                head = current->next;
            }
            else {
                // elementul nu e la inceput
                prev->next = current->next;
            }

            //stegem nodul curent
            delete current;

            //scad lungimea setului
            length--;

            return true; // elementul a fost sters
        }

        // ne mutam la urmatorul nod si continuam cautarea
        prev = current;
        current = current->next;
    }

    return false; // elementul nu a fost gasit
}

//checks whether an element belongs to the set or not
//BC = Theta(1) - daca e primul elemetn adaugat
//WC = Theta(n) - daca elementul nu exista deja in set
//TC = O(n)
bool Set::search(TElem elem) const {
    Node* current = head;
    while (current != nullptr) {
        if (current->data == elem) {
            return true; // Element found
        }
        current = current->next;
    }
    return false; // Element not found
}


//returns the number of elements;
//BC = Theta(1) - constant
//WC = Theta(1) - constant
//TC =Theta(1)
int Set::size() const {
    return length;
}

//check whether the set is empty or not;
//BC = Theta(1) - constant
//WC = Theta(1) - constant
//TC =Theta(1)
bool Set::isEmpty() const {
    return head == nullptr; // sau return length == 0;
}


//destructor
//BC = Theta(1) - daca lungimea setului e 0
//WC = Theta(lungime_set(n)) - trebuie sa stergem toate nodurile
//TC = O(lungime_set(n)) 
Set::~Set() {
    Node* current = head;
    while (current != nullptr) {
        Node* nextNode = current->next; // salvam referinta la urmatorul nod
        delete current; // stergem nodul curent
        current = nextNode; // ne mutam la urmatorul nod
    }
    // tiate nodurile, acum putem sterge head-ul si seta lungimea la 0
    head = nullptr;
    length = 0; 
}



//return an iterator for the set
//BC = Theta(1) - constant
//WC = Theta(1) - constant
//TC =Theta(1)
SetIterator Set::iterator() const {
	return SetIterator(*this);
}

//reverse pt lista inlantuita
//BC = Theta(1)  daca lista e goala sau are un singur element
//WC = Theta(n) - daca lista are mai mult de un element
//TC = O(n)
void Set::reverse() {
    if (head == nullptr || head->next == nullptr) {
        //daca lista este goala sau are un elemnt, nu avem ce sa facem
        return;
    }

    Node* prev = nullptr; // nodul de dinainte incepe la null
    Node* current = head; // nodul curent este capatul listei
    Node* next = nullptr; // avem nevoie de un nou nod next

    while (current != nullptr) {
        // salvam referinta la urmatorul nod
        next = current->next;

        // inversam legaturile
        current->next = prev;

        // mutam pointerul cu o pozitie inainte
        prev = current;
        current = next;
    }
    head = prev; // dupa loop, prev va fi ultimul nod, deci devine head-ul listei
}


