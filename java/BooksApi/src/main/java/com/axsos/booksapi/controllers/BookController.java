package com.axsos.booksapi.controllers;

import java.util.List;

import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestParam;

import com.axsos.booksapi.models.Book;
import com.axsos.booksapi.services.BookServices;

@Controller
public class BookController {
	private final BookServices bookService;

	public BookController(BookServices bookService) {
		this.bookService = bookService;
	}

	@GetMapping("/books")
	public String index(Model model) {
		List<Book> books = bookService.allBooks();
		model.addAttribute("books", books);
		return "index.jsp";
	}

	@GetMapping("/books/new")
	public String newBook() {
		return "new.jsp";
	}

	@PostMapping("/books")
	public String create(
			@RequestParam("title") String title,
			@RequestParam("description") String description,
			@RequestParam("language") String language,
			@RequestParam("pages") Integer pages) {
		Book book = new Book(title, description, language, pages);
		bookService.createBook(book);
		return "redirect:/books";
	}

	@GetMapping("/books/{id}")
	public String show(@PathVariable("id") Long id, Model model) {
		Book book = bookService.findBook(id);
		model.addAttribute("book", book);
		return "show.jsp";
	}
}