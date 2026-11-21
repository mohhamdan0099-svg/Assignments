package com.axsos.displaydate;

import java.util.Date;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;

@Controller
public class DateController {

    @GetMapping("/")
    public String index() {
        return "index";
    }

    @GetMapping("/date")
    public String date(Model model) {
        model.addAttribute("currentDate", new Date());
        return "date";
    }

    @GetMapping("/time")
    public String time(Model model) {
        model.addAttribute("currentTime", new Date());
        return "time";
    }
}