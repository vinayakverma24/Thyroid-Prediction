import streamlit as st
import pickle

model_filename = "model/trained_model.pkl"
encoder_filename = "model/label_encoder.pkl"
with open(model_filename, 'rb') as model_file:
    model = pickle.load(model_file)

with open(encoder_filename, 'rb') as encoder_file:
    encoder = pickle.load(encoder_file)

st.markdown(
    """
    <style>
    .main {
        background-color: #36414D;
    }
    </style>
    """,
    unsafe_allow_html=True
)
st.title("Thyroid Prediction")

name = st.text_input("Type your name")

col1, col2 = st.columns(2)
age = st.slider("Select your age", 0, 100, value=40)
st.write(age)
tsh = st.slider("Thyroid Stimulating Hormone Level", 0.0, 530.0)
st.write(tsh)
tt4 = st.slider("Total Thyroxine TT4", 2.0, 430.0)
st.write(tt4)
fth = st.slider("Free Thyroxine Index", 2.0, 395.0)
st.write(fth)
t3m = st.slider("T3 Measure", 0.0, 11.0)
st.write(t3m)
t4u = st.slider("T4U Measure", 0.0, 2.0)
st.write(t4u)

tsh = 1 if tsh > 0.0 else 0
tt4 = 1 if tt4 > 2.0 else 0
fth = 1 if fth > 2.0 else 0
t3m = 1 if t3m > 0.0 else 0
t4u = 1 if t4u > 0.0 else 0

with col1:
    sex = st.selectbox("Enter sex", ["Male", "Female"])
    thm = st.selectbox("On Thyroxine Medication", ["Yes", "No"])
    hyp = st.selectbox("Hypopituitary Present", ["Yes", "No"])
    gtr = st.selectbox("Goitre Present", ["Yes", "No"])
    psy = st.selectbox("Psychological Symptoms Present", ["Yes", "No"])
    ant = st.selectbox("Anti-Thyroid Medication", ["Yes", "No"])
    hel = st.selectbox("Health Condition", ["Sick", "Fit"])

with col2:
    pre = st.selectbox("Pregnant?", ["Yes", "No"])
    thy = st.selectbox("Thyroid surgery?", ["Yes", "No"])
    rad = st.selectbox("I-131 radiotherapy Treatment", ["Yes", "No"])
    qhyper = st.selectbox("Suspicion regarding Hyperthyroidism", ["Yes", "No"])
    qhypo = st.selectbox("Suspicion regarding Hypothyroidism", ["Yes", "No"])
    lit = st.selectbox("Lithium treatment?", ["Yes", "No"])
    ref = st.selectbox("Referral source", ["STMW", "SVHC", "SVHD", "SVI", "Other"])

stmw, svhc, svhd, svi, oth = 0, 0, 0, 0, 0
if ref == 'STMW':
    stmw = 1
elif ref == 'SVHC':
    svhc = 1
elif ref == 'SVHD':
    svhd = 1
elif ref == 'SVI':
    svi = 1
else:
    oth = 1

sex = 1 if sex == 'Male' else 0
hel = 1 if hel == 'Sick' else 0

binary = [thm, hyp, gtr, psy, ant, pre, thy, rad, qhypo, qhyper, lit]
binary = [1 if x == 'Yes' else 0 for x in binary]

thm, hyp, gtr, psy, ant, pre, thy, rad, qhypo, qhyper, lit = binary

if st.button("Predict"):
    user_input = [[age, sex, thm, 0, ant, hel, pre, thy, rad, qhypo, qhyper, lit, gtr, 0, hyp, psy, tsh, t3m, tt4, t4u, fth, 0, stmw, svhc, svhd, svi, oth]]
    prediction = model.predict(user_input)
    decoded_prediction = encoder.inverse_transform(prediction)[0]
    st.success('Your Result is Ready')
    st.write("Predicted Output: ", decoded_prediction)