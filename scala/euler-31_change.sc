/*
Problem 31
22 November 2002

In England the currency is made up of pound, £, and pence, p, and there are eight coins in general circulation:

    1p, 2p, 5p, 10p, 20p, 50p, £1 (100p) and £2 (200p).

It is possible to make £2 in the following way:

    1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p

How many different ways can £2 be made using any number of coins?
*/

object euler-31_change {
	// http://www.algorithmist.com/index.php/Coin_Change
	def countChange(money: Int, coins: List[Int]): Int = {
		if (money == 0) 1
		else if (money < 0) 0
		else if (coins.isEmpty && money >= 1) 0
		else countChange(money, coins.tail) + countChange(money - coins.head, coins)
	}                                               
	
	countChange(200,List(1, 2, 5, 10, 20, 50, 100, 200))
}