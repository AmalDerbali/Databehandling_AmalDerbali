import pandas as pd



covid19_sex = pd.read_excel("C:/Users/Amal Derbali/Documents/GitHub/Databehandling_AmalDerbali/Lab/Data/Folkhalsomyndigheten_Covid19.xlsx", sheet_name ="Totalt antal per kön")
covid19_region = pd.read_excel("C:/Users/Amal Derbali/Documents/GitHub/Databehandling_AmalDerbali/Lab/Data/Folkhalsomyndigheten_Covid19.xlsx", sheet_name="Totalt antal per region")
covid19_age = pd.read_excel("C:/Users/Amal Derbali/Documents/GitHub/Databehandling_AmalDerbali/Lab/Data/Folkhalsomyndigheten_Covid19.xlsx", sheet_name="Totalt antal per åldersgrupp")

vaccin_df = pd.read_excel("C:/Users/Amal Derbali/Documents/GitHub/Databehandling_AmalDerbali/Lab/Data/Folkhalsomyndigheten_Covid19_Vaccine.xlsx", sheet_name="Vaccinerade kommun och ålder")
vaccin_län = vaccin_df.groupby("Län_namn").mean().reset_index()
vaccin_ålder = vaccin_df.groupby("Ålder").mean().reset_index()

world_data = pd.read_excel("C:/Users/Amal Derbali/Documents/GitHub/Databehandling_AmalDerbali/Lab/Data/Uppgift_4_world_data.xlsx", sheet_name="Sheet1")
world_cases = world_data[world_data["indicator"] == "cases"].reset_index(drop=True)
world_cases_country = world_cases.groupby("country").mean().reset_index()
world_death = world_data[world_data["indicator"] == "deaths"].reset_index(drop=True)
world_death_country = world_death.groupby("country").mean().reset_index()
world_death_country.head()