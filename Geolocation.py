import streamlit as st
import pandas as pd
from streamlit_js_eval import streamlit_js_eval

st.set_page_config(page_title="BMC Geolocation Mapper", page_icon="📍")

# 1. The Full Dataset
data = [
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
    [5553, "SARKALWADI", "SHREE RAM DUDH SARKALWADI", "KOREGAON"],
    [5204, "NANDWAL", "SHIVSAI DUDH NANDVAL", "KOREGAON"],
    [5436, "JAWALI", "AJAY DUDH SANKALAN KENDRA JAWALI", "PHALTAN"],
    [5273, "PIRALE", "VISHNU NARAYAN DUDH", "MALSHIRAS"]
]

df = pd.DataFrame(data, columns=["MCC_CODE", "Village", "BMC_Name", "Tehsil"])

# Initialize session state for storage
if 'collection' not in st.session_state:
    st.session_state.collection = []

st.title("🥛 BMC Geolocation Collector")
st.write("Use this app while physically present at the BMC to record coordinates.")

# 2. Selection
selection = st.selectbox("Select BMC to Geo-Tag", range(len(df)), 
                         format_func=lambda i: f"{df.iloc[i]['Village']} | {df.iloc[i]['BMC_Name']}")

target_bmc = df.iloc[selection]

# 3. Geolocation Logic
loc = streamlit_js_eval(js_expressions='navigator.geolocation.getCurrentPosition(success => {return {lat: success.coords.latitude, lon: success.coords.longitude}})', key='get_loc')

if loc:
    lat, lon = loc['lat'], loc['lon']
    st.success(f"📍 Location Found: {lat}, {lon}")
    
    if st.button("Save this Location"):
        entry = {
            "MCC_CODE": target_bmc["MCC_CODE"],
            "Village": target_bmc["Village"],
            "BMC_Name": target_bmc["BMC_Name"],
            "Latitude": lat,
            "Longitude": lon
        }
        st.session_state.collection.append(entry)
        st.balloons()
        st.write("Saved to list!")
else:
    st.warning("Waiting for GPS signal... Please ensure Location Access is allowed in your browser.")

# 4. Results & Download
if st.session_state.collection:
    st.divider()
    st.subheader("Collected Data")
    res_df = pd.DataFrame(st.session_state.collection)
    st.dataframe(res_df)
    
    csv = res_df.to_csv(index=False).encode('utf-8')
    st.download_button("📥 Download Final CSV", data=csv, file_name="bmc_geolocations.csv", mime="text/csv")
