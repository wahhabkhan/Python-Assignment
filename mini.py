Number_of_reservations = int(input("Enter Number of Reservations:\n"))
Type_of_reservation = str(input("Enter Type of Reservation:\n"))
Number_of_persons = int(input("Enter Number of Persons:\n"))
Number_of_reservation_days = int(input("Enter Number of Reservation Days:\n"))

Online_reservation_services = []
Online_reservation_services.append(Number_of_reservations) 
Online_reservation_services.append(Type_of_reservation)
Online_reservation_services.append(Number_of_persons)
Online_reservation_services.append(Number_of_reservation_days)                                   
#print(Online_reservation_services)

if Type_of_reservation == "Cottage":
    
  Reservation_fee1 = 325.500
  Reservation_fee2 = 450.000
  Room_service_rate = 0.035
  Discount1 = 0.03
  Discount2 = 0.02  
    
  if Number_of_persons >=1 and Number_of_persons <=6:
    Total_reservation_fee = Number_of_persons * Reservation_fee1
    Online_reservation_services.append(Total_reservation_fee)
    Service_tax = Reservation_fee1 * Room_service_rate
    Online_reservation_services.append(Service_tax)
    
    if Total_reservation_fee > 900:
      Discount = Discount1 * Total_reservation_fee
      Online_reservation_services.append(Discount) 
        
    else:
      Discount = Discount2 * Total_reservation_fee
      Online_reservation_services.append(Discount)
        
  Total_bill = (Total_reservation_fee + Service_tax) - Discount
  Online_reservation_services.append(Total_bill)

  else:
    Total_reservation_fee = Number_of_persons * Reservation_fee2
    Online_reservation_services.append(Total_reservation_fee)
    Service_tax = Reservation_fee2 * Room_service_rate    
    Online_reservation_services.append(Service_tax)
    
    if Total_reservation_fee > 900:
      Discount = Discount1 * Total_reservation_fee
      Online_reservation_services.append(Discount)
        
    else:
      Discount = Discount2 * Total_reservation_fee
      Online_reservation_services.append(Discount)
        
  Total_bill = (Total_reservation_fee + Service_tax) - Discount
  Online_reservation_services.append(Total_bill)

  print(Online_reservation_services)
