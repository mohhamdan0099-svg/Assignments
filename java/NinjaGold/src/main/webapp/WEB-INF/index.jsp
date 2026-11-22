<%@ page language="java" contentType="text/html; charset=UTF-8" pageEncoding="UTF-8"%>
<%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core" %>
<%@ taglib prefix="fn" uri="http://java.sun.com/jsp/jstl/functions" %>
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Ninja Gold Game</title>
    <link rel="stylesheet" type="text/css" href="/css/style.css">
</head>
<body>
    <div class="container">
        <div class="header-bar">
            <div class="gold-display">
                <label>Your Gold:</label>
                <span class="gold-box"><c:out value="${gold}"/></span>
            </div>
           
        </div>

        <div class="places-grid">
            <div class="place-card">
                <h2>Farm</h2>
                <p>(earns 10-20 gold)</p>
                <form action="/process" method="post">
                    <input type="hidden" name="building" value="farm">
                    <button type="submit">Find Gold!</button>
                </form>
            </div>

            <div class="place-card">
                <h2>Cave</h2>
                <p>(earns 5-10 gold)</p>
                <form action="/process" method="post">
                    <input type="hidden" name="building" value="cave">
                    <button type="submit">Find Gold!</button>
                </form>
            </div>

            <div class="place-card">
                <h2>House</h2>
                <p>(earns 2-5 gold)</p>
                <form action="/process" method="post">
                    <input type="hidden" name="building" value="house">
                    <button type="submit">Find Gold!</button>
                </form>
            </div>

            <div class="place-card">
                <h2>Quest</h2>
                <p>(earns/takes 0-50 gold)</p>
                <form action="/process" method="post">
                    <input type="hidden" name="building" value="quest">
                    <button type="submit">Find Gold!</button>
                </form>
            </div>

           
        </div>

        <h3>Activities:</h3>
        <div class="activities-box">
            <c:forEach var="activity" items="${activities}">
                <p class="${fn:contains(activity, 'lost') ? 'lost' : 'earned'}">
                    <c:out value="${activity}"/>
                </p>
            </c:forEach>
        </div>
    </div>
</body>
</html>