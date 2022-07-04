package TEST;

public class Ex06_02_1 {
//
//	public static void area(double r) {
//		System.out.println("circle area : " +(r*r*Math.PI));
//	}
//
//	public static void round(double r) {
//		System.out.println("circle round : "+(r*Math.PI));
//	}
//	
//	public static void main(String[] args) {
//		
//		area(2);
//		round(2);
//		
//	}
//}

	public static double carea(double r) {
		return r * r * 3.14;
	}

	public static double cround(double r) {
		return 2 * 3.14 * r;
	}

	public static void main(String[] args) {
		System.out.println("crea(3) = " + carea(3));
		System.out.println("cround(3) = " + cround(3));
	}
}