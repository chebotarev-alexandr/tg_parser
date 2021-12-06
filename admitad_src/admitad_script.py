from admitad import api, items

client_id = "4t50873u2KXNTxPtVECMsaVKUJbbMJ"
client_secret = "2s0gOmxxdMRCzdsSvA5INkZpM2tCnu"
scope = ' '.join(set([items.Me.SCOPE, "coupons", "coupons_for_website", "websites"]))
print(scope)
client = api.get_oauth_client_client(
    client_id,
    client_secret,
    scope
)

print(client.Me.get())

def parce_admitad_data():
    res = client.CouponsForWebsite.get(2080374, limit=500, offset=0)
    res_list = []
    for i in res['results']:
        if i['promocode'] != 'НЕ НУЖЕН' and i['promocode'] !='NOT REQUIRED' and i['promocode'] !='NOT REQUIRE':
            res_list.append({
                'id': i['id'],
                'name': i['name'],
                'description': i['description'],
                'date_start': str(i['date_start']).replace('/"', ''),
                'date_end': str(i['date_end']).replace('/"', ''),
                'promo': i['promocode']
            })
    return res_list

