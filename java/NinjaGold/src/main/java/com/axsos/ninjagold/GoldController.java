package com.axsos.ninjagold;

import java.text.SimpleDateFormat;
import java.util.ArrayList;
import java.util.Date;
import java.util.Random;

import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestParam;

import jakarta.servlet.http.HttpSession;

@Controller
public class GoldController {

   
    
    @GetMapping("/")
    public String index(HttpSession session) {
        if (session.getAttribute("gold") == null) {
            session.setAttribute("gold", 0);
        }
        if (session.getAttribute("activities") == null) {
            session.setAttribute("activities", new ArrayList<String>());
        }

        int gold = (Integer) session.getAttribute("gold");

        return "index.jsp";
    }

    
    @PostMapping("/process")
    public String processGold(@RequestParam("building") String building, HttpSession session) {
        
        int gold = (Integer) session.getAttribute("gold");
        ArrayList<String> activities = (ArrayList<String>) session.getAttribute("activities");

        Random rand = new Random();
        int amount = 0;
        String timestamp = new SimpleDateFormat("MMMM d yyyy h:mm a").format(new Date());
        String logMessage = "";

        switch (building) {
            case "farm":
                // Earns 10 - 20 gold
                amount = rand.nextInt(11) + 10;
                gold += amount;
                logMessage = "You entered a farm and earned " + amount + " gold. (" + timestamp + ")";
                break;

            case "cave":
                // Earns 5 - 10 gold
                amount = rand.nextInt(6) + 5;
                gold += amount;
                logMessage = "You entered a cave and earned " + amount + " gold. (" + timestamp + ")";
                break;

            case "house":
                // Earns 2 - 5 gold
                amount = rand.nextInt(4) + 2;
                gold += amount;
                logMessage = "You entered a house and earned " + amount + " gold. (" + timestamp + ")";
                break;

            case "quest":
                // Earns or loses 0 - 50 gold
                amount = rand.nextInt(51);
                boolean earned = rand.nextBoolean();
                if (earned) {
                    gold += amount;
                    logMessage = "You completed a quest and earned " + amount + " gold. (" + timestamp + ")";
                } else {
                    gold -= amount;
                    logMessage = "You failed a quest and lost " + amount + " gold. Ouch. (" + timestamp + ")";
                }
                break;

            
        }

        
        activities.add(0, logMessage);

        session.setAttribute("gold", gold);
        session.setAttribute("activities", activities);

        return "redirect:/";
    }
}