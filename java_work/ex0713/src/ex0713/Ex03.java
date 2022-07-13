package ex0713;

public class Ex03 {

//	1차원 배열 : 벡터
//	2차원 배열 : 행렬
//	3차원 배열 : 텐서
	public static void main(String[] args) {
		int a[][] = new int[3][4];

		int num = 1;

		for (int i = 0; i < a.length; i++) {
			for (int j = 0; j < a[i].length; j++) {
				a[i][j] = num;
				num++;
			}
		}

		for (int i = 0; i < a.length; i++) {
			for (int j = 0; j < a[i].length; j++) {
				System.out.print(a[i][j] + "\t");
			}
			System.out.println();
		}
	}
}
