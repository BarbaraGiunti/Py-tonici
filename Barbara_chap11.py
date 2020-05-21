# -*- coding: utf-8 -*-
"""
Created on Fri Apr 24 13:47:47 2020

@author: utente
"""

"""
import pygame, math

pygame.init()
surface_size = 1024
main_surface = pygame.display.set_mode((surface_size, surface_size))
my_clock = pygame.time.Clock()

def draw_tree(order, theta, size, position, heading, color=(0,0,0), depth=0):
    
    trunk_ratio = 0.29
    trunk = size*trunk_ratio  
    delta_x = trunk*math.cos(heading)
    delta_y = trunk*math.sin(heading)
    (u,v)=position
    newposition = (u + delta_x, v + delta_y)
    pygame.draw.line(main_surface, color, position, newposition)
    
    if order > 0:
        
        if depth == 0:
            color1 = (255, 0, 0)
            color2 = (0, 0, 255)
        
    else:
        color1 = color
        color2 = color
        
    
    newsize = size*(1-trunk_ratio)
    draw_tree(order-1, theta, newsize, position, heading-theta, color1, depth+1)
    draw_tree(order-1, theta, newsize, position, heading+theta, color2, depth+1)
    

def gameloop():
    
    theta = 0
    while True:
        
        event = pygame.event.poll()
        if event.type == pygame.QUIT:
            break;
            
        theta += 0.01
        
        main_surface.fill((255,255,0))
        draw_tree(9, theta, surface_size*0.9, (surface_size//2,surface_size-50), -math.pi/2)
        
        pygame.dispaly.flip()
        my_clock.tick(120)
        

gameloop()

pygame.quit()
"""

class Point:
    
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
        
    def reflect_x(self):
        
        r = Point(self.x, -self.y)
        return r
    
    def slope_from_origin(self):
        
        if self.x == 0:
            s = 'nan'
        else:
            s = self.y/self.x
        return s
    
    def get_line_to(self, b):
        
        if self.x == b.x:
            line = (self.x, 'nan')
        else:
            m = (self.y-b.y)/(self.x-b.x)
            q = -self.x*m+self.y
            line = (m,q)
        
        return line
        
        

def distance(a,b):
    
    d = ((a.x-b.x)**2+(a.y-b.y)**2)**0.5
    
    return d


#class SMS_store():
    

class Rectangle:
    """A class to manufacture rectangle objects"""
    
    def __init__(self, posn, w, h):
        """initialisate rectagle at posn, with width w, height h"""
        
        self.corner = posn
        self.width = w
        self.height = h
        
    def __str__(self):
        return "({0}, {1}, {2}".format(self.corner, self.width, self.height)

    
    def grow(self, delta_width, delta_height):
        """Grow (or shrink) this objet by deltas"""
        self.width += delta_width
        self.height += delta_height
        
    def move(self, dx, dy):
        """Move this object by the deltas"""
        self.corner.x += dx
        self.corner.y += dy
        
    def area(self):
        """Compute the area of the rectangle"""
        a = self.width*self.height
        
        return a
    
    def perimeter(self):
        """Compute the area of the rectangle"""
        p = self.width*2+self.height*2
        
        return p
    
    def flip(self):
        """Compute the area of the rectangle"""
        R = Rectangle(self.corner, self.height, self.width)
        
        return R
    
    def contains(self, p):
        
        l_1 = self.corner.x <= p.x and (self.corner.x + self.width) > p.x
        l_2 = self.corner.y <= p.y and (self.corner.y + self.height) > p.y
        
        if l_1 and l_2:
            
            return l_1
        else:
            return False
        
class MyTime:
    
    def __init__(self, hrs=0, mins=0, secs=0):
        
        totalsecs = hrs*3600 + mins*60 + secs*60
        self.hours= totalsecs//3600
        leftoversecs = totalsecs % 3600
        self.minutes = leftoversecs//60
        self.seconds = leftoversecs % 60
        
    def to_seconds(self):
        
        return self.hours*3600 + self.minutes*60 + self.seconds
        
    def add_time(t1,t2):
        
        secs = t1.to_seconds() + t2.to_seconds()
        return MyTime(0,0,secs)
    
    def after(self, time2):
        
        return self.to_seconds() > time2.to_seconds()
    
    def between(self, t1, t2):
        
        q1 = self.after(t1) or self.to_seconds() == t1.to_seconds()
        q2 = not self.after(t2)
        return q1 and q2
    
    def __gt__(self, other): 
        
        return self.after(other)


