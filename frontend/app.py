import streamlit as st
import requests
import random

st.set_page_config(page_title="Breast Cancer Prediction", layout="wide")

st.title("Breast Cancer Prediction System")
st.subheader("Enter Feature Values")

st.markdown("""
<style>
    .main {
        background-color: #0E1117;
        color: white;
    }
    .stButton>button {
        border-radius: 10px;
        height: 3em;
        width: 100%;
        font-size: 16px;
    }
    .stNumberInput input {
        border-radius: 8px;
    }
</style>
""", unsafe_allow_html=True)

# ---- SESSION STATE ----
if "data" not in st.session_state:
    st.session_state.data = {}

def get_value(key):
    return st.session_state.data.get(key, 0.0)

# ---- BENIGN SAMPLE ----
benign_sample = {
    "radius_mean": 12.5, "texture_mean": 18.0, "perimeter_mean": 80.0,
    "area_mean": 500.0, "smoothness_mean": 0.09, "compactness_mean": 0.08,
    "concavity_mean": 0.03, "concave points_mean": 0.02, "symmetry_mean": 0.18,

    "radius_se": 0.3, "perimeter_se": 2.0, "area_se": 25.0,
    "compactness_se": 0.01, "concavity_se": 0.015,
    "concave points_se": 0.01, "symmetry_se": 0.015,
    "fractal_dimension_se": 0.002,

    "radius_worst": 13.5, "texture_worst": 22.0,
    "perimeter_worst": 85.0, "area_worst": 550.0,
    "smoothness_worst": 0.12, "compactness_worst": 0.15,
    "concavity_worst": 0.08, "concave points_worst": 0.05,
    "symmetry_worst": 0.25, "fractal_dimension_worst": 0.07
}

# ---- MALIGNANT SAMPLE ----
malignant_sample = {
    "radius_mean": 18.0, "texture_mean": 25.0, "perimeter_mean": 120.0,
    "area_mean": 1000.0, "smoothness_mean": 0.12, "compactness_mean": 0.3,
    "concavity_mean": 0.4, "concave points_mean": 0.2, "symmetry_mean": 0.3,

    "radius_se": 1.0, "perimeter_se": 8.0, "area_se": 150.0,
    "compactness_se": 0.05, "concavity_se": 0.08,
    "concave points_se": 0.05, "symmetry_se": 0.03,
    "fractal_dimension_se": 0.006,

    "radius_worst": 22.0, "texture_worst": 30.0,
    "perimeter_worst": 150.0, "area_worst": 1500.0,
    "smoothness_worst": 0.18, "compactness_worst": 0.5,
    "concavity_worst": 0.6, "concave points_worst": 0.3,
    "symmetry_worst": 0.4, "fractal_dimension_worst": 0.1
}


# ---- INTERMEDIATE SAMPLE ----
intermediate_sample = {
    "radius_mean": 14.5,
    "texture_mean": 21.0,
    "perimeter_mean": 95.0,
    "area_mean": 650.0,
    "smoothness_mean": 0.10,
    "compactness_mean": 0.12,
    "concavity_mean": 0.10,
    "concave points_mean": 0.06,
    "symmetry_mean": 0.22,

    "radius_se": 0.5,
    "perimeter_se": 3.5,
    "area_se": 45.0,
    "compactness_se": 0.02,
    "concavity_se": 0.03,
    "concave points_se": 0.02,
    "symmetry_se": 0.02,
    "fractal_dimension_se": 0.004,

    "radius_worst": 17.0,
    "texture_worst": 25.0,
    "perimeter_worst": 110.0,
    "area_worst": 900.0,
    "smoothness_worst": 0.14,
    "compactness_worst": 0.25,
    "concavity_worst": 0.30,
    "concave points_worst": 0.12,
    "symmetry_worst": 0.30,
    "fractal_dimension_worst": 0.08
}

# ---- RANDOM SAMPLE ----
def generate_random_sample():
    return {
        "radius_mean": random.uniform(10, 20),
        "texture_mean": random.uniform(10, 30),
        "perimeter_mean": random.uniform(70, 130),
        "area_mean": random.uniform(400, 1200),
        "smoothness_mean": random.uniform(0.08, 0.15),
        "compactness_mean": random.uniform(0.05, 0.4),
        "concavity_mean": random.uniform(0.0, 0.5),
        "concave points_mean": random.uniform(0.0, 0.3),
        "symmetry_mean": random.uniform(0.15, 0.35),

        "radius_se": random.uniform(0.1, 1.5),
        "perimeter_se": random.uniform(1, 10),
        "area_se": random.uniform(10, 200),
        "compactness_se": random.uniform(0.005, 0.05),
        "concavity_se": random.uniform(0.005, 0.1),
        "concave points_se": random.uniform(0.005, 0.05),
        "symmetry_se": random.uniform(0.01, 0.05),
        "fractal_dimension_se": random.uniform(0.001, 0.01),

        "radius_worst": random.uniform(12, 25),
        "texture_worst": random.uniform(15, 35),
        "perimeter_worst": random.uniform(80, 170),
        "area_worst": random.uniform(500, 2000),
        "smoothness_worst": random.uniform(0.1, 0.2),
        "compactness_worst": random.uniform(0.1, 0.6),
        "concavity_worst": random.uniform(0.0, 0.7),
        "concave points_worst": random.uniform(0.0, 0.4),
        "symmetry_worst": random.uniform(0.2, 0.5),
        "fractal_dimension_worst": random.uniform(0.05, 0.15)
    }

