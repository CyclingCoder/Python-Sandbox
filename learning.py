# print("helloworld")

# def mean(value):
#     if type(value) == dict:
#         the_mean = sum(value.values()) / len(value)
#     else:
#         the_mean = sum(value) / len(value)

#     return the_mean

# #monday_temperatures = [8.9, 9.1, 9.9]

# student_grades = {"mary": 9.1, "sim": 8.8, "John": 7.5}
# print(mean(student_grades))

# def password(value):
#     if len(value) > 8:
#         return True
#     else:
#         return False

# print(password('12863132'))

# def weather_conditions(farTemp, celciusTemp):
#     if farTemp > 80 or celciusTemp > 60:
#         return "Hot"
#     else:
#         return "Cold"

# user_input_one = float(input("enter far temperature: "))
# user_input_two = float(input("enter celcius temperature: "))
# print(weather_conditions(user_input_one, user_input_two))
# print("user_input_one: ", user_input_one, "user_input_two: ", user_input_two)
# print("first name: ", 'jen')
# print("last name: ", 'green')
# print("phone: ", '123-456-789074')

# first_name = input("first name")
# last_name = input("last name")
# phone = input("phone number")
# print(first_name)
# print(last_name)
# print(phone) 

name=input("enter your name: ")
surname= input("enter your surname: ")
when= "today"
# user_input = input("Enter your name: ")
message = "Hello %s %s" % (name, surname)
# message = f"hello {name}  {surname}. What's up {when}"
print(message)

