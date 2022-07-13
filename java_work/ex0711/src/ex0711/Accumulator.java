package ex0711;

public class Accumulator {

	public static int MAX = 345;
	
	private static int sum = 0;

	public static void add(int i) {
		sum = sum + i;
	}

	public static void showResult() {
		System.out.println("sum = " + sum);
	}

}
