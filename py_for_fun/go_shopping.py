#Create a Store that has an inventory of food items
#You could then have a Shopper class that can purchase items from the Store

#Def a clss Store that holds food categories and categories hold items 
class Store:
    def __init__(self):
        self.veggies ={"tomato":16, "lettuce":9,"potato":15}
        self.fruits ={"apple":13,"banana":7,"mango":30}
        self.categories = [self.veggies, self.fruits]
        print("The original stock was :{stock}".format(stock=self.categories))

    # func sold() deducts user's purchase from the stock  
    def sold(self,food,amount):
        for categ in self.categories:
            for item in categ:
                if item == food:
                    categ[item]-= amount
    
    # func to print out the result
    def __repr__(self):
        rslt = "The stock is now {stock}".format(stock = self.categories)
        return rslt

# class Shopper allows user to buy by adding items to his cart
class Shoppper:
    def __init__(self):
        self.cart = {}

#  buying() lets user precise total n of items, the item and the amount of that item
# everything will be appended to cart and retturned
    def buying(self):
        total_items = int(input("How many items do you want to buy? "))
        while total_items > 0:
            b_item = input("What food is it? ")
            b_amount = int(input("How many of it do you want? "))
            self.cart[b_item] = b_amount
            total_items -= 1
            if total_items <= 0:
                break
        return self.cart

#run the classes and func defined above
moussa = Shoppper()
mylist = moussa.buying()
shop = Store()
print("Customer order is ",mylist)

# loop to deduce one set of {item:amount} at times. (from user's cart)
for x in mylist:
    shop.sold(x,mylist[x])
print(shop)