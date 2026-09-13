
function increase1(){
    var count1=document.querySelector(".count-1");
    var ini=parseInt(count1.innerText);
    count1.innerText=1+ini;
    
}


function increase2(){
    var count2=document.querySelector(".count-2");
    var ini=parseInt(count2.innerText);
    count2.innerText=ini+1;
}


function increase3(){
    var count3=document.querySelector(".count-3");
    count3.innerText++;
}