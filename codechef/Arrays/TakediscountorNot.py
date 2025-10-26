'''
Take discount or Not
You are given a coupon that gives you a discount of Y rupees on each item you buy,
provided the price of the item is at least Y rupees. You have X rupees in
total and there are N items you want to buy, with their respective prices given in the array Prices.
Determine if using the coupon will help you save more money than not using it.

'''
class Solution:
    def check_coupon(self, n, x, y, prices):
        save = 0
        for price in prices:
            if price >= y:
                save += y
            else:
                save += price

        if save > x:
            return "COUPON"
        else:
            return "NO COUPON"
