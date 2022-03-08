from ModuloKlekt import Klekt
from ModuloRestocks import Restocks
from DiscordWebhook import MandarWebhook

#sku = input("SKU?: ")
pid = 'CT8527-016'

nombre, foto, preciosR = Restocks(pid)
linkVentaKlekt, preciosK = Klekt(pid)

print(preciosK)
print(preciosR)

MandarWebhook(foto, nombre, pid, preciosR, preciosK, linkVentaKlekt)