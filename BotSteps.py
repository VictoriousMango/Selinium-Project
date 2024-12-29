from Bot import bot
import config

def IISTFoodBooking():
    url = "https://events.iist.ac.in/foodbook/index.php?option=login"
    SBot = bot()
    SBot._OpenWebsite(url)
    SBot._InputElement_ID("Institute_ID", config.IIST_FoodBookingUsername)
    SBot._InputElement_ID("pin", config.IIST_FoodBookingPassword)

    ## Booking Breakfast
    SBot._ClickBy_ID("Canteen_id")
    SBot._SelectBy_Value(htmlTag="option", value="1")
    SBot._SelectBy_Value(htmlTag="input", name="Servicetype_id", value="59")
    SBot._ClickBy_ID("356")  # Breakfast Select All
    SBot._SelectBy_Value(htmlTag="input", name="Submit", value="Save Booking") # Saving Booking
    SBot._OpenWebsite("https://events.iist.ac.in/foodbook/index.php?option=booking&task=book")

    ## Booking Lunch
    SBot._ClickBy_ID("Canteen_id")
    SBot._SelectBy_Value(htmlTag="option", value="1")
    SBot._SelectBy_Value(htmlTag="input", name="Servicetype_id", value="60")
    SBot._ClickBy_ID("361")  # Lunch Select All
    SBot._SelectBy_Value(htmlTag="input", name="Submit", value="Save Booking") # Saving Booking
    SBot._OpenWebsite("https://events.iist.ac.in/foodbook/index.php?option=booking&task=book")

    ##Booking Dinner
    SBot._ClickBy_ID("Canteen_id")
    SBot._SelectBy_Value(htmlTag="option", value="1")
    SBot._SelectBy_Value(htmlTag="input", name="Servicetype_id", value="61")
    SBot._ClickBy_ID("365")  # Dinner Select All
    SBot._SelectBy_Value(htmlTag="input", name="Submit", value="Save Booking") # Saving Booking
    SBot._OpenWebsite("https://events.iist.ac.in/foodbook/index.php?option=booking&task=book")

    ## Booking Snacks
    SBot._ClickBy_ID("Canteen_id")
    SBot._SelectBy_Value(htmlTag="option", value="1")
    SBot._SelectBy_Value(htmlTag="input", name="Servicetype_id", value="62")
    SBot._ClickBy_ID("372")  # Snacks Select All 
    SBot._ClickBy_ID("428")  # Coffee Select All 
    SBot._SelectBy_Value(htmlTag="input", name="Submit", value="Save Booking") # Saving Booking
    SBot._OpenWebsite("https://events.iist.ac.in/foodbook/index.php?option=booking&task=book")

    print("Program Executed SUccessfully!!!")