package TEST;

import java.util.Scanner;

public class Ex06_01_2 {
	
/*
	public static void sub(int a, int b) {
		
		if (a > b) {
			System.out.println(a-b);
		} 
		else {
			System.out.println(b-a);
		}
		
	}
	
	public static void main(String[] args) {
	
		sub(4,2);
		sub(2,4);
		sub(-8,-5);
		
	}
}
*/
	public static void ABS(int fi, int se) {

		if(fi >se) {
			System.out.println("절대값은 = "+(fi-se));
		} else {
			System.out.println("절대값은 = "+(se-fi));
		}
	}
	
	public static void main(String[] args) {
		Scanner scan = new Scanner(System.in);
		
		System.out.println("첫번째 수 입력");
		int fi = scan.nextInt();
		System.out.println("fi = "+fi);
		
		System.out.println("두번째 수 입력");
		int se = scan.nextInt();
		System.out.println("se = "+se);
		
		ABS(fi, se);
	}
}