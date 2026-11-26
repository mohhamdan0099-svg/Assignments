package com.axsos.booksapi.controllers;

import java.util.List;

import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;

import com.axsos.booksapi.models.Book;
import com.axsos.booksapi.services.BookServices;

@RestController
public class BookApi {
	private final BookServices bookService;

	public BookApi(BookServices bookService) {
		this.bookService = bookService;
	}

	@GetMapping("/api/books")
	public List<Book> index() {
		return bookService.allBooks();
	}

	@PostMapping("/api/books")
	public Book create(
			@RequestParam("title") String title,
			@RequestParam("description") String desc,
			@RequestParam("language") String lang,
			@RequestParam("pages") Integer numOfPages) {
		Book book = new Book(title, desc, lang, numOfPages);
		return bookService.createBook(book);
	}

	@GetMapping("/api/books/{id}")
	public Book show(@PathVariable("id") Long id) {
		return bookService.findBook(id);
	}

	@RequestMapping(value = "/api/books/{id}", method = RequestMethod.PUT)
	public Book update(
			@PathVariable("id") Long id,
			@RequestParam(value = "title") String title,
			@RequestParam(value = "description") String desc,
			@RequestParam(value = "language") String lang,
			@RequestParam(value = "pages") Integer numberOfPages) {
		Book book = bookService.updateBook(id, title, desc, lang, numberOfPages);
		return book;
	}

	@RequestMapping(value = "/api/books/{id}", method = RequestMethod.DELETE)
	public void destroy(@PathVariable("id") Long id) {
		bookService.deleteBook(id);
	}
}
 