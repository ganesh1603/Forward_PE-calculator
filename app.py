import streamlit as st

st.set_page_config(page_title="Forward P/E Calculator", layout="centered")
st.title("📊 Forward P/E & Fair Value Estimator")

# --- Inputs
cmp = st.number_input("Current Market Price (₹)", min_value=1.0, value=405.0, step=1.0)
current_pe = st.number_input("Current P/E", min_value=1.0, value=23.0, step=0.1)
current_eps = st.number_input("Current EPS (₹)", min_value=0.0, value=17.6, step=0.1)
eps_growth = st.number_input("Expected EPS Growth (%)", min_value=0.0, value=31.0, step=0.5)

# --- Calculate on button press
if st.button("Calculate"):
    # EPS projection
    fy26_eps = current_eps * (1 + eps_growth / 100)
    
    # Forward P/E
    forward_pe = cmp / fy26_eps

    # Fair values at different multiples
    target_pes = [18, 20, 22]
    fair_values = {pe: fy26_eps * pe for pe in target_pes}

    # --- Display
    st.markdown("### 📈 Results")
    st.write(f"**Projected FY26 EPS**: ₹{fy26_eps:.2f}")
    st.write(f"**Forward P/E** (CMP ₹{cmp} / EPS ₹{fy26_eps:.2f}): **{forward_pe:.2f}**")

    st.markdown("### 🎯 Fair Value Estimates")
    for pe, price in fair_values.items():
        st.write(f"🔹 At P/E {pe}: ₹{price:.2f}")

    st.markdown("---")
    st.success("Done! You can adjust inputs to explore different scenarios.")
