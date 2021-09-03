from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import StandardScaler
import numpy as np
le1=LabelEncoder()
le2=LabelEncoder()
le3=LabelEncoder()
le4=LabelEncoder()
scaler_x=StandardScaler()
scaler_y=StandardScaler()
le1.classes_=['Andaman and Nicobar Islands', 'Andhra Pradesh',
       'Arunachal Pradesh', 'Assam', 'Bihar', 'Chandigarh',
       'Chhattisgarh', 'Dadra and Nagar Haveli', 'Goa', 'Gujarat',
       'Haryana', 'Himachal Pradesh', 'Jammu and Kashmir ', 'Jharkhand',
       'Karnataka', 'Kerala', 'Madhya Pradesh', 'Maharashtra', 'Manipur',
       'Meghalaya', 'Mizoram', 'Nagaland', 'Odisha', 'Puducherry',
       'Punjab', 'Rajasthan', 'Sikkim', 'Tamil Nadu', 'Telangana ',
       'Tripura', 'Uttar Pradesh', 'Uttarakhand', 'West Bengal']
le2.classes_=['24 PARAGANAS NORTH', '24 PARAGANAS SOUTH', 'ADILABAD',
       'AGAR MALWA', 'AGRA', 'AHMADABAD', 'AHMEDNAGAR', 'AIZAWL', 'AJMER',
       'AKOLA', 'ALAPPUZHA', 'ALIGARH', 'ALIRAJPUR', 'ALLAHABAD',
       'ALMORA', 'ALWAR', 'AMBALA', 'AMBEDKAR NAGAR', 'AMETHI',
       'AMRAVATI', 'AMRELI', 'AMRITSAR', 'AMROHA', 'ANAND', 'ANANTAPUR',
       'ANANTNAG', 'ANJAW', 'ANUGUL', 'ANUPPUR', 'ARARIA', 'ARIYALUR',
       'ARWAL', 'ASHOKNAGAR', 'AURAIYA', 'AURANGABAD', 'AZAMGARH',
       'BADGAM', 'BAGALKOT', 'BAGESHWAR', 'BAGHPAT', 'BAHRAICH', 'BAKSA',
       'BALAGHAT', 'BALANGIR', 'BALESHWAR', 'BALLIA', 'BALOD',
       'BALODA BAZAR', 'BALRAMPUR', 'BANAS KANTHA', 'BANDA', 'BANDIPORA',
       'BANGALORE RURAL', 'BANKA', 'BANKURA', 'BANSWARA', 'BARABANKI',
       'BARAMULLA', 'BARAN', 'BARDHAMAN', 'BAREILLY', 'BARGARH', 'BARMER',
       'BARNALA', 'BARPETA', 'BARWANI', 'BASTAR', 'BASTI', 'BATHINDA',
       'BEED', 'BEGUSARAI', 'BELGAUM', 'BELLARY', 'BEMETARA',
       'BENGALURU URBAN', 'BETUL', 'BHADRAK', 'BHAGALPUR', 'BHANDARA',
       'BHARATPUR', 'BHARUCH', 'BHAVNAGAR', 'BHILWARA', 'BHIND',
       'BHIWANI', 'BHOJPUR', 'BHOPAL', 'BIDAR', 'BIJAPUR', 'BIJNOR',
       'BIKANER', 'BILASPUR', 'BIRBHUM', 'BISHNUPUR', 'BOKARO',
       'BONGAIGAON', 'BOUDH', 'BUDAUN', 'BULANDSHAHR', 'BULDHANA',
       'BUNDI', 'BURHANPUR', 'BUXAR', 'CACHAR', 'CHAMARAJANAGAR',
       'CHAMBA', 'CHAMOLI', 'CHAMPAWAT', 'CHAMPHAI', 'CHANDAULI',
       'CHANDEL', 'CHANDIGARH', 'CHANDRAPUR', 'CHANGLANG', 'CHATRA',
       'CHHATARPUR', 'CHHINDWARA', 'CHIKBALLAPUR', 'CHIKMAGALUR',
       'CHIRANG', 'CHITRADURGA', 'CHITRAKOOT', 'CHITTOOR', 'CHITTORGARH',
       'CHURACHANDPUR', 'CHURU', 'COIMBATORE', 'COOCHBEHAR', 'CUDDALORE',
       'CUTTACK', 'DADRA AND NAGAR HAVELI', 'DAKSHIN KANNAD', 'DAMOH',
       'DANG', 'DANTEWADA', 'DARBHANGA', 'DARJEELING', 'DARRANG', 'DATIA',
       'DAUSA', 'DAVANGERE', 'DEHRADUN', 'DEOGARH', 'DEOGHAR', 'DEORIA',
       'DEWAS', 'DHALAI', 'DHAMTARI', 'DHANBAD', 'DHAR', 'DHARMAPURI',
       'DHARWAD', 'DHEMAJI', 'DHENKANAL', 'DHOLPUR', 'DHUBRI', 'DHULE',
       'DIBANG VALLEY', 'DIBRUGARH', 'DIMA HASAO', 'DIMAPUR',
       'DINAJPUR DAKSHIN', 'DINAJPUR UTTAR', 'DINDIGUL', 'DINDORI',
       'DODA', 'DOHAD', 'DUMKA', 'DUNGARPUR', 'DURG', 'EAST DISTRICT',
       'EAST GARO HILLS', 'EAST GODAVARI', 'EAST JAINTIA HILLS',
       'EAST KAMENG', 'EAST KHASI HILLS', 'EAST SIANG', 'EAST SINGHBUM',
       'ERNAKULAM', 'ERODE', 'ETAH', 'ETAWAH', 'FAIZABAD', 'FARIDABAD',
       'FARIDKOT', 'FARRUKHABAD', 'FATEHABAD', 'FATEHGARH SAHIB',
       'FATEHPUR', 'FAZILKA', 'FIROZABAD', 'FIROZEPUR', 'GADAG',
       'GADCHIROLI', 'GAJAPATI', 'GANDERBAL', 'GANDHINAGAR', 'GANGANAGAR',
       'GANJAM', 'GARHWA', 'GARIYABAND', 'GAUTAM BUDDHA NAGAR', 'GAYA',
       'GHAZIABAD', 'GHAZIPUR', 'GIRIDIH', 'GOALPARA', 'GODDA',
       'GOLAGHAT', 'GOMATI', 'GONDA', 'GONDIA', 'GOPALGANJ', 'GORAKHPUR',
       'GULBARGA', 'GUMLA', 'GUNA', 'GUNTUR', 'GURDASPUR', 'GURGAON',
       'GWALIOR', 'HAILAKANDI', 'HAMIRPUR', 'HANUMANGARH', 'HAPUR',
       'HARDA', 'HARDOI', 'HARIDWAR', 'HASSAN', 'HATHRAS', 'HAVERI',
       'HAZARIBAGH', 'HINGOLI', 'HISAR', 'HOOGHLY', 'HOSHANGABAD',
       'HOSHIARPUR', 'HOWRAH', 'HYDERABAD', 'IDUKKI', 'IMPHAL EAST',
       'IMPHAL WEST', 'INDORE', 'JABALPUR', 'JAGATSINGHAPUR', 'JAIPUR',
       'JAISALMER', 'JAJAPUR', 'JALANDHAR', 'JALAUN', 'JALGAON', 'JALNA',
       'JALORE', 'JALPAIGURI', 'JAMMU', 'JAMNAGAR', 'JAMTARA', 'JAMUI',
       'JANJGIR-CHAMPA', 'JASHPUR', 'JAUNPUR', 'JEHANABAD', 'JHABUA',
       'JHAJJAR', 'JHALAWAR', 'JHANSI', 'JHARSUGUDA', 'JHUNJHUNU', 'JIND',
       'JODHPUR', 'JORHAT', 'JUNAGADH', 'KABIRDHAM', 'KACHCHH', 'KADAPA',
       'KAIMUR (BHABUA)', 'KAITHAL', 'KALAHANDI', 'KAMRUP',
       'KAMRUP METRO', 'KANCHIPURAM', 'KANDHAMAL', 'KANGRA', 'KANKER',
       'KANNAUJ', 'KANNIYAKUMARI', 'KANNUR', 'KANPUR DEHAT',
       'KANPUR NAGAR', 'KAPURTHALA', 'KARAIKAL', 'KARAULI',
       'KARBI ANGLONG', 'KARGIL', 'KARIMGANJ', 'KARIMNAGAR', 'KARNAL',
       'KARUR', 'KASARAGOD', 'KASGANJ', 'KATHUA', 'KATIHAR', 'KATNI',
       'KAUSHAMBI', 'KENDRAPARA', 'KENDUJHAR', 'KHAGARIA', 'KHAMMAM',
       'KHANDWA', 'KHARGONE', 'KHEDA', 'KHERI', 'KHORDHA', 'KHOWAI',
       'KINNAUR', 'KIPHIRE', 'KISHANGANJ', 'KISHTWAR', 'KODAGU',
       'KODERMA', 'KOHIMA', 'KOKRAJHAR', 'KOLAR', 'KOLASIB', 'KOLHAPUR',
       'KOLLAM', 'KONDAGAON', 'KOPPAL', 'KORAPUT', 'KORBA', 'KOREA',
       'KOTA', 'KOTTAYAM', 'KOZHIKODE', 'KRISHNA', 'KRISHNAGIRI',
       'KULGAM', 'KULLU', 'KUPWARA', 'KURNOOL', 'KURUKSHETRA',
       'KURUNG KUMEY', 'KUSHI NAGAR', 'LAHUL AND SPITI', 'LAKHIMPUR',
       'LAKHISARAI', 'LALITPUR', 'LATEHAR', 'LATUR', 'LAWNGTLAI',
       'LOHARDAGA', 'LOHIT', 'LONGDING', 'LONGLENG',
       'LOWER DIBANG VALLEY', 'LOWER SUBANSIRI', 'LUCKNOW', 'LUDHIANA',
       'LUNGLEI', 'MADHEPURA', 'MADHUBANI', 'MADURAI', 'MAHARAJGANJ',
       'MAHASAMUND', 'MAHBUBNAGAR', 'MAHE', 'MAHENDRAGARH', 'MAHESANA',
       'MAHOBA', 'MAINPURI', 'MALAPPURAM', 'MALDAH', 'MALKANGIRI',
       'MAMIT', 'MANDI', 'MANDLA', 'MANDSAUR', 'MANDYA', 'MANSA',
       'MARIGAON', 'MATHURA', 'MAU', 'MAYURBHANJ', 'MEDAK',
       'MEDINIPUR EAST', 'MEDINIPUR WEST', 'MEERUT', 'MEWAT', 'MIRZAPUR',
       'MOGA', 'MOKOKCHUNG', 'MON', 'MORADABAD', 'MORENA', 'MUKTSAR',
       'MUMBAI', 'MUNGELI', 'MUNGER', 'MURSHIDABAD', 'MUZAFFARNAGAR',
       'MUZAFFARPUR', 'MYSORE', 'NABARANGPUR', 'NADIA', 'NAGAON',
       'NAGAPATTINAM', 'NAGAUR', 'NAGPUR', 'NAINITAL', 'NALANDA',
       'NALBARI', 'NALGONDA', 'NAMAKKAL', 'NANDED', 'NANDURBAR',
       'NARAYANPUR', 'NARMADA', 'NARSINGHPUR', 'NASHIK', 'NAVSARI',
       'NAWADA', 'NAWANSHAHR', 'NAYAGARH', 'NEEMUCH', 'NICOBARS',
       'NIZAMABAD', 'NORTH AND MIDDLE ANDAMAN', 'NORTH DISTRICT',
       'NORTH GARO HILLS', 'NORTH GOA', 'NORTH TRIPURA', 'NUAPADA',
       'OSMANABAD', 'PAKUR', 'PALAKKAD', 'PALAMU', 'PALGHAR', 'PALI',
       'PALWAL', 'PANCH MAHALS', 'PANCHKULA', 'PANIPAT', 'PANNA',
       'PAPUM PARE', 'PARBHANI', 'PASHCHIM CHAMPARAN', 'PATAN',
       'PATHANAMTHITTA', 'PATHANKOT', 'PATIALA', 'PATNA', 'PAURI GARHWAL',
       'PERAMBALUR', 'PEREN', 'PHEK', 'PILIBHIT', 'PITHORAGARH',
       'PONDICHERRY', 'POONCH', 'PORBANDAR', 'PRAKASAM', 'PRATAPGARH',
       'PUDUKKOTTAI', 'PULWAMA', 'PUNE', 'PURBI CHAMPARAN', 'PURI',
       'PURNIA', 'PURULIA', 'RAE BARELI', 'RAICHUR', 'RAIGAD', 'RAIGARH',
       'RAIPUR', 'RAISEN', 'RAJAURI', 'RAJGARH', 'RAJKOT', 'RAJNANDGAON',
       'RAJSAMAND', 'RAMANAGARA', 'RAMANATHAPURAM', 'RAMBAN', 'RAMPUR',
       'RANCHI', 'RANGAREDDI', 'RATLAM', 'RATNAGIRI', 'RAYAGADA', 'REASI',
       'REWA', 'REWARI', 'RI BHOI', 'ROHTAK', 'ROHTAS', 'RUDRA PRAYAG',
       'RUPNAGAR', 'S.A.S NAGAR', 'SABAR KANTHA', 'SAGAR', 'SAHARANPUR',
       'SAHARSA', 'SAHEBGANJ', 'SAIHA', 'SALEM', 'SAMASTIPUR', 'SAMBA',
       'SAMBALPUR', 'SAMBHAL', 'SANGLI', 'SANGRUR', 'SANT KABEER NAGAR',
       'SANT RAVIDAS NAGAR', 'SARAIKELA KHARSAWAN', 'SARAN', 'SATARA',
       'SATNA', 'SAWAI MADHOPUR', 'SEHORE', 'SENAPATI', 'SEONI',
       'SEPAHIJALA', 'SERCHHIP', 'SHAHDOL', 'SHAHJAHANPUR', 'SHAJAPUR',
       'SHAMLI', 'SHEIKHPURA', 'SHEOHAR', 'SHEOPUR', 'SHIMLA', 'SHIMOGA',
       'SHIVPURI', 'SHOPIAN', 'SHRAVASTI', 'SIDDHARTH NAGAR', 'SIDHI',
       'SIKAR', 'SIMDEGA', 'SINDHUDURG', 'SINGRAULI', 'SIRMAUR', 'SIROHI',
       'SIRSA', 'SITAMARHI', 'SITAPUR', 'SIVAGANGA', 'SIVASAGAR', 'SIWAN',
       'SOLAN', 'SOLAPUR', 'SONBHADRA', 'SONEPUR', 'SONIPAT', 'SONITPUR',
       'SOUTH ANDAMANS', 'SOUTH DISTRICT', 'SOUTH GARO HILLS',
       'SOUTH GOA', 'SOUTH TRIPURA', 'SOUTH WEST GARO HILLS',
       'SOUTH WEST KHASI HILLS', 'SPSR NELLORE', 'SRIKAKULAM', 'SRINAGAR',
       'SUKMA', 'SULTANPUR', 'SUNDARGARH', 'SUPAUL', 'SURAJPUR', 'SURAT',
       'SURENDRANAGAR', 'SURGUJA', 'TAMENGLONG', 'TAPI', 'TARN TARAN',
       'TAWANG', 'TEHRI GARHWAL', 'THANE', 'THANJAVUR', 'THE NILGIRIS',
       'THENI', 'THIRUVALLUR', 'THIRUVANANTHAPURAM', 'THIRUVARUR',
       'THOUBAL', 'THRISSUR', 'TIKAMGARH', 'TINSUKIA', 'TIRAP',
       'TIRUCHIRAPPALLI', 'TIRUNELVELI', 'TIRUPPUR', 'TIRUVANNAMALAI',
       'TONK', 'TUENSANG', 'TUMKUR', 'TUTICORIN', 'UDAIPUR', 'UDALGURI',
       'UDAM SINGH NAGAR', 'UDHAMPUR', 'UDUPI', 'UJJAIN', 'UKHRUL',
       'UMARIA', 'UNA', 'UNAKOTI', 'UNNAO', 'UPPER SIANG',
       'UPPER SUBANSIRI', 'UTTAR KANNAD', 'UTTAR KASHI', 'VADODARA',
       'VAISHALI', 'VALSAD', 'VARANASI', 'VELLORE', 'VIDISHA',
       'VILLUPURAM', 'VIRUDHUNAGAR', 'VISAKHAPATANAM', 'VIZIANAGARAM',
       'WARANGAL', 'WARDHA', 'WASHIM', 'WAYANAD', 'WEST DISTRICT',
       'WEST GARO HILLS', 'WEST GODAVARI', 'WEST JAINTIA HILLS',
       'WEST KAMENG', 'WEST KHASI HILLS', 'WEST SIANG', 'WEST SINGHBHUM',
       'WEST TRIPURA', 'WOKHA', 'YADGIR', 'YAMUNANAGAR', 'YANAM',
       'YAVATMAL', 'ZUNHEBOTO']
