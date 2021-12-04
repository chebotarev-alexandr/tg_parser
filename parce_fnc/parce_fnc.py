promo_word_list = ['промокод:', 'промо:', 'вводим:', 'промокод', 'промо', 'вводим', 'промокоды', 'промокоды:']
bls_word = ['действует', 'работает', 'не', 'продавцу.', 'Активировать', 'и', 'на', 'действуют', 'который', 'работают', 'по']

#parsing in first chanal 
def parce_message(mes, date):
    filtred_message = mes.lower().replace('\n', ' ').replace('\"', '').replace('-', '').replace(':', '')
    for word in bls_word:
        filtred_message.replace(word, '')
    splited_message = filtred_message.split(' ')
    result = []
    for word in promo_word_list:
        try:
            promo = splited_message[splited_message.index(word) + 1]
            if promo in promo_word_list or promo in bls_word:
                print(f'Error: {promo}')
                raise Exception 
            result.append(promo)
        except:
            print('none')
    return result, date


def parce_admitad(coupons_list):
    pass