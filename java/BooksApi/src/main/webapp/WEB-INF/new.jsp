<%@ page language="java" contentType="text/html; charset=UTF-8" pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>New Book</title>
</head>
<body>
    <h1>New Book</h1>
    <form action="/books" method="post">
        <div>
            <label>Title</label><br>
            <input type="text" name="title">
        </div>
        <div>
            <label>Description</label><br>
            <textarea name="description"></textarea>
        </div>
        <div>
            <label>Language</label><br>
            <input type="text" name="language">
        </div>
        <div>
            <label>Pages</label><br>
            <input type="number" name="pages">
        </div>
        <br>
        <input type="submit" value="Submit">
    </form>
</body>
</html>