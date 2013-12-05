from django.http.response import HttpResponse

def main_view(request):
    return HttpResponse("""
    <!DOCTYPE html>
    <html>
    <head>
        <title>
            Welcome to CSE233Care!
        </title>
    </head>
    <body>
        <h1>Here is the main page</h1>
        <p>Here is where we'll have some bootstrappy things</p>

        <form action="logged_in">
            <input type="submit" value="Log in">
        </form>

        <form action="register">
            <input type="submit" value="Register">
        </form>
    </body>
    </html>
        """)

def logged_in_view(request):
    return HttpResponse("""
    <!DOCTYPE html>
    <html>
    <head>
        <title>
            Hello, Again!
        </title>
    </head>
    <body>
        <h1>Welcome back!</h1>
        <p>
            This will be where we have a list of all of the users info.
            It will contain their 'policy', their 'payment info' and things
            of that nature.
        </p>
    </body
    </html
        """)

def register(request):
    return HttpResponse("""
    <!DOCTYPE html>
    <html>
    <head>
        <title>
            Register
        </title>
    </head>
    <body>
        <h1>Please fill out the following information</h1>
        <p>
            Here we will have a form that will include all of the information
            that we will need to store in the database.
        </p>

        <form>
            Desired username: <input type="text" name="username"><br>
            Desired password: <input type="password" name="username"><br>
            Confirm password: <input type="password" name="username"><br>
            First name: <input type="text" name="firstname"><br>
            Last name: <input type="text" name="lastname"><br>
            Email: <input type="text" name="email"><br>
            Social Security Number: <input type="tel" name="ssn-first">
            <input type="tel" name="ssn-middle">
            <input type="tel" name="ssn-last"><br>
            Age: <input type="number" name="age"><br>
            State: <input type="text" name="state"><br>
            Smoker: 
            <select name="smoker">
            <option value="no">No</option>
            <option value="yes">Yes</option>
            <option value="quit">I did, but I quit</option>
            </select></br>
            Gender: 
            <select name="gender">
            <option value="male">Male</option>
            <option value="female">Female</option>
            </select></br>
            Body Mass Index: <input type="tel" name="bmi"><br>
            Marital Status: 
            <select name="marital">
            <option value="married">Married</option>
            <option value="single">Single</option>
            <option value="divorced">Divorced</option>
            <option value="widowed">Widowed</option>
            </select></br>
            Were you previously insured? 
            <select name="prev_insured">
            <option value="yes">Yes</option>
            <option value="no">No</option>
            </select></br>
            List any pre-existing conditions you have:
            <textarea rows="4" cols="50">
            </textarea></br>
            Please select all that apply to you:<br>
            <b><u>Allergies:</u></b><br>
            <input type="checkbox" value="none">None<br>
            <input type="checkbox" value="aspirin">Aspirin<br>
            <input type="checkbox" value="codeine">Codeine<br>
            <input type="checkbox" value="dermerol">Dermerol<br>
            <input type="checkbox" value="eggs">Eggs<br>
            <input type="checkbox" value="environmental">Environmental<br>
            <input type="checkbox" value="iodine">Iodine<br>
            <input type="checkbox" value="latex">Latex<br>
            <input type="checkbox" value="morphine">Morphine<br>
            <input type="checkbox" value="penicillin">Penicillin<br>
            <input type="checkbox" value="sulfa">Sulfa<br>

            <b><u>Past Medical Illnesses:</u></b><br>
            <input type="checkbox" value="none">None<br>
            <input type="checkbox" value="anemia">Anemia<br>
            <input type="checkbox" value="anxiety">Anxiety<br>
            <input type="checkbox" value="asthma">Asthma<br>
            <input type="checkbox" value="atrial_fibrillation">Atrial Fibrillation<br>
            <input type="checkbox" value="back_pain">Back Pain<br>
            <input type="checkbox" value="breast_cancer">Breast Cancer<br>
            <input type="checkbox" value="cancer">Cancer<br>
            <input type="checkbox" value="chronic_lung_disease">Chronic Lung Disease<br>
            <input type="checkbox" value="cirrhosis_of_liver">Cirrhosis of Liver<br>
            <input type="checkbox" value="colitis">Colitis<br>
            <input type="checkbox" value="colon_cancer">Colon Cancer<br>
            <input type="checkbox" value="colon_polyps">Colon Polyps<br>
            <input type="checkbox" value="congestive_heart_failure">Congestive Heart Failure<br>
            <input type="checkbox" value="chrons_disease">Chron's Disease<br>
            <input type="checkbox" value="depression">Depression<br>
            <input type="checkbox" value="diabetes">Diabetes<br>
            <input type="checkbox" value="diverticulitis">Diverticulitis<br>
            <input type="checkbox" value="diverticulosis">Diverticulosis<br>
            <input type="checkbox" value="duodenal_ulcer">Duodenal Ulcer<br>
            <input type="checkbox" value="emphysema">Emphysema<br>
            <input type="checkbox" value="fatty_liver">Fatty Liver<br>
            <input type="checkbox" value="frequent_urinary_infections">Frequent Urinary Infections<br>
            <input type="checkbox" value="gall_stones">Gall Stones<br>
            <input type="checkbox" value="glaucoma">Glaucoma<br>
            <input type="checkbox" value="gout">Gout<br>
            <input type="checkbox" value="heart_attack">Heart Attack<br>
            <input type="checkbox" value="heart_disease">Heart Disease<br>
            <input type="checkbox" value="hear_murmur">Heart MurMur (MVP)<br>
            <input type="checkbox" value="heart_valve_replacement">Heart Valve Replacement<br>
            <input type="checkbox" value="hepatitis_a">Hepatitis A<br>
            <input type="checkbox" value="hepatitis_b">Hepatitis B<br>
            <input type="checkbox" value="hepatitis_c">Hepatitis C<br>
            <input type="checkbox" value="hiatal_hernia">Hiatal Hernia<br>
            <input type="checkbox" value="high_blood_pressure">High Blood Pressure<br>
            <input type="checkbox" value="high_cholesterol">High Cholesterol<br>
            <input type="checkbox" value="history_suicide">History of Suicide Attempt<br>
            <input type="checkbox" value="hiv_aids">HIV/AIDS<br>
            <input type="checkbox" value="irregular_heart_beat">Irregular Heart Beat<br>
            <input type="checkbox" value="irritable_bowel_syndrom">Irritable Bowel Syndrom<br>
            <input type="checkbox" value="kidney_disease">Kidney Disease<br>
            <input type="checkbox" value="kidney_failure">Kidney Failure<br>
            <input type="checkbox" value="kidney_stones">Kidney Stones<br>
            <input type="checkbox" value="lactose_intolerance">Lactose Intolerance<br>
            <input type="checkbox" value="lupus">Lupus<br>
            <input type="checkbox" value="migraines">Migraines<br>
            <input type="checkbox" value="numbness_extremites">Numbness in Extremites<br>
            <input type="checkbox" value="osteoarthritis">Osteoarthritis<br>
            <input type="checkbox" value="osteoporosis">Osteoporosis<br>
            <input type="checkbox" value="pancreatitis">Pancreatitis<br>
            <input type="checkbox" value="paralysis">Paralysis<br>
            <input type="checkbox" value="parkinsons_disease">Parkinson's Disease<br>
            <input type="checkbox" value="phlebitis">Phlebitis<br>
            <input type="checkbox" value="pneumonia">Pneumonia<br>
            <input type="checkbox" value="prostate_problem">Prostate Problem<br>
            <input type="checkbox" value="radiation_therapy">Radiation Therapy<br>
            <input type="checkbox" value="raynauds_disease">Raynaud's Disease<br>
            <input type="checkbox" value="reflux">Reflux<br>
            <input type="checkbox" value="rheumatic_fever">Rheumatic Fever<br>
            <input type="checkbox" value="rheumatoid_arthritis">Rheumatoid Arthritis<br>
            <input type="checkbox" value="schizophrenia">Schizophrenia<br>
            <input type="checkbox" value="scleroderma">Scleroderma<br>
            <input type="checkbox" value="seizures">Seizures<br>
            <input type="checkbox" value="skin_cancer">Skin Cancer<br>
            <input type="checkbox" value="sleep_apnea">Sleep Apnea<br>
            <input type="checkbox" value="stomach_ulcer">Stomach Ulcer<br>
            <input type="checkbox" value="stroke">Stroke<br>
            <input type="checkbox" value="tb">TB (Tuberculosis)<br>
            <input type="checkbox" value="tb_skin">TB Skin Test Positive<br>
            <input type="checkbox" value="thyroid_disease">Thyroid Disease<br>
            <input type="checkbox" value="ulcerative_colitis">Ulcerative Colitis<br>
            Other: <input type="text" name="other"><br>

            <b><u>Past Medical Illnesses:</u></b><br>
            <input type="checkbox" value="none_surgery">None<br>
            <input type="checkbox" value="aicd">AICD - Automatic Implantbale Cardiac Difibrillator<br>
            <input type="checkbox" value="appendix">Appendix<br>
            <input type="checkbox" value="av_graft_left">AV Graft Left<br>
            <input type="checkbox" value="av_graft_right">AV Graft Right<br>
            <input type="checkbox" value="breast">Breast<br>
            <input type="checkbox" value="c_section">C - Section<br>
            <input type="checkbox" value="colon_resection">Colon Resection<br>
            <input type="checkbox" value="colostomy">Colostomy<br>
            <input type="checkbox" value="coronary_artery_disease">Coronary Artery Disease<br>
            <input type="checkbox" value="coronary_stent_placement">Coronary Stent Placement<br>
            <input type="checkbox" value="gallbladder">Gallbladder<br>
            <input type="checkbox" value="gastric_bypass">Gastric Bypass<br>
            <input type="checkbox" value="groin_hernia">Groin Hernia<br>
            <input type="checkbox" value="heart_valve_replacement">Heart Valve Replacement<br>
            <input type="checkbox" value="hemorrhoids">Hemorrhoids<br>
            <input type="checkbox" value="hiatal_hernia">Hiatal Hernia<br>
            <input type="checkbox" value="joint_replacement">Joint Replacement<br>
            <input type="checkbox" value="kidney_surgery">Kidney Surgery<br>
            <input type="checkbox" value="mastectomy_bilateral">Mastectomy Bilateral<br>
            <input type="checkbox" value="mastectomy_left">Mastectomy Left<br>
            <input type="checkbox" value=""mastectomy_right>Mastectomy Right<br>
            <input type="checkbox" value="obesity_surgery">Obesity Surgery<br>
            <input type="checkbox" value="pacemaker_implant">Pacemaker Implant<br>
            <input type="checkbox" value="port_a_cath_insertion">Port-a-Cath Insertion<br>
            <input type="checkbox" value="previous_surgery">Previous Surgery<br>
            <input type="checkbox" value="prostate_surgery">Prostate Surgery<br>
            <input type="checkbox" value="stomach_surgery">Stomach Surgery<br>
            <input type="checkbox" value="thyroid_surgery">Thyroid Surgery<br>
            <input type="checkbox" value="tonsil_surgery">Tonsil Surgery<br>
            <input type="checkbox" value="tubal_ligation">Tubal Ligation<br>
            <input type="checkbox" value="tummy_tuck">Tummy Tuck<br>
            <input type="checkbox" value="uterus_surgery">Uterus Surgery<br>
        </form>
    </body
    </html
        """)
