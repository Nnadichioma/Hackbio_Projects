# **What Single-Cell Data Is Teaching Us About Cancer Evolution**

# **Introduction** 

Cancer is not a single disease but a constantly changing collection of cell types that evolve and adapt to survive. Tumour evolution occurs as cells acquire genetic and epigenetic changes, forming distinct subgroups or “subclones” (Andor et al., 2015). These subclones interact with each other and with their surrounding environment, creating a diverse and dynamic ecosystem within the tumour (Ciriello et al., 2023). The more diverse a tumour becomes, the harder it is to treat, and studies show that cancers with many subclones often have poorer outcomes (Cosgrove et al., 2024).

Traditional genetic tools have advanced our understanding of cancer but provide only an average view of all the cells in a tumour. This masks the subtle yet critical differences between individual cells. Single-cell RNA sequencing (scRNA-seq) overcomes this limitation by analysing gene activity in each cell separately, revealing which cells drive tumour growth, resist therapy, or interact with neighbouring cell types (Andor et al., 2015).

The technology behind this breakthrough has evolved rapidly. Early single-cell methods could examine only a few cells at a time, whereas modern droplet-based systems like 10x Genomics now profile thousands of cells in a single run (Wang et al., 2023). Enhancements such as Smart-seq3 have improved accuracy (Tieng et al., 2025), while spatial transcriptomics techniques like MERFISH and Slide-seq allow scientists to map where each cell sits within the tissue (Williams et al., 2022). Integrating single-cell RNA data with genomic, proteomic, and epigenomic information now offers an unprecedented view of tumour ecosystems (Catalano et al., 2025).

Through this new lens, cancer is no longer seen as a uniform mass but as a living, evolving community of diverse cells. This essay, therefore, examines how single-cell data have transformed our understanding of cancer evolution, revealing that cancers evolve not in isolation but through continuous molecular dialogue within a dynamic ecosystem.

# **Heterogeneity, Resistance, and Evolution**

Every tumour is unique. Within the same tumour, some cells divide rapidly, some remain dormant, and others adapt to survive treatments. This diversity, known as heterogeneity, is the fuel for cancer evolution (Sun 2015; Dentro et al., 2021). It exists at multiple levels: genetic differences (mutations), molecular changes (gene expression), and environmental influences (the surrounding tissue and immune cells).

scRNA-seq has shown that cancer cells resist treatment not only through permanent genetic mutations but also through flexibility. Under stress, they can alter their identity, a process known as **cellular** **plasticity**, to survive and later revert to their original state once the treatment ends (Niu et al., 2024). The tumour microenvironment (TME), the collection of immune, stromal, and vascular cells surrounding the tumour, supports this adaptability. It can limit drug penetration and shield cancer cells from attack (Sun, 2015). Using scRNA-seq, scientists have discovered that these interactions are complex conversations between cells,  signals that determine which cells live, die, or adapt (Watson et al., 2013). In short, cancer evolves not in isolation but as an interconnected, communicating system.

# **Mapping Tumour Heterogeneity through scRNA-seq** 

Thanks to scRNA-seq, scientists can now “see” the complexity within tumours that was previously hidden. Each cancer contains layers of diversity:

* **Genetic heterogeneity:** Subclones carry distinct mutations, forming evolutionary lineages.  
* **Transcriptomic heterogeneity:** Even genetically identical cells adopt different gene expression states, such as proliferative versus quiescent.  
* **Microenvironmental heterogeneity:** Interactions with immune and stromal cells shape spatial and functional diversity.

## **How scRNA-seq Maps Heterogeneity**

When using scRNA-seq in tumour studies, the tumour tissue is dissociated into single cells, their transcriptomes are then captured and analysed by dimensionality reduction (UMAP/t-SNE), clustering, and trajectory inference. The result we get is a map of cell populations: malignant epithelial clusters, immune and stromal clusters, and rare subsets. Computational analysis may help us see pseudotime of cell states, detect copy-number variation signatures in scRNA data to infer subclones, and compute cell-cell interaction networks via ligand-receptor pairing. Through this, we can identify:

* distinct subclones of cancer cells  
* plastic transitions  
* rare or emergent populations  
* diverse microenvironment niches (immune, stromal, vascular) that correlate with tumour behaviour.

## **Key Findings Across Tumour Types**

scRNA-seq has revealed critical patterns of heterogeneity and adaptation across multiple cancers:

