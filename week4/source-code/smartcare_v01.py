appointments = [] #Creates the list

def book_appointment(patient_name, practitioner_name, appointment_time): #
    if not patient_name:
        raise ValueError("Patient name cannot be empty")
    appointment = {
        "patient": patient_name,
        "practitioner": practitioner_name,
        "time": appointment_time
    }
    appointments.append(appointment)

def display_appointments():
    if not appointments:
        print("No appointments recorded.")
        return
    for appointment in appointments:
        print(f"Patient: {appointment['patient']} | Practitioner: {appointment['practitioner']} | Time: {appointment['time']}")

print("Welcome to SmartCare: The Clinical Appointment Booking System!")

#Added a text based ui

while True:
    print("Please make a selection from the following:\n"
    "1. Create Appointment\n"
    "2. View Bookings\n"
    "3. Exit\n"
    #"4. Save bookings to file\n"
    )
    selection = input("") 
    if selection == "1":
        book_appointment(input("Patient Name: "), input("Praciticoner Name: "), input("Appointment time (24hrs): "))
    elif selection == "2":
        display_appointments()
    elif selection == "3":
        break
    #elif selection == "4":
        #Save appointments to csv file
    #elif selection in appointments
        #Print the details of the relevant appointment
    else:
        print("Invalid selection. Please type the number of the option you wish to select.")