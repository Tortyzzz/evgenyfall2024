import math
def best_days_for_gold(prices):
    if not prices:
        return None, None

    min_price_index = 0
    max_profit = 0
    buy_day = sell_day = 0

    for current_day in range(1, len(prices)):

        if prices[current_day] < prices[min_price_index]:
            min_price_index = current_day
        else:

            current_profit = prices[current_day] - prices[min_price_index]

            if current_profit > max_profit:
                max_profit = current_profit
                buy_day = min_price_index
                sell_day = current_day

    return buy_day, sell_day


def max_profit(prices):
    if not prices:
        return 0

    min_price = float(math.inf)
    max_profit = 0

    for price in prices:

        if price < min_price:
            min_price = price

        current_profit = price - min_price

        if current_profit > max_profit:
            max_profit = current_profit

    return max_profit

gold_prices_1 = [100, 120, 140, 160, 180, 200, 220]
gold_prices_2 = [200, 180, 220, 160, 240, 260, 210]
gold_prices_3 = [250, 230, 210, 190, 170, 150, 130]
gold_prices_4 = [200, 200, 200, 200, 200, 200, 200]
gold_prices_5 = [150, 160, 155, 170, 180, 175, 165]

results = [
    max_profit(gold_prices_1),
    max_profit(gold_prices_2),
    max_profit(gold_prices_3),
    max_profit(gold_prices_4),
    max_profit(gold_prices_5)
]

days_of_week = ["Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота", "Воскресенье"]

for i in range(1, len(results) + 1):
    buy_day_index = sell_day_index = results[i - 1]

    print(f"Максимальная прибыль для набора {i}: {results[i - 1]}")

    print(f"Набор {i}: Купить в {days_of_week[buy_day_index]}, Продать в {days_of_week[sell_day_index]}")