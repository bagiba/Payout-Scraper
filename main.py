from Modules.ModuloKlekt import Klekt
from Modules.ModuloRestocks import Restocks
from Utilities.DiscordWebhook import MandarWebhook

#sku = input("SKU?: ")
pid = 'DH4402-001'

nombre, foto, preciosR = Restocks(pid)
linkVentaKlekt, preciosK = Klekt(pid)

print(preciosK)
print(preciosR)

MandarWebhook(foto, nombre, pid, preciosR, preciosK, linkVentaKlekt)