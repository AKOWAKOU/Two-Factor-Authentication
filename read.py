import csv


with open("receivers.csv", "r") as file:
    reader = csv.reader(file)
    next(reader)
    for name, email, designation, salary in reader:
        print(f"Sending email to {name} on email: {email}")
        # TODO: Send email
