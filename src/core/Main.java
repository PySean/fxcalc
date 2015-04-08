package core;

import core.controller.Controller;

public class Main {

	public static void main(String[] args) {
		Model model = new Model();
		Controller controller = new Controller(model);
		View view = new View(model, controller);
		System.out.println("Hello world!");
	}

}