le3.classes_=['Autumn', 'Kharif', 'Rabi', 'Summer','Whole Year ', 'Winter']
le4.classes_=['apple', 'banana', 'blackgram', 'coffee', 'grapes', 'jute',
       'lentil', 'maize', 'mango', 'orange', 'papaya', 'rice']


scaler_x=StandardScaler()
scaler_y=StandardScaler()
scaler_y.var_=2.21843763e+10
scaler_y.mean_=63944.11448649
scaler_y.scale_=148944.2053662
scaler_x.var_=np.array([1.04932882e+02, 3.38652891e+04, 2.07868064e+00, 9.25639984e+00,
       2.65943690e+09]).reshape(1,-1)
scaler_x.mean_=np.array([1.65372862e+01, 3.11887146e+02, 1.97662653e+00, 8.14965092e+00,
       2.54789329e+04]).reshape(1,-1)

scaler_x.scale_=np.array([1.02436752e+01, 1.84025240e+02, 1.44176303e+00, 3.04243321e+00,
       5.15697285e+04]).reshape(1,-1)

def change(arr):
    try:
        arr[0]=le1.transform(np.array([arr[0]])[0])
    except:
        arr[0]=8

    try:
        arr[1]=le2.transform(np.array([arr[1]])[0])
    except:
        arr[1]=5
    try:
        arr[2]=le3.transform(np.array([arr[2]])[0])
    except:
        arr[2]=1

    try:
        arr[3]=le2.transform(np.array([arr[3]])[0])
    except:
        arr[3]=3

    try:
        arr=scaler_x.transform(np.array(arr).reshape(1,-1))
    except:
        pass
    return arr

