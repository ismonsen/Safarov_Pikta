import requests


def fns(ifns, oktmmf):
    r = requests.post("https://service.nalog.ru/addrno-proc.json", data={'c': 'next', 'step': 1, 'npKind': 'fl',
                                                                         'ifns': ifns, 'oktmmf': oktmmf})
    if r.status_code == 200:
        mass = {'Получатель платежа': r.json()['payeeDetails']['payeeName'],
                'ИНН получателя': r.json()['payeeDetails']['payeeInn'],
                'КПП получателя': r.json()['payeeDetails']['payeeKpp'],
                'Банк получателя': r.json()['payeeDetails']['bankName'],
                'БИК': r.json()['payeeDetails']['bankBic'],
                'Счет №': r.json()['payeeDetails']['payeeAcc']}
        for key, val in mass.items():
            print(f'{key} : {val}')
    else:
        print('Введены неверные код ИНФС и/или ОКТМО')


ifns_val = input('Введите код ИФНС: ')
oktmmf_val = input('Введите ОКТМО: ')
fns(ifns_val, oktmmf_val)
