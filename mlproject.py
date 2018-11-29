# -*- coding: utf-8 -*-
"""
Created on Tue Oct 23 18:45:49 2018

@author: vineet
"""

#import pandas as pd


import networkx as nx
import matplotlib.pyplot as plt

p_graph = nx.Graph()

p_graph.add_node("A")
p_graph.add_node("B")
p_graph.add_node("C")
p_graph.add_node("D")
p_graph.add_node("E")
p_graph.add_node("F")

p_graph.add_edge("A","B")
p_graph.add_edge("A","C")
p_graph.add_edge("B","C")
p_graph.add_edge("B","D")
p_graph.add_edge("C","D")
p_graph.add_edge("D","F")
p_graph.add_edge("D","E")
p_graph.add_edge("C","F")


assert len(p_graph.nodes()) == 6
assert len(p_graph.edges()) == 8


nx.draw(p_graph)
plt.show()


def friends(graph,user):
    return set(graph.neighbors(user))

#m= friends(p_graph,'A')
#print(m)

def friends_of_friends(graph,user):
    userfriends = friends(graph,user)
    finalfriends = set()
    for names in userfriends:
        
        friends_of_userfriends = friends(graph,names)
        for names2 in friends_of_userfriends:
            if(names2 not in userfriends and names2 != user):
                finalfriends.add(names2)
    return finalfriends

#n = friends_of_friends(p_graph,'A')
#print(n)
        

  
def common_friends(graph,user1,user2):
    user1friends = friends(graph,user1)
    user2friends = friends(graph,user2)
    commonfriends = user1friends.intersection(user2friends)
    return commonfriends


#o = common_friends(p_graph,'A','E')
#print(o)
    

#p = set(p_graph.nodes())
#type(p)


def number_of_common_friends_map(graph,user):
    all_names = set(p_graph.nodes())
    all_names.remove(user)
    users_friends = friends(graph,user)
    friend_map = {}
    for names in all_names:
        temp_friends = common_friends(graph,user,names)
        num_friends = len(temp_friends)
        if num_friends>0 and names not in users_friends:
            friend_map[names] = num_friends
    return friend_map



q = number_of_common_friends_map(p_graph,'A')
print(q)
    
import operator
def number_map_sorted_list(friendmap):
    temp_list=sorted(friendmap.items(),key=operator.itemgetter(1),reverse=True)
    friend_list = [items[0] for items in temp_list]
    return friend_list

#r = number_map_sorted_list(q)
#print(r)
    

def recommend_by_number_of_common_friends(graph,user):
    friendmap = number_of_common_friends_map(graph,user)
    friend_recommend = number_map_sorted_list(friendmap)
    return friend_recommend

def create_facebook_graph(file_path):
    fb_graph = nx.read_edgelist(file_path, create_using = nx.Graph(), nodetype = int)
    print (nx.info(fb_graph))
    return fb_graph;
    
def draw_facebook_graph(graph):
    nx.draw(graph)
    plt.savefig("fb.pdf")
    plt.show()



s = recommend_by_number_of_common_friends(p_graph,'A')
print(s)
t = recommend_by_number_of_common_friends(p_graph,'D')
print(t)
u = recommend_by_number_of_common_friends(p_graph,'F')
print(u)

def influence_map(graph,user):
    result=0
    friends_influence = dict()
    friendmap = number_of_common_friends_map(graph, user)
    for k in friendmap.keys():
        x= common_friends(graph,k,user)
        
        for cf in x:
            no_of_friends=len(friends(graph,cf))
            result = result + (float(1)/no_of_friends)
            
        friends_influence[k] = result
        result = 0
    return friends_influence

def recommend_by_influence(graph, user):
    friendmap = influence_map(graph, user)
    return number_map_sorted_list(friendmap)

s = recommend_by_influence(p_graph,'A')
print(s)


file_path = "facebook_combined.txt"
fb_graph = create_facebook_graph(file_path)

#this method call wil take long time to execute.
#draw_facebook_graph(fb_graph)