* **Breast cancer**: NK cells, once thought homogeneous, were shown to comprise six subtypes with distinct functions, while malignant epithelial cells varied by gene expression and tumour program — revealing hidden complexity in immune and cancer compartments.  
* **Ovarian cancer**: Tumours with high stromal content showed exclusion of CD8⁺ and NK cells and were enriched in CXCL12⁺ fibroblasts and immunosuppressive Tregs. CAFs engaged in immune modulation via the NECTIN2–TIGIT axis.  
* **Pancreatic cancer (PDAC)**: Chemotherapy remodelled the TME more than tumour epithelium, enriching metallothionein⁺ CAFs and reshaping immune–stromal signalling.  
* **Lung cancer**: Transcriptional heterogeneity correlated with neutrophil infiltration and patient outcomes; distinct immune–stromal phenotypes stratified disease subtypes.  
* **Leukaemia**: scRNA-seq tracked relapse-predictive immune niches in paediatric AML and identified therapy-persistent blast states with active PD-1 signalling in T-ALL.

By separating tumours into their individual components, scRNA-seq can identify rare cells that drive relapse, track how treatment changes cell states, and map the microenvironment that supports cancer growth. Across cancers, these studies reveal the same principle: diversity fuels evolution.

# **What scRNA-seq data is revealing about Resistance** 

Cancer therapy often fails not because treatments are ineffective, but because tumours evolve. Single-cell RNA sequencing (scRNA-seq) has shown that resistance is not simply genetic — it is ecological and adaptive, shaped by dynamic, reversible changes in cell state and microenvironmental interactions.

scRNA-seq has uncovered several key mechanisms behind resistance:

* Epithelial–Mesenchymal Transition (EMT): scRNA-seq reveals how tumour cells adopt mesenchymal traits under stress, enhancing motility and drug resistance. These transitions are not permanent mutations, but plastic states that can reverse once treatment is withdrawn (Huang et al., 2022).  
* Metabolic Reprogramming: Single-cell data shows how subpopulations shift their metabolic profiles (e.g., enhanced glycolysis or lipid metabolism) in response to environmental pressures supporting survival under therapy (Liu et al., 2024).  
* Epigenetic Plasticity: Resistance emerges not just from fixed gene changes, but from flexible chromatin states. scRNA-seq integrated with ATAC-seq and histone profiling has identified slow-cycling, stress-tolerant subclones that evade therapy by entering a reversible dormancy (Mossner et al., 2021).  
* Drug-Tolerant Persister Cells: Perhaps the clearest evolutionary insight, scRNA-seq has traced how rare cells survive therapy by entering a persister state, later reactivating to repopulate the tumour, a classic example of Darwinian selection under pressure (Li et al., 2025).  
* Immune Evasion: scRNA-seq has mapped immune checkpoint expression at single-cell resolution, exposing how tumours sculpt immunosuppressive niches. These are not random but evolutionarily selected microenvironments that shield vulnerable cancer cells (Tufail et al., 2025).  
* Together, these findings shift our view: resistance is not an afterthought of therapy — it is a core part of tumour evolution. And it is scRNA-seq that is teaching us to see it — cell by cell, state by state.

# **Tumour Microenvironment (TME) and Cell \- Cell Interactions** 

A tumour does not exist in isolation; it grows within a complex neighbourhood of non-cancerous cells collectively called the tumour microenvironment (TME), an intrinsic milieu within which tumour cells thrive *(Li, Z., et al., 2025\)*.   
The TME is made of immune cells, fibroblasts, and blood vessels that support or oppose tumour growth (Li et al., 2025; Wang et al., 2021). Together, these cells create a very dynamic microenvironment where they constantly exchange molecular messages, growth factors, cytokines, and chemokines, much like residents negotiating in a noisy city square. Some defend the healthy tissues; others unintentionally help the tumour to survive and resist treatment *(Perez-Moreno, 2009\)*.   
The big question is *‘How can we eavesdrop on the crosstalk, the conversation that keeps cancer alive, to better understand the TME?’* The answer is scRNA sequencing. 

scRNA-seq has revealed this ecosystem in stunning detail by profiling gene expression in thousands of individual cells. For example, scRNA-seq has uncovered: 

