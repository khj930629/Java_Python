package TEST;

public class Test02 {
	// 문제 05-2 조건 연산자
	public static void main(String[] args) {
		int num1 = 50;
		int num2 = 100;
//		int big;
//		int diff;
		
		if (num1 > num2) {
			System.out.println("큰 수 : " + num1);
			if (num1 < num2)
				System.out.println("큰 수 : " + num2);
		}
		
		if (num1 > num2) {
			System.out.println("절댓값: " + (num1 - num2));
			if (num1 < num2)
				System.out.println("절댓값: " + (num2 - num1));
		}
	}
}
