package ex0630;

public class ForInFor {

	public static void main(String[] args) {
		for (int i = 0; i < 3; i++) {
			System.out.println("시작");
			for (int j = 0; j < 3; j++) {
				System.out.println("i = " + i + "j = " + j);
			}
			System.out.println();
			for (int k = 0; k < 3; k++) {
				System.out.println("i = " + i + "k = " + k);
			}
			System.out.println();
		}
	}
}
