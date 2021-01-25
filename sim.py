import random

# declare contents of the deck
deck = ["Dusknoir Lv. X", "Dusknoir SP", "Dusknoir SC", "Dusknoir SC", "Dusclops", "Dusclops", "Duskull", "Duskull", "Duskull", "Duskull", "Giratina Lv. X", "Giratina Lv. X", "Giratina", "Giratina LL", "Spiritomb", "Spiritomb", "Azelf", "Uxie", "Unown G", "Cynthia's Feelings", "Cynthia's Feelings", "Roseanne's Research", "Roseanne's Research", "Roseanne's Research", "Roseanne's Research", "Bebe's Search", "Bebe's Search", "Bebe's Search", "Bebe's Search", "Marley's Request", "Luxury Ball", "Premier Ball", "Premier Ball", "Warp Point", "Warp Point", "Energy Restore", "Energy Restore", "Night Maintenance", "Night Maintenance", "Night Maintenance", "Rare Candy", "Rare Candy", "Rare Candy", "Rare Candy", "Expert Belt", "Expert Belt", "Broken Time Space", "Broken Time Space", "Psychic Energy", "Psychic Energy", "Psychic Energy", "Psychic Energy", "Psychic Energy", "Psychic Energy", "Psychic Energy", "Psychic Energy", "Psychic Energy", "Psychic Energy", "Psychic Energy", "Psychic Energy"]
d0 = [] # list of success with getting duskull out turn 1
check = 0
draws = 10000000

# main simulation loop
for i in range(draws):

    sdeck = deck # create shuffled deck list
    random.shuffle(sdeck) # shuffle deck
    prizes = []
    hand = []
    discard = []

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
            d0.append(1)
            check += 1
            continue

        # TURN 1
        hand.append(sdeck[13])

        if "Duskull" in hand: # duskull in hand
            d0.append(1)

        elif "Roseanne's Research" in hand: # can search out a basic
            d0.append(1)

        elif "Bebe's Search" in hand and len(hand) >= 2: # return a card to deck to search out a pokemon
            d0.append(1)

        elif "Luxury Ball" in hand: # search out a non lv. X pokemon
            d0.append(1)

        elif "Azelf" in hand and "Giratina" in hand or "Giratina LL" in hand or "Spiritomb" in hand or "Uxie" in hand or "Unown G" in hand and "Duskull" in prizes and len(hand) >= 3: # can check prizes for any card
            d0.append(1)

        else: # no duskull first turn
            d0.append(0)

# output section
print("Duskull draws: " + str(sum(d0)))
print("Total draws: " + str(len(d0)))
print("Duskull chance: "+ str(round((sum(d0)*100)/len(d0), 2)) + "%")
print("\n")
print("Basic chance: " + str(round((len(d0)*100/draws), 2)) + "%")
print("Duskull as basic chance: " + str(round((check*100)/len(d0), 2)) + "%")
print("\n")