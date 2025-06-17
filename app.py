import streamlit as st

st.set_page_config(page_title="Forward P/E Calculator", layout="centered")

st.title("📈 Forward P/E & Fair Value Calculator")

# --- Input fields
cmp = st.number_input("Enter CMP (₹)", min_value=1.0, value=405.0, step=1.0)
current_eps = st.number_input("Enter Current EPS (₹)", min_value=0.0, value=17.6, step=0.1)
eps_growth = st.number_input("Expected EPS Growth (%)", min_value=0.0, value=31.0, step=0.5)

# --- Calculations
fy26_eps = current_eps * (1 + eps_growth / 100)
forward_pe = cmp / fy26_eps

# --- Display results
st.markdown("### 🧮 Results")
st.write(f"**FY26 EPS (Est.)**: ₹{fy26_eps:.2f}")
st.write(f"**Forward P/E**: {forward_pe:.2f}")

# --- Fair value estimation
st.markdown("### 🎯 Fair Value Range")

target_pe_values = [18, 20, 22]

for pe in target_pe_values:
    fair_price = fy26_eps * pe
    st.write(f"🔹 Target P/E {pe}: ₹{fair_price:.2f}")

# --- Note
st.markdown("---")
st.info("This tool assumes 1-year forward EPS. Adjust growth % as needed for multi-year outlook.")
