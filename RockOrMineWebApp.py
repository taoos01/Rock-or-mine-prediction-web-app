import numpy as np
import pickle
import streamlit as st

loaded_model = pickle.load(open( 'C:/Users/Mahdi/OneDrive/Desktop/Projects/RockOrMine.sav','rb'))

def rockPrediction(input_data):
    # input_data = (0.0453,0.0523,0.0843,0.0689,0.1183,0.2583,0.2156,0.3481,0.3337,0.2872,0.4918,0.6552,0.6919,0.7797,0.7464,0.9444,1.0000,0.8874,0.8024,0.7818,0.5212,0.4052,0.3957,0.3914,0.3250,0.3200,0.3271,0.2767,0.4423,0.2028,0.3788,0.2947,0.1984,0.2341,0.1306,0.4182,0.3835,0.1057,0.1840,0.1970,0.1674,0.0583,0.1401,0.1628,0.0621,0.0203,0.0530,0.0742,0.0409,0.0061,0.0125,0.0084,0.0089,0.0048,0.0094,0.0191,0.0140,0.0049,0.0052,0.0044)

    # Converting input data to numpy array
    input_data_as_numpy_array = np.asarray(input_data)

    # Reshaping the input data
    input_data_reshape = input_data_as_numpy_array.reshape(1, -1)

    # Standardizing the input data
    # std_data = scaler.transform(input_data_reshape)
    print(input_data_reshape)

    # Making prediction
    prediction = classifier.predict(std_data)
    print(prediction)

    if (prediction[0] == 'M'):
        return ("The object is MINE")
    else:
        return ("The object is ROCK")
    
def main():
    st.title("Rock or mine prediction")

    inputs = []
    for i in range(59):
        value = st.text_input(f"Input {i+1}", "")
        inputs.append(value)

    if st.button("Predict"):
        try:
            inputs = list(map(float, inputs))  # Convert all to float
            result = rockPrediction(inputs)
            st.success(result)
        except ValueError:
            st.error("⚠ Please enter valid numeric values for all inputs.")
    
    st.success(inputs)


if __name__ == '__main__':
    main()