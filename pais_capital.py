import streamlit as st
import pandas as pd

# Datos de países, capitales y población de las capitales
data = {
    'País': ['Argentina', 'Bolivia', 'Brasil', 'Chile', 'Colombia', 'Costa Rica', 'Cuba', 'Ecuador', 'El Salvador',
             'Guatemala', 'Honduras', 'México', 'Nicaragua', 'Panamá', 'Paraguay', 'Perú', 'República Dominicana', 
             'Uruguay', 'Venezuela'],
    'Capital': ['Buenos Aires', 'La Paz', 'Brasilia', 'Santiago', 'Bogotá', 'San José', 'La Habana', 'Quito',
                'San Salvador', 'Ciudad de Guatemala', 'Tegucigalpa', 'Ciudad de México', 'Managua', 'Ciudad de Panamá', 
                'Asunción', 'Lima', 'Santo Domingo', 'Montevideo', 'Caracas'],
    'Población (millones)': [15.62, 2.11, 4.82, 7.21, 10.97, 3.16, 2.14, 2.99, 2.18, 3.01, 2.94, 22.3, 1.05, 1.85, 
                             2.81, 9.75, 2.17, 1.77, 2.82]
}

# Crear un DataFrame
df = pd.DataFrame(data)

# Configuración de la aplicación
st.title('Capitales de Latinoamérica y su Población')

# Mostrar la tabla
st.write('A continuación se muestra una tabla con los países de Latinoamérica, sus capitales y la población de estas ciudades:')
st.dataframe(df)

# Pie de página
st.caption('Fuente: Datos recopilados de Wikipedia y Saber es Práctico (2024).')
