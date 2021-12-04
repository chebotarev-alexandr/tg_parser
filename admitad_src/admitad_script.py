from admitad import api, items

client_id = "zKoVx0Wwhr5zBblC5XMbbeg46UEAjs"
client_secret = "fzyk2QYXkJz27AlkADDkO4c0TYkOrB"
scope = ' '.join(set([items.Me.SCOPE]))
client = api.get_oauth_client_client(
    client_id,
    client_secret,
    scope
)

print(client.Me.get())

res = client.Coupons.get()

print(res)