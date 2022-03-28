from Modules.ModuloKlekt import Klekt
from Modules.ModuloRestocks import Restocks
from Utilities.DiscordWebhook import MandarWebhook
from Modules.ModuloAlias import Alias

pid = 'DD1875-100'

nombre, foto, preciosR = Restocks(pid)
linkVentaKlekt, preciosK = Klekt(pid)
listAlias = Alias(pid)
#print(preciosK)
#print(preciosR)
#print(listAlias)
MandarWebhook(foto, nombre, pid, preciosR, preciosK, linkVentaKlekt,listAlias)