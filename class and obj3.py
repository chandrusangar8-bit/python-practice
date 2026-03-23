class laptop:
    price=""
    processor=""
    ram=""

hp=laptop()
dell=laptop()
lenovo=laptop()

hp.price="45000"
hp.processor="ryzen5"
hp.ram="12gb"

dell.price="40000"
dell.processor="ryzen4"
dell.ram="8gb"

lenovo.price="50000"
lenovo.processor="ryzen5"
lenovo.ram="16gb"

print("hp:",hp.price,hp.processor,hp.ram)
print("dell:",dell.price,dell.processor,dell.ram)
print("lenovo:",lenovo.price,lenovo.processor,lenovo.ram)
