"""
Lecture 1 question 9: Poker Odds

Usage: python L1Q9.py N s

Deals N hands of 5 cards from a French deck and checks for various poker
scores. If s==1, puts the hand back in the deck and shuffles it after each
hand, otherwise draws from the deck untl it runs out of cards before putting
them back in. Prints the frequentist probability of obtaining each score and
plots the frequency of each score as a function of the number of plays.

Pietro Rescigno - Scientific Computing with Python 23/24
"""
import random
import sys
import numpy as np
import matplotlib.pyplot as plt
import argparse

class Card:
    
    def __init__(self, suit=1, rank=2):
        if suit < 1 or suit > 4:
            print("invalid suit, setting to 1")
            suit = 1
            
        self.suit = suit
        self.rank = rank
        
    def value(self):
        """ we want things order primarily by rank then suit """
        return self.suit + (self.rank-1)*14
    
    # we include this to allow for comparisons with < and > between cards 
    def __lt__(self, other):
        return self.value() < other.value()

    def __eq__(self, other):
        return self.rank == other.rank and self.suit == other.suit
    
    def __repr__(self):
        return self.__str__()
    
    def __str__(self):
        suits = [u"\u2660",  # spade
                 u"\u2665",  # heart
                 u"\u2666",  # diamond
                 u"\u2663"]  # club
        
        r = str(self.rank)
        if self.rank == 11:
            r = "J"
        elif self.rank == 12:
            r = "Q"
        elif self.rank == 13:
            r = "K"
        elif self.rank == 14:
            r = "A"
                
        return r +':'+suits[self.suit-1]

class Deck:
    """ the deck is a collection of cards """

    def __init__(self):

        self.nsuits = 4
        self.nranks = 13
        self.minrank = 2
        self.maxrank = self.minrank + self.nranks - 1

        self.cards = []

        for rank in range(self.minrank,self.maxrank+1):
            for suit in range(1, self.nsuits+1):
                self.cards.append(Card(rank=rank, suit=suit))

    def shuffle(self):
        random.shuffle(self.cards)

    def get_cards(self, num=1):
        hand = []
        for n in range(num):
            hand.append(self.cards.pop())

        return hand
    
    def __str__(self):
        string = ""
        for c in self.cards:
            string += str(c) + " "
        return string


def score(hand):
	global npa
	global npp
	global nt
	global nstr
	global nflush
	global nfull
	global npok
	global nstrflush
	global nroyflush
	
	if(len(hand)!=5):
		print(f"Error: expected hand of 5 cards")
		return
	clist = np.zeros(14,int) # List that contains how many cards
				 # of a given rank are in the hand
	ranklist = np.zeros(5,int) # List that contains the ranks
			           # of the cards in the hand
	i=0            	    
	for c in sorted(hand):
		r = c.rank	
		clist[r-1] += 1
		ranklist[i]=r
		i+=1
	
	# Pair(s)
	npairs = ((clist==2).astype(int)).sum()
	
	# Tris
	tris = ((clist==3).astype(int)).sum()

	# Poker 
	poker = ((clist==4).astype(int)).sum()

	if (poker==1):
		npok+=1
		#print("Poker")
	if (tris==1):
		if (npairs==1):
			nfull+=1
			#print("Full House")
		else:
			nt+=1
			#print("Three of a kind")
	
	if (npairs==2):
		npp+=1
		#print("Two pair")
	if (npairs==1 and  tris==0):
		npa+=1
		#print("Pair")
	
	# Check for flushes and straight
	if (hand[0].suit==hand[1].suit and
	    hand[1].suit==hand[2].suit and 
	    hand[2].suit==hand[3].suit and 
	    hand[3].suit==hand[4].suit):
		if ((ranklist[1:]-ranklist[:-1]==np.array([1,1,1,1])).all()):
			if(ranklist[0]==10):
				nroyflush+=1
				#print("Royal flush")
			else:
				nstrflush+=1
				#print("Straight flush")
		else:
			nflush+=1
			#print("Flush")
	else:
		if ((ranklist[1:]-ranklist[:-1]==np.array([1,1,1,1])).all()):	
			nstr+=1
			#print("Straight")
	
	#if (npairs==0 and tris==0 and poker==0):
		#print("High card")
################################################

if (len(sys.argv)!=3):
	print(f'Expected 2 arguments:int N, int s\nDefaulting to N=10000, s=1')
	N=10000
	s=1
