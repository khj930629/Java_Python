package ex0701;

public class Ex01 {

	public static void doA(int a) {
		System.out.println("doA 메서드 시작");
		System.out.println("a = " +a);		
		System.out.println("doA 메서드 끝");
	}
	
	public static void main(String[] args) {
	System.out.println("프로그램 시작");	
		doA(24);
		doA(30);
		doA(25);
		doA(32);
		doA(18);
		doA(20);
		doA(21);
		doA(33);
		System.out.println("프로그램 끝");
		
	}
}
