from datetime import datetime


def sort_data(listing):
    return sorted(listing, key=lambda x: datetime.strptime(x['date'], "%Y-%m-%dT%H:%M:%S.%f"), reverse=True)


def data_normal(string):
    string_split = string.split('T')
    string_split_more = string_split[0].split('-')
    return f'{string_split_more[2]}.{string_split_more[1]}.{string_split_more[0]}'


def saving_card_from(string):
    string_split = string.split(' ')
    card = [i for i in string_split[-1]]
    count = 0
    for _ in card:
        if len(card) == 16:
            if count in range(6, 12):
                card[count] = '*'
            count += 1
        elif len(card) == 20:
            if count in range(6, 16):
                card[count] = '*'
            count += 1
    save_card = ''
    k = 1
    for i in card:
        if k % 4 == 0:
            save_card += i + ' '
        else:
            save_card += i
        k += 1
    return f'{' '.join(string_split[:len(string_split) - 1])} {save_card}'


def saving_card_to(string):
    string_split = string.split(' ')
    return f'{string_split[0]} **{string_split[1][-4:]}'
