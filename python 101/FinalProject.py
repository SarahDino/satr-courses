#قم ببناء برنامج يُمثل دليل الهاتف، بحيث يقوم باستقبال رقم الهاتف، ويعود لنا باسم صاحب الرقم
phone_dict = {
    '1111': 's',
    '2222': 'a'
}


# ---------------------------------------


#Start an infinite loop to allow users to continue operations until they choose to exit.
while True:
#Ask the user what action they want to perform.
    action = input(" Enter 'search', 'add', or 'exit' : ")


# ---------------------------------------


    # Check if user wants to exit.
    if action == 'exit':
        break

#في حال تم إرسال رقم موجود في الدليل سيتم طباعة اسم صاحب الرقم المُدخل، وفي حال تم إدخال رقم غير موجود بدليل الهاتف، تطبع الرسالة:
#Check if user wants to search.
    elif action == 'search':
#Get the query input from user (it can be either name or phone number) and convert to lowercase.
        query = input("Enter name or phone number: ")

#Loop through items in the phone dictionary to find a match.
        for phone , name in phone_dict.items():

#If the query matches a phone or name in the dictionary.
#Print the associated name if the query is a phone, or the phone if the query is a name.
          if query == phone or query == name:
           print(name if query == phone else phone)
           break  # If a match is found, exit the loop
        else:  # This block will execute only if the for loop didn't break (i.e., no match was found)
         print("Sorry, the " + query + " is not found.")

#This block will execute only if the for loop didn't break (no match was found)
        #else:
             #print(" Sorry, the "+query+" is not found ")
#go back to actions menu


# ---------------------------------------


#اجعل البرنامج يقوم بالسماح للمستخدم بإضافة مستخدم جديد مع رقمه للدليل.
    elif action == 'add':

#Get the name input from the user and convert to lowercase.
        name = input("Name: ")

#Get the phone input from the user.
        phone = input("Phone (4 digits): ")

#Check if phone input is valid 4 digits and only numbers.
        if len(phone) == 4 and phone.isdigit():

#Add the new entry to the phone dictionary.
            phone_dict[phone] = name
        else:
#If phone input is invalid, print an error message.
            print("invalid entry")

#If the user enters an unrecognized action, print a message.
    else:
        print("Unknown action.")