package ex0627;

public class Ex03 {

	public static void main(String[] args) {
		
		int num1 = 10;
		int num2 = 20;

		if(num1 < num2) {
			System.out.println("값이 참이면 실행된다.");
			System.out.println("두줄 이상부터 괄호를 사용");
		}
		
		if(num1 < num2)
			System.out.println("한줄이면 괄호 생략 가능");
		
	}
}
