start_day = int(input("Ranging from 0 to 6 days with 0 representing Sunday, from 0-6 what day is it? "))
days_to_wait = int(input("And what is the length of your stay? "))
end_day = (start_day + days_to_wait) % 7
print(end_day)