class Card:
    
    suits = ["Clubs", "Diamons", "Hearts", "Spades"]
    ranks = ["narf", "Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]
    
    def __init__(self, suit=0, rank=0):
        self.suit = suit
        self.rank = rank
        
    def __str__(self):
        return (self.ranks[self.rank] + " of " + self.suits[self.suit])

    
    def cmp(self, other):
        if self.suit > other.suit: return 1
        if self.suit < other.suit: return -1
        if self.rank > other.rank: return 1
        if self.rank < other.rank: return -1
        return 0
    
    def __eq__(self, other):
        return self.cmp(other) == 0
    
    def __le__(self, other):
        return self.cmp(other) <= 0
    
    def __ge__(self, other):
        return self.cmp(other) >= 0
    
    def __gt__(self, other):
        return self.cmp(other) > 0
    
    def __lt__(self, other):
        return self.cmp(other) < 0
    
    def __ne__(self, other):
        return self.cmp(other) != 0
    


class Deck:
    
    def __init__(self):
        self.cards = []
        for suit in range(4):
            for rank in range(1,14):
                self.cards.append(Card(suit, rank))
                
    """            
    def print_decl(self):
        for card in self.cards:
            print(card)
    """
    def __str__(self):
        s = ""
        for i in range(len(self.cards)):
            s = s + " "*i + str(self.cards[i]) + "\n"
        
        return s
    
    def shuffle(self):
        import random 
        rng = random.Random()
        """
        num_cards = len(self.cards)
        for i in range(num_cards):
            j = rng.randrange(i,num_cards)
            (self.cards[i], self.cards[j]) = (self.cards[j], self.cards[i])
        """  
        rng.shuffle(self.cards)
        
    def remove(self, card):
        if card in self.cards:
            self.cards.remove(card)
            return True
        else:
            return False
        
    def pop(self):
        return self.cards.pop()
    
    def is_empty(self):
        return self.cards == []
    

class Hand(Deck):
    #pass
    def __init__(self, name=""):
        self.cards = []
        self.name = name
    
    def add(self, card):
        self.cards.append(card)
        
    def deal(self, hands, num_cards=999):
        num_hands = len(hands)
        for i in range(num_cards):
            if self.is_empty():
                break
            card = self.pop()
            hand = hands[i%num_hands]
            hand.add(card)
            
    def __str__(self):
        s = "Hand " + self.name
        if self.is_empty():
            s += " is empty\n"
        else:
            s += " contains\n"
        return s + Deck.__str_(self)
    
class CardGame:
    def __init__(self):
        self.deck = Deck()
        self.deck.shuffle()
        
class OldMaidHand(Hand):
    
    def remove_matches(self):
        count = 0
        original_cards = self.cards[:]
        for card in original_cards:
            match = Card(3-card.suit,card.rank)
            if match in self.cards:
                self.cards.remove(card)
                self.cards.remove(match)
                print("Hand{0}: {1} matchs {2}".format(self.name,card,match))
                count += 1
        return count
    
class OldMaidGame(CardGame):
    def play(self, names):
        self.deck.remove(Card(0,12))
        
        self.hands = []
        for name in names:
            self.hands.append(OldMaidHand(name))
            
        self.deck.deal(self.hands)
        print("-------- Cards have been dealt")
        self.print_hands()
        
        matches = self.remove_all_matches()
        print("-------Matches discarded, play begins")
        self.print_hands()
        
        turn = 0
        num_hands = len(self.hands)
        while matches < 25:
            matches += self.play_one_turn(turn)
            turn = (turn + 1)% num_hands
            
        print("-------Game is over")
        self.print_hands
        
        
    
        
        
        
        
        
        
        
        
        
        
        