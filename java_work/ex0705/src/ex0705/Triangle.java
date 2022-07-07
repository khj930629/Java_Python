package ex0705;

public class Triangle {

	double width, height;

	public Triangle(double wid, double hei) {
		width = wid;
		height = hei;
	}

	public double Area() {
		double area = (width * height) * 0.5d;
		System.out.println("삼각형의 넓이 : " + area);
		return area;
	}

	public static void main(String[] args) {
		Triangle t1 = new Triangle(3.5, 2);
		t1.Area();
//		System.out.println("t1 삼각형의 넓이 : " + t1.Area());

		Triangle t2 = new Triangle(4, 5);
		t2.Area();
//		System.out.println("b 삼각형의 넓이 : " + t2.Area());
	}
}
