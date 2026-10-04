class store:
    def __init__(self,name):
        self.name=name
        self.list=[]

    def add_product(self,new_product):
        self.list.append=new_product    
    def sell_product(self,id):
        self.list.pop=id    
    def inflation(self,percent_increase):
        pass
    def set_clearnece(self,category,percent_discount):
        pass   




class product:
    def __init__(self,name,price,category):
        self.name=name
        self.price=price
        self.category=category

    def update_price (self,percent_change,is_increased):
        if is_increased is True:
            self.price+=(self.price*percent_change)
        if is_increased is False:
            self.price-=(self.price*percent_change)    

    def print_info(self):
        print(f"name:{self.name} ,price: {self.price} , category:{self.category}")

