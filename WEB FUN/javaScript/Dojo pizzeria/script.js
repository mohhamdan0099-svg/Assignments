function pizzaOven(crust,sause,cheese,toppings){
    var pizza={}
    pizza.crust=crust;
    pizza.sause=sause;
    pizza.cheese=cheese;
    pizza.toppings=toppings;
    return pizza;
}


var pizzaone=pizzaOven("deep dish","traditional","mozzarella",["pepperoni","sausage"])
console.log(pizzaone);

var pizzatwo=pizzaOven("hand tossed","marinara",["mozzarella","feta"],["mashrooms","olives","onions"])
console.log(pizzatwo);

var pizzathree=pizzaOven("deep dish","traditional","mozzarella",["mashrooms","olives","onions"])
console.log(pizzathree);