* Immune exhaustion signatures, such as PD-1+ T cells and M2 macrophages, create immunosuppressive niches.  
* Fibroblast heterogeneity, with subtypes like CXCL12+ CAFs that recruit immune-suppressive cells and LRRC15+ CAFs that remodel extracellular matrix to block drug access (Deng et al,.2021; Cords et al., 2024).  
* Ligand–receptor networks that reveal “crosstalk” circuits, e.g., CXCL12–CXCR4, PD-L1–PD-1, and TGFB–TGFBR, that help cancer cells evade, adapt, and thrive (Peng et al., 2022).

These findings show that, thanks to scRNA-seq data, we can listen in on the ongoing conversation and target these crosstalk pathways to disrupt the supportive interactions between tumour cells and their microenvironment. *(Li et al., 2022).* scRNA-seq has exposed that cancer evolution is collective. Decoding these interactions gives us more than a list of cell types; it gives us a functional atlas of tumour evolution in context. This offers new strategies for cancer therapy. 

# **Integrating with Multi-Omics and Spatial Data** 

To see the bigger picture, scientists are combining scRNA-seq with spatial technologies that preserve tissue structure (Yan et al., 2024; Xia, 2025). Spatial omics is based on counting transcripts of a gene at a distinct tissue location. In other words, it utilises transcriptomics analysis to analyse expression patterns of genes and cells while maintaining tissue integrity. (Williams et al., 2022\)  However, spatial transcriptomics does not have the high resolution of single-cell sequencing. To understand the role of different cell types within a tissue structure, several integration methods have been developed to combine scRNA sequencing and spatial transcriptomics.

In their study on the *‘Spatial single cell analysis of tumour microenvironment remodelling pattern in primary central nervous system lymphoma’*, Xia Yuan et al. performed spatial transcriptomics and matched the corresponding single-cell sequencing data of primary central nervous system lymphoma  PCNSL patients.

It was found that tumour cells may achieve a “TME remodelling pattern” through an “immune pressure-sensing model”, in which they could choose to reshape the TME into a barrier environment or a cold environment according to the immune pressure. From the integration of spatial transcriptomics with scRNA-seq, they were able to discover the spatial and temporal distribution of and characteristics of immune checkpoint molecules and CAR-T target molecules in immunotherapy through the spatial communication analysis. The data from their study clarified the tumour microenvironment remodelling pattern of PCNSL and provided a reference for immunotherapy treatment options (Xia, Y.,2025). 

Integration methods of scRNA sequencing and spatial omics are divided into two categories: 

* Deconvolution methods applied to spatial barcoding data with scRNA seq data as background.  
* Mapping methods \- uses high-plex RNA imaging data to localise scRNA-seq subpopulations and is more flexible as it doesn’t require previously developed cell subtype models.

In terms of integration with other single-cell omics technologies for a better understanding of cell functions and disease resistance mechanisms, researchers have developed AI models for integration using feature links. 

scRNA-seq generates immense volumes of data, but only gives a snapshot of gene expression. However, computational analysis makes cancer evolution visible. Clustering algorithms like Louvain and Leiden identify tumour subpopulations and rare cell types, revealing the cellular diversity that drives evolutionary branching (Xiang et al., 2022). Tools such as pseudotime analysis and RNA velocity go further, reconstructing how cells transition over time, tracking tumour progression, therapy response, and the emergence of resistant states (Teppei, 2025).

Meanwhile, ligand–receptor inference maps the communication between tumour, immune, and stromal cells,  uncovering ecological interactions that shape cancer evolution (Vahid et al., 2023).

Finally, AI models help detect patterns across thousands of cells, predicting how cancers may adapt to future treatments. AI-powered integration tools like **scMODEL** (Wang, 2025\) merge data from RNA, DNA, and proteins to create a multidimensional view of tumours. This integration helps researchers understand not just which genes are active, but how cells work together in context.

These computational advances make scRNA-seq not just descriptive, but predictive, allowing us to see how tumours evolve, adapt, and survive.

# **Translation and Clinical Implications** 

Single-cell data is not just changing how we study tumours, it’s changing how we treat them. By revealing the cellular and ecological complexity of cancer, **scRNA-seq is unlocking new biomarkers, stratifying patients, and guiding targeted therapies**. 

Single-cell research is already shaping clinical practice. Fibroblast and immune signatures can predict which patients will respond to immunotherapy (Chen et al., 2025; Peng et al., 2025). Combining single-cell data with spatial and genomic analysis helps doctors identify vulnerabilities unique to each tumour. Though challenges remain, such as cost and data complexity-advances in organoid models and AI are rapidly moving these discoveries into hospitals (Rafique et al., 2021).

