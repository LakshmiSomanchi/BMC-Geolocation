import streamlit as st
import pandas as pd
from streamlit_geolocation import streamlit_geolocation

st.set_page_config(page_title="BMC Geo-Collector", page_icon="📍")

# --- 1. THE DATASET ---
bmc_list = [
    [5381, "SHIRSATWADI", "SHIVKRUPA DUDH SAN KEND SHIRSATWADI", "INDAPUR"],
    [5408, "BHUINJ", "SHRIRAM DUDH SANKALAN & SHIT.BHUINJ", "WAI"],
    [38, "Gunaware", "MORESHWAR JEDHEWASTI", "PHALTAN"],
    [5488, "Borjaiwadi", "JYOTIRLING DUDH SANK KEN BORJAIWADI", "KOREGAON"],
    [5131, "DHAIGUDEMALA", "SHRIRAM DUDH PIMPRE DHAIGUDEMALAKHANDALA", "KHANDALA"],
    [5143, "Venkatesh Agro", "VENKATESH AGRO PADEGAONBARAMATI", "BARAMATI"],
    [5111, "Akole", "Sant Bhagva Baba Dudh Sankalan KendraINDAPUR", "INDAPUR"],
    [5357, "Waghwasti", "SHREE DATTA DUDH SANKA. WAGHAWASTIBARAMATI", "BARAMATI"],
    [5445, "DEVULGOAN RAJE", "BHAIRAVNATH DEVULGOAN RAJEDAUND", "DAUND"],
    [5337, "Hingani", "JAY HANUMAN DUDH VITTHALNAGARDAUND", "DAUND"],
    [5300, "Boribel", "SHIVTEJ DUDH PAWARWASTI BORIBELDAUND", "DAUND"],
    [5376, "KHADAKI", "HINDAVI DAIRY FARM KHADAKI DAUNDDAUND", "DAUND"],
    [5125, "SOMANTHALI", "SHREE DATTA SOMANTHALIPHALTAN", "PHALTAN"],
    [5573, "HIVRE", "VANGNA DUDH HIVRE COW MILKKOREGAON", "KOREGAON"],
    [5406, "Azadpur", "SHREE DATT MILK DAIRY AZADPURKOREGAON", "KOREGAON"],
    [5347, "ANPATWADI", "SHRI DATT DOODH DAIRY ANPATWADIKOREGAON", "KOREGAON"],
    [5015, "SASTEWADI", "SHREE GANESH SASTEWADI BMCPHALTAN", "PHALTAN"],
    [5124, "MUNJAWADI", "SAYALI, MUNJAWADIPHALTAN", "PHALTAN"],
    [5115, "BARAD", "HANUMAN BARADPHALTAN", "PHALTAN"],
    [5302, "BARAD", "SHIVSHANKAR DUDH BARADPHALTAN", "PHALTAN"],
    [8, "HOL", "GOVIND DUDH SANKALAN KENDRA HOLPHALTAN", "PHALTAN"],
    [5493, "VAJEGOAN", "VAJUBAI VAJEGOAN COOLERPHALTAN", "PHALTAN"],
    [5590, "SONAWADI", "DURGADEVI DUDH ZIRAPVASTI COOLERPHALTAN", "PHALTAN"],
    [5145, "MATHACHIWADI", "GOKUL DUDH MATHACHIWADIPHALTAN", "PHALTAN"],
    [5142, "VIDNI", "VIGHNAHARTA VIDNI COOLERPHALTAN", "PHALTAN"],
    [5435, "VANJALE ( Dudhebabi)", "GOVIND MAHILA SWATKRANTI VANJALEPHALTAN", "PHALTAN"],
    [5398, "MIRDE", "JANAI DUDH SANKLAN KENDRA MIRDEPHALTAN", "PHALTAN"],
    [1205, "SADASHIVNAGAR", "GOVIND MILK & MILK PRODUCTS MMC SADASHIVNAGARMALSHIRAS", "MALSHIRAS"],
    [1203, "MALSHIRAS", "GOVIND MILK AND MILK PRODUCTS MCC - MALSHIRASMALSHIRAS", "MALSHIRAS"],
    [1204, "MOTEWADI", "GOVIND DUDH SANKALAN KENDRA - MOTEWADI (GOKULNAGAR)MALSHIRAS", "MALSHIRAS"],
    [1211, "VANIMALA", "GOVIND MILK CC - VANEMALAMALSHIRAS", "MALSHIRAS"],
    [5022, "PACWAD", "JAY BHAVANI ANBHULEWADIMAN", "MAN"],
    [5109, "KHADAKI", "SUPRIYA MILKMAN", "MAN"],
    [5405, "BHALAWADI", "MAULI DUDH SANKALAN KENDR.BHALAWADIMAN", "MAN"],
    [5490, "MOHI", "MAHALAXMI DUDH MOHIMAN", "MAN"],
    [1201, "DAHIWADI", "BRAMHACHAITANYA MILK & MILK PRODUCTS PVT. LTD.MAN", "MAN"],
    [5582, "MALWADI", "SHRI GANESH DUDH SAK VARKUTE MASWADMAN", "MAN"],
    [5647, "BHATKI", "JAGDAMBA DUDH BHATKIMAN", "MAN"],
    [5413, "MARDI", "SUDARSHAN DUDH SANKALAN KEND.MARDIMAN", "MAN"],
    [5556, "RANAND", "SHREE JAYHARI RANAND PHALTAN COOLERMAN", "MAN"],
    [5301, "WAVARHIRE", "SHRINATH DUDH SANK.KENDRA WAVARHIREMAN", "MAN"],
    [5090, "GHADGEMALA", "JAY MHALLAR DUDH KALAJPHALTAN", "PHALTAN"],
    [5112, "HINGANGAON", "BHAIRAVNATH DUDH HINGANGAONPHALTAN", "PHALTAN"],
    [5107, "SASWAD", "WAGHESHWARI SASWADPHALTAN", "PHALTAN"],
    [5450, "SASWAD", "GOVIND DUDH SANKALAN KENDRA SASWADPHALTAN", "PHALTAN"],
    [5404, "GIRAVI", "JAY TULJABHAVANI DUDH SAN.KEN.GIRVIPHALTAN", "PHALTAN"],
    [5085, "GIRAVI", "MEGHRAJ DUDH GIRVIPHALTAN", "PHALTAN"],
    [5283, "WATHARPHATA", "RAJMUDRA DUDH WATHARPHATA BMCPHALTAN", "PHALTAN"],
    [5320, "DALAWDI", "SHRINATH ROKADESHOR DALAWDI BMCPHALTAN", "PHALTAN"],
    [5049, "JINTI", "JITOBA BULK COOLER JINTIPHALTAN", "PHALTAN"],
    [5565, "MANDAVKHADAK", "BHAIRAVNATH MANDAVKHADAK COOLERPHALTAN", "PHALTAN"],
    [5306, "NAIKBOMWADI", "JAY HANUMAN BMC NAIKBOMWADIPHALTAN", "PHALTAN"],
    [5546, "PINGLEWASTI", "BHAIRAVNATH PINGLEWASTIBARAMATI", "BARAMATI"],
    [5188, "KARKHEL", "A.S.DAIRY FARMBARAMATI", "BARAMATI"],
    [5284, "PANCABIGA", "NIRAI DUDH SANKALAN KEND.PANCABIGAPHALTAN", "PHALTAN"],
    [5506, "DISKAL", "DISKAL SAMRUDHI DUDH UTPADAK MANDALKHATAV", "KHATAV"],
    [5489, "OZARDE", "SHREE KRUSHNAMAI SAH DUDH SANSTHAWAI", "WAI"],
    [5447, "BHAVDHAN", "SWARAJ DUDH SANKALAN KENDRA BAVDHANWAI", "WAI"],
    [5334, "KULKJAI", "YOGESHWARI DUDH SANK.KEND.KULAKJAIMAN", "MAN"],
    [5189, "LAXMI SOMANTHALI", "LAXMI DUDH DAIRY ALGUDEWADI COOLERPHALTAN", "PHALTAN"],
    [5149, "PIMPODE", "SHREE KRISHNA DAIRY, PIMPODEKOREGAON", "KOREGAON"],
    [5553, "SARKALWADI", "SHREE RAM DUDH SARKALWADIKOREGAON", "KOREGAON"],
    [5204, "NANDWAL", "SHIVSAI DUDH NANDWALKOREGAON", "KOREGAON"],
    [5436, "JAWALI", "AJAY DUDH SANKALAN KENDRA JAWALIPHALTAN", "PHALTAN"],
    [5273, "PIRALE", "VISHNU NARAYAN DUDHMALSHIRAS", "MALSHIRAS"]
]

