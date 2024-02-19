#include <iostream>
#include<fstream>
#include <vector>
#include <string>
#include <algorithm>
#include <set>

using namespace std;

ifstream fin("n5.in");
ofstream fout("n5.out");

// number of partitions using dynamic programming
int CalculateNumber(int n) {
    vector<vector<int>> Matrix(n + 1, vector<int>(n + 1, 0)); //  matrix
    Matrix[0][0] = 1; // Base case

    // dynamic programming
    for (int i = 1; i <= n; i++) {
        Matrix[i][0] = Matrix[i - 1][i - 1];
        for (int j = 1; j <= i; j++) {
            Matrix[i][j] = Matrix[i - 1][j - 1] + Matrix[i][j - 1];
        }
    }

    return Matrix[n][0]; //first element of the last row represents the result
}

//  join elements of a vector 
string Join(const vector<string>& elements, const string& delimiter) {
    string result;
    if (!elements.empty()) {
        result = elements[0];
        for (int i = 1; i < elements.size(); i++) {
            result += delimiter + elements[i];
        }
    }
    return result;
}

//  print the partitions
void PrintPartitions(vector<int>& partitionIndices, int n) {
    vector<string> partitions; // List of partitions
    vector<string> pairs; // List of pairs of elements within partitions

    // loop to group elements into partitions
    for (int group : set<int>(partitionIndices.begin() + 1, partitionIndices.begin() + n + 1)) {
        vector<string> partition; // Elements within a partition
        for (int element = 1; element <= n; element++) {
            if (partitionIndices[element] == group) {
                partition.push_back("a" + to_string(element));
            }
        }

        // generate pairs of elements within the same partition
        if (partition.size() > 1) {
            for (size_t i = 0; i < partition.size(); i++) {
                for (size_t j = 0; j < partition.size(); j++) {
                    if (i != j) {
                        pairs.push_back("(" + partition[i] + ", " + partition[j] + ")");
                    }
                }
            }
        }
        partitions.push_back("{" + Join(partition, ", ") + "}"); // add partition to the list
    }

    // print the partitions
    if (partitions.size() == 1) {
        fout << partitions[0] << " -> A x A" << endl;
    }
    else if (!pairs.empty()) {
        fout << "{ " << Join(partitions, ", ") << " } -> dA U { " << Join(pairs, ", ") << " }" << endl;
    }
    else {
        fout << "{ " << Join(partitions, ", ") << " } -> dA" << endl;
    }
}

// backtracking
void Backtracking(int currentIndex, vector<int>& partitionIndices, int n) {
    int maxPartitionIndex = *max_element(partitionIndices.begin() + 1, partitionIndices.begin() + currentIndex); // maximum partition number
    for (int i = 1; i <= maxPartitionIndex + 1; i++) {
        partitionIndices[currentIndex] = i; // setting the partition number for the current element
        if (currentIndex == n) {
            PrintPartitions(partitionIndices, n); // printing
        }
        else {
            Backtracking(currentIndex + 1, partitionIndices, n); // backtracking again
        }
    }
}

int main() {
    int n;
    fin >> n; // read n

    vector<int> partitionIndices(n + 1, 0); 

    fout << "The number of partitions on the set A is " << CalculateNumber(n) << "\n\n";

    fout << "Their corresponding equivalence relations are: " << "\n";

    Backtracking(1, partitionIndices, n); // generate 
    return 0;
}