# **Future Directions and Conclusion**

The next step is prediction: using single-cell data to foresee how a tumour will evolve and tailoring treatments accordingly. To reach this, the field must focus on:

1. **Standardisation**: Harmonising sample prep, sequencing, and analysis to ensure reproducibility across studies.  
2. **4D Cancer Atlases**: Integrating spatial, temporal, and molecular data to trace how tumours evolve under therapy in real time.  
3. **AI Models**: Using deep learning to simulate treatment outcomes based on single-cell profiles, enabling personalised therapy planning before drugs are even administered.

Single-cell data is changing our understanding of cancer evolution. It has taught us that tumours are not uniform masses but dynamic ecosystems, where different cells adapt, interact, and evolve under pressure. Rather than being driven solely by genetic mutations, cancer evolution unfolds through cellular plasticity, ecological cooperation, and spatially organised microenvironment processes that only single-cell resolution can fully reveal.

scRNA-seq shows us that:

* Heterogeneity is the engine of evolution,  not a complication, but the core mechanism.  
* Resistance is adaptive and reversible, emerging from phenotypic shifts rather than fixed mutations.  
* Evolution is ecological, shaped by cell–cell interactions and the tumour microenvironment, not just by internal mutations.

In essence, single-cell data teaches us that cancer evolves like a living system, flexible, contextual, and collaborative. This challenges the linear, mutation-centric model of tumour progression and opens new paths for predicting, intercepting, and ultimately outmanoeuvring cancer’s adaptive strategies.

### **References**