def predict(arr):

    import requests

    # NOTE: you must manually set API_KEY below using information retrieved from your IBM Cloud account.
    API_KEY = "McsFLx4OecKVAiAYsOpudQUJJHbYWO22f3WMAAiBdd5k"
    token_response = requests.post('https://iam.cloud.ibm.com/identity/token', data={"apikey": API_KEY, "grant_type": 'urn:ibm:params:oauth:grant-type:apikey'})
    mltoken = token_response.json()["access_token"]

    header = {'Content-Type': 'application/json', 'Authorization': 'Bearer ' + mltoken}

    # NOTE: manually define and pass the array(s) of values to be scored in the next line
    payload_scoring ={"input_data": [{"field": [["0","1","2","3","4"]], "values":[arr]}]}
    response_scoring = requests.post('https://us-south.ml.cloud.ibm.com/ml/v4/deployments/7ce98628-6c33-4d0b-bfe5-440a4b77212a/predictions?version=2021-09-02', json=payload_scoring, headers={'Authorization': 'Bearer ' + mltoken})
    print("Scoring response")
    print(response_scoring.json())
    return response_scoring.json()['predictions'][0]['values'][0][0]
    
def inverse(arr):
    return scaler_y.inverse_transform(arr)

def yield_pred(arr):
    arr=change(arr)
    arr=list(arr[0])
    arr=predict(arr)
    arr=inverse(np.array([arr]))
    return arr[0]