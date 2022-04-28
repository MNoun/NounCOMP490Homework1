# Created by: Mitchell Noun
# Date created: 4/21/22
# Class: COMP490 Senior Design and Development
# Assignment: Homework 1
from dataclasses import dataclass


@dataclass
class ItemData:
    name: str
    price: float
    type: str


def main():
    return


def calculateTotalCharge(state, itemList):
    totalCharge = 0.0
    taxWic = 0.0  # tax for Wic Eligible food
    taxClothes = 0.0  # tax for clothes
    taxElse = 0.0  # tax for everything else

    # get taxes for each state
    if state == "Massachusetts":
        taxWic = 0.0
        taxClothes = 0.0
        taxElse = 0.0625
    elif state == "New Hampshire":
        taxWic = 0.0
        taxClothes = 0.0
        taxElse = 0.0
    else:
        taxWic = 0.0
        taxClothes = 0.055
        taxElse = 0.055

    if len(itemList) > 0:  # only calculate if there is something in the shopping cart
        for item in itemList:
            if item.type == "Wic":
                totalCharge = totalCharge + item.price
                totalCharge = totalCharge + (item.price*taxWic)
            elif item.type == "Clothes":
                totalCharge = totalCharge + item.price
                totalCharge = totalCharge + (item.price*taxClothes)
            else:
                totalCharge = totalCharge + item.price
                totalCharge = totalCharge + (item.price*taxElse)
    else:
        return totalCharge  # returns 0.0

    return totalCharge


if __name__ == '__main__':
    main()
