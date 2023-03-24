from firebase_admin import credentials, firestore, initialize_app

cred = credentials.Certificate('oddsbrew-80bea-firebase-adminsdk-vpuex-763c317863.json')
initialize_app(cred)

db = firestore.client()

def get_db():
    users_ref = db.collection('data')
    docs = users_ref.stream()

    users_list = []

    for doc in docs:
        users_list.append(doc.to_dict())

    return users_list
print(get_db())