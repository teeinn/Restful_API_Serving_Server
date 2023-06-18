class ModelInfo:
    column_name_to_change: dict = {
        "Adaptivity Level": 'Adaptivity_Level',
        "Education Level": "Education_Level",
        "Institution Type": "Institution_Type",
        "IT Student": "IT_Student",
        "Financial Condition": "Financial_Condition",
        "Internet Type": "Internet_Type",
        "Network Type": "Network_Type",
        "Class Duration": "Class_Duration",
        "Self Lms": "Self_Lms",
        "Load-shedding": "Load_shedding"
    }
    classes: list = ['Low', 'Moderate', 'High']
    label: str = "Adaptivity_Level"

modelInfo = ModelInfo()