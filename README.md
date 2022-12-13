About this software
=======
Molecular dynamics simulations are used to study the thermodynamic and dynamical behavior of molecules and their aggregates. In a typical simulation, the positions of all the atoms in the system are tracked at each time step. This produces a very large number of data points, which can be used to identify anomalous behavior. For example, if a molecule suddenly starts moving faster than expected, this could be an indication of an anomaly. Alternatively, if the distribution of atom positions suddenly changes, this could be a sign of an anomaly.
In this project, the Isolation Forest algorithm is used to detect anomalies/outliers in Molecular Dynamics Simulation results (RMSD). 

Authors
=======
Majid Jafari, 

Department of Biochemistry and Molecular Biology, Michigan State University

Installation
=======
**Requirements:**
	
	- Python 3.7 or above
	- Numpy
	- Matplotlib
	- Ambertools
	- ParmEd
	- Scikit-learn
	
**First way (Simple and fast):**

All you need to do is to run the following, it creates a new conda environment in the "envs" directory with the name "envs" and installs all the packages specified in the requirements.yml file (all the packages that you need to run the program). It then activates the newly created environment.

`conda env create --prefix ./envs --file requirements.yml`

`conda activate ./envs`

Make sure you put the requirements.yml file in the current directory (repo directory) so conda can find it.


**Second way:**

1. The code below creates a new conda environment with the specified packages installed in the directory specified by the "--prefix" flag. In this case, the environment will be located in the directory "./envs" and will include the packages python, matplotlib, and numpy. It then activates the environment, so that any packages installed in the environment can be used.

`conda create --prefix ./envs python matplotlib numpy`

`conda activate ./envs`

2. After you activate the new environment, run one of the following:

`conda install -c conda-forge ambertools`

`conda install -c "conda-forge/label/cf202003" ambertools`

This code installs the Ambertools software package onto your new environment.

3. The following will install the ParmEd library (Python-based molecular environment manipulation and analysis toolkit) into the current conda environment.

`conda install -c conda-forge parmed`


4. The code below will install the scikit-learn, numpy, and matplotlib libraries or upgrade it to the latest version, if it is installed on the system.

`pip install -U scikit-learn`

`pip install numpy`

`conda install matplotlib`


To deactivate or remove the new environment (envs): 

`conda deactivate`

`rm -rf ./envs`

Testing
=======

This program is only tested on Linux operating system (Ubuntu and Mint distributions). The current program uses sander to run the simulations. So, if you want to run the simulations on GPU you should specify the path to the `pmemd.cuda` executable istead of `sander` in lines 64-70 of the `run.py` script.

You can detect outliers for other numerical data like RMSF and Rg. To do that, you can change the command line in **line 44** of the **analysis.py** to the command line of interest. Please note that in the script I used **CPPTRAJ** to do the analyses. So, make sure to use the cpptraj command lines.

**Important notes:**

	- You should modify the tleap.in file in the source folder based on your simulation system.
	- You should change the min.in, heat.in, eq.in, and md.in flags based on your simulation system.
	- I used a small peptide to test the scripts. So, make sure to put your protein coordiinates file (pdb file) in the source directory.
	- Please create the input files of your system with the same file names in the source directory.

All you need to do is to run the following command after activating the conda environment:

To use the scripts, you must first activate the conda environment by `conda activate name` and then run:

`python main.py`

It will then continue to do the calculation by using:
 
	- Sander (basic MD engine of AMBER) to perform the simulations.
	- CPPTRAJ to do the analysis (RMSD here).
	- Isolation Forest algorithm to detect anomalies.

You can find all the output and input files of the testing in the Models/test folder. By the way, you can run a test simulation by using the input parameters in the Models/Source_files. You should just navigate to the Models folder and run `python main.py`. The simulation length is 50 ps, just for test purposes. As I mentioned, you should modify the input files based on your simulation system.

Additinal information
=======
**Isolation Forest** is an unsupervised learning algorithm that isolates anomalies by randomly selecting a feature and then randomly selecting a split value between the maximum and minimum values of the selected feature. The algorithm then isolates the anomalies by creating shorter paths for them in the decision tree.

**Scikit-learn** is a Python library for machine learning built on top of NumPy, SciPy and matplotlib. It provides a wide range of tools for data analysis and machine learning, including classification, regression, clustering and model selection algorithms.

**Ambertools** is a suite of programs for molecular mechanics and molecular dynamics simulations, as well as tools for modeling, analysis, and visualization of biopolymers.

