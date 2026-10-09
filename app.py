import streamlit as st
import streamlit.components.v1 as components

# =====================================================================
# DIGITAL WRISTBAND FOR FOOD MANAGEMENT — CODESPACE PRODUCTION FRAMEWORK
# =====================================================================

st.set_page_config(page_title="Digital Wristband Simulator", page_icon="⌚", layout="wide")

# Main Application Title
st.title("🍽️ Digital Wristband for Food Management")
st.subheader("Simulation Environment: Wearable Hardware Screen Display")
st.write(
    "This app demonstrates the software logic of our wearable wristband project. "
    "Adjust the user profile year-by-year on the left to watch the slim wristband display "
    "recalculate and change portions for every single year of age."
)

st.markdown("---")

# Split the application interface into two clean operational columns
col_sensor_inputs, col_wristband_screen = st.columns(2)

with col_sensor_inputs:
    st.header("📥 Simulated Entry Kiosk Inputs")
    st.write("Configure the guest parameters to transmit live initial states to the wearable device:")

    # 1. Primary Profile Configurations (Every single year will drive calculations)
    age = st.slider("Guest Age (Years)", min_value=5, max_value=85, value=25)
    gender = st.selectbox("Gender", ["Male", "Female"])
    
    # 2. Dynamic Age-to-Vitals Simulation Engine (Rapidly alters readings based on biology)
    if age <= 12:
        simulated_temp = 99.2 + ((12 - age) * 0.05)
    elif age >= 65:
        simulated_temp = 97.4 - ((age - 65) * 0.03)
    else:
        simulated_temp = 98.6
        
    if gender == "Male":
        base_systolic = 118 + (age * 0.35)
        base_diastolic = 78 + (age * 0.15)
    else:
        base_systolic = 114 + (age * 0.40)
        base_diastolic = 74 + (age * 0.18)

    # 3. Live Transmitted Vitals Configuration
    st.markdown("#### ⌚ Live Transmitted Vitals")
    body_temp = st.slider("Simulated Sensor Temperature (°F)", min_value=96.0, max_value=102.0, value=float(round(simulated_temp, 1)), step=0.1)
    
    resting_systolic = int(round(base_systolic))
    resting_diastolic = int(round(base_diastolic))
    
    systolic_bp = st.slider(
        "Simulated Systolic Blood Pressure (mmHg)", 
        min_value=90, 
        max_value=170, 
        value=resting_systolic
    )
    
    if systolic_bp > (resting_systolic + 15):
        st.info(f"⚡ **Exertion Detected:** Spiked Blood Pressure ({systolic_bp} mmHg) indicates active movement/dancing.")
    else:
        st.caption(f"ℹ️ Standard calculated resting baseline for this profile is around {resting_systolic}/{resting_diastolic} mmHg.")

    # 4. Crowd Health Distribution Selector (Simulating 1-2 people out of 100)
    st.markdown("---")
    st.markdown("#### 🤒 Crowd Health Status Selector")
    health_condition = st.selectbox(
        "Current Daily Physical State", 
        ["Perfectly Healthy (98% of Guests)", "Mild Fever (1-2% Incident Rate)", "Seasonal Cough & Cold (1-2% Incident Rate)"]
    )

    # 5. Core Methodology Side Reference Panel
    st.markdown("### ℹ️ Core Baseline Reference")
    st.info(
        f"**System Logic Note:** The underlying algorithm initiates a standard biological capacity calculation "
        f"based on target gender averages (450g for Males and 380g for Females). The logic then shifts "
        f"dynamically according to age profiles, temperature spikes, blood pressure exertion levels, and sickness variables "
        f"to output simple serving counts."
    )

