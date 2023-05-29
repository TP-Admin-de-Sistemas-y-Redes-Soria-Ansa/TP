import httplib2

# Crear una instancia del cliente
http = httplib2.Http()

# Realizar una solicitud GET
response, content = http.request("https://sipa.huergo.com.ar/", "GET")

# Imprimir la respuesta
if response.status == 200:
    print(content.decode())
else:
    print("Error en la solicitud. Código de estado:" , response.status)