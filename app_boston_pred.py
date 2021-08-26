
#this line has to be at the beginning of the cell
# otherwise an error is generated.
# The code line  above  extracts the python file, and give it the name
# app_boston_pred.py 
 # These are the crucial libraries used to create the webapp and to read
    
# the saved nodel
import pickle
import streamlit as st
 
# loading the trained model
pickle_in = open('lin_reg_Boston.pkl', 'rb')
regressor = pickle.load(pickle_in)
 
#to make it the app faster we use cache
@st.cache()
  
# defining the function which will make the prediction using the data which the user inputs 
def prediction(crim,zn,indus,chas,nox,rm,age,dis,rad,tax,ptratio,black,lsta):  
 
    # Making predictions using the column names from saved model
    prediction = regressor.predict( 
        [[crim,zn,indus,chas,nox,rm,age,dis,rad,tax,ptratio,black,lsta]])
     
    return prediction
      
  
# this is the main function in which we define our webpage  
def main():       
    # front end elements of the web page 
    html_temp = """ 
    <div style ="background-color:green;padding:12px"> 
    <h1 style ="color:black;text-align:center;"> Boston 
     House Price predictor</h1> 
    </div> 
    """
      
    # display the front end aspect 
    st.markdown(html_temp, unsafe_allow_html = True)
   
    # following lines create boxes in which user can enter data required to make prediction 
    # We can enter values for the predictors
    crim = st.number_input("crim") 
    zn = st.number_input("zn") 
    indus = st.number_input("indus") 
    chas = st.number_input("chas") 
    nox = st.number_input("nox")
    rm = st.number_input("rm")
    age = st.number_input("age")
    dis = st.number_input("dis")
    rad = st.number_input("rad")
    tax = st.number_input("tax")
    ptratio = st.number_input("ptratio")
    black = st.number_input("black")
    lsta = st.number_input("lsta")
   
    # when 'Predict' is clicked, make the prediction a
    if st.button("Predict"): 
        result = prediction(crim,zn,indus,chas,nox,rm,age,dis,rad,tax,ptratio,black,lsta) 
        st.success('Predicted house price is : {}'.format(result))
    return None 
        
if __name__=='__main__': 
        main()
