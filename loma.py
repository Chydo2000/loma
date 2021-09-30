def trip_cost(number_of_nights, city, number_of_day):
 
  def hotel_cost(number_of_nights):
    x = 140
    s = number_of_nights * x
    return s
  
  def plane_ride_cost(city):
    if city == "Крым":
      city_1 = 120
      return city_1  
    elif city == "Шри-Ланка":
      city_1 = 800
      return city_1
    elif city == "Каир":
      city_1 = 400
      return city_1
    elif city == "Сочи":
      city_1 = 120
      return city_1 
  
  def rental_car_cost(number_of_day):
    sum_ = 0
    x = 40*1.01**number_of_day
    for i in range(1, number_of_day+1):
      sum_ += x
    if number_of_day>=7:
      sale = 50
      sum_1=sum_-sale
      return sum_1  
    if 3<=number_of_day<=6:
      sale_2 = 20
      sum_1=sum_-sale_2
      return sum_1 
     
  print('Полная стоимость:', round(hotel_cost(number_of_nights) + plane_ride_cost(city) + rental_car_cost(number_of_day)), 'y.e.')