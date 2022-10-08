#If the bill was $150.00, split between 5 people, with 12% tip.

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇

bill = input("How much is the bill? ")
bill_as_float = float(bill)

person = input("How many person to split between? ")
person_as_int = int(person)

tip_percent = input("How many percent(%) of tip? 10? 12? 15? ")
tip_percent_as_float = (int(tip_percent) / 100) + 1

bill_per_person = bill_as_float // person_as_int
bill_per_person_w_tax = round(bill_per_person * tip_percent_as_float, 2)
print(
    f"Each person should pay ({bill_as_float} / {person_as_int}) * {tip_percent_as_float} = {bill_per_person_w_tax:.2f}"
)
