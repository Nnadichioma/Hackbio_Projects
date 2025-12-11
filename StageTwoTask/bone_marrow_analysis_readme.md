# Bone Marrow Single-Cell RNA-seq Analysis

## Project Overview
This project analyzes a human **bone marrow single-cell RNA-seq dataset** (bone_marrow.h5ad`) to identify cell populations, quantify cell type proportions, and annotate clusters using canonical markers. The analysis uses **Scanpy** and **Decoupler** for preprocessing, clustering, visualization, and cell type scoring.

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

| Data Type      | File Name                    | Download Link |
|----------------|-----------------------------|---------------|
| Raw Data       | bone_marrow.h5ad            | [Download](https://drive.google.com/file/d/14O01KspPMehZ1i4V6ZrwZIzHwoudz-nk/view?usp=drive_link) |
| Processed Data | bone_marrow_processed.h5ad  | [Download](https://drive.google.com/file/d/1mZMZ44--bOnzgC5-YwQE-AP8MxwbsUPo/view?usp=drive_link) |

**Note:** All input/output paths are parameterized at the top of the notebook for easy modification.  Datasets and figures are referenced using relative paths within the project folder structure.

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

## Environment Setup & Running the Notebook

1. **Clone repository:**
git clone <repository_url>
cd HackBioInternship/StageTwoTask/

2. **Create a virtual environment and install dependencies:**
python -m venv venv
**Linux/macOS**
source venv/bin/activate
**Windows**       
venv\Scripts\activate
pip install -r requirements.txt

3. **Download the raw and processed datasets:**
data/raw/bone_marrow.h5ad
data/processed/bone_marrow_processed.h5ad

4. **Open the Notebook:**
`notebooks/bone_marrow_analysis.ipynb`

---

## Step-by-Step Workflow
| Step | Task / Deliverable | Key Analytical Approach |
|------|------------------|------------------------|
| 1    | Data Loading | Load `AnnData` object; verify unique genes & cells. Includes exception handling to catch missing files or I/O errors for robust execution. |
| 2    | Quality Control | Calculate QC metrics, visualize, filter low-quality cells & genes |
| 3    | Doublet Detection | Identify potential doublets using Scrublet; validated by predicted doublet scores and visualization of doublet-enriched cells on UMAP |
| 4    | Normalization & Feature Selection | Normalize counts, log-transform, select top 1000 highly variable genes |
| 5    | Dimensionality Reduction | PCA, neighbor graph, UMAP embedding |
| 6    | Clustering | Leiden clustering at multiple resolutions; parameter tuning explored to optimize cluster separation |
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

**Cluster Variable Interpretation:**
- Some clusters (e.g., Gamma delta T cells) appear in multiple clusters due to heterogeneous expression of stress- or cytokine-related genes.

- T memory and NK cells show variability likely reflecting different activation states or lineage differentiation.

- Observed heterogeneity highlights functional diversity within immune populations.

**Note:** - Leiden clustering was performed at multiple resolutions (0.2, 0.5, 1.0, 2.0) to explore cluster granularity. Resolution 1.0 was chosen for final annotation as it balanced biological interpretability and cluster separation.

---

## Tissue Source Justification

**Evidence supporting bone marrow origin:**
- Presence of **neutrophils** and **platelets**, absent in PBMC preps.
- Diverse **mature hematopoietic lineages**: T cells, B cells, NK cells, monocytes, plasma cells.  

**Exceptions:**  
- Hematopoietic stem and progenitor cells (HSPCs) and erythroid progenitors were not detected, likely due to low abundance or sampling bias.

- Batch effects are minimal; QC metrics show consistent read counts and mitochondrial content across cells.

> **Conclusion:** Sample is consistent with bone marrow, with minor underrepresentation of progenitors. Further validation could be achieved using reference bone marrow datasets.

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

> **Interpretation:** The immune profile indicates **indicates a high relative abundance of T memory and gamma delta T cells**, with both **innate and adaptive cells engaged** (not a healthy baseline), suggesting **possible immune activation**The patient **might be experiencing infection or inflammation**, though confounding factors such as **sampling bias, individual variability, or other pathological states** cannot be ruled out..
---

## Figures

All figures are stored in Figures/ folder. Major figure types include QC plots, PCA analysis, highly variable genes, clustering UMAPs, and cell type annotation plots (dotplots, violin, tracks, heatmaps).

---

## Directory Structure

HackbioInternship/
└── StageTwoTask/
    ├── notebooks/
    │   └── bone_marrow_analysis.ipynb
    ├── data/
    │   ├── raw/
    │   │   └── bone_marrow.h5ad
    │   └── processed/
    │       └── bone_marrow_processed.h5ad
    ├── figures/
    │   ├── Genes_Detected_Per_Cell.png
    │   ├── Total_RNA_Detected_Per_Cell.png
    │   ├── MT_Pct_Counts.png
    │   ├── RIBO_Pct_Counts.png
    │   ├── HB_Pct_Counts.png
    │   ├── stress_doublet_variants/           # folder containing stress/doublet variant plots
    │   ├── PCA_Variance_Ratio.png
    │   ├── PCA_MT_Pct_Counts.png
    │   ├── Highly_Variable_Genes.png
    │   ├── Igraph+Iterations.png
    │   ├── Nearest_Neighbor.png
    │   ├── Umap_Leiden_res_*.png
    │   ├── Umap_Leiden.png
    │   ├── Umap_Double_Doublets.png
    │   ├── Dotplot_CellType.png
    │   ├── Stacked_Violin_CellType.png
    │   ├── Matrixplot_CellType.png
    │   ├── Heatmap_CellType.png
    │   ├── Tracksplot_CellType.png
    │   ├── Bcells_Leiden_res_1_0.png
    │   ├── Bcells_Violin_Leiden_res_1_0_Plot.png
    │   ├── Filtered_MT_Pct_Counts.png
    │   └── ...other figures
    └── README.md

---

## Reproducibility Notes
- All steps can be rerun from `notebooks/bone_marrow_analysis.ipynb`.  
- Package versions ensure consistent outputs.  
- Data and results are organized for easy replication or extension.

---

## Summary
- Complete workflow: **QC → normalization → clustering → annotation → visualization**.  
- Tissue source: **bone marrow**, with active immune cell composition.  
- Observed clusters indicate both **innate and adaptive immune activation**, consistent with **infection or inflammatory response**.
- Cluster variability reflects **functional heterogeneity**  within immune populations.
- Clustering parameters were tuned to optimize biological relevance and reproducibility.