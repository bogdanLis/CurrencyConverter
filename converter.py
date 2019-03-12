import requests
import logging
import sys
from typing import Dict


ERRORS: Dict[int, str] = {
    1: 'Введите сумму USD',
    2: 'Введите одно значение',
    3: 'Введите корректную сумму USD',
    4: 'Введите положительную сумму USD',
}


def isfloat(value):
    try:
        float(value)
        return True
    except ValueError:
        return False


def output(output_string: str, is_error: bool = False):
    '''
        Метод для вывода информации в консоль. Также осуществляет логгирование.
        Keyword arguments:
        output_string - сформированная строка для вывода вользователю
        is_error - флаг наличия ошибки 
    '''
    FORMAT = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    logging.basicConfig(filename="converter.log", format=FORMAT)
    if is_error:
        logging.error(output_string)
    else:
        logging.info(output_string)

    print(output_string)


class CurrencyConverter:
    '''
        Конвертер валют USD -> RUB
        Актуальный курс по ЦБ подгружается при инициализации
    '''
    ACCURACY = 2

    def __init__(self):
        self._usd_rate = requests.get(
                        'https://www.cbr-xml-daily.ru/daily_json.js'
                        ).json()['Valute']['USD']['Value']

    def calculate(self, usd_amount: float) -> float:
        return round(usd_amount*self._usd_rate, self.ACCURACY)


def main(cli_args):
    error_code: int = 0
    if len(cli_args) == 1:
        error_code = 1
    elif len(cli_args) > 2:
        error_code = 2
    else:
        usd_amount = cli_args[1]
        if not isfloat(usd_amount):
            error_code = 3
            if not float(usd_amount) >= 0:
                error_code = 4
    if error_code == 0:
        converter = CurrencyConverter()
        output('{} RUB'.format(converter.calculate(float(usd_amount))))
    else:
        output("Код ошибки: {0}  Текст ошибки: {1}".format(
                                                    error_code, 
                                                    ERRORS[error_code]), True)
    return error_code

if __name__ == '__main__':
    main(sys.argv)
