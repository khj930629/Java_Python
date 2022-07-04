package TEST;

public class Ex06_03_2 {
		
	public static void two(int n) {
		if ( n == 0) {
			return;
		}
		else {
			two(n/2);
			System.out.println(n%2+" ");
		}
	}
	
	public static void main(String[] args) {
		two(10);
	}
}
