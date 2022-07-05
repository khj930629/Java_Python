package ex0705;

public class Triangle {

	double width, height;

	public Triangle(double wid, double hei) {
		width = wid;
		height = hei;
	}

	public double Area() {
		double area = (width * height) / 2;
		return area;
	}

	public static void main(String[] args) {
		Triangle a = new Triangle(3.5, 2);
		System.out.println("a 삼각형의 넓이 : " + a.Area());

		Triangle b = new Triangle(4, 5);
		System.out.println("b 삼각형의 넓이 : " + b.Area());
	}
}
