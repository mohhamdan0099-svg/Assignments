function hideit(){
    var hidebox=document.querySelector(".last-box")
    hidebox.remove();
}

function custom(){
    alert();
}

function changeDegree(){
    var hotDegree1=document.querySelector(".hot-degreeone");
    var hotDegree2=document.querySelector(".hot-degreetwo");
    var hotDegree3=document.querySelector(".hot-degreethree");
    var hotDegree4=document.querySelector(".hot-degreefour");

    hotDegree1.innerText="75°";
    hotDegree2.innerText="80°";
    hotDegree3.innerText="69°";
    hotDegree4.innerText="78°";

    var coldDegree1=document.querySelector(".cold-degreeone");
    var coldDegree2=document.querySelector(".cold-degreetwo");
    var coldDegree3=document.querySelector(".cold-degreethree");
    var coldDegree4=document.querySelector(".cold-degreefour");

    coldDegree1.innerText="65°";
    coldDegree2.innerText="66°";
    coldDegree3.innerText="61°";
    coldDegree4.innerText="70°";

}