# ---- BUTTONS ----
col1, col2, col3 , col4 , col5 = st.columns(5)

with col1:
    if st.button("Load Benign"):
        st.session_state.data = benign_sample

with col2:
    if st.button("Load Malignant"):
        st.session_state.data = malignant_sample

with col3:
    if st.button("Intermediate Case"):
        st.session_state.data=intermediate_sample
with col4:
    if st.button("Random"):
        st.session_state.data=generate_random_sample()
with col5:
    if st.button("Clear"):
        st.session_state.data = {}

st.markdown("---")

# ---- TWO COLUMN LAYOUT ----
col1, col2 = st.columns(2)

with col1:
    st.markdown("### Mean Features")
    radius_mean = st.number_input("radius_mean", value=get_value("radius_mean"))
    texture_mean = st.number_input("texture_mean", value=get_value("texture_mean"))
    perimeter_mean = st.number_input("perimeter_mean", value=get_value("perimeter_mean"))
    area_mean = st.number_input("area_mean", value=get_value("area_mean"))
    smoothness_mean = st.number_input("smoothness_mean", value=get_value("smoothness_mean"))
    compactness_mean = st.number_input("compactness_mean", value=get_value("compactness_mean"))
    concavity_mean = st.number_input("concavity_mean", value=get_value("concavity_mean"))
    concave_points_mean = st.number_input("concave points_mean", value=get_value("concave points_mean"))
    symmetry_mean = st.number_input("symmetry_mean", value=get_value("symmetry_mean"))

    st.markdown("### SE Features")
    radius_se = st.number_input("radius_se", value=get_value("radius_se"))
    perimeter_se = st.number_input("perimeter_se", value=get_value("perimeter_se"))
    area_se = st.number_input("area_se", value=get_value("area_se"))
    compactness_se = st.number_input("compactness_se", value=get_value("compactness_se"))
    concavity_se = st.number_input("concavity_se", value=get_value("concavity_se"))
    concave_points_se = st.number_input("concave points_se", value=get_value("concave points_se"))
    symmetry_se = st.number_input("symmetry_se", value=get_value("symmetry_se"))
    fractal_dimension_se = st.number_input("fractal_dimension_se", value=get_value("fractal_dimension_se"))

with col2:
    st.markdown("### Worst Features")
    radius_worst = st.number_input("radius_worst", value=get_value("radius_worst"))
    texture_worst = st.number_input("texture_worst", value=get_value("texture_worst"))
    perimeter_worst = st.number_input("perimeter_worst", value=get_value("perimeter_worst"))
    area_worst = st.number_input("area_worst", value=get_value("area_worst"))
    smoothness_worst = st.number_input("smoothness_worst", value=get_value("smoothness_worst"))
    compactness_worst = st.number_input("compactness_worst", value=get_value("compactness_worst"))
    concavity_worst = st.number_input("concavity_worst", value=get_value("concavity_worst"))
    concave_points_worst = st.number_input("concave points_worst", value=get_value("concave points_worst"))
    symmetry_worst = st.number_input("symmetry_worst", value=get_value("symmetry_worst"))
    fractal_dimension_worst = st.number_input("fractal_dimension_worst", value=get_value("fractal_dimension_worst"))

st.markdown("---")

# ---- PREDICT ----
if st.button("Predict"):

    data = {
        "radius_mean": radius_mean,
        "texture_mean": texture_mean,
        "perimeter_mean": perimeter_mean,
        "area_mean": area_mean,
        "smoothness_mean": smoothness_mean,
        "compactness_mean": compactness_mean,
        "concavity_mean": concavity_mean,
        "concave points_mean": concave_points_mean,
        "symmetry_mean": symmetry_mean,

        "radius_se": radius_se,
        "perimeter_se": perimeter_se,
        "area_se": area_se,
        "compactness_se": compactness_se,
        "concavity_se": concavity_se,
        "concave points_se": concave_points_se,
        "symmetry_se": symmetry_se,
        "fractal_dimension_se": fractal_dimension_se,

        "radius_worst": radius_worst,
        "texture_worst": texture_worst,
        "perimeter_worst": perimeter_worst,
        "area_worst": area_worst,
        "smoothness_worst": smoothness_worst,
        "compactness_worst": compactness_worst,
        "concavity_worst": concavity_worst,
        "concave points_worst": concave_points_worst,
        "symmetry_worst": symmetry_worst,
        "fractal_dimension_worst": fractal_dimension_worst
    }

    try:
        response = requests.post("https://breast-cancer-api-st6j.onrender.com/predict", json=data)

        if response.status_code == 200:
            result = response.json()

            if result["prediction"] == "Malignant":
                st.error(f"Malignant")
            else:
                st.success(f"Benign")

                    # ---- PROGRESS BAR ----
            st.progress(result['confidence'])

            st.markdown(f"### Confidence: {result['confidence']*100:.2f}%")

            if result['confidence']<0.7:
                st.warning('Model is uncertain about this  prediction')
        else:
            st.error("API Error")

    except:
        st.error("Backend not running. Start FastAPI server.")