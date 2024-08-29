 # lista de invitados 
 
guests = ['Tupac', 'Marley', 'Eric Clapton']

print(f"{guests[2]} will not attend this party\n")

del guests[2]
guests.insert(2, 'Elon Musk')
print(guests)

message = f"\nHello {guests[0]}!, you are invited to my party."
message1 = f"\nHello {guests[1]}!, you are invited to my party."
message2 = f"\nHello {guests[2]}!, you are invited to my party."

print(message,message1, message2)

print("Hi!, there is a big table, are lot space")

guests.insert(0, 'Dr. Dre')
guests.insert(2, 'Snoop Dogg')
guests.append('Gustavo Cerati')

print(guests)

print("Only are invited two people")

print(f"Hi {guests[0]}!, sorry but you are not invited",guests.pop(0))
print(f"Hi {guests[1]},sorry but you are not invited",guests.pop(1))
print(f"Hi {guests[2]},sorry but you are not invited",guests.pop(2))
print(f"Hi {guests[2]},sorry but you are not invited",guests.pop(2))

print(f"\nHi {guests[0]}, you are invited",guests.pop(0))
print(f"Hi {guests[0]}, you are invited",guests.pop(0))

guests.clear()

print(guests)



