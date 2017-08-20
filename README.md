## Welcome to the AIRR Minimal Standards Working Group

### Introduction

The Minimal Standards Working Group has created experimental metadata standards to describe how AIRR-Seq data are generated and evaluated for quality. These metadata include clinical and demographic data on the subjects, sample information, cell phenotypes, nucleic acid purification, immune receptor amplification, sequencing library preparation, sequencing protocol, deposition of the raw sequencing data, and documentation of the computational pipelines used to generate the processed data. A Guidelines Manuscript is being prepared that outlines the set of metadata recommended for submission of AIRR-Seq data for publication or curation in an AIRR-compliant public data repository.

### Members
Syed Ahmad, Chan Bukhari, Brian Corrie, Bjoern Peters, Bojan Zimonja, Chaim Schramm, Christian Busse, Corey Watson, Encarnita Mariotti-ferrandiz, Felix Breden, Florian Rubelt, Jean Büerckert, Jerome Jaglale, Lindsay Cowell, Eline Luning Prak (co-chair), Marie-paule Lefranc, Nishanth Marthandan, Richard Bruskiewich, Scott Boyd, Scott Christley, Uri Hershberg, Steven Kleinstein (co-chair), Uri Laserson, William Faison


![Image](https://github.com/airr-community/airr-standards/blob/master/Images/accepted-data-elements.png)

### <a href="https://github.com/airr-community/airr-standards/raw/master/AIRR%20Minimal%20Standard%20Data%20Elements.xlsx"><img src="https://github.com/airr-community/airr-standards/blob/master/Images/download.png" alt="download"  height="75" width="75"/></a>   AIRR Community Accpted Elements  
<hr>

### AIRR data submission to BioProject, BioSample and SRA

<hr>
The National Center for Biotechnology Information (NCBI) repositories constitute a major public resource for sharing diverse types of biomedical data. These repositories provide the necessary infrastructure for researchers to submit experimental data and associated metadata as part of the science-dissemination process. AIRR Minimal Standards WG has developed templates to submit AIRR data to the NCBI's BioProject, BioSample, Sequence Read Archive and GenBank (Figure below).


<img src="https://github.com/airr-community/airr-standards/blob/master/Images/airr-ncbi.png" alt="airr-ncbi" />

Follwoing is a tutorial to submit AIRR data to the NCBI

1. Go to https://submit.ncbi.nlm.nih.gov/subs/sra/ and login with your NCBI account (create an account if necessary).

2. Click on "create new submission". You will see a form as below. Fill the form with required information and click on "continue".

<img src="https://github.com/airr-community/airr-standards/blob/master/Images/manual1.png" alt="airr-ncbi" />

3. If you are submitting for the first time, check “Yes” on the "new BioProject" or "new BioSample" options to create a new project or BioSample, respectively.

<img src="https://github.com/airr-community/airr-standards/blob/master/Images/manual2.png" alt="airr-ncbi" />

4. Fill in the project information. Add as much relevant information you can add in description. It will help later in searching the particular submission.

<img src="https://github.com/airr-community/airr-standards/blob/master/Images/manual3.png" alt="airr-ncbi" />

5- The AIRR templates are not yet listed on the NCBI website. NCBI compliant AIRR templates can be download in the download section of this repository.
NCBI allows both web-based and command-line submissions and accepts .tsv files (for web-based submission) and XML (for bulk submission through command line and FTP). AIRR Minimal Standards WG is providing NCBI compliant AIRR templates  for the both types of submissions.
<a href="https://github.com/airr-community/airr-standards/raw/master/NCBI%20Templates/AIRR_BioSample_v1.0.xls">AIRR_BioSample_v1.0</a> and <a href="https://github.com/airr-community/airr-standards/raw/master/NCBI%20Templates/AIRR_SRA_v1.0.xls">AIRR_SRA_v1.0</a> are the templates (blank)  for the BioSample and SRA that you can fill-up using MS Excel. People had some difficulty in editing the files therefore we kept the MS Excel as default software to edit but **you must need to save the templates in .tsv format prior to upload at the NCBI**. 

### Filled AIRR-NCBI Metadata Examples   <a href="https://github.com/airr-community/airr-standards/blob/master/Filled_NCBI_Templates/F_AIRR_BS.tsv">BioSample</a>  <a href="https://github.com/airr-community/airr-standards/blob/master/Filled_NCBI_Templates/F_AIRR_SRA.tsv">SRA</a>

### Detailed Documentation about AIRR seq data specification can be viewed and download here <a href="https://www.overleaf.com/8640205fsmvkppdygzb#/30770054/"><img src="https://github.com/airr-community/airr-standards/blob/master/Images/download.png" alt="download"  height="75" width="75"/></a>

### Bulk Data Submission (An example based solution)

In case you are planning to populate the AIRR template files programmatically, please use <a href="https://github.com/airr-community/airr-standards/blob/master/NCBI-XML%20Templates/AIRR_BS_SRA_v1.0.xml"> AIRR_BS_SRA_v1.0.xml</a> file (its filled with dummy data).

### How to cite?

To be updated

### Support or Contact

If you are interested to know more about AIRR Standards or looking for help in NCBI templates. Please create an issue or send email to Ahmad
<a href="mailto:ahmad.chan@yale.edu">Syed **Ahmad** Chan Bukhari</a> or <a href="mailto:steven.kleinstein@yale.edu">Steven Kleinstein</a>
