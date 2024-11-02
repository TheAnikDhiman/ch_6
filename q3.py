p1="Make a lot of money"
p2="buy now"
p3="subscribe this"
p4="click this"
message = input("Enter Your Message: ")
if (p1 in message or p2 in message or p3 in message or p4 in message):
    print("You are a spammer")
else:
    print("You are not a spammer")
