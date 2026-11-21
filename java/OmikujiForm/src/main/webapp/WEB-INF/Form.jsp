<%@ page language="java" contentType="text/html; charset=UTF-8" pageEncoding="UTF-8"%>
<!-- New line below to use the JSP Standard Tag Library -->
<%@ taglib prefix = "c" uri = "http://java.sun.com/jsp/jstl/core"%>

<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Omikuji Form</title>
    <script src="https://cdn.jsdelivr.net/npm/@tailwindcss/browser@4"></script>
</head>

<body class="bg-gray-100 min-h-screen flex items-center justify-center p-6">

    <form action="/omikuji/form" method="post"
        class="bg-white w-full max-w-lg p-8 rounded-2xl shadow-lg space-y-5">

        <h1 class="text-2xl font-bold text-purple-700 text-center mb-6">
            Omikuji Form
        </h1>

        <div>
            <label for="number" class="block text-gray-700 font-medium mb-2">
                Pick any number from 5 to 25
            </label>
            <input type="number" name="number" id="number"
                min="5" max="25" required
                class="w-full border border-gray-300 rounded-lg p-3 focus:outline-none focus:ring-2 focus:ring-purple-500">
        </div>

        <div>
            <label for="city" class="block text-gray-700 font-medium mb-2">
                City Name:
            </label>
            <input type="text" name="city" id="city" required
                class="w-full border border-gray-300 rounded-lg p-3 focus:outline-none focus:ring-2 focus:ring-purple-500">
        </div>

        <div>
            <label for="person" class="block text-gray-700 font-medium mb-2">
                Person Name:
            </label>
            <input type="text" name="person" id="person" required
                class="w-full border border-gray-300 rounded-lg p-3 focus:outline-none focus:ring-2 focus:ring-purple-500">
        </div>

        <div>
            <label for="hoppy" class="block text-gray-700 font-medium mb-2">
                Hobby:
            </label>
            <input type="text" name="hoppy" id="hoppy" required
                class="w-full border border-gray-300 rounded-lg p-3 focus:outline-none focus:ring-2 focus:ring-purple-500">
        </div>

        <div>
            <label for="thing" class="block text-gray-700 font-medium mb-2">
                Thing:
            </label>
            <input type="text" name="thing" id="thing" required
                class="w-full border border-gray-300 rounded-lg p-3 focus:outline-none focus:ring-2 focus:ring-purple-500">
        </div>

        <div>
            <label for="something" class="block text-gray-700 font-medium mb-2">
                Say Something nice to someone:
            </label>
            <textarea rows="4" name="something" id="something" required
                class="w-full border border-gray-300 rounded-lg p-3 focus:outline-none focus:ring-2 focus:ring-purple-500 resize-none"></textarea>
        </div>

        <div class="pt-2">
            <p class="text-sm text-gray-500 mb-3">
                Submit and show a friend!
            </p>
            <input type="submit" value="Submit"
                class="w-full bg-purple-600 hover:bg-purple-700 text-white font-semibold py-3 rounded-lg cursor-pointer transition duration-200">
        </div>

    </form>

</body>
</html>