import random


atlantic = [
    "Buffalo Sabres",
    "Boston Bruins",
    "Detroit Red Wings",
    "Florida Panthers",
    "Tampa Bay Lightning",
]

metropolitan = [
    "New Jersey Devils",
    "Columbus Blue Jackets",
    "Washington Capitals",
    "Carolina Hurricanes",
    "New York Islanders",
    "Pittsburgh Penguins",
    "New York Rangers",
    "Philadelphia Flyers"
]

central = [
    "Minnesota Wild",
    "St. Louis Blues",
    "Nashville Predators",
    "Colorado Avalanche",
    "Dallas Stars",
    "Chicago Blackhawks",
    "Arizona Coyotes"
]

pacific = [
    "Vegas Golden Knights",
    "San Jose Sharks",
    "Seattle Kraken",
    "Anaheim Ducks",
    "Los Angeles Kings",
]

canadian = [
    "Toronto Maple Leafs",
    "Ottawa Senators",
    "Montreal Canadiens",
    "Winnipeg Jets",
    "Edmonton Oilers",
    "Calgary Flames",
    "Vancouver Canucks"
]

die = atlantic + metropolitan + central + pacific


def generate_random_num(n: int) -> int:
    return random.randint(0, n-1)


def shuffle():
    random.shuffle(atlantic)
    random.shuffle(metropolitan)
    random.shuffle(central)
    random.shuffle(pacific)
    random.shuffle(canadian)
    random.shuffle(die)


def build_card(n: int):
    shuffle()

    atlantic_num = generate_random_num(len(atlantic))
    metropolitan_num = generate_random_num(len(metropolitan))
    central_num = generate_random_num(len(central))
    pacific_num = generate_random_num(len(pacific))
    canadian_num = generate_random_num(len(canadian))
    die_num = generate_random_num(len(die))

    print(f'card {n}')
    print(f'atlantic team: {atlantic[atlantic_num]}')
    print(f'metropolitan team: {metropolitan[metropolitan_num]}')
    print(f'central team: {central[central_num]}')
    print(f'pacific team: {pacific[pacific_num]}')
    print(f'canadian team: {canadian[canadian_num]}')
    print(f'die team: {die[die_num]}')

    del atlantic[atlantic_num]
    del metropolitan[metropolitan_num]
    del central[central_num]
    del pacific[pacific_num]
    del canadian[canadian_num]
    del die[die_num]


if __name__ == '__main__':
    build_card(1)
    print('\n')
    build_card(2)
