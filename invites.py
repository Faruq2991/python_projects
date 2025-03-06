
def main():
    guest = ["Buhari", "Ishaq", "Ceaser", "DY", "Msster", "Twister", "Goma"]
    guest.append("Musty")
    for _ in range(len(guest)):
        print(invititation(_, "Umar Faruq"))

def invititation(reciever, sender):
    return f"""

    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    Dear {reciever},

    Kindly accept this as an official invitation to my wedding,
    which will In Sha Allah takes place as follows:

    Date: 23/08/2025
    Venue: Central Mosque
    Time: After Jummat Prayer

    Thank you as you honor this invitation, and if you are unable to make it, 
    kindly say a prayer for us. 
    Thank you.
    Sender {sender}.
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""
main()