df_master = pd.DataFrame(bmc_list, columns=["MCC_CODE", "Village", "BMC_Name", "Tehsil"])

# Session state to keep collected data across reruns
if 'data_log' not in st.session_state:
    st.session_state.data_log = []

st.title("📍 BMC Geolocation Collector")

# --- Step 1: Select BMC ---
selection = st.selectbox(
    "1. Select the BMC", 
    range(len(df_master)), 
    format_func=lambda i: f"{df_master.iloc[i]['Village']} | {df_master.iloc[i]['BMC_Name']}"
)
selected_row = df_master.iloc[selection]

# --- Step 2: Get Location ---
st.subheader("2. Get Current Coordinates")
st.write("Click the button below to fetch GPS data from your phone.")
location = streamlit_geolocation()

if location['latitude'] is not None:
    lat = location['latitude']
    lon = location['longitude']
    
    st.success(f"Location Captured: Lat {lat}, Lon {lon}")
    
    # --- Step 3: Save Entry ---
    if st.button("Save this Location"):
        entry = {
            "MCC_CODE": selected_row["MCC_CODE"],
            "Village": selected_row["Village"],
            "BMC_Name": selected_row["BMC_Name"],
            "Tehsil": selected_row["Tehsil"],
            "Latitude": lat,
            "Longitude": lon
        }
        st.session_state.data_log.append(entry)
        st.toast("Entry saved locally!")

# --- Step 4: Show Table and Download ---
if st.session_state.data_log:
    st.divider()
    st.subheader("Collected List")
    log_df = pd.DataFrame(st.session_state.data_log)
    st.table(log_df)
    
    # Download Logic
    csv = log_df.to_csv(index=False).encode('utf-8')
    st.download_button(
        label="📥 Download Geolocation CSV",
        data=csv,
        file_name="bmc_geolocations.csv",
        mime="text/csv"
    )
else:
    st.info("No locations saved yet. Capture a location and click 'Save'.")
