# Veille Technologique: Cloud Computing in Morocco

## Overview
This repository contains the source files and documentation for a technological watch (veille technologique) project focused on analyzing the cloud computing ecosystem in Morocco. The objective is to evaluate investment opportunities in a sovereign cloud infrastructure, aligning with Morocco's digital transformation goals, such as *Maroc Digital 2030*. The project explores the theoretical foundations of cloud computing, market trends, regulatory frameworks, cybersecurity imperatives, and economic viability, with a particular emphasis on establishing a Moroccan Sovereign Cloud.

## Project Context
This work was conducted as part of the "Techniques de Veille" module at the **École Nationale des Sciences Appliquées de Tétouan** (ENSA Tétouan), under the supervision of Pr. Younes Wadiai. It aims to provide a comprehensive analysis of the cloud computing landscape in Morocco, addressing:
- **Market Analysis**: Growth trends in ICT, SaaS, IaaS, PaaS, and cybersecurity markets.
- **Regulatory and Security Frameworks**: Compliance with local (e.g., Décret n° 2-24-921) and international regulations (e.g., GDPR, Cloud Act, ISO 27001).
- **Investment Opportunities**: Feasibility study for establishing data centers in Casablanca-Settat, Rabat-Salé-Kénitra, and Essaouira, leveraging energy-efficient cooling and local workforce advantages.
- **Data Insights**: Analysis of adoption rates, regional disparities, and startup ecosystems using advanced data processing and visualization tools.

## Repository Structure
- **/docs**:
  - `rapport.pdf` # Main report containing the full technological watch analysis.
  - `cloud_souverain_parte_1.pptx` # First presentation of the project, introducing the concept of a sovereign cloud.
  - `cloud_souverain_parte_2.pptx` # Second presentation, detailing market analysis and investment plans.
- **/data**:
  - `Dashboard_veille.pbix` # Power BI file for data visualization and dashboard creation.
  - **/Eropean_union_data**:
    - `UE_data_processing.ipynb` # Jupyter Notebook for processing European Union data, including cloud computing adoption.
    - `UE_data_processing.py` # Python script for processing European Union data.
    - `UE_data.xlsx` # Excel file containing raw data related to European Union statistics.
  - **/moroccan_data**:
    - `AI in morocco.xlsx` # Excel file with data on AI adoption and trends in Morocco.
    - `cloud_providers_per_years.xlsx` # Excel file tracking cloud provider trends over the years in Morocco.
    - `final_output.xlsx` # Processed output data for Moroccan cloud market analysis.
    - `Financement_gov_startup.xlsx` # Excel file with data on government funding for startups in Morocco.
    - `gouvernement_transformation.json` # JSON file with data on government digital transformation initiatives.
    - `iaas_data.json` # JSON file with data on Infrastructure as a Service (IaaS) market trends in Morocco.
    - `iaas.xlsx` # Excel file with additional IaaS-related data.
    - `IT_distribution.xlsx` # Excel file with data on IT resource distribution in Morocco.
    - `morocco_IT_overview.xlsx` # Excel file summarizing the IT landscape in Morocco.
    - `mss.json` # JSON file with data on cybersecurity and social security incidents in Morocco.
    - `PaaS.json` # JSON file with data on Platform as a Service (PaaS) market trends in Morocco.
    - `saas.json` # JSON file with data on Software as a Service (SaaS) market trends in Morocco.
- **/scripts**:
  - Python scripts and Power Query transformations used for data processing.
- **/figures**:
  - Visualizations and dashboards generated with Power BI, including cloud adoption trends in Europe and Morocco's digital ecosystem.
- **/references**:
  - List of references cited in the report, including market studies, regulatory documents, and media sources.
- **/Cloud_Maroc_Atlas_web_site**:
  - `index.html` # Main HTML file for the AtlasCloud website, defining the structure and content of the web page.
  - `main.css` # Main CSS file for styling the AtlasCloud website, including font, color variables, and layout styles.
  - `main.js` # Main JavaScript file for interactive features, such as navigation, animations, and sliders.

## Key Findings
- **Market Growth**: The Moroccan ICT market is projected to grow at a CAGR of 6.21% from 2024 to 2029, with SaaS (15.9% CAGR) and AI dataset markets (28.8% CAGR) showing significant potential.
- **Cybersecurity Needs**: 40% of Moroccan SMEs face cyber risks, and the 2025 CNSS data breach underscores the need for robust, locally-hosted cloud solutions.
- **Investment Feasibility**: A proposed investment of $114.5M–$225M for three Tier III+ data centers could yield a ROI of 22–33% within five years, supported by $17M–$46M in public/private subsidies.
- **Strategic Locations**: Data centers in Casablanca-Settat, Rabat-Salé-Kénitra, and Essaouira can cover 62% of the market, leveraging seawater cooling to reduce OPEX by 40%.
- **Service Offerings**: The proposed cloud will offer IaaS, PaaS, SaaS, and Managed Security Services (MSS), targeting 1,208 enterprises by Year 5.

## Technologies Used
- [![Pandas](https://img.shields.io/badge/Pandas-150458?style=flat&logo=pandas&logoColor=white)](https://pandas.pydata.org/) : Python library for data manipulation and analysis, used for cleaning and processing datasets.
- [![Power BI](https://img.shields.io/badge/Power%20BI-F2C811?style=flat&logo=powerbi&logoColor=black)](https://powerbi.microsoft.com/) : Microsoft tool for creating interactive dashboards and visualizations, used to analyze cloud adoption trends and Morocco's digital ecosystem.
- [![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=flat&logo=html5&logoColor=white)](https://developer.mozilla.org/en-US/docs/Web/HTML) : Markup language for structuring web-based dashboards or documentation.
- [![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=flat&logo=css3&logoColor=white)](https://developer.mozilla.org/en-US/docs/Web/CSS) : Styling language for designing visually appealing web interfaces and reports.
- [![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=flat&logo=javascript&logoColor=black)](https://developer.mozilla.org/en-US/docs/Web/JavaScript) : Programming language for adding interactivity to web-based visualizations or dashboards.
- [![Power Query](https://img.shields.io/badge/Power%20Query-217346?style=flat&logo=microsoft-excel&logoColor=white)](https://learn.microsoft.com/en-us/power-query/) : ETL processes for data extraction and transformation, integrated with Excel and Power BI.
- [![NumPy](https://img.shields.io/badge/NumPy-013243?style=flat&logo=numpy&logoColor=white)](https://numpy.org/) : Additional Python library for numerical computations and data analysis.


## How to Use This Repository
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-username/cloud-morocco-veille.git
   ```

## Acknowledgments
We express our gratitude to Pr. Younes Wadiai for his guidance, our team for their collaborative efforts, and our families for their unwavering support throughout this project.
