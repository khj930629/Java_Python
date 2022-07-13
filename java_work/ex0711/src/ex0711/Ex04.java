package ex0711;

public class Ex04 {
	Ex04(){
		BB b1 = new BB();
		
		System.out.println(b1.toString());
		
//		문자열 비교는 equals로 해야한다.
		System.out.println("abc".equals(new String("abc")));
		System.out.println("abc" == new String("abc"));
	}
	
	public static void main(String[] args) {
		new Ex04();
	}
}
