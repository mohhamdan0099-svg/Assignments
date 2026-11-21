package com.axsos.omikujiform;

import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;

import jakarta.servlet.http.HttpSession;

@Controller

public class HomeController {
	@GetMapping("/")
	public String render() {
		return "redirect:/omikuji";
	}
	
	@GetMapping("/omikuji")
	public String omikuji() {
		return "Form.jsp";
	}
	
	@PostMapping("/omikuji/form")
	public String form(
			@RequestParam (value ="number") String number ,
			@RequestParam (value ="city") String city,
			@RequestParam (value ="person") String person,
			@RequestParam (value ="thing") String thing,
			@RequestParam (value ="something")String something,
			HttpSession session
			) {
		session.setAttribute("number", number);
		session.setAttribute("city", city);
		session.setAttribute("person", person);
		session.setAttribute("thing", thing);
		session.setAttribute("something", something);
		return "redirect:/omikuji/show";
	}
	
	@GetMapping("/omikuji/show")
	public String show() {
		return "Show.jsp";
	}
}