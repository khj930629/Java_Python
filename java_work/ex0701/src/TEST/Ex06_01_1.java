package TEST;

public class Ex06_01_1 {

	public static void main(String[] args) {

		doA(4, 2);
		doA(9, 4);
		doA(21, 5);

	}
	
	public static void doA(int n1, int n2) {
		
		System.out.println("두수의 덧셈 = " + (n1 + n2));
		System.out.println("두수의 뺄셈 = " + (n1 - n2));
		System.out.println("두수의 곱셈 = " + (n1 * n2));
		System.out.println("두수의 나눗셈 몫 = " + (n1 / n2));
		System.out.println("두수의 나눗셈 몫 = " + (n1 % n2));
	}
}