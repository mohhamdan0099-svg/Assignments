function changeName(){
    var namechange=document.querySelector(".jane");
    namechange.innerText="Mohammad";
}

function requestone(){
    var requested=document.querySelector("#one");
    var changenum=document.querySelector(".badge");
    requested.remove();
    changenum.innerText--;
    
}

function requesttwo(){
    var requested=document.querySelector("#two");
    var changenum=document.querySelector(".badge");
    requested.remove();
    changenum.innerText--;
    
}

function accept(){
    var changenum2=document.querySelector("#accept");
    changenum2.innerText++;
}


