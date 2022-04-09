import streamlit as st
import pandas as pd
import numpy as np


from PIL import Image
test_image = Image.open(r'C:\Users\njvdb\projects\fork\src\app\test.jpg')
st.image(test_image, caption= "Kraftwerk im Sonnenuntergang")


st.title('Vorhersage der deutschen CO2-Emissionen')

"Autor: Dimitri Bennhäuser (https://github.com/dimitribenn)"

from scipy.stats import linregress

years = [2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020]
emissions_per_year = [10.3, 10.0, 10.1, 10.2, 9.7, 9.7, 9.7, 9.5, 9.1, 8.5, 7.7]
temp_per_year = [7.9, 9.6, 9.1, 8.7, 10.3, 9.9, 9.5, 9.6, 10.5, 10.2, 10.4]

regression_result = linregress(years, emissions_per_year)
scipy_slope = regression_result.slope
scipy_intercept = regression_result.intercept

regression_result_temp = linregress(years, temp_per_year)
scipy_slope_temp = regression_result_temp.slope
scipy_intercept_temp = regression_result_temp.intercept

def scipy_model(desired_year):
    model_result = scipy_slope * desired_year + scipy_intercept
    return model_result

def scipy_model_temp(desired_year):
    model_result_temp = scipy_slope_temp * desired_year + scipy_intercept_temp
    return model_result_temp

desired_year = st.number_input('Jahr', value=2022)

prediction = scipy_model(desired_year)
prediction_rounded = round(prediction, 2)

prediction_temp = scipy_model_temp(desired_year)
prediction_temp_rounded = round(prediction_temp, 2)

"Die Vorhersage der Emissionen für das ausgewählte Jahr ist:"

st.write(prediction_rounded)

"Tonnen pro Kopf pro Jahr gg"

"Die Vorhersage der durschnittlichen Temperatur für das ausgewählte Jahr ist:"
st.write(prediction_temp_rounded)

"Grad Celsius"

st.subheader("Über das Modell und die Daten")

"Der öffentliche Link zur App: https://share.streamlit.io/dimitribenn/biz_analytics_a_new_app/BA_App_Fork/src/app/app.py"

"Das Modell ist ein lineares Regressionsmodell auf Grundlage von 2010 bis 2020. "
"Es steht ein Datenpunkt pro Jahr zur Verfügung."

"Die Daten stammen aus folgenden Quellen:"

"- Global Carbon Project. (2021). Supplemental data of Global Carbon Project 2021 (1.0) [Data set]. " \
"Global Carbon Project. https://doi.org/10.18160/gcp-2021. "
"- Andrew, Robbie M., & Peters, Glen P. (2021). The Global Carbon Project's fossil CO2 emissions dataset [Data set]. " \
"Zenodo. https://doi.org/10.5281/zenodo.5569235."
"- DWD. Entwicklung der Jahresmitteltemperatur in Deutschland in ausgewählten Jahren von 1960 bis 2021. [Data set]." \
    "https://de-statista-com.ezp.hs-duesseldorf.de/statistik/daten/studie/914891/umfrage/durchschnittstemperatur-in-deutschland/"