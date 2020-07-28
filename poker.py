__author__ = '/dat'

#холдем

import time
import random
from collections import namedtuple
from itertools import *
import operator

print("--------------------")   
print('ТЕХАССКИЙ ХОЛДЕМ')
print('Добро пожаловать!')
print("--------------------")


 
class Card(namedtuple('Card', 'face, suit')):
    def __repr__(self):
        return ''.join(self)
 
 
suit = '♥ ♦ ♣ ♠'.split()
# ordered strings of faces
faces   = '2 3 4 5 6 7 8 9 10 j q k a'
lowaces = 'a 2 3 4 5 6 7 8 9 10 j q k'
# faces as lists
face   = faces.split()
lowace = lowaces.split()
 
 
def straightflush(hand):
    f,fs = ( (lowace, lowaces) if any(card.face == '2' for card in hand)
             else (face, faces) )
    ordered = sorted(hand, key=lambda card: (f.index(card.face), card.suit))
    first, rest = ordered[0], ordered[1:]
    if ( all(card.suit == first.suit for card in rest) and
         ' '.join(card.face for card in ordered) in fs ):
        return 'стрит-флеш', ordered[-1].face
    return False
 
def fourofakind(hand):
    allfaces = [f for f,s in hand]
    allftypes = set(allfaces)
    if len(allftypes) != 2:
        return False
    for f in allftypes:
        if allfaces.count(f) == 4:
            allftypes.remove(f)
            return 'каре', [f, allftypes.pop()]
    else:
        return False
 
def fullhouse(hand):
    allfaces = [f for f,s in hand]
    allftypes = set(allfaces)
    if len(allftypes) != 2:
        return False
    for f in allftypes:
        if allfaces.count(f) == 3:
            allftypes.remove(f)
            return 'фуллхаус', [f, allftypes.pop()]
    else:
        return False
 
def flush(hand):
    allstypes = {s for f, s in hand}
    if len(allstypes) == 1:
        allfaces = [f for f,s in hand]
        return 'флеш', sorted(allfaces,
                               key=lambda f: face.index(f),
                               reverse=True)
    return False
 
def straight(hand):
    f,fs = ( (lowace, lowaces) if any(card.face == '2' for card in hand)
             else (face, faces) )
    ordered = sorted(hand, key=lambda card: (f.index(card.face), card.suit))
    first, rest = ordered[0], ordered[1:]
    if ' '.join(card.face for card in ordered) in fs:
        return 'стрит', ordered[-1].face
    return False
 
def threeofakind(hand):
    allfaces = [f for f,s in hand]
    allftypes = set(allfaces)
    if len(allftypes) <= 2:
        return False
    for f in allftypes:
        if allfaces.count(f) == 3:
            allftypes.remove(f)
            return ('сет', [f] +
                     sorted(allftypes,
                            key=lambda f: face.index(f),
                            reverse=True))
    else:
        return False
 
def twopair(hand):
    allfaces = [f for f,s in hand]
    allftypes = set(allfaces)
    pairs = [f for f in allftypes if allfaces.count(f) == 2]
    if len(pairs) != 2:
        return False
    p0, p1 = pairs
    other = [(allftypes - set(pairs)).pop()]
    return 'две пары', pairs + other if face.index(p0) > face.index(p1) else pairs[::-1] + other
 
def onepair(hand):
    allfaces = [f for f,s in hand]
    allftypes = set(allfaces)
    pairs = [f for f in allftypes if allfaces.count(f) == 2]
    if len(pairs) != 1:
        return False
    allftypes.remove(pairs[0])
    return 'пара', pairs + sorted(allftypes,
                                      key=lambda f: face.index(f),
                                      reverse=True)
 
def highcard(hand):
    allfaces = [f for f,s in hand]
    return 'старшая-карта', sorted(allfaces,
                               key=lambda f: face.index(f),
                               reverse=True)
 
handrankorder =  (straightflush, fourofakind, fullhouse,
                  flush, straight, threeofakind,
                  twopair, onepair, highcard)
 
def rank(cards):
    hand = handy(cards)
    for ranker in handrankorder:
        rank = ranker(hand)
        if rank:
            break
    assert rank, "Не могу проранжировать карты: %r" % cards
    return rank
 
