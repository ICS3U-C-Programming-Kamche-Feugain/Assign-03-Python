#!/usr/bin/env python3\
# Created By:Kamche
# Created on: November 2, 2026
# This program ask the user for its age,
# time of day and status to calculate
# and give the passenger a train fare ticket.
import constants


def main():
    # Welcome the passenger to my train station
    print("Welcome to Kamche's train station")
    print("Where everything is like a dream")

    try:
        # get passenger information to calculate fare ticket
        age_input_str = input("Enter your age: ")
        age_input_int = int(age_input_str)

        status = input("Are you a student? (yes/no): ")
        time_of_day = input("Enter the time of the day (peak or off peak): ")

        # Check passenger information

        # Calculate the fare ticket
        if age_input_int >= 65:
            fare = constants.SENIOR_FARE
        elif age_input_int < 12:
            fare = constants.CHILD_FARE
        elif age_input_int <= 21:
            fare = constants.YOUTH_FARE
        elif status == "yes":
            fare = constants.STUDENT_FARE
        else:
            fare = constants.ADULT_FARE

        # Apply peak surcharge
        if time_of_day == "peak" and age_input_int >= 12:
            fare = fare + constants.PEAK_SURCHARGE

        # Display results
        print("\n TRAIN FARE ")
        print("Passenger age: {}".format(age_input_int))
        print("Status: {}".format(status))
        print("Time of the day: {}".format(time_of_day)

        if age_input_int < 12:
            print("Total fare: Free")
        else:
            print("The total fare: ${:.2f}".format(fare))

    except ValueError:
        print(
            "{} is a invalid entry.Please enter a valid number for age".format(
                age_input_str
            )
        )

    finally:
        print("Thank you for traveling with us!!")


if __name__ == "__main__":
    main()
