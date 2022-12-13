from run import *

####create the analysis directory###
analysis_str="analysis_" + today.isoformat()
path3=os.getcwd() + '/' + analysis_str
isdir=os.path.isdir(path3)

def main():
    """
    The main function for the analysis.py script. 
    It takes the path of the simulation and analysis directories as the argument
    and calculates the RMSD of the PDB files and creates an RMSD graph.
    """
    #Copy the required files to the analysis directory if it doesn't exist
    mkdir_func(analysis_str,path3,isdir)
    modelstr='run_' + today.isoformat()
    path2=os.getcwd() +'/'+ modelstr
    amber_out_dict={
    'md_traj':path2 + '/' + 'md.nc',
    'md_rst':path2 + '/' + 'md.rst7',
    'md_parm':path2 + '/' + 'protein.parm7',
    'des_traj':path3 + '/' + 'md.nc',
    'des_rst':path3 + '/' + 'md.rst7',
    'des_parm':path3 + '/' + 'protein.parm7'
    }
    if os.path.isfile(amber_out_dict.get('md_traj')):
        shutil.move(amber_out_dict.get('md_traj'), amber_out_dict.get('des_traj'))
        print(f"The trajecotry file is being moved to the {analysis_str} directory!")
    else:
        print(f"md.nc: No such file or directory!")
    time.sleep(3)
    if os.path.isfile(amber_out_dict.get('md_rst')):
        shutil.move(amber_out_dict.get('md_rst'), amber_out_dict.get('des_rst'))
        print(f"The restart file is being moved to the {analysis_str} directory!")
    else:
        print(f"md.rst7: No such file or directory!")
    time.sleep(3)
    if os.path.isfile(amber_out_dict.get('md_parm')):
        shutil.copy(amber_out_dict.get('md_parm'), amber_out_dict.get('des_parm'))
        print(f"The parameter file is copied to the {analysis_str} directory!")
    else:
        print(f"protein.parm7: No such file or directory!") 
    time.sleep(3)
    ####Do the analyses####
    
    #####create cptraj1.in#####
    os.chdir(path3)
    cptraj1=open('cptraj1.in', 'w')
    print('parm protein.parm7', file=cptraj1)
    print('trajin md.nc', file=cptraj1)
    print('rms ToFirst @CA= first out rmsd.txt mass', file=cptraj1)
    print('run', file=cptraj1)
    print('quit', file=cptraj1)
    cptraj1.close()
    
    ####create cptraj2.in######	
    
    cptraj2=open('cptraj2.in', 'w')
    print('parm protein.parm7', file=cptraj2)
    print('trajin md.nc', file=cptraj2)
    print('rms ToFirst @CA= first out rmsd.agr mass', file=cptraj2)
    print('run', file=cptraj2)
    print('quit', file=cptraj2)
    cptraj2.close()
    
    time.sleep(2)
    
    path4=path3+'/'+'rmsd.txt'
    path5=path3+'/'+'rmsd.agr'
    
    os.popen('cpptraj -i cptraj1.in').read()
    if os.path.isfile(path4):
        print("The rmsd.txt file is successfully created.")
        time.sleep(3)
    else:
        print(f"Something went wrong with cpptraj, please check the input files in the {analysis_str} direcotry.")
        time.sleep(3)
    
    os.popen('cpptraj -i cptraj2.in').read()
        
    if os.path.isfile(path4):
        print("The rmsd.agr file is successfully created.")
        time.sleep(3)
    else:
        print(f"Something went wrong with cpptraj, please check the input files in the {analysis_str} direcotry.")
        time.sleep(3)
    os.chdir(path)
    pass
if __name__ == '__main__':
  main()