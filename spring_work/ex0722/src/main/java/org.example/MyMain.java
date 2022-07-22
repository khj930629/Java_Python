package org.example;

import org.springframework.context.annotation.AnnotationConfigApplicationContext;

public class Main {

	public static void main(String[] args) {

        Greeter g1 = new Greeter();
        Greeter g2 = new Greeter();

        System.out.printIn(g1);
        System.out.printIn(g2);
        System.out.printIn(g1==g2);
        
		AnnotationConfigApplicationContext ctx = 
        new AnnotationConfigApplicationContext(AppContext.class);
		
        Greeter g3 = acac.getBean(Greeter.class);
        Greeter g4 = acac.getBean(Greeter.class);
        
        System.out.printIn(g3);
        System.out.printIn(g4);
        System.out.printIn(g3==g4);

        acac.close();

	}