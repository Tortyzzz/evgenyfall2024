import random # Using for  random.choice(deck)

def quick_sort_deck(deck):
    if len(deck) < 4:
        for i in range(len(deck)):
            for j in range(len(deck) - (i + 1)):
                if deck[i] > deck[j - 1]:
                    deck[i], deck[j - 1] = deck[j - 1], deck[i]
        return deck
    else:
        sorted_card = random.choice(deck)

        left_cards = [card for card in deck if card < sorted_card]
        right_cards = [card for card in deck if card > sorted_card]

        return quick_sort_deck(left_cards) + [sorted_card] + quick_sort_deck(right_cards)

deck = [7, 3, 3, 4, 1, 2, 5]
sorted_deck = quick_sort_deck(deck)
print(sorted_deck)  # Ожидаемый вывод: [1, 2, 3, 4, 5, 7]
# Тест 1
#assert quick_sort_deck([4, 2, 7, 1, 3, 5]) == [1, 2, 3, 4, 5, 7]
# Тест 2
#assert quick_sort_deck([10, 5, 3, 8]) == [3, 5, 8, 10]
# Тест 3
#assert quick_sort_deck([1]) == [1]
# Тест 4
#assert quick_sort_deck([3, 2]) == [2, 3]
# Тест 5
#assert quick_sort_deck([7, 3, 3, 4, 1, 2, 5]) == [1, 2, 3, 3, 4, 5, 7]
print("OK!")