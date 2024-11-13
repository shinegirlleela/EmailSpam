import streamlit as st
import pickle

model = pickle.load(open('spam.pkl','rb'))
cv = pickle.load(open('vectorizer.pkl','rb'))

st.title("Email Spam Classification Appliction")
st.write("This is a Machine Learning Application to Classify emails as Spam or Ham")
user_input = st.text_area("Enter an email to classify",height=150)
if st.button("Classify"):

    if user_input :
        data = [user_input]
        vect = cv.transform(data).toarray()
        pred = model.predict(vect) 
        if pred == 0:
            st.success("This Email is not Spam")
        else:
            st.error("This is Spam Email")
    else:
        print("Type Email")