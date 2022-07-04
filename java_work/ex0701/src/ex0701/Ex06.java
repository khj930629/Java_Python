package ex0701;

public class Ex06 {
	
	/*
	 * fatorial(3) 
	 * 3*fatorial(2)
	 * 3*2*fatorial(1)
	 * 3*2*1
	 * 
	 * fatorial(6)
	 * 6*fatorail(5)
	 * 6*5*fatorial(4)
	 * 6*5*4*fatorial(3)
	 * 6*5*4*3*fatorial(2)
	 * 6*5*4*3*2*fatorial(1)
	 * 6*5*4*3*2*1
	 */

	public static int factorial(int n) {

		if (n == 1) {
			return 1;
		} else {
			return n * factorial(n - 1);
		}
	}

	public static void main(String[] args) {
		System.out.println(factorial(3));
		System.out.println(factorial(6));
	}
}
