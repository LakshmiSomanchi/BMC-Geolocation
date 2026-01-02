import streamlit as st
import pandas as pd
from streamlit_js_eval import streamlit_js_eval

st.set_page_config(page_title="BMC Geolocation Collector", page_icon="📍", layout="centered")

# --- 1. DATASET SETUP ---
# Pre-loading your 65 BMCs
bmc_list = [
    [5381, "SHIRSATWADI", "SHIVKRUPA DUDH SAN KEND SHIRSATWADI", "INDAPUR"],
    [5408, "BHUINJ", "SHRIRAM DUDH SANKALAN & SHIT.BHUINJ", "WAI"],
    [38, "Gunaware", "MORESHWAR JEDHEWASTI", "PHALTAN"],
    [5488, "Borjaiwadi", "JYOTIRLING DUDH SANK KEN BORJAIWADI", "KOREGAON"],
    [5131, "DHAIGUDEMALA", "SHRIRAM DUDH PIMPRE DHAIGUDEMALA", "KHANDALA"],
    [5143, "Venkatesh Agro", "VENKATESH AGRO PADEGAON", "BARAMATI"],
    [5111, "Akole", "Sant Bhagva Baba Dudh Sankalan Kendra", "INDAPUR"],
    [5357, "Waghwasti", "SHREE DATTA DUDH SANKA. WAGHAWASTI", "BARAMATI"],
    [5445, "DEVULGOAN RAJE", "BHAIRAVNATH DEVULGOAN RAJE", "DAUND"],
    [5337, "Hingani", "JAY HANUMAN DUDH VITTHALNAGAR", "DAUND"],
    [5300, "Boribel", "SHIVTEJ DUDH PAWARWASTI BORIBEL", "DAUND"],
    [5376, "KHADAKI", "HINDAVI DAIRY FARM KHADAKI DAUND", "DAUND"],
    [5125, "SOMANTHALI", "SHREE DATTA SOMANTHALI", "PHALTAN"],
    [5573, "HIVRE", "VANGNA DUDH HIVRE COW MILK", "KOREGAON"],
    [5406, "Azadpur", "SHREE DATT MILK DAIRY AZADPUR", "KOREGAON"],
    [5347, "ANPATWADI", "SHRI DATT DOODH DAIRY ANPATWADI", "KOREGAON"],
    [5015, "SASTEWADI", "SHREE GANESH SASTEWADI BMC", "PHALTAN"],
    [5124, "MUNJAWADI", "SAYALI, MUNJAWADI", "PHALTAN"],
    [5115, "BARAD", "HANUMAN BARAD", "PHALTAN"],
    [5302, "BARAD", "SHIVSHANKAR DUDH BARAD", "PHALTAN"],
    [8, "HOL", "GOVIND DUDH SANKALAN KENDRA HOL", "PHALTAN"],
    [5493, "VAJEGOAN", "VAJUBAI VAJEGOAN COOLER", "PHALTAN"],
    [5590, "SONAWADI", "DURGADEVI DUDH ZIRAPVASTI COOLER", "PHALTAN"],
    [5145, "MATHACHIWADI", "GOKUL DUDH MATHACHIWADI", "PHALTAN"],
    [5142, "VIDNI", "VIGHNAHARTA VIDNI COOLER", "PHALTAN"],
    [5435, "VANJALE ( Dudhebabi)", "GOVIND MAHILA SWATKRANTI VANJALE", "PHALTAN"],
    [5398, "MIRDE", "JANAI DUDH SANKLAN KENDRA MIRDE", "PHALTAN"],
    [1205, "SADASHIVNAGAR", "GOVIND MILK & MILK PRODUCTS MMC SADASHIVNAGAR", "MALSHIRAS"],
    [1203, "MALSHIRAS", "GOVIND MILK AND MILK PRODUCTS MCC - MALSHIRAS", "MALSHIRAS"],
    [1204, "MOTEWADI", "GOVIND DUDH SANKALAN KENDRA - MOTEWADI", "MALSHIRAS"],
    [1211, "VANIMALA", "GOVIND MILK CC - VANEMALA", "MALSHIRAS"],
    [5022, "PACWAD", "JAY BHAVANI ANBHULEWADI", "MAN"],
    [5109, "KHADAKI", "SUPRIYA MILK", "MAN"],
    [5405, "BHALAWADI", "MAULI DUDH SANKALAN KENDR.BHALAWADI", "MAN"],
    [5490, "MOHI", "MAHALAXMI DUDH MOHI", "MAN"],
    [1201, "DAHIWADI", "BRAMHACHAITANYA MILK & MILK PRODUCTS PVT. LTD.", "MAN"],
    [5582, "MALWADI", "SHRI GANESH DUDH SAK VARKUTE MASWAD", "MAN"],
    [5647, "BHATKI", "JAGDAMBA DUDH BHATKI", "MAN"],
    [5413, "MARDI", "SUDARSHAN DUDH SANKALAN KEND.MARDI", "MAN"],
    [5556, "RANAND", "SHREE JAYHARI RANAND PHALTAN COOLER", "MAN"],
    [5301, "WAVARHIRE", "SHRINATH DUDH SANK.KENDRA WAVARHIRE", "MAN"],
    [5090, "GHADGEMALA", "JAY MHALLAR DUDH KALAJ", "PHALTAN"],
    [5112, "HINGANGAON", "BHAIRAVNATH DUDH HINGANGAON", "PHALTAN"],
    [5107, "SASWAD", "WAGHESHWARI SASWAD", "PHALTAN"],
    [5450, "SASWAD", "GOVIND DUDH SANKALAN KENDRA SASWAD", "PHALTAN"],
    [5404, "GIRAVI", "JAY TULJABHAVANI DUDH SAN.KEN.GIRVI", "PHALTAN"],
    [5085, "GIRAVI", "MEGHRAJ DUDH GIRVI", "PHALTAN"],
    [5283, "WATHARPHATA", "RAJMUDRA DUDH WATHARPHATA BMC", "PHALTAN"],
    [5320, "DALAWDI", "SHRINATH ROKADESHOR DALAWDI BMC", "PHALTAN"],
    [5049, "JINTI", "JITOBA BULK COOLER JINTI", "PHALTAN"],
    [5565, "MANDAVKHADAK", "BHAIRAVNATH MANDAVKHADAK COOLER", "PHALTAN"],
    [5306, "NAIKBOMWADI", "JAY HANUMAN BMC NAIKBOMWADI", "PHALTAN"],
    [5546, "PINGLEWASTI", "BHAIRAVNATH PINGLEWASTI", "BARAMATI"],
    [5188, "KARKHEL", "A.S.DAIRY FARM", "BARAMATI"],
    [5284, "PANCABIGA", "NIRAI DUDH SANKALAN KEND.PANCABIGA", "PHALTAN"],
    [5506, "DISKAL", "DISKAL SAMRUDHI DUDH UTPADAK MANDAL", "KHATAV"],
    [5489, "OZARDE", "SHREE KRUSHNAMAI SAH DUDH SANSTHA", "WAI"],
    [5447, "BHAVDHAN", "SWARAJ DUDH SANKALAN KENDRA BAVDHAN", "WAI"],
    [5334, "KULKJAI", "YOGESHWARI DUDH SANK.KEND.KULAKJAI", "MAN"],
    [5189, "LAXMI SOMANTHALI", "LAXMI DUDH DAIRY ALGUDEWADI COOLER", "PHALTAN"],
    [5149, "PIMPODE", "SHREE KRISHNA DAIRY, PIMPODE", "KOREGAON"],
    [5553, "SARKALWADI", "SHREE RAM DUDH SARKALWADIKOREGAON", "KOREGAON"],
    [5204, "NANDWAL", "SHIVSAI DUDH NANDVAL", "KOREGAON"],
    [5436, "JAWALI", "AJAY DUDH SANKALAN KENDRA JAWALI", "PHALTAN"],
    [5273, "PIRALE", "VISHNU NARAYAN DUDH", "MALSHIRAS"]
]

