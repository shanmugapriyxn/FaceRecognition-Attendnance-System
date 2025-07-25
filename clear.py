import pickle 
with open('data/names.pkl', 'wb') as w:
    pickle.dump([],w)
with open('data/faces.pkl', 'wb') as f:
    pickle.dump([],f)