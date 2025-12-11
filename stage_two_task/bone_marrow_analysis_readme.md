# Bone Marrow Single-Cell RNA-seq Analysis

## Project Overview
This project analyzes a human **bone marrow single-cell RNA-seq dataset** (`bone_marrow.h5ad`) to identify cell populations, quantify cell type proportions, and annotate clusters using canonical markers. The analysis leverages **Scanpy** and **Decoupler** for preprocessing, clustering, visualization, and cell type scoring.

**Biological Questions:**
1. Which cell types are present in the dataset?
2. What are the biological roles of each identified cell type?
3. Can we map major hematopoietic and immune cell populations in bone marrow?
4. Can we assess patient health status based on immune cell composition?

---

## Dataset Information
| Attribute          | Value                                                                 |
|-------------------|----------------------------------------------------------------------|
| File               | bone_marrow.h5ad                                                   |
| Cells × Genes      | 14783 × 17374                                                    |
| Metadata           | Disease stage, treatment, tissue type, cell annotations, QC metrics |
| Tissue             | Human bone marrow                                                    |

---

## Raw & Processed Data Download
Because GitHub does not allow uploading large files (>25MB), the raw and processed datasets are stored in Google Drive.
📥 Download the data:
Raw Data
* Bone marrow raw (bone_marrow.h5ad)
👉 https://drive.google.com/file/d/14O01KspPMehZ1i4V6ZrwZIzHwoudz-nk/view?usp=drive_link
Processed Data
* Bone marrow raw (bone_marrow_processed.h5ad)
👉 https://drive.google.com/file/d/1mZMZ44--bOnzgC5-YwQE-AP8MxwbsUPo/view?usp=drive_link


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
| 1    | **Data Loading** | Load `AnnData` object; verify unique genes & cells |
| 2    | **Quality Control** | Calculate QC metrics: n_genes, total_counts, %MT, %RIBO, %HB; visualize via violin & scatter plots; filter low-quality cells & genes |
| 3    | **Doublet Detection** | Identify potential doublets using Scrublet |
| 4    | **Normalization & Feature Selection** | Normalize total counts, log-transform, select top 1000 highly variable genes |
| 5    | **Dimensionality Reduction** | PCA, neighbors calculation, UMAP embedding |
| 6    | **Clustering** | Leiden clustering at multiple resolutions (0.2, 0.5, 1.0, 2.0) |
| 7    | **Cell Type Annotation** | Score cells using Decoupler ULM method with canonical markers; assign cell type labels |
| 8    | **Marker Visualization** | Dotplots, stacked violin plots, matrix plots, tracks plots for marker genes across clusters |
| 9    | **Tissue Source Justification** | Evaluate lineage populations & progenitors to confirm bone marrow origin |
| 10   | **Patient Health Assessment** | Calculate cluster proportions; interpret immune activation patterns |

---

## Cell Type Annotation (leiden_res1_0)
| Cluster | Cell Type           | Function                                                                 |
|---------|------------------|-------------------------------------------------------------------------|
| 0       | Neutrophils        | Phagocytose pathogens, innate defense                                   |
| 1       | Monocytes          | Differentiate into macrophages/DCs, mediate inflammation                |
| 2       | Gamma delta T cells| Early responders to stressed/infected cells without MHC                |
| 3       | Gamma delta T cells| Same as above                                                           |
| 4       | T memory cells     | Adaptive immune cells; respond to previously encountered antigens       |
| 5       | NK cells           | Kill virus-infected or transformed cells                                |
| 6       | T memory cells     | Adaptive immune cells; rapid recall response                             |
| 7       | B cells memory     | Produce antibodies upon re-exposure                                     |
| 8       | Platelets          | Clotting and wound healing, derived from megakaryocytes                 |
| 9       | Plasma cells       | Terminal B cells secreting antibodies                                   |

---

## Tissue Source Justification
Evidence supporting **bone marrow origin**:

- Presence of **neutrophils** and **platelets**, absent in PBMC preps.  
- Diverse **mature hematopoietic lineages**: T cells, B cells, NK cells, monocytes, plasma cells.  

**Exceptions:**  
- Hematopoietic stem and progenitor cells (HSPCs) and erythroid progenitors were not detected.  
- Likely due to low abundance or sampling bias, but overall lineage composition supports marrow origin.

> **Conclusion:** Sample is consistent with bone marrow, with some progenitors likely underrepresented.

---

## Patient Health Assessment
| Cell Type           | Percent of Total Cells|
|-------------------  |---------------------- |
| T memory cells      | 28.05%               |
| Gamma delta T cells | 18.76% + 8.88%       |
| NK cells            | 11.97%               |
| Neutrophils         | 8.03%                |
| B cells memory      | 7.32%                |
| Monocytes           | 5.50%                |
| Plasma cells        | 4.76%                |
| Platelets           | 1.28%                |

**Interpretation:**  
- Elevated **T memory cells** and **NK cells** indicate adaptive and innate immune activation.  
- Moderate neutrophils and monocytes reflect active inflammation.  
- Presence of B cells and plasma cells suggests ongoing antibody-mediated response.  

> **Conclusion:** Patient shows signs of **infection or active immune response**, not a healthy baseline.

---

## Directory Structure

Hackbio_Internship/
└── stage_two_task/
    ├── notebooks/             
    │   └── bone_marrow_analysis.ipynb
    ├── data/
    │   ├── raw/               # Original/raw .h5ad or gene expression matrices
    │   │   └── bone_marrow.h5ad
    │   └── processed/         # Processed AnnData objects
    │       └── bone_marrow_processed.h5ad
    ├── figures/               # All saved plots
    │   ├── n_genes_violin.png
    │   ├── scatter_pct_MT.png
    │   ├── scatter_pct_RIBO.png
    │   ├── scatter_pct_HB.png
    │   ├── umap_leiden.png
    │   ├── umap_doublet.png
    │   ├── tracksplot_celltypes.png
    │   └── ...others
    └── README.md              # Project description, instructions, and interpretation

---

## Reproducibility Notes
- All steps can be rerun from `notebooks/analysis.ipynb`.  
- Package versions ensure consistent outputs.  
- Data and results are organized for ease of replication or extension to new datasets.

---

## Summary
- Complete workflow: **QC → normalization → clustering → annotation → visualization**.  
- Tissue source: **bone marrow**, with some progenitors undetected.