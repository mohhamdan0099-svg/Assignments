function hideit(){
    var hidebox=document.querySelector(".last-box")
    hidebox.remove();
}

function custom(){
    alert();
}

function removed(Element){
    Element.remove();
    
}

function changeDegree(element){

    
    var hotDegree1=document.querySelector("#degreejs");
    var hotDegree2=document.querySelector(".hot-degreetwo");
    var hotDegree3=document.querySelector(".hot-degreethree");
    var hotDegree4=document.querySelector(".hot-degreefour");

    hotDegree1.innerText="87";
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






//     var degreee=document.querySelector('#degreejs');
//     var c=document.querySelector('#degreejs');
//     var c=parseInt(degreee.innerText);
//     var ini=parseInt(degreee.innerText);
//     if(element.value === "f°"){
//     degreee.innerHTML=ini+10;
//     }
//     else(){
    
//     }
// }


// hotDegree1.innerText=(hotDegree1.innerText * 9 / 5) + 32;



