# NMSC-TCIA-Dataset
High-resolution dermatopathology WSI dataset for machine learning research
# NMSC Whole Slide Image Dataset (TCIA Project)

## Overview
This project presents a high-resolution dermatopathology dataset of whole slide images (WSIs) for non-melanoma skin cancer (NMSC), including basal cell carcinoma (BCC), squamous cell carcinoma (SCC), mixed BCC/SCC, and normal skin.

The dataset was developed to support machine learning research in computational pathology, with a focus on reproducibility, data quality, and multimodal learning.

> 🔗 The dataset will be publicly available via The Cancer Imaging Archive (TCIA).  
> (Access link will be added upon publication.)

---

## Motivation
While machine learning models in medical imaging are widely studied, the process of **data collection, curation, and standardization** is often underreported.

This project aims to highlight the critical steps required to build a reliable medical imaging dataset, including:
- Data retrieval from clinical archives  
- Slide preparation and digitization  
- Quality control and expert validation  
- Metadata structuring  
- Standardization to DICOM format  

---

## Dataset Summary
- **Total slides:** 2,955  
- **Diagnostic categories:**
  - Basal cell carcinoma (BCC): 1,570  
  - Squamous cell carcinoma (SCC): 296  
  - Mixed BCC/SCC: 15  
  - Non-tumor (normal skin): 1,073

## Data Source
The dataset was collected retrospectively from dermatology clinical archives at:
- Kepler University Hospital Linz, Austria  


All data were anonymized prior to processing and release.

- **Data format:**
  - Original: MRXS, SVS  
  - Standardized: DICOM  

- **Annotations:**
  - Expert-reviewed diagnoses  
  - Histopathological subtypes  
  - Clinical metadata (age, sex, anatomical site)  
  - Pathology reports (German + English)

---

## Data Curation Pipeline
The dataset was created through a multi-step pipeline:

1. Patient and case identification  
2. Slide retrieval from clinical archive  
3. Slide cleaning and preparation  
4. Whole slide image digitization  
5. Pathologist review and diagnostic verification  
6. Quality control and filtering  
7. Metadata extraction and validation  
8. Conversion to DICOM format  
9. Final dataset assembly and standardization  

This process ensures high-quality, reliable data suitable for machine learning applications.

---

## Technical Contributions
This project includes:

- Development of a structured WSI data curation workflow  
- Standardization of histopathology images to DICOM format  
- Integration of image data with structured and textual metadata  
- Preparation of a multimodal dataset for AI research  

---

## Related Resources
The following repositories provide additional details:

- WSI-to-DICOM conversion pipeline : https://github.com/solmazhaddady/WSI-to-DICOM-Converter 
- Multimodal experiments  *(to be added)*  
- Data curation workflow : https://github.com/solmazhaddady/WSI-Data-Curation-Pipeline  

---

## Status
Dataset and manuscript are currently under preparation and submission.  
Links and additional resources will be updated upon publication.

---

## Author
Solmaz Haddady  
MSc Artificial Intelligence – Medical Imaging  

---

## Contact
For questions or collaboration inquiries, feel free to reach out.
Email: solmazhaddadi4003@gmail.com
