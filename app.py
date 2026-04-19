import streamlit as st

# Page config
st.set_page_config(page_title="Smart Farming AI", layout="centered")

# Title
st.title("🌾 Smart Farming AI")
st.markdown("### 🚀 AI Based Yield, Fertilizer & Price Prediction")

st.markdown("---")

# Inputs Section
st.subheader("📥 Enter Farm Details")

rainfall = st.slider("🌧 Rainfall (mm)", 50, 300, 120)
temperature = st.slider("🌡 Temperature (°C)", 15, 40, 25)
humidity = st.slider("💧 Humidity (%)", 30, 90, 60)

N = st.slider("🧪 Nitrogen (N)", 20, 150, 80)
P = st.slider("🧪 Phosphorus (P)", 10, 100, 40)
K = st.slider("🧪 Potassium (K)", 10, 120, 50)

pH = st.slider("⚖ Soil pH", 5.5, 8.5, 6.5)

arrival_volume = st.slider("🚚 Market Arrival Volume", 100, 1000, 500)
diesel_price = st.slider("⛽ Diesel Price", 80, 110, 90)

st.markdown("---")

# Prediction Button
if st.button("🚀 Predict"):

    # Yield Prediction
    yield_pred = rainfall*0.02 + temperature*0.5 + N*0.03 - pH*2

    # Fertilizer Recommendation
    if N < 50:
        fert = "High Nitrogen Fertilizer Needed"
    elif P < 30:
        fert = "High Phosphorus Fertilizer Needed"
    else:
        fert = "Balanced Fertilizer"

    # Price Prediction
    price = 2000 + yield_pred*10 - arrival_volume*0.5 + diesel_price*5

    st.markdown("## 📊 Results")

    st.success(f"🌾 Predicted Yield: {round(yield_pred,2)}")
    st.info(f"🧪 Fertilizer Recommendation: {fert}")
    st.warning(f"💰 Estimated Market Price: ₹{round(price,2)}")

st.markdown("---")
st.caption("Made with ❤️ using Streamlit")
