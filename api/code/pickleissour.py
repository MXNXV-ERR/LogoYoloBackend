import joblib

def getJoblibModelPred(text):
    model=joblib.load(open('api/code/Adaboost.pkl','rb'))
    
    pred =model.predict([["10.4","15.2","12","132","0","123","21","2","1","2","3"]])
    print(pred[0])
    class_names = ['Fake', 'Genuine']
    return class_names[pred[0]] 


