from taxi import Taxi

taxi_one = Taxi("Prius 1", 100)
print(taxi_one)

taxi_one.drive(40)
print(taxi_one)
taxi_one.start_fare()
taxi_one.drive(100)
print(taxi_one)

