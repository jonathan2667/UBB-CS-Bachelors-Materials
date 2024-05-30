#include "Repository.h"
#include<fstream>
#include<sstream>
#include<iostream>

using namespace std;

void Repository::loadFromFile()
{
    ifstream file("disorder.txt");
    string line;
    while (std::getline(file, line))
    {
        istringstream iss(line);
        string category, name, list;
        const char delimiter = '|';
        getline(iss, category, delimiter);
        getline(iss, name, delimiter);
        getline(iss, list, delimiter);
        disorders.push_back(Disorder(category, name, list));
    }
    file.close();
}