with col_wristband_screen:
    st.header("⌚ Simulated Wristband Interface")
    st.write("This graphical console simulates the real-time slim vertical display on the physical wristband:")

    # =====================================================================
    # CONTINUOUS ARITHMETIC CORE — SYSTEM CHANGES ON EVERY SINGLE AGE YEAR
    # =====================================================================
    gender_factor = 1.0 if gender == "Male" else 0.84

    if age <= 20:
        age_factor = 0.4 + (age * 0.03) 
    elif age <= 50:
        age_factor = 1.0 - ((age - 20) * 0.004)
    else:
        age_factor = 0.88 - ((age - 50) * 0.008)

    live_multiplier = gender_factor * age_factor

    bp_delta = max(0, systolic_bp - resting_systolic)
    if bp_delta > 0:
        live_multiplier *= (1.0 + (bp_delta * 0.012))

    rice_sickness_drop = 1.0
    sweet_sickness_drop = 1.0
    
    status_label = "NORMAL"
    if health_condition == "Mild Fever (1-2% Incident Rate)":
        status_label = "FEVER"
        live_multiplier *= 0.82
        rice_sickness_drop = 0.55  
    elif health_condition == "Seasonal Cough & Cold (1-2% Incident Rate)":
        status_label = "COLD"
        sweet_sickness_drop = 0.45 

    if age <= 12 and status_label == "NORMAL":
        status_label = "JUNIOR"
    elif age >= 65 and status_label == "NORMAL":
        status_label = "SENIOR"
    elif bp_delta > 15 and status_label == "NORMAL":
        status_label = "DANCE ACT"

    rice_value = round(2.0 * live_multiplier * rice_sickness_drop, 1)
    curry_value = round(1.8 * live_multiplier, 1)
    fry_value = round(1.5 * live_multiplier, 1)
    
    bread_value = max(1, round(2.0 * live_multiplier))
    starter_value = max(1, round(3.0 * live_multiplier))
    
    sweet_value = round(1.0 * live_multiplier * sweet_sickness_drop, 1)
    ice_cream_value = round(1.0 * live_multiplier * sweet_sickness_drop, 1)

    rice_value = max(0.4, rice_value)
    curry_value = max(0.4, curry_value)
    fry_value = max(0.4, fry_value)
    sweet_value = max(0.2, sweet_value)
    ice_cream_value = max(0.2, ice_cream_value)

    # =====================================================================
    # SLIM OVERSYNC MOCKUP BLOCK EXECUTED THROUGH ISOLATED HTML COMPONENT
    # =====================================================================
    html_template = f"""
    <div style="background-color: #0f0f0f; border: 8px solid #cbb295; border-radius: 40px; padding: 25px 15px; font-family: 'Courier New', monospace; color: #00FF00; box-shadow: 8px 8px 25px rgba(0,0,0,0.6); max-width: 250px; margin: auto; text-align: center;">
        
        <div style="border-bottom: 1px solid #333; padding-bottom: 10px; margin-bottom: 15px;">
            <span style="font-size: 11px; color: #888; letter-spacing: 2px;">BAND v1.0</span><br>
            <span style="font-size: 14px; font-weight: bold; color: #FFFF00; letter-spacing: 1px;">[{status_label}]</span>
        </div>

        <div style="font-size: 13px; color: #FFFFFF; text-align: left; padding-left: 10px; margin-bottom: 20px; line-height: 1.8;">
            🌡️ <span style="color: #888;">TMP:</span> <span style="color: #00FF00; font-weight: bold;">{body_temp}°F</span><br>
            💓 <span style="color: #888;">VTL:</span> <span style="color: #00FF00; font-weight: bold;">{systolic_bp}/{resting_diastolic}</span><br>
            👤 <span style="color: #888;">USR:</span> <span style="color: #00FF00; font-weight: bold;">{gender[:1]}-{age}Yrs</span>
        </div>

        <div style="background-color: #1a1a1a; border-radius: 15px; padding: 15px 10px; border: 1px solid #2a2a2a; text-align: left;">
            <p style="text-align: center; margin: 0 0 10px 0; font-size: 12px; color: #00FFFF; font-weight: bold; letter-spacing: 1px;">📋 MENU TARGETS</p>
            <div style="font-size: 12px; line-height: 1.8; color: #E0E0E0;">
                🍚 CHK BIRYANI: <span style="color: #FFFF00; font-weight: bold;">{rice_value} Scp</span><br>
                🥘 CHK CURRY:   <span style="color: #FFFF00; font-weight: bold;">{curry_value} Ldl</span><br>
                🥩 MTN FRY:     <span style="color: #FFFF00; font-weight: bold;">{fry_value} Pcs</span><br>
                🫓 BREAD/NAAN:  <span style="color: #FFFF00; font-weight: bold;">{bread_value} Pcs</span><br>
                🍨 WED SWEET:   <span style="color: #FFFF00; font-weight: bold;">{sweet_value} Srv</span><br>
                🍦 ICE CREAM:   <span style="color: #FFFF00; font-weight: bold;">{ice_cream_value} Scp</span>
            </div>
        </div>

        <div style="margin-top: 20px; font-size: 9px; color: #555; letter-spacing: 2px;">
            • NFC ONLINE •
        </div>
    </div>
    """
    
    # Executing isolation call structure natively to completely bypass markdown code-parsing error drops
    components.html(html_template, height=450)
    
    st.markdown("<br>", unsafe_allow_html=True)
    st.caption(
        "💡 **Simulation Verification:** Move the age slider slowly year-by-year (e.g. 20, 21, 22, 23). "
        "Notice how the Chicken Biryani scoops and Mutton Fry pieces now shift fluidly on every single step!"
    )