else:
	N=int(sys.argv[1])
	s=int(sys.argv[2])

mydeck= Deck()
npa=0
npp=0 
nt=0 
nstr=0
nflush=0
nfull=0
npok=0
nstrflush=0
nroyflush=0

mydeck.shuffle()
#hand=mydeck.get_cards(5)
#hand[0] = Card(suit=1, rank=10)
#hand[1] = Card(suit=2, rank=11)
#hand[2] = Card(suit=1, rank=12)
#hand[3] = Card(suit=1, rank=13)
#hand[4] = Card(suit=1, rank=14)
#score(hand)
#for c in sorted(hand): print(c)

pairlist=[]
dpairlist=[]
trislist=[]
strlist=[]
flushlist=[]
fulllist=[]
poklist=[]
strflushlist=[]
royflushlist=[]
for i in range(1,N+1):
	if(s==1):
		# Probability of being dealt different scores
		mydeck = Deck()
		mydeck.shuffle()
	else:
		if (52-5*i)<5: 
			# Goes through the deck before reshuffling
			mydeck=Deck()
			mydeck.shuffle()
	hand = mydeck.get_cards(5)
	score(hand)#,npa,npp,nt,nf,npok)
	pairlist.append(npa/i)
	dpairlist.append(npp/i)
	trislist.append(nt/i)
	strlist.append(nstr/i)
	flushlist.append(nflush/i)
	fulllist.append(nfull/i)
	poklist.append(npok/i)
	strflushlist.append(nstrflush/i)
	royflushlist.append(nroyflush/i)

nnone = N-npa-npp-nt-nstr-nflush-nfull-npok-nstrflush-nroyflush

print(f'You just played {N} hands of poker. You got:\n')

print(f'Nothing {nnone} times ({100.0*nnone/N:1.4f} %)')
print(f'Pair {npa} times ({100*(pairlist[-1]):1.4f} %)')
print(f'Double pair {npp} times ({100*(dpairlist[-1]):1.4f} %)')
print(f'Three of a kind {nt} times ({100*(trislist[-1]):1.4f} %)')
print(f'Straight {nstr} times ({100*strlist[-1]:1.4f} %)')
print(f'Flush {nflush} times ({100*flushlist[-1]:1.4f} %)')
print(f'Full house {nfull} times ({100*(fulllist[-1]):1.4f} %)')
print(f'Poker {npok} ({100*(poklist[-1]):1.4f} %)')
print(f'Straight flush {nstrflush} times({100*strflushlist[-1]:1.4f} %)')
print(f'Royal flush {nroyflush} times ({100*royflushlist[-1]:1.4f} %)\n')
print(f'You probably lost a lot of money')
plt.xscale("log")
plt.yscale("log")
A=0.6
plt.plot(pairlist, label='Pair', color='C0')
plt.plot(pairlist[-1]*np.ones(len(pairlist)), '--', color='C0',alpha=A)
plt.plot(dpairlist, label='2 Pair', color='C1')
plt.plot(dpairlist[-1]*np.ones(len(pairlist)), '--', color='C1', alpha=A)
plt.plot(trislist, label='Tris', color='C2')
plt.plot(trislist[-1]*np.ones(len(pairlist)), '--', color='C2', alpha=A)
plt.plot(strlist, label='Straight', color='C3')
plt.plot(strlist[-1]*np.ones(len(pairlist)), '--', color='C3', alpha=A)
plt.plot(flushlist, label='Flush', color='C4')
plt.plot(flushlist[-1]*np.ones(len(pairlist)), '--', color='C4', alpha=A)
plt.plot(fulllist, label='Full', color='C5')
plt.plot(fulllist[-1]*np.ones(len(pairlist)), '--', color='C5', alpha=A)
plt.plot(poklist, label='Poker', color='C6')
plt.plot(poklist[-1]*np.ones(len(pairlist)), '--', color='C6', alpha=A)
plt.plot(strflushlist, label='Straight flush', color='C7')
plt.plot(strflushlist[-1]*np.ones(len(pairlist)), '--', color='C7', alpha=A)
plt.plot(royflushlist, label='Royal flush', color='C8')
plt.plot(royflushlist[-1]*np.ones(len(pairlist)), '--', color='C8', alpha=A)
plt.legend()
plt.xlabel("Number of hands")
plt.ylabel("Score frequency")
plt.show()

