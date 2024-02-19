#include <iostream>
#include<fstream>


using namespace std;

ifstream fin("n4.in");
ofstream fout("n4.out");

int A[101][101], n, d;

//Function where we print the result
void afis()
{
    n++;
    fout << "Associative Table Operation Number: " << n;
    fout << "\n";
    for (int i = 0; i < d; ++i)
    {
        for (int j = 0; j < d; ++j)
            fout << (char)('a' + (A[i][j])) << " ";
        fout << "\n";

    }fout << "\n";
}

//Function that ferifies Associativty
bool verif()
{
    for (int i = 0; i < d; ++i)
        for (int j = 0; j < d; ++j)
            for (int k = 0; k < d; ++k)
                if (A[A[i][j]][k] != A[i][A[j][k]]) return 0;
    return 1;
}

//Function that verifies if we have reached all the possible operation table
bool gata()
{
    for (int i = 0; i < d; ++i)
        for (int j = 0; j < d; ++j)
            if (A[i][j] < d - 1) return 0;
    return 1;
}

//Function that computes and solve the problem.
void back()
{
    while (!gata())
    {

        int i = 0, j = 0;
        if (verif()) afis();
        A[i][j]++;
        while (A[i][j] == d)
        {
            A[i][j] = 0;
            if (j < d - 1) j++;
            else i++, j = 0;
            A[i][j]++;
        }
    }
}
int main()
{
    fin >> d;
    
    back();

    // As the last matrice is not verifies, we need to print it as it is associative because it will contain all the same elements
    n++;
    fout << "Associative Table Operation Number: " << n;
    fout << "\n";
    for (int i = 0; i < d; ++i)
    {
        for (int j = 0; j < d; ++j)
            fout << (char)('a' + d -1) << " ";
        fout << "\n";

    }fout << "\n";

    return 0;
}