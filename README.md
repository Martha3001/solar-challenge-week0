# **Solar Energy Potential Analysis**  

## **📌 Overview**  
This project analyzes solar energy potential across three countries (**Benin, Sierra Leone, and Togo**) by evaluating key solar irradiance metrics (GHI, DNI, DHI) and environmental factors (temperature, wind speed, humidity). The goal is to identify optimal locations for solar energy deployment.  

🔑 **Key Deliverables:**  
- **Data Cleaning & EDA** for each country (`<country>_eda.ipynb`).  
- **Cross-country comparison** (`compare_countries.ipynb`).   

---

## **🚀 Quick Start**  

### **1. Clone the Repository**  
```bash
git clone https://github.com/Martha3001/solar-challenge-week0.git
cd solar-challenge-week0
```

### **2. Set Up Python Environment**  
#### **Using `venv` (Recommended)**  
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
.\venv\Scripts\activate   # Windows
pip install -r requirements.txt
```

### **3. Run Jupyter Notebooks**  

- Open and execute:  
  - `notebooks/benin_eda.ipynb`  
  - `notebooks/sierra_leone_eda.ipynb`  
  - `notebooks/togo_eda.ipynb`  
  - `notebooks/compare_countries.ipynb`  

---

## **📂 Repository Structure**  
```
solar-challenge-week0/  
├── .github/  
│   └── workflows/  
│       └── ci.yml            # GitHub Actions CI  
├── data/                     # Raw & cleaned data (gitignored)  
├── notebooks/                # Jupyter notebooks for EDA  
├── src/                      # Python modules   
├── tests/                    # Unit tests  
├── .gitignore  
├── README.md                 # This file  
└── requirements.txt          # Python dependencies  
```



