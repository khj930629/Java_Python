package ex0711;

/*
 * [String 클래스의 활용]
 * 다음 주민등록 번호의 중간에 삽입된 - 를 지우고 공백으로 채워서 출력하는 프로그램을 작성해보자.
 * 990925-1012999
 */
public class Ex05 {

	public static void main(String[] args) {
		String s1 = "990925-1012999";
		String s2 = s1.substring(0, 6) + ' ' + s1.substring(7);
		System.out.println(s2);
	}
}
