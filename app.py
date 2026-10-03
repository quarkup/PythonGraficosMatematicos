#***************************************************
# https://www.youtube.com/watch?v=PBZQVmLcb5I&list=PLMi6KgK4_mk2rK5jD-BK5RigFIP2QSq8W&index=12

# MultiSelect Widget - Web App with Python Streamlit Lesson 12

# Turtle Code
#***************************************************
#-------------------------------------------------------------------------------------
import streamlit as st
import numpy as np
import pandas as pd
import plotly.express as px
from streamlit_option_menu import option_menu
from numerize.numerize import numerize
from query import *
import matplotlib.pyplot as plt
import plotly as px
#-------------------------------------------------------------------------------------
#-----------Definir el espacio de la malla-------------------
x = np.linspace(-8, +8, 100)

y = (np.sin(x))*x**2

#-------------------------------------------------------------------------------------
#st.title("Actualización de datos...!!!")
data = pd.DataFrame({
   'x' : np.linspace(-8, +8, 100),
   'y' : y   
                    })
#--------------------------------------------------------------
st.subheader("Gráfico de lineas")
fig, ax =plt.subplots()
plt.grid()   #---------------------------------WFCZ---
ax.plot(data['x'], data['y'])
st.pyplot(fig)
#---------------------------------------------
#fig = px.line(df_selection.groupby("continente")["poblacion"].sum().reset_index(), x="continente", y="poblacion")
#fig = px.line(data, x="x", y="y")
#st.subheader("😊 Gráfico de Lineas")  #???????????????????????????
#st.plotly_chart(fig)
#---------------------------------------------
#plt.grid(True)
#plt.plot(x,y)
#plt.show()

#---------------------------------------------
data