Andor, N., Graham, T.A., Jansen, M., Xia, L.C., Aktipis, C.A., Petritsch, C., Ji, H.P. and Maley, C.C. (2015). Pan-cancer analysis of the extent and consequences of intratumor heterogeneity. *Nature Medicine*, 22(1), pp.105–113. doi:[https://doi.org/10.1038/nm.3984](https://doi.org/10.1038/nm.3984).

Catalano M, D'Angelo A, De Logu F, Nassini R, Generali D, Roviello G. Navigating Cancer Complexity: Integrative Multi-Omics Methodologies for Clinical Insights. Clin Med Insights Oncol. 2025 Oct 21;19:11795549251384582. Doi: 10.1177/11795549251384582. PMID: 41147019; PMCID: PMC12553891.

Chen, M. et al. (2025). Single-cell and bulk RNA-sequencing reveal PRRX2-driven cancer-associated fibroblast-mediated perineural invasion for predicting the immunotherapy outcome in colorectal cancer. Frontiers in Cell and Developmental Biology. https://doi.org/10.3389/fcell.2025.1620388

Ciriello, G., Magnani, L., Aitken, S.J., Akkari, L., Behjati, S., Hanahan, D., Landau, D.A., Lopez-Bigas, N., Lupiáñez, D.G., Marine, J.-C., Martin-Villalba, A., Natoli, G., Obenauf, A.C., Oricchio, E., Scaffidi, P., Sottoriva, A., Swarbrick, A., Tonon, G., Vanharanta, S. and Zuber, J. (2023). Cancer Evolution: A Multifaceted Affair. *Cancer Discovery*, 14(1), pp.OF1–OF13. doi:[https://doi.org/10.1158/2159-8290.CD-23-0530](https://doi.org/10.1158/2159-8290.CD-23-0530).

Cords, L., de Souza, N. and Bodenmiller, B. (2024). Classifying cancer-associated fibroblasts—The good, the bad, and the target. *Cancer Cell*. Doi:[https://doi.org/10.1016/j.ccell.2024.08.011](https://doi.org/10.1016/j.ccell.2024.08.011).

Cosgrove, P.A., Bild, A.H., Dellinger, T.H., Badie, B., Portnow, J. and Nath, A. (2024). Single-Cell Transcriptomics Sheds Light on Tumour Evolution: Perspectives from City of Hope’s Clinical Trial Teams. *Journal of Clinical Medicine*, 13(24), 7507\. doi:[https://doi.org/10.3390/jcm13247507](https://doi.org/10.3390/jcm13247507).

Deng CC, Hu YF, Zhu DH, Cheng Q, Gu JJ, Feng QL, Zhang LX, Xu YP, Wang D, Rong Z, Yang B. Single-cell RNA-seq reveals fibroblast heterogeneity and increased mesenchymal fibroblasts in human fibrotic skin diseases. Nat Commun. 2021 Jun 17;12(1):3709. doi: 10.1038/s41467-021-24110-y. PMID: 34140509; PMCID: PMC8211847.

Dentro, S.C. et al. (2021). Characterising genetic intra-tumour heterogeneity across 2,658 human cancer genomes. *Cell*, 184(8), pp.2239–2254.e39. doi:10.1016/j.cell.2021.03.009.

Huang Y, Hong W, Wei X. The molecular mechanisms and therapeutic strategies of EMT in tumor progression and metastasis. J Hematol Oncol. 2022 Sep 8;15(1):129. doi: 10.1186/s13045-022-01347-8. PMID: 36076302; PMCID: PMC9461252.

Li, Z., Li, J., Bai, X. et al.Tumour microenvironment as a complex milieu driving cancer progression: a mini review. Clin Transl Oncol 27, 1943–1952 (2025). [https://doi.org/10.1007/s12094-024-03697-w](https://doi.org/10.1007/s12094-024-03697-w) 

Li H, Xu W, Cheng W, Yu G, Tang D. Drug-tolerant persister cell in cancer: reversibility, microenvironmental interplay, and therapeutic strategies. Front Pharmacol. 2025 Aug 14;16:1612089. doi: 10.3389/fphar.2025.1612089. PMID: 40894234; PMCID: PMC12391116.

Liaghat, S. et al. (2024) ‘The role of EMT in therapy resistance’, *Frontiers in Oncology*, 14, p. 100234\.

Liu J, Tran V, Vemuri VNP, Byrne A, Borja M, Kim YJ, Agarwal S, Wang R, Awayan K, Murti A, Taychameekiatchai A, Wang B, Emanuel G, He J, Haliburton J, Oliveira Pisco A, Neff NF. Concordance of MERFISH spatial transcriptomics with bulk and single-cell RNA sequencing. Life Sci Alliance. 2022 Dec 16;6(1):e202201701. doi: 10.26508/lsa.. 202201701\. PMID: 36526371; PMCID: PMC9760489. 

Liu S, Zhang X, Wang W, Li X, Sun X, Zhao Y, Wang Q, Li Y, Hu F, Ren H. Metabolic reprogramming and therapeutic resistance in primary and metastatic breast cancer. Mol Cancer. 2024 Nov 21;23(1):261. doi: 10.1186/s12943-024-02165-x. PMID: 39574178; PMCID: PMC11580516.

Liu, X., Zhang, Z., Tan, C. et al. Global trends in machine learning applications for single-cell transcriptomics research. Hereditas 162, 164 (2025). https://doi.org/10.1186/s41065-025-00528-y

Menon, A. et al. (2020) ‘Epigenetic plasticity and reversible dormancy in cancer evolution’, *Nature Reviews Molecular Cell Biology*, 21(12), pp. 747–761.

Niu, X. et al. (2024). Cancer plasticity in therapy resistance: Mechanisms and novel strategies. *Drug Resistance Updates*, 76, 101114\. doi:10.1016/j.drup.2024.101114.

Peng, L., Wang, F., Wang, Z., Tan, J., Huang, L., Tian, X., Liu, G. and Zhou, L. (2022). Cell-cell communication inference and analysis in the tumour microenvironments from single-cell transcriptomics: data resources and computational strategies. *Briefings in Bioinformatics.* Doi:[https://doi.org/10.1093/bib/bbac234](https://doi.org/10.1093/bib/bbac234).

Peng, R., Yu, L., & Xu, B. (2025). Integrating single-cell and bulk RNA sequencing data establishes a cuproptosis-related gene predictive signature in breast cancer. Discover Oncology. [https://doi.org/10.1007/s12672-025-03525-9](https://doi.org/10.1007/s12672-025-03525-9) 

Rafique R, Islam SMR, Kazi JU. Machine learning in the prediction of cancer therapy. Comput Struct Biotechnol J. 2021 Jul 8;19:4003-4017. Doi: 10.1016/j.csbj.2021.07.003. PMID: 34377366; PMCID: PMC8321893. 

Sun, Y. (2015). Tumour microenvironment and cancer therapy resistance. *Cancer Letters*, 380(1), pp.205–215. doi:10.1016/j.canlet.2015.07.044.

Teppei Shimamura, RNA velocity and beyond: Current advances in modelling single-cell transcriptional dynamics, Allergology International, Volume 74, Issue 4, 2025, Pages 525-533, ISSN 1323-8930, [https://doi.org/10.1016/j.alit.2025.08.005](https://doi.org/10.1016/j.alit.2025.08.005). 

Tieng FYF, Lee LH, Ab Mutalib NS. Single-cell RNA-sequencing of circulating tumour cells: A practical guide to workflow and translational applications. Cancer Metastasis Rev. 2025 Oct 6;44(4):75. doi: 10.1007/s10555-025-10293-z. PMID: 41053409; PMCID: PMC12500777.

Timperi, E. and Romano, E. (2023). Stromal circuits involving tumour-associated macrophages and cancer-associated fibroblasts. *Frontiers in Immunology.* Doi:[https://doi.org/10.3389/fimmu.2023.1194642](https://doi.org/10.3389/fimmu.2023.1194642).

Vahid MR, Kurlovs AH, Andreani T, Augé F, Olfati-SDoie R, de Rinaldis E, Rapaport F, Savova V. DiSiR: fast and robust method to identify ligand-receptor interactions at the subunit level from single-cell RNA-sequencing data. NAR Genom Bioinform. 2023 Mar 23;5(1):lqad030. Doi: 10.1093/nargab/lqad030. PMID: 36968431; PMCID: PMC10034587.  

Wang, G., Zhao, J., Lin, Y., Liu, T., Zhao, Y. and Zhao, H. (2025). scMODAL: a general deep learning framework for comprehensive single-cell multi-omics data alignment with feature links. *Nature Communications*, 16(1). doi:[https://doi.org/10.1038/s41467-025-60333-z](https://doi.org/10.1038/s41467-025-60333-z).

Wang, G., Zhao, J., Lin, Y., Liu, T., Zhao, Y. and Zhao, H. (2025). scMODAL: a general deep learning framework for comprehensive single-cell multi-omics data alignment with feature links. *Nature Communications*, 16(1). doi:[https://doi.org/10.1038/s41467-025-60333-z](https://doi.org/10.1038/s41467-025-60333-z).

Wang, S. et al. (2023). The evolution of Single-Cell RNA Sequencing Technology and Application: Progress and Perspectives. *International Journal of Molecular Sciences*, 24(3), 2943\. doi:10.3390/ijms24032943.

Wang, T. et al. (2024). Effect of fibroblast heterogeneity on prognosis and drug response in ovarian cancer (identification of CXCL12-positive fibroblasts associated with chemoresistance). \[Open access\]. DOI available via PubMed Central.

Wang, W., Wang, L., Wang, L., She, J. and Zhu, J. (2021). Examining heterogeneity of stromal cells in tumour microenvironment based on pan-cancer single-cell RNA sequencing data. *Cancer Biology and Medicine.* Doi:[https://doi.org/10.20892/J.ISSN.2095-3941.2020.0762](https://doi.org/10.20892/J.ISSN.2095-3941.2020.0762).

Williams, C.G., Lee, H.J., Asatsuma, T., Vento-Tormo, R. and Haque, A. (2022). An introduction to spatial transcriptomics for biomedical research. *Genome Medicine*, 14(1). doi:[https://doi.org/10.1186/s13073-022-01075-1](https://doi.org/10.1186/s13073-022-01075-1).

Xiang Lin, Haoran Liu, Zhi Wei, Senjuti Basu Roy, Nan Gao, An active learning approach for clustering single-cell RNA-seq data, Laboratory Investigation, Volume 102, Issue 3,2022, Pages 227-235, ISSN 0023-6837,[https://doi.org/10.1038/s41374-021-00639-w](https://doi.org/10.1038/s41374-021-00639-w). 

Xia, Y., Sun, T., Li, G. et al. Spatial single-cell analysis of tumour microenvironment remodelling pattern in primary central nervous system lymphoma. Leukaemia 37, 1499–1510 (2023). [https://doi.org/10.1038/s41375-023-01908-x](https://doi.org/10.1038/s41375-023-01908-x) 

Yan, C., Zhu, Y., Chen, M., Yang, K., Cui, F., Zou, Q. and Zhang, Z. (2024). Integration tools for scRNA-seq data and spatial transcriptomics sequencing data. *Briefings in Functional Genomics*, 23(4), pp.295–302. doi:[https://doi.org/10.1093/bfgp/elae002](https://doi.org/10.1093/bfgp/elae002).

