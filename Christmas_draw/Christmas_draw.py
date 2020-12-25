import smtplib
from random import randint
"""
For a given group of people, the program draws who is giving a Christmas gift to whom 
and then sends an e-mail with the appropriate information to each person.

The program ensures that a given person does not draw himself.
Each person in the email can only see the person to whom they are giving the gift.
"""

dict_of_emails = {
    'person1': 'person1@gmail.com',
    'person2': 'person2@gmail.com',
    'person3': 'person3@gmail.com',
    'person4': 'person4@gmail.com',
    'person5': 'person5@gmail.com',
    # and so on
}


def draw_people(dict_of_people_and_its_emails):
    """
    functions draw people and provide person can't draw himself
    """
    list_of_people = [email for email in dict_of_emails]
    list_of_people_copy = [email for email in dict_of_emails]
    people_after_draw = {}
    for people in list_of_people:
        random_number = randint(0, len(list_of_people_copy)-1)
        people_after_draw[people] = list_of_people_copy[random_number]
        list_of_people_copy.remove(list_of_people_copy[random_number])
    print(people_after_draw)
    for every_people in people_after_draw:
        if every_people == people_after_draw[every_people]:
            return draw_people(dict_of_people_and_its_emails)
    return people_after_draw


who_to_who = draw_people(dict_of_emails)
print(who_to_who)

smtpObj = smtplib.SMTP('smtp.gmail.com', 587)
smtpObj.ehlo()
smtpObj.starttls()
email = input('put your email: ')
password = input('put your email password: ')
smtpObj.login(email, password)

for email in who_to_who:
    message = """
    Your selected person is: """ + who_to_who[email] + """
    """
    # print("you send mail to: " + dict_of_emails[email] + " Your selected person is: " + who_to_who[email])
    smtpObj.sendmail(email, dict_of_emails[email], message)

smtpObj.quit()
