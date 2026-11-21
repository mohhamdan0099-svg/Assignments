<%@ page language="java" contentType="text/html; charset=UTF-8" pageEncoding="UTF-8"%>
<%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core" %>
<%@ taglib prefix="fmt" uri="http://java.sun.com/jsp/jstl/fmt" %>
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Fruit Store</title>
    <link rel="stylesheet" type="text/css" href="/css/style.css">
</head>
<body>
    <div class="container">
        <h1>Fruit Store</h1>
        <table>
            <thead>
                <tr>
                    <th>Name</th>
                    <th>Price</th>
                </tr>
            </thead>
            <tbody>
                <c:forEach var="fruit" items="${fruits}">
                    <tr>
                        <td>
                            <c:choose>
                                <c:when test="${fruit.name.startsWith('G')}">
                                    <span class="orange-text"><c:out value="${fruit.name}"/></span>
                                </c:when>
                                <c:otherwise>
                                    <c:out value="${fruit.name}"/>
                                </c:otherwise>
                            </c:choose>
                        </td>
                        <td>
                            $<fmt:formatNumber value="${fruit.price}" pattern="0.00"/>
                        </td>
                    </tr>
                </c:forEach>
            </tbody>
        </table>
    </div>
</body>
</html>