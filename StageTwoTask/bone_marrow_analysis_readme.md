# Bone Marrow Single-Cell RNA-seq Analysis

## Project Overview
This project analyzes a human **bone marrow single-cell RNA-seq dataset** (bone_marrow.h5ad) to identify cell populations, quantify cell type proportions, and annotate clusters using canonical markers. The analysis uses **Scanpy** and **Decoupler** for preprocessing, clustering, visualization, and cell type scoring.

**Biological Questions:**
1. Which cell types are present in the dataset?
2. What are the biological roles of each identified cell type?
3. Can we map major hematopoietic and immune cell populations in bone marrow?
4. Can we assess patient immune status based on cell type composition?

---

## Dataset Information
| Attribute          | Value                                                                 |
|-------------------|----------------------------------------------------------------------|
| File               | bone_marrow.h5ad                                                   |
| Cells × Genes      | 14,783 × 17,374                                                    |
| Metadata           | Disease stage, treatment, tissue type, cell annotations, QC metrics |
| Tissue             | Human bone marrow                                                    |

---

## Raw & Processed Data Download

Because GitHub does not allow uploading large files (>25MB), the raw and processed datasets are stored in Google Drive.  

📥 **Download the data:**

| Data Type       | File Name                        | Download Link |
|-----------------|---------------------------------|---------------|
| Raw Data        | bone_marrow.h5ad                | [Download](https://drive.google.com/file/d/14O01KspPMehZ1i4V6ZrwZIzHwoudz-nk/view?usp=drive_link) |
| Processed Data  | bone_marrow_processed.h5ad      | [Download](https://drive.google.com/file/d/1mZMZ44--bOnzgC5-YwQE-AP8MxwbsUPo/view?usp=drive_link) |

---

## Dependencies
| Package    | Version |
|-----------|---------|
| Python    | 3.13.7  |
| scanpy    | 1.11.5  |
| anndata   | 0.12.6  |
| pandas    | 2.3.0   |
| matplotlib| 3.10.7  |
| seaborn   | 0.13.2  |
| decoupler | 2.1.2   |
| requests  | 2.32.5  |

---

## Step-by-Step Workflow
| Step | Task / Deliverable | Key Analytical Approach |
|------|------------------|------------------------|
| 1    | Data Loading | Load `AnnData` object; verify unique genes & cells |
| 2    | Quality Control | Calculate QC metrics, visualize, filter low-quality cells & genes |
| 3    | Doublet Detection | Identify potential doublets using Scrublet |
| 4    | Normalization & Feature Selection | Normalize counts, log-transform, select top 1000 highly variable genes |
| 5    | Dimensionality Reduction | PCA, neighbor graph, UMAP embedding |
| 6    | Clustering | Leiden clustering at multiple resolutions |
| 7    | Cell Type Annotation | Score cells using Decoupler ULM method with canonical markers |
| 8    | Marker Visualization | Dotplots, violin plots, matrix plots, tracks plots |
| 9    | Tissue Source Justification | Confirm bone marrow origin using lineage composition |
| 10   | Patient Immune Status | Calculate cluster proportions; interpret immune activity |

---

## Cell Type Annotation (leiden_res1_0)
| Cluster | Cell Type           | Function / Biological Role |
|---------|------------------|----------------------------|
| 0       | Neutrophils        | Phagocytosis, first responders, innate immunity |
| 1       | Monocytes          | Inflammation, cytokine production, immune signaling |
| 2       | Gamma delta T cells| Rapid stress recognition, cytokine release |
| 3       | Gamma delta T cells| Rapid stress recognition, cytokine release |
| 4       | T memory cells     | Antigen recognition, adaptive effector function |
| 5       | NK cells           | Cytotoxic activity, viral defense, innate immunity |
| 6       | T memory cells     | Antigen recognition, adaptive effector function |
| 7       | B cells memory     | Long-term humoral immunity |
| 8       | Platelets          | Hematopoiesis, inflammation modulation |
| 9       | Plasma cells       | Terminal B cells secreting antibodies, active humoral response |

---

## Tissue Source Justification
**Evidence supporting bone marrow origin:**
- Presence of **neutrophils** and **platelets**, absent in PBMC preps.
- Diverse **mature hematopoietic lineages**: T cells, B cells, NK cells, monocytes, plasma cells.  

**Exceptions:**  
- Hematopoietic stem and progenitor cells (HSPCs) and erythroid progenitors were not detected, likely due to low abundance or sampling bias.  

> **Conclusion:** Sample is consistent with bone marrow, with minor underrepresentation of progenitors.

---

## Patient Immune Status
| Cell Type           | Percent of Total Cells | Interpretation |
|-------------------  |---------------------- |----------------|
| T memory cells      | 28.05%               | Adaptive immune activation; antigen recall |
| Gamma delta T cells | 18.76% + 8.88%       | Rapid response to stressed/infected cells; cytokine release |
| NK cells            | 11.97%               | Cytotoxic, viral defense; innate activation |
| Neutrophils         | 8.03%                | First responders, phagocytosis, innate immunity |
| B cells memory      | 7.32%                | Humoral immunity; antibody production potential |
| Monocytes           | 5.50%                | Inflammatory response, cytokine production |
| Plasma cells        | 4.76%                | Active antibody secretion; adaptive humoral response |
| Platelets           | 1.28%                | Inflammation modulation; confirms marrow origin |

> **Interpretation:** The immune profile indicates **active immune response**, with both **innate and adaptive cells engaged**. This is not a healthy baseline, suggesting **infection or inflammation**.

---

## Directory Structure

HackBioInternship/
└── StageTwoTask/
├── notebooks/
│ └── bone_marrow_analysis.ipynb
├── data/
│ ├── raw/
│ │ └── bone_marrow.h5ad
│ └── processed/
│ └── bone_marrow_processed.h5ad
├── figures/
│ ├── n_genes_violin.png
│ ├── scatter_pct_MT.png
│ ├── scatter_pct_RIBO.png
│ ├── scatter_pct_HB.png
│ ├── umap_leiden.png
│ ├── umap_doublet.png
│ ├── tracksplot_celltypes.png
│ └── ...others
└── README.md

## Reproducibility Notes
- All steps can be rerun from `notebooks/bone_marrow_analysis.ipynb`.  
- Package versions ensure consistent outputs.  
- Data and results are organized for easy replication or extension.

---

## Summary
- Complete workflow: **QC → normalization → clustering → annotation → visualization**.  
- Tissue source: **bone marrow**, with active immune cell composition.  
- Observed clusters indicate both **innate and adaptive immune activation**, consistent with **infection or inflammatory response**.