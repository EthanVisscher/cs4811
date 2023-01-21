# submission.py
# ----------------
# Attribution Information: This part of the project was adapted from CS221 and 
# the PacMan Projects. 
# For the PacMan Projects: 
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).
# 08-2020
 

from __future__ import print_function
import math 
import collections
import shop


############################################################
# Question 1 - addition 

def add(a, b): 
    "Return the sum of a and b"
    return a + b


############################################################
# Question 2 - buyLotsOfFruit 
fruitPrices = {'apples':2.00, 'oranges': 1.50, 'pears': 1.75,
              'limes':0.75, 'strawberries':1.00}

def buyLotsOfFruit(orderList):
    """
        orderList: List of (fruit, numPounds) tuples

    Returns cost of order. If some fruit is not in list, print an error 
    message and return None.
    """
    totalCost = 0.0

    for order in orderList:
        if fruitPrices[order[0]] is None:
            print("Fruit not in list")
            return None

        totalCost += (order[1] * fruitPrices[order[0]])  
    
    return totalCost


############################################################
# Question 3 - shopSmart 

def shopSmart(orderList, fruitShops):
    """
        orderList: List of (fruit, numPound) tuples
        fruitShops: List of FruitShops

    Return the FruitShop where your order costs the least.
    """
    "*** YOUR CODE HERE ***"
    cheapestShop = None
    cheapestTotalCost = -1

    for fruitShop in fruitShops:
        totalCost = 0.0
        for order in orderList:
            if fruitShop.getCostPerPound(order[0]) is None:
                print("Fruit not in list")
                return None

            totalCost += (order[1] * fruitShop.getCostPerPound(order[0])) 

        if cheapestTotalCost == -1:
            cheapestTotalCost = totalCost
            cheapestShop = fruitShop
        elif cheapestTotalCost > totalCost:
            cheapestTotalCost = totalCost
            cheapestShop = fruitShop
    
    return cheapestShop 


############################################################
# Question 4 - findAlphabetLastWord 

def findAlphabetLastWord(text):
    """
    Given a string |text|, return the word in |text| that comes last
    alphabetically (that is, the word that would appear last in a dictionary).
    A word is defined by a maximal sequence of characters without whitespaces.
    You might find max() and list comprehensions handy here.
    """
    return sorted(text.split())[-1]


############################################################
# Question 5 - euclideanDistance 

def euclideanDistance(loc1, loc2):
    """
    Return the Euclidean distance between two locations, where the locations
    are pairs of numbers (e.g., (3, 5)).
    """
    "*** YOUR CODE HERE ***"
    return ((loc2[0] - loc1[0])**2 + (loc2[1] - loc1[1])**2)**.5


############################################################
# Question 6 - findSingletonWords

def findSingletonWords(text):
    """
    Splits the string |text| by whitespace and returns the set of words that
    occur exactly once.
    If no singleton words exist return the emptyset.
    """
    "*** YOUR CODE HERE ***"
    ret = []
    words = text.split() 
    for word in words:
        if words.count(word) == 1:
            ret.append(word)

    return set(ret) 


############################################################
# Question 7 - lenLongestPalindrome

def lenLongestPalindrome(text): 
    """
    A palindrome is a string that is equal to its reverse (e.g., 'ana'). 
    Computer the length of the longest palindrome that can be obtained by 
    deleting letters from text. 
    Do not try a brute force approach on this function.  Your algorithm should 
    run in O(len(text)^2) time. 
    Consider defining a recurrence before you begin coding. 
    """
    if text == text[::-1]:
        return len(text)
    return 1
        









############################################################
#  Extra Functions you may want to define