package com.axsos.booksapi.services;

import java.util.List;
import java.util.Optional;

import org.springframework.stereotype.Service;

import com.axsos.booksapi.models.Book;
import com.axsos.booksapi.repositories.BookRepository;

@Service
public class BookServices {
	private final BookRepository bookRepository;

	public BookServices(BookRepository bookRepository) {
		this.bookRepository = bookRepository;
	}

	public List<Book> allBooks() {
		return bookRepository.findAll();
	}

	public Book createBook(Book b) {
		return bookRepository.save(b);
	}

	public Book findBook(Long id) {
		Optional<Book> optionalBook = bookRepository.findById(id);
		if (optionalBook.isPresent()) {
			return optionalBook.get();
		} else {
			return null;
		}
	}

	public Book updateBook(Long id, String title, String desc, String lang, Integer numOfPages) {
		Book book = findBook(id);
		if (book != null) {
			book.setTitle(title);
			book.setDescription(desc);
			book.setLanguage(lang);
			book.setNumberOfPages(numOfPages);
			return bookRepository.save(book);
		}
		return null;
	}

	public void deleteBook(Long id) {
		bookRepository.deleteById(id);
	}
}