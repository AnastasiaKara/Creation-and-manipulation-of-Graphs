# # 1st Assignment - Network Connectivity - part B
# This assignment involves the importing and analysis of an internal email communication network amongst employees
# of a manufacturing company.
#
# Each node depicts and employee and each directed edge between two nodes depicts and individual mail. The node to the
# left represents the sender and the node to the right represents the recipient.

import networkx as nx


# ### Question 1
#
# Use NetworkX to load up the directed multigraph, located in `mail_network.txt` and make sure the node names are
# strings.
#
# [*Returns a directed multigraph networkx graph]

def answer_one():
    # Your Code Here
#    sender = []
#    recipient = []
    B1 = nx.MultiDiGraph()
    file = open('mail_network.txt','r')
    first_line = True
    for line in file:
        if first_line:
            first_line = False #this is done to skip the header
            continue
        line = line.strip('\n')
        temp = line.split('\t')
        B1.add_node(temp[0])
        B1.add_node(temp[1])
        B1.add_edge(temp[0], temp[1])
#        sender.append(temp[0])
#        recipient.append(temp[1])
        
    for n in nx.nodes(B1):
        print(type(n)) #make sure nodes are of type 'str'
    
    return B1 # Your Answer Here


# ### Question 2
#
# Find the number of employees and mails in the graph from Question 1.
#
# [*Returns a tuple (<num_of_employees>, <num_of_mails>).*


def answer_two(G):
    # Your Code Here
    l = [] #create tuple that will store result
    l.append(G.number_of_nodes())
    l.append(G.number_of_edges())
    T1 = tuple(l)
    return T1 # Your Answer Here


# ### Question 3
#
# * Part 1. For this part, we assume that the information in this company can only be exchanged via mail.
#
#   Whenever an employee sends a mail to another employee, a one-way communication channel is created, which allows the
#   sender to provide info to the receiver, but not vice versa
#
#   Based on the mail transaction present in our dataset, detect whether it is possible for info to go from every employ
#   to every other employ (True, False)
#
# * Part 2. For this part, we assume that the communication channel that is established by a mail allows for vice-versa
#           communication (both ways)
#
#   Based on the mail transaction present in our dataset, detect whether it is possible for info to go from every employ
#   to every other employ (True, False)
#
# [*Returns a tuple of bools (<part1>, <part2>)]

def answer_three(G):
    # Your Code Here
    # Part1
    lis = []
    lis1 = []
    lis2 = []
    lis3 = []
    for n in nx.nodes(G):
        for u in nx.nodes(G):
            if n != u:
                lis.append(G.has_edge(n,u))
            else:
                continue
        Part1 = list(lis)   
        
    # Part2
    count = 0
    while(count < G.number_of_nodes()):
        for n in nx.nodes(G):
            for u in nx.nodes(G):
                if n != u:
    #                lis1.append(G.has_edge(n,u))
    #                lis2.append(G.has_edge(u,n))
                    if (lis1.append(G.has_edge(n,u)) == True and lis2.append(G.has_edge(u,n)) == True):
                        lis3.append(True)
                    else:
                        lis3.append(False)
                else:
                    continue
                count = count + 1
            Part2 = list(lis3)
    
    Result = Part1,Part2
    
    return Result # Your Answer Here


# ### Question 4
#
# What is the number of nodes in the largest (in terms of nodes) weakly connected component?
#
# [*Returns an int]


def answer_four(G):
    # Your Code Here
    largest = max(nx.weakly_connected_components_subgraphs(G), key = len)
    num_of_nodes_weakly = len(largest.nodes())
    return num_of_nodes_weakly # Your Answer Here


# ### Question 5
#
# What is the number of nodes in the largest (in terms of nodes) strongly connected component?
#
# [*Returns an int]

def answer_five(G):
    # Your Code Here
    largest = max(nx.strongly_connected_components(G), key = len)
    num_of_nodes_strongest = len(largest)
    return num_of_nodes_strongest # Your Answer Here


# ### Question 6
#
# Use the NetworkX function for strongly connected component subgraphs to find the subgraph of nodes in a largest
# strongly connected component. Assume that this graph is called G_sc.
#
# [*Returns a NetworkX MultiDiGraph named G_sc]


def answer_six(G):
    # Your Code Here
    All_sc = list(nx.strongly_connected_component_subgraphs(G))
    num_nodes = All_sc[0].number_of_nodes()
    max_index = 0
    for i in range(1, len(All_sc)):
        if All_sc[i].number_of_nodes() > num_nodes:
            num_nodes = All_sc[i].number_of_nodes()
            max_index = i
    G_sc = All_sc[max_index]
    return G_sc # Your Answer Here


# ### Question 7
#
# Calculate the average distance between nodes in G_sc (from question 6)
# distance =  number of edges in a shortest path (also called a graph geodesic) connecting them
# [*Returns a float]

def answer_seven(G):
    # Your Code Here
    av_distance = nx.average_shortest_path_length(G)
    return av_distance # Your Answer Here


# ### Question 8
#
# Calculate the largest possible distance between two employees in the G_sc graph (from question 6)
#
# [*Returns an int]


def answer_eight():
    # Your Code Here

    return  # Your Answer Here


# ### Question 9
#
# Find the set of nodes in G_sc with eccentricity equal to the diameter
#
# [*Returns the set of the node(s)]


def answer_nine():
    # Your Code Here

    return  # Your Answer Here


# ### Question 10
#
# Find the set of nodes in G_sc with eccentricity equal to the diameter
#
# [*Returns the set of the node(s)]


def answer_ten():
    # Your Code Here

    return  # Your Answer Here


# ### Question 11
#
# Find which node in G_sc is connected to the most other nodes by a shortest path of length equal to the diameter
# of G_sc
#
# Find the number of nodes that are connected to this node
#
# [*Returns a tuple (<name of node>, <number of satisfied connected nodes>)]


def answer_eleven():
    # Your Code Here

    return  # Your Answer Here


# ### Question 12
#
# Assuming that we want to prevent the communication from flowing from the node that we found in question 11 from any
# node in the center of G_sc, detect the smallest number of nodes you would need to remove from the graph (you are not
# allowed to remove the node from the previous question or the center nodes).
#
# [*Returns an integer]

def answer_twelve():
    # Your Code Here

    return  # Your Answer Here


# ### Question 13
#
#
# Create an undirected graph named G_un using G_sc (it is possible to ignore the attributes).
#
# [*Returns a NetworkX Graph (G_un)]

# In[ ]:

def answer_thirteen():
    # Your Code Here

    return  # Your Answer Here


# ### Question 14
#
# Find the transitivity and the average clustering coefficient of graph G_un.
#
# [*Returns a tuple (<transitivity>, <avg_clustering_coefficient>]

# In[ ]:

def answer_fourteen():
    # Your Code Here

    return  # Your Answer Here
