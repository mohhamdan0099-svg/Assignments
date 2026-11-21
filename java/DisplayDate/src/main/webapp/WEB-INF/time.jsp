<%@ page language="java" contentType="text/html; charset=UTF-8" pageEncoding="UTF-8"%>
<%@ taglib prefix="fmt" uri="jakarta.tags.fmt" %>
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Time</title>
    <link rel="stylesheet" href="/css/style.css">
    <script src="/js/timeAlert.js" defer></script>
</head>
<body>
    <p class="time-text">
        <fmt:formatDate value="${currentTime}" pattern="h:mm a" />
    </p>
</body>
</html>