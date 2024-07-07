import streamlit as st
import pickle

model_filename = "model/trained_model.pkl"
encoder_filename = "model/label_encoder.pkl"
with open(model_filename, 'rb') as model_file:
    model = pickle.load(model_file)

with open(encoder_filename, 'rb') as encoder_file:
    encoder = pickle.load(encoder_file)
    

st.title("Thyroid Prediction")
st.sidebar.header('Dashboard `iNeuron.ai`')
nav = st.sidebar.radio("Navigation",["Prediction"])

if nav == "Prediction":  
    name = st.text_input("Type your name")
    

    age = st.slider("Select your age",0,100,value=40)
    st.write(age)
    sex = st.selectbox("Enter sex",["Male","Female"])
    
    tsh = st.slider("Thyroid Stimulating Hormone Level",0.0, 530.0)
    st.write(tsh)
    tt4 = st.slider("Total Thyroxine TT4",2.0,430.0)
    st.write(tt4)
    fth = st.slider("Free Thyroxine Index",2.0,395.0)
    st.write(fth)
    t3m = st.slider("T3 Measure",0.0,11.0)
    st.write(t3m)
    t4u = st.slider("T4U Measure",0.0,2.0) 
    st.write(t4u)
    if tsh > 0.0:
      tsh = 1
    else:
      tsh = 0
    if tt4 > 2.0:
      tt4 = 1
    else:
      tt4 = 0
    if fth > 2.0:
      fth = 1
    else:
      fth = 0
    if t3m > 0.0:
      t3m = 1
    else:
      t3m = 0
    if t4u > 0.0:
      t4u = 1
    else:
      t4u = 0
      
    thm = st.selectbox("On Thyroxine Medication",["Yes","No"])
    hyp = st.selectbox("Hypopituitary Present",["Yes","No"])
    gtr = st.selectbox("Goitre Present",["Yes","No"])
    psy = st.selectbox("Pshylogical Symptoms Present",["Yes","No"])
    ant = st.selectbox("Anti-Thyroid Medication",["Yes","No"])
    
    hel = st.selectbox("Health Condition",["Sick","Fit"])
    
    pre = st.selectbox("Pregnant?",["Yes","No"])
    thy = st.selectbox("Thyroid surgery?",["Yes","No"])
    rad = st.selectbox("I-131 radiotherapy Treatment",["Yes","No"])
    qhyper = st.selectbox("Suspicion regarding Hyperthyroidism",["Yes","No"])
    qhypo = st.selectbox("Suspicion regarding Hypothyroidism",["Yes","No"])
    lit = st.selectbox("Lithium treatment?",["Yes","No"])
    
    ref = st.selectbox("Referal source",["STMW","SVHC","SVHD","SVI","Other"])
    stmw = 0
    svhc = 0
    svhd = 0
    svi = 0
    oth = 0

    if ref == 'STMW':
      stmw = 1
    if ref == 'SVHC':
      svhc = 1
    if ref == 'SVHD':
      svhd = 1
    if ref == 'SVI':
      svi = 1
    if ref == 'Other':
      oth = 1

    #st.subheader("Selected inputs are:")
    #st.write(tsh)
    if sex == 'Male':
      sex = 1
    else:
      sex = 0
    if hel == 'Sick':
       hel = 1
    else:
       hel = 0
    binary = [thm,hyp,gtr,psy,ant,pre,thy,rad,qhypo,qhyper,lit]
    for i in range(11):
      if binary[i] == 'Yes':
        binary[i] = 1
      else:
        binary[i] = 0
       
    thm = binary[0]
    hyp = binary[1]
    gtr = binary[2]
    psy = binary[3]
    ant = binary[4]
    pre = binary[5]
    thy = binary[6]
    rad = binary[7]
    qhypo = binary[8]
    qhyper = binary[9]
    lit = binary[10]

    if st.button("Predict"):
        #user_input = [[15,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,0,0,0,0,0,1]]
        user_input = [[age,sex,thm,0,ant,hel,pre,thy,rad,qhypo,qhyper,lit,gtr,0,hyp,psy,tsh,t3m,tt4,t4u,fth,0,stmw,svhc,svhd,svi,oth]]
        
        prediction = model.predict(user_input)
        decoded_prediction = encoder.inverse_transform(prediction)[0]
        
        st.success('Your Result is Ready')
        st.write("Predicted Output: ",decoded_prediction)
        
