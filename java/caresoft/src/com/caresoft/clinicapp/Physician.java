package com.caresoft.clinicapp;

import java.util.ArrayList;

public class Physician extends User implements HIPAACompliantUser {
    private ArrayList<String> patientNotes;

    public Physician(Integer id) {
        this.id = id;
        this.patientNotes = new ArrayList<String>();
    }

    @Override
    public boolean assignPin(int pin) {
        if (pin >= 1000 && pin <= 9999) {
            this.pin = pin;
            return true;
        }
        return false;
    }

    @Override
    public boolean accessAuthorized(Integer confirmedAuthID) {
        if (confirmedAuthID == null || this.id == null) {
            return false;
        }
        return this.id.equals(confirmedAuthID);
    }

    public void newPatientNotes(String notes, String patientName, String date) {
        String report = String.format("Datetime Submitted: %s \n", date);
        report += String.format("Reported By ID: %s\n", this.id);
        report += String.format("Patient Name: %s\n", patientName);
        report += String.format("Notes: %s \n", notes);
        this.patientNotes.add(report);
    }

    public ArrayList<String> getPatientNotes() {
        return patientNotes;
    }

    public void setPatientNotes(ArrayList<String> patientNotes) {
        this.patientNotes = patientNotes;
    }
}