def handy(cards='2♥ 2♦ 2♣ k♣ q♦'):
    hand = []
    for card in cards.split():
        f, s = card[:-1], card[-1]
        assert f in face, "Непонятное лицо %r" % f
        assert s in suit, "Непонятная масть %r" % s
        hand.append(Card(f, s))
    assert len(hand) == 5, "Должно быть 5 карт, не %i" % len(hand)
    assert len(set(hand)) == 5, "Все карты должны быть уникальны %r" % cards
    return hand


def texas_holdem(account):
    while 0 < account < 2000:
        bank = 0
        suit = ['♠', '♥', '♦', '♣']
        val = ['a', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'j', 'q', 'k']
        deck = []
        for s in suit:
            for v in val:
                deck.append(v + s)
        print("Стартовая ставка - 1$")
        account -= 1
        bank += 3
        print('Банк:', bank,'$')
        d = random.choice(deck)
        deck.remove(d)
        c = random.choice(deck)
        deck.remove(c)
        d2 = random.choice(deck)
        deck.remove(d2)
        c2 = random.choice(deck)
        deck.remove(c2)
        d3 = random.choice(deck)
        deck.remove(d3)
        c3 = random.choice(deck)
        deck.remove(c3)
        print("\n Ваши две карты:\n\t", d, " и", "\n\t", c,"\n")
        t1 = random.choice(deck)
        deck.remove(t1)
        t2 = random.choice(deck)
        deck.remove(t2)
        t3 = random.choice(deck)
        deck.remove(t3)
        t4 = random.choice(deck)
        deck.remove(t4)
        t5 = random.choice(deck)
        deck.remove(t5)
        hand1 = [t1, t2, t3, t4, t5, d, c]
        x=[]
        best = []
        d1 = 0
        dict1 = {}
        bestDict = {}
        for i in combinations(hand1, 5):
            bestID = 0
            y = list(i)
            x.append(y)
            if len(x) == 21:
                for f in x:
                    d1 += 1
                    dict1[d1]=y
                    bestID += 1
                    def best_cards(hands2):
                        for cards in hands2:
                            r = rank(cards)
                            if r[0] == 'стрит-флеш':
                                bestDict[bestID] = 8
                                best.append(8)
                                return
                            elif r[0] == 'каре':
                                bestDict[bestID] = 7
                                best.append(7)
                                return
                            elif r[0] == 'фуллхаус':
                                bestDict[bestID] = 6
                                best.append(6)
                                return
                            elif r[0] == 'флеш':
                                bestDict[bestID] = 5
                                best.append(5)
                                return
                            elif r[0] == 'стрит':
                                bestDict[bestID] = 4
                                best.append(4)
                                return
                            elif r[0] == 'сет':
                                bestDict[bestID] = 3
                                best.append(3)
                                return
                            elif r[0] == 'две пары':
                                bestDict[bestID] = 2
                                best.append(2)
                                return
                            elif r[0] == 'пара':
                                bestDict[bestID] = 1
                                best.append(1)
                                return
                            else:
                                bestDict[bestID] = 0
                                best.append(0)
                                return
                    handd1 = ' '.join(map(str, f))
                    hands = [handd1]
                    best_cards(hands)
            else:
                continue
        bestSetId = max(best)
        #print(bestSetId)
        id_best1 = max(iter(bestDict), key=(lambda key: bestDict[key]))
        player1 = x.pop(id_best1-1)
        #print(player1)
        hand2 = [t1, t2, t3, t4, t5, d2, c2]
        x = []
        best2 = []
        d1 = 0
        dict1 = {}
        bestDict = {}
        for i in combinations(hand2, 5):
            bestID = 0
            y = list(i)
            x.append(y)
            if len(x) == 21:
                for f in x:
                    d1 += 1
                    dict1[d1] = y
                    bestID += 1
                    def best_cards2(hands2):
                        for cards in hands2:
                            r = rank(cards)
                            if r[0] == 'стрит-флеш':
                                bestDict[bestID] = 8
                                best2.append(8)
                                return
                            elif r[0] == 'каре':
                                bestDict[bestID] = 7
                                best2.append(7)
                                return
                            elif r[0] == 'фуллхаус':
                                bestDict[bestID] = 6
                                best2.append(6)
                                return
                            elif r[0] == 'флеш':
                                bestDict[bestID] = 5
                                best2.append(5)
                                return
                            elif r[0] == 'стрит':
                                bestDict[bestID] = 4
                                best2.append(4)
                                return
                            elif r[0] == 'сет':
                                bestDict[bestID] = 3
                                best2.append(3)
                                return
                            elif r[0] == 'две пары':
                                bestDict[bestID] = 2
                                best2.append(2)
                                return
                            elif r[0] == 'пара':
                                bestDict[bestID] = 1
                                best2.append(1)
                                return
                            else:
                                bestDict[bestID] = 0
                                best2.append(0)
                                return

                    handd1 = ' '.join(map(str, f))
                    hands = [handd1]
                    best_cards2(hands)
            else:
                continue
        bestSetId2 = max(best2)
        #print(bestSetId2)
        id_best1 = max(iter(bestDict), key=(lambda key: bestDict[key]))
        player2 = x.pop(id_best1 - 1)
        #print(player2)
        hand3 = [t1, t2, t3, t4, t5, d3, c3]
        x = []
        best3 = []
        d1 = 0
        dict1 = {}
        bestDict = {}
        for i in combinations(hand3, 5):
            bestID = 0
            y = list(i)
            x.append(y)
            if len(x) == 21:
                for f in x:
                    d1 += 1
                    dict1[d1] = y
                    bestID += 1
                    def best_cards3(hands2):
                        for cards in hands2:
                            r = rank(cards)
                            if r[0] == 'стрит-флеш':
                                bestDict[bestID] = 8
                                best3.append(8)
                                return
                            elif r[0] == 'каре':
                                bestDict[bestID] = 7
                                best3.append(7)
                                return
                            elif r[0] == 'фуллхаус':
                                bestDict[bestID] = 6
                                best3.append(6)
                                return
                            elif r[0] == 'флеш':
                                bestDict[bestID] = 5
                                best3.append(5)
                                return
                            elif r[0] == 'стрит':
                                bestDict[bestID] = 4
                                best3.append(4)
                                return
                            elif r[0] == 'сет':
                                bestDict[bestID] = 3
                                best3.append(3)
                                return
                            elif r[0] == 'две пары':
                                bestDict[bestID] = 2
                                best3.append(2)
                                return
                            elif r[0] == 'пара':
                                bestDict[bestID] = 1
                                best3.append(1)
                                return
                            else:
                                bestDict[bestID] = 0
                                best3.append(0)
                                return
                    handd1 = ' '.join(map(str, f))
                    hands = [handd1]
                    best_cards3(hands)
            else:
                continue
        bestSetId3 = max(best3)
        game_results = []
        game_results.append(bestSetId)
        game_results.append(bestSetId2)
        game_results.append(bestSetId3)
        #print(bestSetId3)
        id_best1 = max(iter(bestDict), key=(lambda key: bestDict[key]))
        player3 = x.pop(id_best1 - 1)
        #print(player3)
        print("У вас", account,'$')
        print("Сделайте вашу ставку")
        bet = input("Ставка: ")
        bet2 = random.randint(1, 10)
        bet3 = random.randint(1, 10)
        if bet.isdigit():
            bet = int(bet)
            if bet > account:
                    print('Вы не можете поставить больше чем есть у вас на счету.')
                    print("--------------------")  
                    continue
            else:
                account -= bet
                bank1 = bet + bet2 + bet3
                bank += bank1
                print('Банк:', bank,'$')
                print("Играем!")
                time.sleep(1)
                print("======================================")
                time.sleep(1)
                print ("На столе:\n\t", t1,'||',t2,'||',t3, "В руке:",d,c)
                print("У вас", account,'$')
                print("Сделайте вашу ставку")
                bet = input("Ставка: ")
                bet2 = random.randint(10, 50)
                bet3 = random.randint(10, 50)
                if bet.isdigit():
                    bet = int(bet)
                    if bet > account:
                        print('Вы не можете поставить больше чем есть у вас на счету.')
                        print("--------------------")
                    else:
                        account -= bet
                        bank2 = bet + bet2 + bet3
                        bank += bank2
                        print('Банк:', bank,'$')
                        print("Играем!")
                        time.sleep(1)
                        print("======================================")
                        time.sleep(1)
                        print ("На столе:\n\t", t1,'||',t2,'||',t3,'||',t4,"В руке:",d,c)
                        print("У вас", account,'$')
                        print("Сделайте вашу ставку")
                        bet = input("Ставка: ")
                        bet2 = random.randint(10, 50)
                        bet3 = random.randint(10, 50)
                        if bet.isdigit():
                            bet = int(bet)
                            if bet > account:
                                print('Вы не можете поставить больше чем есть у вас на счету.')
                                print("--------------------")
                            else:
                                account -= bet
                                bank3 = bet + bet2 + bet3
                                bank += bank3
                                print('Банк:', bank,'$')
                                print("Играем!")
                                time.sleep(1)
                                print("======================================")
                                time.sleep(1)
                                print ("На столе:\n\t", t1,'||',t2,'||',t3,'||',t4,'||',t5,"В руке:",d,c)
                                print("У вас", account,'$')
                                print("Сделайте вашу ставку")
                                bet = input("Ставка: ")
                                if bet.isdigit():
                                    bet = int(bet)
                                    if bet > account:
                                        print('Вы не можете поставить больше чем есть у вас на счету.')
                                        print("--------------------")
                                    else:
                                        account -= bet
                                        bank4 = bet + bet2 + bet3
                                        bank += bank4
                                        print('Банк:', bank,'$')
                                        pl1 = ' '.join(map(str, player1))
                                        pl2 = ' '.join(map(str, player2))
                                        pl3 = ' '.join(map(str, player3))
                                        hands = [pl1, pl2, pl3]
                                        print(hands)
                                        print("%-18s %-15s %s" % ("КОМБИНАЦИЯ", "НАЗВАНИЕ", "ИНДЕКСЫ"))
                                        for cards in hands:
                                            r = rank(cards)
                                            print("%-18r %-15s %r" % (cards, r[0], r[1]))
                                        if bestSetId == max(game_results):
                                            print("Вы выйграли!")
                                            account += bank
                                            print("Выйгрыш:", bank, '$')
                                            time.sleep(1)
                                        elif bestSetId2 == max(game_results):
                                            print("Выйграл 2 игрок.")
                                            time.sleep(1)
                                        elif bestSetId3 == max(game_results):
                                            print("Выйграл 3 игрок.")
                                            time.sleep(1)
                                        else:
                                            won_lose = int(input("Выйграл: "))
                                            if won_lose == 1:
                                                print("Вы выйграли!")
                                                account += bank
                                                print("Выйгрыш:", bank, '$')
                                                time.sleep(1)
                                            elif won_lose == 2:
                                                print("Выйграл 2 игрок.")
                                                time.sleep(1)
                                            elif won_lose == 3:
                                                print("Выйграл 3 игрок.")
                                                time.sleep(1)
                                            elif won_lose == 4:
                                                print("Выйграли вы и 2 игрок.")
                                                account += bank/2
                                                print("Выйгрыш:", bank, '$')
                                                time.sleep(1)
                                            elif won_lose == 5:
                                                print("Выйграли вы и 3 игрок.")
                                                account += bank/2
                                                print("Выйгрыш:", bank, '$')
                                                time.sleep(1)
                                            elif won_lose == 6:
                                                print("Выйграл 2 и 3 игрок.")
                                                time.sleep(1)
                                            else:
                                                print("Ничья.")
                                                account += bank/3
                                                print("Выйгрыш:", bank, '$')
                                                time.sleep(1)
                                else:
                                    print('Значение должно быть числом.')
                                    print("--------------------")
                                    continue
                        else:
                            print('Значение должно быть числом.')
                            print("--------------------")
                            continue     
                else:
                    print('Значение должно быть числом.')
                    print("--------------------")
                    continue   
        else:
            print('Значение должно быть числом.')
            print("--------------------")
            continue
    print('Вы превысили лимит или у вас нет денег на счету. Далее игра невозможна. Спасибо за игру!')

            
texas_holdem(20) 