#pragma once

#include <map>
#include <utility>
#include <vector>
#include <string>

class Graph {
private:
    std::map<int, std::vector<int>> outMap, inMap;
    std::map<std::pair<int, int>, int> costMap;
public:
    // constructor
    explicit Graph(int nrVertices);

    // Number of vertices
    int nrVertices();

    // Number of edges
    int nrEdges();

    // Returns a pair of iterators that iterate through the set of vertices
    std::pair<std::map<int, std::vector<int>>::iterator, std::map<int, std::vector<int>>::iterator> setOfVertices();

    // Check if a vertex exists
    bool isVertex(int v);

    // Check if an edge exists
    bool isEdge(int v1, int v2);

    // Add an edge
    void addEdge(int v1, int v2, int cost);

    // In degree of a vertex
    int inDegree(int x);

    // Out degree of a vertex
    int outDegree(int x);

    // Returns a pair of iterators that iterate through the set of outbound edges of a vertex
    std::pair <std::vector<int>::iterator, std::vector<int>::iterator> inboundEdge(int x);

    // Returns a pair of iterators that iterate through the set of inbound edges of a vertex
    std::pair <std::vector<int>::iterator, std::vector<int>::iterator> outboundEdge(int x);

    // Get the cost of an edge
    void changeCost(int x, int y, int val);
    
    // Modify the cost of an edge
    int getCost(int x, int y);

    // Add a vertex
    void removeEdge(int x, int y);

    // Remove an edge
    void addVertex(int val);

    // Remove a vertex
    void removeVertex(int val);

    Graph(const Graph& other);

    // Assignment operator
    Graph& operator=(const Graph& other);

    // Save the graph to a file
    std::string toString();
};
