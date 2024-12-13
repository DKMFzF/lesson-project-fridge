from decimal import Decimal
import datetime as dt
from datetime import date, timedelta

# const
DATE_FORMAT = '%Y-%m-%d'
goods = {}

# add new prod
def add(items: dict, title: str, amount: Decimal, expiration_date=None) -> object:
    if title not in items:
        items[title] = []
    expiration_date = dt.datetime.strptime(
        expiration_date,
        DATE_FORMAT
    ).date() if expiration_date else expiration_date
    return items[title].append(
        {
            'amount': amount,
            'expiration_date': expiration_date
        }
    )

# valid new prod
def add_by_note(items: dict, note: str) -> object:
    parts = note.split(' ')
    if len(parts[-1].split('-')) == 3:
        expiration_date = parts[-1]
        good_amount = Decimal(parts[-2])
        title = str.join(' ', parts[0:-2])
        return add(items, title, good_amount, expiration_date)
    good_amount = Decimal(parts[-1])
    title = str.join(' ', parts[0:-1])
    return add(items, title, good_amount)


# search prod
def find(items: dict, needle: str) -> list:
    arrAchiev = []
    needleLow = needle.lower()
    for key in items.keys():
        if needleLow in key.lower():
            arrAchiev.append(key)
    return arrAchiev


# count prods
def amount(items: dict, needle: str):
    countProd = Decimal('0')
    for key in items.keys():
        if needle.lower() in key.lower():
            for value in items[key]:
                countProd += value['amount']
    return countProd


# expire prod
def expire(items, in_advance_days=0):
    TODAY = date.today()
    arrTemplateDate = []
    for key, product_list in items.items():
        amountCounter = 0
        for value in product_list:
            if value['expiration_date'] is not None:
                expiration_date = value['expiration_date']
                if expiration_date <= TODAY or TODAY + timedelta(days=in_advance_days) >= expiration_date:
                    amountCounter += value['amount']
        if amountCounter > 0:
            arrTemplateDate.append((key, amountCounter))
    return arrTemplateDate
