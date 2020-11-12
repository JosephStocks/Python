pre_tip_amount = float(input("Total bill amount? "))
level_of_service = input("Level of service? ").strip().lower()

service2tip_dict = {"good": 0.2,
                    "fair": 0.15,
                    "bad": 0.1}

tip_amount = service2tip_dict[level_of_service] * pre_tip_amount
total_w_tip = tip_amount + pre_tip_amount

print(f"Tip amount: ${tip_amount:.2f}")
print(f"Total amount: ${total_w_tip:.2f}")