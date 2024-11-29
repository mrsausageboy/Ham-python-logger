restart = "yes"
log_file = "m7tbqham_radio_log.txt"  

while restart.lower() == "yes":
    your_call = input("Please enter your callsign: ") 
    there_call = input("Please enter their callsign: ") 
    Freq = input("Please enter the frequency: ")
    mode = input("Please enter the mode of your contact: ") 
    
    with open(log_file, "a") as file:
        file.write(f"\nYour callsign: {your_call}\nThere callsign: {there_call}\nMode: {mode}\nFrequency: {Freq}\n")

    restart = input("\nWould you like to log another contact? (yes/no): ")

print("Thank you for using the Ham Radio Logbook!")
