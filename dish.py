indian = ["samosa","daal","Chana masala","naan","parota","rooti","Butter chicken"]
chinese = ["egg roll","pot sticker","Dim Sums","Szechwan Chilli Chicken", "fried rice"]
italian = ["pizza","pasta","risotto","Panzenella","Margherita Pizza"]

dish = input("Enter the dish name :")

if dish in indian:
    print("Dish is indian")
elif dish in chinese:
    print("Dish is chinese")
elif dish in italian:
    print("Dish is italian")
else:
    print("not available")