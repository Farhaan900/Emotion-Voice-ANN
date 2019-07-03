#import os
import librosa
import numpy as np
import csv 
import os
file_name = 'output.wav'
folder = 'audio'


def new_num():
    f=open('number.txt','r')
    num = f.read()
    f.close()
    num2=int(num)+1
    f=open('number.txt','w')
    f.write(str(num2))
    f.close()
    return num2

def parser():
    # function to load files and extract features
    
    file_name = 'output.wav'

    # handle exception to check if there isn't a file which is corrupted
    try:
        # here kaiser_fast is a technique used for faster extraction
        X, sample_rate = librosa.load(file_name, res_type='kaiser_fast') 
        # we extract mfcc feature from data
        mfccs = np.mean(librosa.feature.mfcc(y=X, sr=sample_rate, n_mfcc=40).T,axis=0) 
    except Exception as e:
        print("Error encountered while parsing file: ", file_name)
        print (e)
        return None, None
    
    
    num = new_num()
    feature = mfccs.tolist()
    #label = row.Class
    
    feature.insert(0,num)
    
    while 1 :
        print ("gender \n1> male\n2> female \n" )
        gender = input("enter gender code : ")
        if gender > '2' or gender < '1' :
            continue
            exit()
        else :
            break 
    while 1 :
        print ("emotions \n1> Happy\n2> Sad\n3> Angry\n4> surprised\n5> fear" )
        code = input("enter emotion code : ")
        if code > '7' or code < '1' :
            continue
            exit()
        else :
            break 
            
        
    
    feature.insert(41,int(gender)-1)
    for i in range(42,45) :
        if(i != int(code)+41) :
            feature.insert(i,0)
        else :
            feature.insert(42,1)
     
    print (feature)
    #return [feature, label]
    
    
    
    outfile = open("pidx.csv","a",newline='')
    out = csv.writer(outfile)
    out.writerow(feature)
    outfile.close()
    dest=os.path.join(folder,str(num)+'.wav')
    print (dest)
    os.rename(file_name,dest)
#temp = train.apply(parser, axis=1)
#temp.columns = ['feature', 'label']

