package TEST;

public class Ex05_04_3 {

	public static void main(String[] args) {
		int num = 1;
		int sum = 0;

		while (num < 1001) {
			if ((num % 2 == 0) && (num % 7 == 0)) {
				System.out.println("2와 7의 공배수 : " + num);
				sum += num;
			}
			num+=1;
		}
		System.out.println("2와 7의 공배수들의 합 : " + sum++);
	}
}
