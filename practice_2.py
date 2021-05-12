def store():
    instruction = input(" Welcome to ABC ltd. Which of the product do you want to purchase, leather or rubber? (leather/rubber):")

    if instruction != "leather":
        return print("Out of stock")
    else:
        print("Continue processing to purchase")

        store_quality = input("what quality of leather do you want? designer or madeinkogi?")
        if store_quality != "designer":
            return print("Quality are sold here!")
        else:
            print("Done!,next..")

            store_size = input("Variety of sizes are available(40-45), pick your size:")
            if store_size != str(40-45):
                return print("size not available")
            else:
                print("Click the pay button")




store()

