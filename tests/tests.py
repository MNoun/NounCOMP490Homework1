import main
import pytest

def testCalculateTotalCharge():
    state1 = "Massachusetts"
    state2 = "New Hampshire"
    state3 = "Maine"

    item = main.ItemData("food", 1.50, "Wic")
    item2 = main.ItemData("shirt", 2.75, "Clothes")
    item3 = main.ItemData("pen", 1.50, "Else")
    itemList = [item, item2, item3]

    total1 = main.calculateTotalCharge(state1, itemList)
    total2 = main.calculateTotalCharge(state2, itemList)
    total3 = main.calculateTotalCharge(state3, itemList)
    assert total1 == 5.84375  # Massachusetts happy path
    assert total2 == 5.75  # New Hampshire happy path
    assert total3 == 5.98375  # Maine happy path

    itemList2 = []
    total4 = main.calculateTotalCharge(state1, itemList2)
    assert total4 == 0.0  # empty shopping cart test
