import random

# declare contents of the deck
deck = ["Dusknoir Lv. X", "Dusknoir SP", "Dusknoir SC", "Dusknoir SC", "Dusclops", "Dusclops", "Duskull", "Duskull", "Duskull", "Duskull", "Giratina Lv. X", "Giratina Lv. X", "Giratina", "Giratina LL", "Spiritomb", "Spiritomb", "Azelf", "Uxie", "Unown G", "Cynthia's Feelings", "Cynthia's Feelings", "Roseanne's Research", "Roseanne's Research", "Roseanne's Research", "Roseanne's Research", "Bebe's Search", "Bebe's Search", "Bebe's Search", "Bebe's Search", "Marley's Request", "Luxury Ball", "Premier Ball", "Premier Ball", "Warp Point", "Warp Point", "Energy Restore", "Energy Restore", "Night Maintenance", "Night Maintenance", "Night Maintenance", "Rare Candy", "Rare Candy", "Rare Candy", "Rare Candy", "Expert Belt", "Expert Belt", "Broken Time Space", "Broken Time Space", "Psychic Energy", "Psychic Energy", "Psychic Energy", "Psychic Energy", "Psychic Energy", "Psychic Energy", "Psychic Energy", "Psychic Energy", "Psychic Energy", "Psychic Energy", "Psychic Energy", "Psychic Energy"]
d0 = [] # list of success with getting duskull out turn 1
d1 = [] # list of success with getting dusclops out turn 1
d2 = [] # list of success with getting dusknoir out turn 1
check = 0
inc0 = False
inc1 = False
inc2 = False
draws = 10000000

