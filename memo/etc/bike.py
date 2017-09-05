bike_purchase_price = 61
repair_price = 10
bike_selling_price = 45
loss = (bike_purchase_price + repair_price) - bike_selling_price
person_used = 2
loss_per_person = loss / person_used
print(loss_per_person)
money_i_gave_for_bike = 20
money_i_gave_for_ticket = 3
park_ticket_he_give = 20
print((money_i_gave_for_bike + money_i_gave_for_ticket) - (loss_per_person + park_ticket_he_give))
# 45만 - / 61 - 35 = 총 손해액 26만 / 2 = 인당 13손해.    20만원 - 13만원 = 7만원.   전일 잘못정산금액 20만원 - 3만원 - 판매차액7만원 = 10만원 다시 보내주면됨.
