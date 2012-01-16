import java.math.BigInteger;
import java.util.ArrayList;
import java.util.List;

/**
 * Problem 3
 * 02 November 2001
 * 
 * The prime factors of 13195 are 5, 7, 13 and 29.
 * 
 * What is the largest prime factor of the number 600851475143 ?
 */
public class Problem3 {

	public static void main(String[] args) {
		BigInteger n = new BigInteger("600851475143");
		BigInteger max = n.divide(new BigInteger("2")).add(BigInteger.ONE);
		List<BigInteger> primes = new ArrayList<BigInteger>();

		for (BigInteger i = BigInteger.ONE; i.compareTo(max) == -1; i = i.add(BigInteger.ONE)) {
			if (n.remainder(i).compareTo(BigInteger.ZERO) == 0) {
				System.out.println("Factor: " + i);
				if (isPrime(i)) {
					primes.add(i);
				}
			}
		}

		System.out.println("Largest prime factor of the number 600851475143 = " + primes.get(primes.size() - 1));
	}

	private static boolean isPrime(BigInteger candidate) {
		BigInteger max = candidate.divide(new BigInteger("2")).add(BigInteger.ONE);
		for (BigInteger i = new BigInteger("2"); i.compareTo(max) == -1; i = i.add(BigInteger.ONE)) {
			if (candidate.remainder(i).compareTo(BigInteger.ZERO) == 0) {
				return false;
			}
		}
		return true;
	}
}
