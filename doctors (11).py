# Hospital Management

import pandas as pd
import matplotlib.pyplot as plt

def showdoctors():
    dtf=pd.read_csv('medical.csv')
    dtf.to_csv('medical.csv',header=True,index=False)
    print(dtf)
    input('Press Enter For Choices')
  
def adddoctors():
    d_id=int(input('Enter D_ID'))
    name=input('Enter Name')
    branch=input('Enter Branch')
    blood_group=input('Enter Blood Group')
    salary=int(input('Enter Salary'))
    dtf=pd.read_csv('medical.csv')
    dtf.loc[len(dtf.index)]=[d_id,name,branch,blood_group,salary]
    dtf.to_csv('medical.csv',header=True,index=False)  
    
    input('Press Enter For Choices')

def deletedoctors():
    dtf=pd.read_csv('medical.csv')
    n=input('Enter Name to Delete')
    dtf=dtf[dtf['Name']!=n]
    dtf.to_csv('medical.csv',header=True,index=False)
    input('Press Enter For Choices')

def editdoctors():
     dtf=pd.read_csv('medical.csv')
     dtf=pd.read_csv('medical.csv')
     n=input('Enter Name to Edit Branch ')
     index=dtf[dtf['Name']==n].index
     dtf.loc[index,'Branch']=input('Enter New Branch ')
     dtf.to_csv('medical.csv',header=True,index=False)
     input('press enter for choices')

def showdoctorgraph():
    dtf=pd.read_csv('medical.csv')
    dtf.plot()
    plt.title('Doctor Record')
    plt.show()

def showpatients():
    dtf=pd.read_csv('patients.csv')
    dtf.to_csv('patients.csv',header=True,index=False)
    print(dtf)
    input('Press Enter For Choices')

def addpatient():
    p_id=int(input('Enter Patient ID'))
    p_name=input('Enter Patient Name')
    p_branch=input('Enter Branch of Patient')
    p_dob=input('Enter DOB')
    treatment_fees=int(input('enter fees'))
    dtf=pd.read_csv('patients.csv')
    dtf.loc[len(dtf.index)]=[p_id,p_name,p_branch,p_dob,treatment_fees]
    dtf.to_csv('patients.csv',header=True,index=False)

def deletepatient():
    dtf=pd.read_csv('patients.csv')
    n=input('Enter Name to Delete')
    dtf=dtf[dtf['P_Name']!=n]
    dtf.to_csv('patients.csv',header=True,index=False)
    
    input('Press Enter For Choices')

def editpatients():
    dtf=pd.read_csv('patients.csv')
    n=input('Enter name to edit branch ')
    index=dtf[dtf['P_Name']==n].index
    dtf.loc[index,'P_Branch']=input('Enter new branch ')
    dtf.to_csv('patients.csv',header=True,index=False)
    input('press enter for choices')

def showpatientgraph():
    dtf=pd.read_csv('patients.csv')
    dtf.plot()
    plt.title('Patient Record')
    plt.show()    
    
     
    
print('================================HOSPITAL MANAGEMENT===============================')
while True:
    print('''
1. For Show Doctor Details
2. For Add New Doctor
3. For Delete Doctor Record
4. For Graph Of Doctors
5. For Edit Doctor Details
6. For Show Patient Details
7. For Add New Patient
8. For Delete Patient Record
9. For Graph of Patient
10.For Edit Details of Patient 
11.For Exit''')
    choice=int(input('Enter Your Choice'))
    if choice==1:
        showdoctors()
    elif choice==2:
        adddoctors()
    elif choice==3:
        deletedoctors()
    elif  choice==4:
        showdoctorgraph()
    elif choice==5:
        editdoctors()
    elif choice==6:
        showpatients()
    elif choice==7:
        addpatient()
    elif choice==8:
        deletepatient()
    elif choice==9:
        showpatientgraph()
    elif choice==10:
        editpatients()
    elif choice==11:
        break

       
       
               
