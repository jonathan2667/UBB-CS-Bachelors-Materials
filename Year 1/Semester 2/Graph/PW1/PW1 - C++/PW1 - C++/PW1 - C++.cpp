#include <iostream>
#include "Graph.h"
#include <fstream>
#include <exception>

// Reads a graph from a specified file and returns a Graph object initialized with the read data.
Graph readFile(char file[200]) {
    
    std::ifstream fin(file);
    int nrV, nrE;
    fin >> nrV >> nrE;
    Graph G(nrV);
    for (int i = 0; i < nrE; ++i) {
        int v1, v2, cost;
        fin >> v1 >> v2 >> cost;
        G.addEdge(v1, v2, cost);
    }
    return G;
}

// Generates a random graph with a specified number of vertices and edges and returns a Graph object initialized with the generated data.
Graph generateGraph(int nrV, int nrE) {
    Graph G(nrV);
    int v1, v2, cost;
    for (int i = 0; i < nrE; ++i) {
        v1 = rand() % nrV;
        v2 = rand() % nrV;
        cost = rand() % 300;
        if (G.isEdge(v1, v2)) {
            i--;
        }
        else {
            G.addEdge(v1, v2, cost);
        }
    }
    return G;
}

// Reads a graph from the user and returns a Graph object initialized with the read data.
Graph StartRead() {
    std::cout << "Graph program: 1 - generate, 2 - read from file\n";
    int cmd;
    std::cin >> cmd;
    if (cmd != 1 and cmd != 2) {
        std::cout << "Invalid";
        throw std::exception();
    }
    if (cmd == 2) {
        std::cout << "Enter text name: ";
        char file[200];
        std::cin >> file;
        Graph g = readFile(file);
        return g;
    }
    else {
        std::cout << "Please enter number of vertices: ";
        int nrV, nrE;
        std::cin >> nrV;
        std::cout << "Please enter number of edges: ";
        std::cin >> nrE;
        Graph g = generateGraph(nrV, nrE);
        return g;
    }
}

// Prints the menu and performs the specified operation on the graph.
void printMenu(Graph& G) {
    std::cout << "Graph Operations\n1. Get the number of vertices\n2. The set of vertices\n3. Check if there is an edge between 2 vertices\n4. In degree of a vertex\n5. Out degree of a vertex\n6. The outbound edges of a vertex\n7. The inbound edges of a vertex\n8. Get the cost of an edge\n9. Modify the cost of an edge\n10. Add edge\n11. Remove edge\n12. Add vertex\n13. Remove vertex\n14. Save graph to file\n15. To String Graph\n0. Exit\n";
    int cmd;
    std::cout << "Command: ";
    std::cin >> cmd;
    switch (cmd) {
    case 1:
        std::cout << G.nrVertices() << '\n';
        break;
    case 2: {
        auto p = G.setOfVertices();
        for (auto i = p.first; i != p.second; ++i) {
            std::cout << i->first << ' ';
        }
        std::cout << '\n';
        break;
    }
    case 3: {
        int v1, v2;
        std::cout << "Vertices: ";
        std::cin >> v1 >> v2;
        std::cout << G.isEdge(v1, v2) << '\n';
        break;
    }
    case 4: {
        int v1;
        std::cout << "Vertex: ";
        std::cin >> v1;
        std::cout << G.inDegree(v1) << '\n';
        break;
    }
    case 5: {
        int v1;
        std::cout << "Vertex: ";
        std::cin >> v1;
        std::cout << G.outDegree(v1) << '\n';
        break;
    }
    case 6: {
        int v1;
        std::cout << "Vertex: ";
        std::cin >> v1;
        auto p = G.outboundEdge(v1);
        for (auto i = p.first; i != p.second; ++i) {
            std::cout << *i << '\n';
        }
        break;
    }
    case 7: {
        int v1;
        std::cout << "Vertex: ";
        std::cin >> v1;
        auto p = G.inboundEdge(v1);
        for (auto i = p.first; i != p.second; ++i) {
            std::cout << *i << '\n';
        }
        break;
    }
    case 8: {
        int v1, v2;
        std::cout << "Edge: ";
        std::cin >> v1 >> v2;
        std::cout << G.getCost(v1, v2) << '\n';
        break;
    }
    case 9: {
        int v1, v2, cost;
        std::cout << "Edge: ";
        std::cin >> v1 >> v2;
        std::cout << "Cost: ";
        std::cin >> cost;
        G.changeCost(v1, v2, cost);
        break;
    }
    case 10: {
        int v1, v2, cost;
        std::cout << "Edge: ";
        std::cin >> v1 >> v2;
        std::cout << "Cost: ";
        std::cin >> cost;
        G.addEdge(v1, v2, cost);
        break;
    }
    case 11: {
        int v1, v2;
        std::cout << "Edge: ";
        std::cin >> v1 >> v2;
        G.removeEdge(v1, v2);
        break;
    }
    case 12: {
        G.addVertex(G.nrVertices());
        break;
    }
    case 13: {
        int v1;
        std::cout << "Vertex: ";
        std::cin >> v1;
        G.removeVertex(v1);
        break;
    }
    case 14: {
        std::string fileName;
        std::cout << "File name: ";
        std::cin >> fileName;
        std::cout << "The copy of the graph is saved to " << fileName << "...\n";
        std::ofstream printCopy(fileName);
        printCopy << G.toString();
        printCopy.close();
        break;
    }
    case 15: {
		std::cout << G.toString() << '\n';
		break;
	}
 
    case 0:
        throw 0; break;
    default:
        std::cout << "Invalid command\n";
        break;
    }
}

// Main function
int main() {
    std::ios::sync_with_stdio(false);
    Graph G = Graph(0);
    try {
        G = StartRead();
    }
    catch (std::exception& e) {
        std::cout << "Invalid data\n";
    }
    while (true) {
        try {
            printMenu(G);
            //std::cout << G.toString() << '\n';
        }
        catch (int e) {
            std::cout << "Goodbye\n";
            return 0;
        }
    }
}