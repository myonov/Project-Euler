import java.math.BigInteger;

public class pr216 {
	public static void main(String[] args) {
		long l = 50000000;
		
		long a = 0;
		
		for (long i = 2; i <= l; ++i) {
			BigInteger bn = new BigInteger("" + (2 * i * i - 1));

			if ( bn.isProbablePrime(20) )
				a++;
		}
		
		System.out.println(a);
	}
}
