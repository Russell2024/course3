import json
from utils import *


def normal_output(file_name):
    with open(file_name, encoding='utf-8') as f:
        operations = json.load(f)

    operations_sort = sort_data(operations)

    executed_five = []
    i = 0

    for operation in operations_sort:
        if i < 5:
            if operation['state'] == 'EXECUTED':
                executed_five.append(operation)
                i += 1

    for i in range(len(executed_five)):
        if 'from' in executed_five[i]:
            print(f'{data_normal(executed_five[i]['date'])} {executed_five[i]['description']}\n'
                  f'{saving_card_from(executed_five[i]['from'])} -> {saving_card_to(executed_five[i]['to'])}\n'
                  f'{executed_five[i]['operationAmount']['amount']} {executed_five[i]['operationAmount']['currency']['name']}')
        else:
            print(f'{data_normal(executed_five[i]['date'])} {executed_five[i]['description']}\n'
                  f'-> {saving_card_to(executed_five[i]['to'])}\n'
                  f'{executed_five[i]['operationAmount']['amount']} {executed_five[i]['operationAmount']['currency']['name']}')
        print()
    return ''


if __name__ == '__main__':
    normal_output('operations.json')