# main simulation loop
for i in range(draws):

    sdeck = deck # create shuffled deck list
    random.shuffle(sdeck) # shuffle deck
    prizes = []
    hand = []
    discard = []
    inc0 = False
    inc1 = False
    inc2 = False

    if len(sdeck) < 60:
        sdeck = deck # create shuffled deck list
        random.shuffle(sdeck) # shuffle deck

    # loop to get prize cards
    for j in range(6):
        prizes.append(sdeck[j])

    # loop to get starting hand
    for j in range(7):
        hand.append(sdeck[j+6])

    # check for basic
    if "Duskull" in hand or "Giratina" in hand or "Giratina LL" in hand or "Spiritomb" in hand or "Azelf" in hand or "Uxie" in hand or "Unown G" in hand:
        
        # TURN 0
        if "Duskull" in hand: # duskull in hand
            if inc0 == False:
                d0.append(1)
                check += 1
                inc0 = True

            if "Rare Candy" in hand: # can attempt to field dusknoir
                if "Dusknoir SP" in hand or "Dusknoir SC" in hand: # dusknoir already in hand
                    if inc2 == False:
                        d2.append(1)
                        inc2 = True

                elif "Luxury Ball" in hand: # search out a non lv. x pokemon
                    if inc2 == False:
                        d2.append(1)
                        inc2 = True

                elif "Bebe's Search" in hand and len(hand) >= 4: # return a card to deck to search out a pokemon
                    if inc2 == False:
                        d2.append(1)
                        inc2 = True

                elif "Azelf" in hand and "Dusknoir SP" in prizes or "Dusknoir SC" in prizes and len(hand) >=4: # can check prizes for any card
                    if inc2 == False:
                        d2.append(1)
                        inc2 = True

            elif "Broken Time Space" in hand: # can evolve pokemon the turn they are played
                if "Luxury Ball" in hand and "Dusknoir SP" in hand or "Dusknoir SC" in hand: # search out a non lv. x pokemon
                    if inc1 == False:
                        d1.append(1)
                        inc1 = True
                    if inc2 == False:
                        d2.append(1)
                        inc2 = True

                elif "Bebe's Search" in hand and "Dusknoir SP" in hand or "Dusknoir SC" in hand and len(hand) >=5: # return a card to deck to search out a pokemon
                    if inc1 == False:
                        d1.append(1)
                        inc1 = True
                    if inc2 == False:
                        d2.append(1)
                        inc2 = True

                elif "Luxury Ball" in hand and "Bebe's Search" in hand and len(hand) >=5: # search out a non lv. x pokemon and return a card to deck to search out a pokemon
                    if inc1 == False:
                        d1.append(1)
                        inc1 = True
                    if inc2 == False:
                        d2.append(1)
                        inc2 = True

                elif "Azelf" in hand and "Luxury Ball" in hand and len(hand) >=5 and "Dusclops" in prizes or "Dusknoir SP" in prizes or "Dusknoir SC" in prizes: # search out a non lv. x pokemon and can check prizes for any card
                    if inc1 == False:
                        d1.append(1)
                        inc1 = True
                    if inc2 == False:
                        d2.append(1)
                        inc2 = True

                elif "Azelf" in hand and "Bebe's Search" in hand and len(hand) >=6 and "Dusclops" in prizes or "Dusknoir SP" in prizes or "Dusknoir SC" in prizes: # can check prizes for any card and return a card to deck to search out a pokemon
                    if inc1 == False:
                        d1.append(1)
                        inc1 = True
                    if inc2 == False:
                        d2.append(1)
                        inc2 = True

            elif "Spiritomb" in hand: # search for a card that evolved from your pokemon and evolve it
                if inc1 == False:
                    d1.append(1)
                    inc1 = True

            elif "Dusclops" in hand: # dusclops in hand
                if inc1 == False:
                    d1.append(1)
                    inc1 = True

                if "Broken Time Space" in hand: # can attempt to field dusknoir
                    if "Dusknoir SP" in hand or "Dusknoir SC" in hand:
                        if inc2 == False:
                            d2.append(1)
                            inc2 = True

                    elif "Bebe's Search" in hand and len(hand) >=5: # return a card to deck to search out a pokemon
                        if inc2 == False:
                            d2.append(1)
                            inc2 = True

                    elif "Luxury Ball" in hand: # search out a non lv. x pokemon
                        if inc2 == False:
                            d2.append(1)
                            inc2 = True

                    elif "Azelf" in hand and len(hand) >=5 and "Dusknoir SP" in prizes or "Dusknoir SC" in prizes:
                        if inc2 == False:
                            d2.append(1)
                            inc2 = True

        # TURN 1
        hand.append(sdeck[13])

        if "Duskull" in hand: # duskull in hand
            if inc0 == False:
                d0.append(1)
                inc0 = True

            if "Rare Candy" in hand: # can attempt to field dusknoir
                if "Dusknoir SP" in hand or "Dusknoir SC" in hand: # dusknoir already in hand
                    if inc2 == False:
                        d2.append(1)
                        inc2 = True

                elif "Luxury Ball" in hand: # search out a non lv. x pokemon
                    if inc2 == False:
                        d2.append(1)
                        inc2 = True

                elif "Bebe's Search" in hand and len(hand) >= 4: # return a card to deck to search out a pokemon
                    if inc2 == False:
                        d2.append(1)
                        inc2 = True

                elif "Azelf" in hand and "Dusknoir SP" in prizes or "Dusknoir SC" in prizes and len(hand) >=3: # can check prizes for any card
                    if inc2 == False:
                        d2.append(1)
                        inc2 = True

            elif "Broken Time Space" in hand: # can evolve pokemon the turn they are played
                if "Luxury Ball" in hand and "Dusknoir SP" in hand or "Dusknoir SC" in hand: # search out a non lv. x pokemon
                    if inc1 == False:
                        d1.append(1)
                        inc1 = True
                    if inc2 == False:
                        d2.append(1)
                        inc2 = True

                elif "Bebe's Search" in hand and "Dusknoir SP" in hand or "Dusknoir SC" in hand and len(hand) >=5: # return a card to deck to search out a pokemon
                    if inc1 == False:
                        d1.append(1)
                        inc1 = True
                    if inc2 == False:
                        d2.append(1)
                        inc2 = True

                elif "Luxury Ball" in hand and "Bebe's Search" in hand and len(hand) >=5: # search out a non lv. x pokemon and return a card to deck to search out a pokemon
                    if inc1 == False:
                        d1.append(1)
                        inc1 = True
                    if inc2 == False:
                        d2.append(1)
                        inc2 = True

                elif "Azelf" in hand and "Luxury Ball" in hand and len(hand) >=5 and "Dusclops" in prizes or "Dusknoir SP" in prizes or "Dusknoir SC" in prizes: # search out a non lv. x pokemon and can check prizes for any card
                    if inc1 == False:
                        d1.append(1)
                        inc1 = True
                    if inc2 == False:
                        d2.append(1)
                        inc2 = True

                elif "Azelf" in hand and "Bebe's Search" in hand and len(hand) >=6 and "Dusclops" in prizes or "Dusknoir SP" in prizes or "Dusknoir SC" in prizes: # can check prizes for any card and return a card to deck to search out a pokemon
                    if inc1 == False:
                        d1.append(1)
                        inc1 = True
                    if inc2 == False:
                        d2.append(1)
                        inc2 = True

            elif "Spiritomb" in hand: # search for a card that evolved from your pokemon and evolve it
                if inc1 == False:
                    d1.append(1)
                    inc1 = True

            elif "Dusclops" in hand: # dusclops in hand
                if inc1 == False:
                    d1.append(1)
                    inc1 = True

                if "Broken Time Space" in hand: # can attempt to field dusknoir
                    if "Dusknoir SP" in hand or "Dusknoir SC" in hand:
                        if inc2 == False:
                            d2.append(1)
                            inc2 = True

                    elif "Bebe's Search" in hand and len(hand) >=5: # return a card to deck to search out a pokemon
                        if inc2 == False:
                            d2.append(1)
                            inc2 = True

                    elif "Luxury Ball" in hand: # search out a non lv. x pokemon
                        if inc2 == False:
                            d2.append(1)
                            inc2 = True

                    elif "Azelf" in hand and len(hand) >=5 and "Dusknoir SP" in prizes or "Dusknoir SC" in prizes:
                        if inc2 == False:
                            d2.append(1)
                            inc2 = True

        elif "Roseanne's Research" in hand: # can search out a basic
            if inc0 == False:
                d0.append(1)
                inc0 = True

            if "Rare Candy" in hand: # can attempt to field dusknoir
                if "Dusknoir SP" in hand or "Dusknoir SC" in hand: # dusknoir already in hand
                    if inc2 == False:
                        d2.append(1)
                        inc2 = True

                elif "Luxury Ball" in hand: # search out a non lv. x pokemon
                    if inc2 == False:
                        d2.append(1)
                        inc2 = True

                elif "Azelf" in hand and "Giratina" in hand or "Giratina LL" in hand or "Uxie" in hand or "Spiritomb" in hand or "Unown G" in hand and "Dusknoir SP" in prizes or "Dusknoir SC" in prizes and len(hand) >=5: # can check prizes for any card
                    if inc2 == False:
                        d2.append(1)
                        inc2 = True

            elif "Broken Time Space" in hand: # can evolve pokemon the turn they are played
                if "Luxury Ball" in hand and "Dusknoir SP" in hand or "Dusknoir SC" in hand: # search out a non lv. x pokemon
                    if inc1 == False:
                        d1.append(1)
                        inc1 = True
                    if inc2 == False:
                        d2.append(1)
                        inc2 = True

                elif "Azelf" in hand and "Giratina" in hand or "Giratina LL" in hand or "Uxie" in hand or "Spiritomb" in hand or "Unown G" in hand and "Luxury Ball" in hand and len(hand) >=6 and "Dusclops" in prizes or "Dusknoir SP" in prizes or "Dusknoir SC" in prizes: # search out a non lv. x pokemon and can check prizes for any card
                    if inc1 == False:
                        d1.append(1)
                        inc1 = True
                    if inc2 == False:
                        d2.append(1)
                        inc2 = True

            elif "Spiritomb" in hand: # search for a card that evolved from your pokemon and evolve it
                if inc1 == False:
                    d1.append(1)
                    inc1 = True

            elif "Dusclops" in hand: # dusclops in hand
                if inc1 == False:
                    d1.append(1)
                    inc1 = True

                if "Broken Time Space" in hand: # can attempt to field dusknoir
                    if "Dusknoir SP" in hand or "Dusknoir SC" in hand:
                        if inc2 == False:
                            d2.append(1)
                            inc2 = True

                    elif "Luxury Ball" in hand: # search out a non lv. x pokemon
                        if inc2 == False:
                            d2.append(1)
                            inc2 = True

                    elif "Azelf" in hand and "Giratina" in hand or "Giratina LL" in hand or "Uxie" in hand or "Spiritomb" in hand or "Unown G" in hand and len(hand) >=6 and "Dusknoir SP" in prizes or "Dusknoir SC" in prizes:
                        if inc2 == False:
                            d2.append(1)
                            inc2 = True

        elif "Bebe's Search" in hand and len(hand) >= 2: # return a card to deck to search out a pokemon
            if inc0 == False:
                d0.append(1)
                inc0 = True

            if "Rare Candy" in hand: # can attempt to field dusknoir
                if "Dusknoir SP" in hand or "Dusknoir SC" in hand: # dusknoir already in hand
                    if inc2 == False:
                        d2.append(1)
                        inc2 = True

                elif "Luxury Ball" in hand: # search out a non lv. x pokemon
                    if inc2 == False:
                        d2.append(1)
                        inc2 = True

                elif "Azelf" in hand and "Giratina" in hand or "Giratina LL" in hand or "Uxie" in hand or "Spiritomb" in hand or "Unown G" in hand and "Dusknoir SP" in prizes or "Dusknoir SC" in prizes and len(hand) >=6: # can check prizes for any card
                    if inc2 == False:
                        d2.append(1)
                        inc2 = True

            elif "Broken Time Space" in hand: # can evolve pokemon the turn they are played
                if "Luxury Ball" in hand and "Dusknoir SP" in hand or "Dusknoir SC" in hand: # search out a non lv. x pokemon
                    if inc1 == False:
                        d1.append(1)
                        inc1 = True
                    if inc2 == False:
                        d2.append(1)
                        inc2 = True

                elif "Azelf" in hand and "Luxury Ball" in hand and "Giratina" in hand or "Giratina LL" in hand or "Uxie" in hand or "Spiritomb" in hand or "Unown G" in hand and len(hand) >=7 and "Dusclops" in prizes or "Dusknoir SP" in prizes or "Dusknoir SC" in prizes: # search out a non lv. x pokemon and can check prizes for any card
                    if inc1 == False:
                        d1.append(1)
                        inc1 = True
                    if inc2 == False:
                        d2.append(1)
                        inc2 = True

            elif "Spiritomb" in hand: # search for a card that evolved from your pokemon and evolve it
                if inc1 == False:
                    d1.append(1)
                    inc1 = True

            elif "Dusclops" in hand: # dusclops in hand
                if inc1 == False:
                    d1.append(1)
                    inc1 = True

                if "Broken Time Space" in hand: # can attempt to field dusknoir
                    if "Dusknoir SP" in hand or "Dusknoir SC" in hand:
                        if inc2 == False:
                            d2.append(1)
                            inc2 = True

                    elif "Luxury Ball" in hand: # search out a non lv. x pokemon
                        if inc2 == False:
                            d2.append(1)
                            inc2 = True

                    elif "Azelf" in hand and "Giratina" in hand or "Giratina LL" in hand or "Uxie" in hand or "Spiritomb" in hand or "Unown G" in hand and len(hand) >=7 and "Dusknoir SP" in prizes or "Dusknoir SC" in prizes:
                        if inc2 == False:
                            d2.append(1)
                            inc2 = True

        elif "Luxury Ball" in hand: # search out a non lv. X pokemon
            if inc0 == False:
                d0.append(1)
                inc0 = True

            if "Rare Candy" in hand: # can attempt to field dusknoir
                if "Dusknoir SP" in hand or "Dusknoir SC" in hand: # dusknoir already in hand
                    if inc2 == False:
                        d2.append(1)
                        inc2 = True

                elif "Bebe's Search" in hand and len(hand) >= 5: # return a card to deck to search out a pokemon
                    if inc2 == False:
                        d2.append(1)
                        inc2 = True

                elif "Azelf" in hand and "Giratina" in hand or "Giratina LL" in hand or "Uxie" in hand or "Spiritomb" in hand or "Unown G" in hand and "Dusknoir SP" in prizes or "Dusknoir SC" in prizes and len(hand) >=5: # can check prizes for any card
                    if inc2 == False:
                        d2.append(1)
                        inc2 = True

            elif "Broken Time Space" in hand: # can evolve pokemon the turn they are played
                if "Bebe's Search" in hand and "Dusknoir SP" in hand or "Dusknoir SC" in hand and len(hand) >=6: # return a card to deck to search out a pokemon
                    if inc1 == False:
                        d1.append(1)
                        inc1 = True
                    if inc2 == False:
                        d2.append(1)
                        inc2 = True

                elif "Azelf" in hand and "Bebe's Search" in hand and "Giratina" in hand or "Giratina LL" in hand or "Uxie" in hand or "Spiritomb" in hand or "Unown G" in hand and len(hand) >=7 and "Dusclops" in prizes or "Dusknoir SP" in prizes or "Dusknoir SC" in prizes: # can check prizes for any card and return a card to deck to search out a pokemon
                    if inc1 == False:
                        d1.append(1)
                        inc1 = True
                    if inc2 == False:
                        d2.append(1)
                        inc2 = True

            elif "Spiritomb" in hand: # search for a card that evolved from your pokemon and evolve it
                if inc1 == False:
                    d1.append(1)
                    inc1 = True

            elif "Dusclops" in hand: # dusclops in hand
                if inc1 == False:
                    d1.append(1)
                    inc1 = True

                if "Broken Time Space" in hand: # can attempt to field dusknoir
                    if "Dusknoir SP" in hand or "Dusknoir SC" in hand:
                        if inc2 == False:
                            d2.append(1)
                            inc2 = True

                    elif "Bebe's Search" in hand and len(hand) >=6: # return a card to deck to search out a pokemon
                        if inc2 == False:
                            d2.append(1)
                            inc2 = True

                    elif "Azelf" in hand and "Giratina" in hand or "Giratina LL" in hand or "Uxie" in hand or "Spiritomb" in hand or "Unown G" in hand and len(hand) >=6 and "Dusknoir SP" in prizes or "Dusknoir SC" in prizes:
                        if inc2 == False:
                            d2.append(1)
                            inc2 = True

        elif "Azelf" in hand and "Giratina" in hand or "Giratina LL" in hand or "Spiritomb" in hand or "Uxie" in hand or "Unown G" in hand and "Duskull" in prizes and len(hand) >= 3: # can check prizes for any card
            if inc0 == False:
                d0.append(1)
                inc0 = True

            if "Rare Candy" in hand: # can attempt to field dusknoir
                if "Dusknoir SP" in hand or "Dusknoir SC" in hand: # dusknoir already in hand
                    if inc2 == False:
                        d2.append(1)
                        inc2 = True

                elif "Luxury Ball" in hand: # search out a non lv. x pokemon
                    if inc2 == False:
                        d2.append(1)
                        inc2 = True

                elif "Bebe's Search" in hand and len(hand) >= 5: # return a card to deck to search out a pokemon
                    if inc2 == False:
                        d2.append(1)
                        inc2 = True

            elif "Broken Time Space" in hand: # can evolve pokemon the turn they are played
                if "Luxury Ball" in hand and "Dusknoir SP" in hand or "Dusknoir SC" in hand: # search out a non lv. x pokemon
                    if inc1 == False:
                        d1.append(1)
                        inc1 = True
                    if inc2 == False:
                        d2.append(1)
                        inc2 = True

                elif "Bebe's Search" in hand and "Dusknoir SP" in hand or "Dusknoir SC" in hand and len(hand) >=6: # return a card to deck to search out a pokemon
                    if inc1 == False:
                        d1.append(1)
                        inc1 = True
                    if inc2 == False:
                        d2.append(1)
                        inc2 = True

                elif "Luxury Ball" in hand and "Bebe's Search" in hand and len(hand) >=6: # search out a non lv. x pokemon and return a card to deck to search out a pokemon
                    if inc1 == False:
                        d1.append(1)
                        inc1 = True
                    if inc2 == False:
                        d2.append(1)
                        inc2 = True

            elif "Spiritomb" in hand: # search for a card that evolved from your pokemon and evolve it
                if inc1 == False:
                    d1.append(1)
                    inc1 = True

            elif "Dusclops" in hand: # dusclops in hand
                if inc1 == False:
                    d1.append(1)
                    inc1 = True

                if "Broken Time Space" in hand: # can attempt to field dusknoir
                    if "Dusknoir SP" in hand or "Dusknoir SC" in hand:
                        if inc2 == False:
                            d2.append(1)
                            inc2 = True

                    elif "Bebe's Search" in hand and len(hand) >=6: # return a card to deck to search out a pokemon
                        if inc2 == False:
                            d2.append(1)
                            inc2 = True

                    elif "Luxury Ball" in hand: # search out a non lv. x pokemon
                        if inc2 == False:
                            d2.append(1)
                            inc2 = True

        else: # no duskull first turn
            d0.append(0)

# output section
print("Duskull fields: " + str(sum(d0)))
print("Total fields: " + str(len(d0)))
print("Duskull chance: "+ str(round((sum(d0)*100)/len(d0), 2)) + "%")
print("\n")
print("Basic chance: " + str(round((len(d0)*100/draws), 2)) + "%")
print("Duskull as basic chance: " + str(round((check*100)/len(d0), 2)) + "%")
print("\n")
print("Dusclops fields: " + str(sum(d1)))
print("Total fields: " + str(len(d0)))
print("Dusclops chance: "+ str(round((sum(d1)*100)/len(d0), 2)) + "%")
print("\n")
print("Dusknoir fields: " + str(sum(d2)))
print("Total fields: " + str(len(d0)))
print("Dusknoir chance: "+ str(round((sum(d2)*100)/len(d0), 2)) + "%")
print("\n")