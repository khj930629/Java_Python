package TEST;

public class Ex06_03_1 {

//	public static int PowerN(int n) {
//
//		if (n == 0) {
//			return 1;
//		}
//		return 2 * PowerN(n - 1);
//	}
//
//	public static void main(String[] args) {
//
//		System.out.println("2의 3승은 : " + PowerN(3));
//		System.out.println("2의 5승은 : " + PowerN(5));
//		System.out.println("2의 9승은 : " + PowerN(9));
//	}
//}

	public static void main(String[] args) {
		int result = doA(3);
		System.out.println("result = " + result);
		result = doA(5);
		System.out.println("result = " + result);
	}
	/*
	 * doA(3)
	 * 2 * doA(2)
	 * 2 * 2 * doA(1)
	 * 2 * 2 * 2 * doA(0)
	 * return 2 * 2 * 2 * 1
	 * 8
	 */
	public static int doA(int n) {
		if ( n == 0)
			return 1;
		else
			return 2*doA(n-1);
	}
}