df_master = pd.DataFrame(bmc_list, columns=["MCC_CODE", "Village", "BMC_Name", "Tehsil"])

# --- 2. STATE MANAGEMENT ---
if 'collected_rows' not in st.session_state:
    st.session_state.collected_rows = []

# --- 3. UI LAYOUT ---
st.title("🥛 BMC Geolocation Collector")
st.info("Ensure GPS is ON. Open this app in Chrome/Safari on your mobile.")

# Selection box
selection = st.selectbox(
    "1. Select BMC Name", 
    range(len(df_master)), 
    format_func=lambda i: f"{df_master.iloc[i]['Village']} | {df_master.iloc[i]['BMC_Name']}"
)
target = df_master.iloc[selection]

st.divider()

# --- 4. IMPROVED GEOLOCATION LOGIC ---
st.subheader("2. Get Location")
capture_trigger = st.checkbox("Activate GPS Capture")

if capture_trigger:
    # We include enableHighAccuracy and a timeout to force the browser to try harder
    loc = streamlit_js_eval(
        js_expressions='navigator.geolocation.getCurrentPosition(s => {return {lat: s.coords.latitude, lon: s.coords.longitude}}, e => {return {err: e.message}}, {enableHighAccuracy:true, timeout:10000})',
        key='get_loc'
    )

    if loc:
        if 'err' in loc:
            st.error(f"Error: {loc['err']}")
            st.warning("Please check your browser settings and allow 'Location' for this site.")
        else:
            lat, lon = loc['lat'], loc['lon']
            st.success(f"📍 Coordinates Found: {lat}, {lon}")
            
            # Map Preview
            map_data = pd.DataFrame({'lat': [lat], 'lon': [lon]})
            st.map(map_data)

            if st.button("Save this Entry"):
                new_entry = {
                    "MCC_CODE": target["MCC_CODE"],
                    "Village": target["Village"],
                    "BMC_Name": target["BMC_Name"],
                    "Tehsil": target["Tehsil"],
                    "Latitude": lat,
                    "Longitude": lon
                }
                st.session_state.collected_rows.append(new_entry)
                st.success("✅ Entry saved to the temporary table below!")
    else:
        st.write("⌛ Fetching GPS signal... please wait.")

# --- 5. DATA TABLE & EXPORT ---
if st.session_state.collected_rows:
    st.divider()
    st.subheader("3. Collected Data List")
    temp_df = pd.DataFrame(st.session_state.collected_rows)
    st.dataframe(temp_df)
    
    csv_data = temp_df.to_csv(index=False).encode('utf-8')
    st.download_button(
        label="📥 Download Collected Data (CSV)",
        data=csv_data,
        file_name="bmc_collected_locations.csv",
        mime="text/csv"
    )
