def main():
    time = input("What's the time? ")
    float_time=convert(time)
    if 7.0 <= float_time <= 8.0:
        print("breakfast time")
    elif 12.0 <= float_time <= 13.0:
        print("lunch time")
    elif 18.0 <= float_time <= 19.0:
        print("dinner time")
    else:
        return 


def convert(time):

    hours, minutes = time.split(":")
    total_hours = float(hours) + float(minutes)/60
    return total_hours

if __name__ == "__main__":
    main()
