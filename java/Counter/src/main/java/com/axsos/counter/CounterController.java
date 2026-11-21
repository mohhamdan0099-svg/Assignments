package com.axsos.counter; // Match your base package

import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.RequestMapping;
import jakarta.servlet.http.HttpSession;

@Controller
public class CounterController {

   
    @RequestMapping("/")
    public String index(HttpSession session) {
        if (session.getAttribute("count") == null) {
            session.setAttribute("count", 1);
        } else {
            Integer currentCount = (Integer) session.getAttribute("count");
            session.setAttribute("count", currentCount + 1);
        }
        return "server.jsp";
    }

    @RequestMapping("/counter")
    public String counter(HttpSession session) {
        if (session.getAttribute("count") == null) {
            session.setAttribute("count", 0);
        }
        return "counter.jsp";
    }

}