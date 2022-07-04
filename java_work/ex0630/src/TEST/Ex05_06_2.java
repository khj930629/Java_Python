package TEST;

public class Ex05_06_2 {

	  public static void main(String[] args) {
	       
		  int num = 1; // 1,3,5,7,9
		  int sum = 0;
	    
	        while(true) {
	        	sum += num; // sum = sum + num;
	        	num += 2; // num = num + 2;
	        	System.out.println("홀수 = " + num);
	        	if (sum > 1000)
	        		break;
	        }
	        System.out.println("합 = "+ sum);
	        
	        }
	  }
