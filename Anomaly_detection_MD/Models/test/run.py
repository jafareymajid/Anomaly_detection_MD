import os
import shutil #to copy files and directories
import time, datetime
"""
This program creates a directory and copies the required files for simulations in it.
It then runs tleap to make AMBER input files, gives some information about the system using ParMed,
and finally runs the simulation.
"""
#Creat a directory and copy the required files for simulations in it
today=datetime.date.today()
modelstr='run_' + today.isoformat()
path=os.getcwd()
path1=os.getcwd() +'/'+'Source_files'
path2=os.getcwd() +'/'+ modelstr
isdir=os.path.isdir(path2)
def mkdir_func(x,y,z):
    """
    This function is used to create a directory.
    """
    y=os.getcwd() +'/'+ x
    z=os.path.isdir(y)
    if z:
        shutil.rmtree(x) #to remove non empty directory
        os.mkdir(x)
    else:
        os.mkdir(x)
    print(f"Directory {x} is created.")
    
    time.sleep(2)
def main():
    """
    This function copies the file from the source path to the destination path.
    """
    mkdir_func(modelstr,path2,isdir)
    for files in os.listdir(path1):
#defines the files path
        source=path1 + '/' + files
        dest= path2 + '/' + files
#copy files
        if os.path.isfile(source):
            shutil.copy(source, dest)
            print(f"{files} is copied to the {modelstr} directory!")
        else:
            print(f"{files}: No such file or directory!")
    time.sleep(1)
        #run tleap to make AMBER input files
    print("Preparing your system using tleap...")
    os.chdir(path2)
    os.system("tleap -s -f tleap.in > tleap.out")
    #os.system("ambpdb -p protein.parm7 < protein.rst7 > protein_amb.pdb")
    time.sleep(1)
    #give some information about the system
    print("Running ParMed to get your system information...")
    time.sleep(2)
    parmd=open("parmd.in", "w")
    print("parm protein.parm7", file=parmd)
    print("summary", file=parmd)
    parmd.close()
    os.system("parmed -i parmd.in")
    #run the simulation
    print("Running the minimization step using sander...")
    time.sleep(3)
    ########os.popen(command).read(): waits until the outputs of the previous command are created.
    os.popen("sander -O -i min.in -o min.out -p protein.parm7 -c protein.rst7 -ref protein.rst7 -r min.rst7 -inf min.mdinfo -x min.nc").read()
    print("The minimization step is finished. Running the heating step...")
    os.popen("sander -O -i heat.in -o heat.out -p protein.parm7 -c min.rst7 -ref protein.rst7 -r heat.rst7 -inf heat.mdinfo -x heat.nc").read()
    print("The heating step is finished. Running the equilibration step...")
    os.popen("sander -O -i eq.in -o eq.out -p protein.parm7 -c heat.rst7 -ref protein.rst7 -r eq.rst7 -inf eq.mdinfo -x eq.nc").read()
    print("The equilibration step is finished. Running the production step...")
    os.popen("sander -O -i md.in -o md.out -p protein.parm7 -c eq.rst7 -ref protein.rst7 -r md.rst7 -inf md.mdinfo -x md.nc").read()
    print("The simulation is finished.")
    os.chdir(path) #go back to the home directory
    #pass
if __name__ == '__main__':
  main()