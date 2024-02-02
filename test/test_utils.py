from src.utils import *


def test_data_normal():
    assert data_normal('2022-01-01T00:00:00.000000') == '01.01.2022'


def test_saving_card_from():
    assert saving_card_from('Счет 1119147751996705') == 'Счет 1119 14** **** 6705 '


def test_saving_card_to():
    assert saving_card_to('Счет 1119147751996705') == 'Счет **6705'

