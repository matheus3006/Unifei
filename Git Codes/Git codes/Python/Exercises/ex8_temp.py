def celsius_to_farenheit(celsius):
    return celsius * (9/5) + 32

cel = input('Digite a temperatura em celsius: ')
far = celsius_to_farenheit(float (cel))

print(cel + ' C equivale a ' + str(far) + ' F')
    