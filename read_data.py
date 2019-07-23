from firebase import firebase
firebase = firebase.FirebaseApplication('https://home-ehrlfa.firebaseio.com', None)
while True:
    nyala = firebase.get('/nyalakan', None)
    mati = firebase.get('/matikan', None)
    kipas = firebase.get('/kipas',None)
    a = len(kipas)
    b = len(nyala)
    if a == 1 and b == 1:
        print('kipas nyala')
    else:
        print('kipas mati')
