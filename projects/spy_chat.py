from spy_details import spy_admin,friend_list,spy,addchat    #IMPORTING main spy,spy friends and used functions
from steganography.steganography import Steganography
from datetime import datetime


print "Greetings"

confirmation = raw_input("press y if you are " + spy_admin.salutation + " " + spy_admin.name)

status_list = ["Being idiot","prince of thorns","random generic statement"]  #various cool status to choose from


def add_friend():   #Function to add frien which is self explanatory


    name= raw_input("Please add your friend's name: ")
    salutation = raw_input("Are they Mr. or Ms.?: ")
    age = int(raw_input("Age?"))
    rating = float(raw_input("Spy rating?"))


    if (len(name)) > 0 and age > 12 and (rating >= 0 and rating <=5):
        spy_friend=spy(name,salutation,age,rating)
        friend_list.append(spy_friend)
        print 'Friend Added!'
    else:
        print 'Sorry! Invalid entry. We can\'t add spy with the details you provided'




def add_status(final_status):   # function to add status
    temp_status = None
    status_index=0

    if final_status != None:
        print 'Your current status message is %s \n' % (final_status)
    else:
        print "you have no current status"
    choice = raw_input("do you want to select from older statuses (y/n)")

    if choice == "y" or choice == "Y":
        item_position = 1
        for message in status_list:
            print '%d. %s' % (item_position, message)
            item_position = item_position + 1
        status_index = int(raw_input("enter index of new status"))
        temp_status = status_list[status_index-1]
        return temp_status
    elif choice == "n" or choice == "N":

        temp_status=raw_input("enter new status:")
        status_list.append(temp_status)
        return temp_status
    else:
        print "invalid choice status not updated"
        temp_status = final_status
        return final_status

def choose_friend(): #Function to choose friend this function returns the index of friend and will be used quite a lot
    index=0
    for name in friend_list:
        print "%d %s" % (index + 1,friend_list[index].name)
        index = index + 1
    friend_choice=int(raw_input("enter index of friend"))
    return friend_choice-1

def send_message(): #function to add text to photo

    friend_choose = choose_friend()

    original_image = raw_input("Enter the name of image in directory:")
    original_image="F:/study/pics/files to modify/" + original_image     #adding directory to file name
    output_path = raw_input("Enter the name of new image thus formed:")
    output_path = "F:/study/pics/files that are to be sent/" + output_path #adding directory to file name
    text = raw_input("What is the message: ")
    Steganography.encode(original_image, output_path, text)

    new_chat=addchat(text,True)

    friend_list[friend_choose].chats.append(new_chat)     #adding message to list so that we can read them later

    print "Your secret message image is ready!"

def read_latest_message(): #message decoder from received file
    print"which friend sent this"
    friend_choose=choose_friend()
    output=raw_input("enter the image name in directory")
    output="F:/study/pics/files that are received/" + output #adding directory to file name
    text = Steganography.decode(output)
    print "message is: %s" % (text)
    new_chat = addchat(text, False)
    friend_list[friend_choose].chats.append(new_chat)

def older_chats():   #function to read older chats
    print "which chat do you want to read from"
    friend_choose=choose_friend()
    for chats in friend_list[friend_choose].chats:
        if chats.sent_by_me:
            print '[%s] %s: %s' % (chats.time.strftime("%d %B %Y"), 'You said:', chats.message)
        else:
            print '[%s] %s said: %s' % (chats.time.strftime("%d %B %Y"), friend_list[friend_choose].name, chats.message)


def start_chat(spy_name, spy_age, spy_rating):   #main controlling function on loop which controls the rest of the functions
    final_status=None


    print " Welcome " + "spy_salutation " + spy_name + " age: " + str(spy_age) + " and rating of: " + str(spy_rating)

    show_menu = True

    while show_menu == True:
        menu_choices = "What do you want to do? \n 1. Add a status update \n 2. Add a friend \n 3. Send a secret message \n 4. Read a secret message \n 5. Read Chats from a user \n 6. Close Application \n"
        menu_choice = raw_input(menu_choices)

        if len(menu_choice) > 0:
            menu_choice = int(menu_choice)

            if menu_choice == 1:
                print 'You chose to update the status'
                final_status = add_status(final_status)
                print "your current status is %s" % (final_status)
            elif menu_choice == 2:
                print "you chose to add a friend"
                add_friend()
            elif menu_choice == 3:
                send_message()
            elif menu_choice == 4:
                print"Plz select"
                read_latest_message()
            elif menu_choice == 5:
                older_chats()
            elif menu_choice == 6:
                print"Goodbye and Good luck"
                show_menu=False
            else:
                print "invalid choice : exiting program"
                show_menu = False


if confirmation == "y" or confirmation == "Y":   #if you want to continue as spy_admin
    start_chat(spy_admin.name, spy_admin.age, spy_admin.rating)
else:                                             # crete your own identity
    spy_name = ''
    spy_salutation = ''
    spy_age = 0
    spy_rating = 0.0

    spy_name = raw_input("Tell us your spy name: ")

    if len(spy_name) > 0:
        spy_salutation = raw_input("Enter salutation ")

        spy_age = raw_input("Enter age")
        spy_age = int(spy_age)
        if(spy_age < 80 and spy_age >=14):

            spy_rating = float(raw_input("enter rating"))
            if(spy_rating<=5 and spy_rating>=0):

                
                if spy_rating > 4.5:
                    print"You are excellent"
                elif spy_rating > 3:
                    print"you are good"
                elif spy_rating > 1.5:
                    print"you are okay"
                elif spy_rating > 0:
                    print"your resources would be used best elsewhere"
                spy.name=spy_name
                spy.age=spy_age
                spy.salutation=spy_salutation
                spy.rating=spy_rating
                start_chat(spy_admin.name, spy_admin.age, spy_admin.rating)
        else:
            print "your age is not correct to be a spy"
    else:
        print 'Please enter valid spy name'
