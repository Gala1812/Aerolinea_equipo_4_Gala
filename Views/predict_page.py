import streamlit as st
import pickle
import numpy as np
import pandas as pd


def load_model():
    with open('saved_steps.pkl', 'rb') as file:
        pipeline = pickle.load(file)
    return pipeline

pipeline = load_model()

def show_predict_page():
    st.title("Formulario satisfacción de clientes")

    st.write("""### Por favor complete nuestra encuesta para evaluar la calidad de nuestros servicios.""")
    st.subheader("Le llevará un máximo de 10 minutos y nos ayudará a mejorar la calidad de los servicios que brindamos.")


    Gender  = (
        "Mujer",
        "Hombre",
    )

    Customer_Type = (
        "cliente leal",
        "cliente desleal",
    )
    Type_of_Travel = ( 
        'Viaje Personal',
        'Viaje de Negocio',
    )
    Class = (
        'Business', 
        'Eco', 
        'Eco Plus',
    )

    Gender = st.selectbox("Género", Gender)
    Customer_Type = st.selectbox("Tipo de cliente",  Customer_Type)
    Age = st.slider("Edad", 0, 100, 1)
    Type_of_Travel = st.selectbox("Tipo de Viaje",  Type_of_Travel)
    Class = st.selectbox("Clase",  Class)
    
    Flight_Distance = st.slider("Distancia de vuelo", 0, 5000, 10)
    Inflight_wifi_service = st.slider("Servicio wifi a bordo", 0, 5, 1)
    Departure_Arrival_time_convenient = st.slider("Hora de salida/llegada conveniente", 0, 5, 1)
    Ease_of_Online_booking = st.slider("Facilidad de reserva en línea", 0, 5, 1)
    Gate_location = st.slider("Ubicación de la puerta", 0, 5, 1)
    Food_and_drink = st.slider("Comida y bebida", 0, 5, 1)
    Online_boarding = st.slider("Embarque online", 0, 5, 1)
    Seat_comfort = st.slider("Confort del asiento", 0, 5, 1)
    Inflight_entertainment = st.slider("Entretenimiento a bordo:", 0, 5, 1)
    Onboard_service = st.slider("Servicio a bordo", 0, 5, 1)
    Leg_room_service = st.slider("Servicio de habitaciones para piernas", 0, 5, 1)
    Baggage_handling = st.slider("Manejo de equipaje", 0, 5, 1)
    Checkin_service = st.slider("Servicio de Check-in", 0, 5, 1)
    Inflight_service = st.slider("Servicio a bordo", 0, 5, 1, key="inflight_service_slider")
    Cleanliness = st.slider("Limpieza", 0, 5, 1, key="Cleanliness_slider")
    Departure_Delay_Minutes = st.slider("Retraso de salida en minutos", 0, 1600, 1)
    Arrival_Delay_Minutes = st.slider("Retraso de llegada en minutos", 0, 1600, 1)

    column_mapping = {
        'Gender': 'Gender',
        'Customer Type': 'Customer Type',
        'Age': 'Age',
        'Type_of_Travel': 'Type of Travel',
        'Class': 'Class',
        'Flight Distance': 'Flight Distance',
        'Inflight wifi service': 'Inflight wifi service',
        'Departure/Arrival time convenient': 'Departure/Arrival time convenient',
        'Ease of Online booking': 'Ease of Online booking',
        'Gate location': 'Gate location',
        'Food and drink': 'Food and drink',
        'Online boarding': 'Online boarding',  
        'Seat comfort': 'Seat comfort',  
        'Inflight entertainment': 'Inflight entertainment',
        'On-board service': 'On-board service',
        'Leg room service': 'Leg room service',
        'Baggage handling': 'Baggage handling',
        'Checkin service': 'Checkin service',  
        'Inflight service': 'Inflight service', 
        'Cleanliness': 'Cleanliness',
        'Departure Delay in Minutes': 'Departure Delay in Minutes',
        'Arrival Delay in Minutes': 'Arrival Delay in Minutes'          
        }
        
   
    ok = st.button("Nivel de satisfacción")

    if ok:
        X = pd.DataFrame({
            'Gender': [Gender],
            'Customer Type': [Customer_Type],
            'Age': [Age],
            'Type of Travel': [Type_of_Travel],
            'Class': [Class],
            'Flight Distance': [Flight_Distance],
            'Inflight wifi service': [Inflight_wifi_service],
            'Departure/Arrival time convenient': [Departure_Arrival_time_convenient],
            'Ease of Online booking': [Ease_of_Online_booking],
            'Gate location': [Gate_location],
            'Food and drink': [Food_and_drink],
            'Online boarding': [Online_boarding],
            'Seat comfort': [Seat_comfort],
            'Inflight entertainment': [Inflight_entertainment],
            'On-board service': [Onboard_service],
            'Leg room service': [Leg_room_service],
            'Baggage handling': [Baggage_handling],
            'Checkin service': [Checkin_service],
            'Inflight service': [Inflight_service],
            'Cleanliness': [Cleanliness],
            'Departure Delay in Minutes': [Departure_Delay_Minutes],
            'Arrival Delay in Minutes': [Arrival_Delay_Minutes]
        })
        
        X= X.rename(columns=column_mapping)
        st.write(X)

    # Predict the satisfaction level
        Nivel_de_satisfacción = pipeline.predict(X)

        st.subheader(f"Nivel de satisfacción: {'satisfecho' if Nivel_de_satisfacción == 1 else 'insatisfecho'}")
