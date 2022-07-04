package ex0630;

public class WhileBasic {

	public static void main(String[] args) {

		int num = 0;
		while (num < 5) {
			System.out.println("I like Java " + num);
			num++;
		}
		
//		for (선언; 조건; 연산) {}
		for (num = 1; num < 5; num++) {
			System.out.println("I like Java " + num);
		}
	}
}
