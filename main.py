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
    state1 = "Massachusetts"
    state2 = "New Hampshire"
    state3 = "Maine"

    itemList = []
    itemList = ItemData
    calculateTotalCharge(state1, itemList)

    return


def calculateTotalCharge(state, itemList):
    totalCharge = 0.0
    taxWic = 0.0  # tax for Wic Eligible food
    taxClothes = 0.0  # tax for clothes
    taxElse = 0.0  # tax for everything else

    if state == "Massachusetts":
        taxWic =
        taxClothes =
        taxElse =
    elif state == "New Hampshire":
        taxWic =
        taxClothes =
        taxElse =
    else:
        taxWic =
        taxClothes =
        taxElse =

    for item in itemList:
        if item.type == "Wic":
            totalCharge = totalCharge + item.price
            totalCharge = totalCharge + (totalCharge*taxWic)
        elif item.type == "Clothes":
            totalCharge = totalCharge + item.price
            totalCharge = totalCharge + (totalCharge * taxClothes)
        else:
            totalCharge = totalCharge + item.price
            totalCharge = totalCharge + (totalCharge * taxElse)

    return totalCharge


if __name__ == '__main__':
    main()
