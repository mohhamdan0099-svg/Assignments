
<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core"%>

<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Your Omikuji Fortune</title>
    <script src="https://cdn.jsdelivr.net/npm/@tailwindcss/browser@4"></script>
 
</head>

<body class="bg-purple-50 min-h-screen flex items-center justify-center p-6">

    <div class="bg-white max-w-xl w-full p-10 rounded-2xl shadow-xl text-center">

        <div class="text-5xl mb-5">🔮</div>

        <h1 class="text-3xl font-bold text-purple-700 mb-6">
            Here is your Omikuji!
        </h1>

        <p class="text-lg text-gray-700 leading-9 mb-8">
            In
            <span class="font-bold text-purple-600">
                <c:out value="${number}"/>
            </span>
            years, you will live in
            <span class="font-bold text-purple-600">
                <c:out value="${city}"/>
            </span>
            with
            <span class="font-bold text-purple-600">
                <c:out value="${person}"/>
            </span>
            as your roommate,
            <span class="font-bold text-purple-600">
                <c:out value="${hoppy}"/>
            </span>
            for a living. The next time you see
            <span class="font-bold text-purple-600">
                <c:out value="${thing}"/>
            </span>,
            you will have good luck. Also,
            <span class="font-bold text-purple-600">
                <c:out value="${something}"/>
            </span>
        </p>

        <a href="/omikuji"
            class="inline-block bg-purple-600 hover:bg-purple-700 text-white font-semibold px-8 py-3 rounded-lg transition duration-200 shadow-md">
            Go Back
        </a>

    </div>

</body>
</html>