

import sys
sys.setrecursionlimit(8000)

sex=input()
age=int(input())
total_cholesterol=int(input())
smoker=input()
hdl=int(input())
sys_BP=int(input())
medi_status=input()


def genTestCase(sex, age, total_cholesterol, smoker, hdl, sys_BP, medi_status):
    points=0
    if sex =="M":
        if(age<=34):
            points=-9
        elif(age<=39):
            points=-4
        elif(age<=44):
            points=0
        elif(age<=49):
            points=3    
        elif(age<=54):
            points=6
        elif(age<=59):
            points=8
        elif(age<=64):
            points=10        
        elif(age<=69):
            points=11
        elif(age<=74):
            points=12
        elif(age<=79):
            points=13
        ###############################
        if(total_cholesterol<160):
            points+=0
        elif(total_cholesterol<199&age<=39):
            points+=4
        elif(total_cholesterol<199&age<=49):
            points+=3       
        elif(total_cholesterol<199&age<=59):
            points+=2                 
        elif(total_cholesterol<199&age<=69):
            points+=1     
        elif(total_cholesterol<199&age<=79):
            points+=0
        ###################################
        elif(total_cholesterol<239&age<=39):
            points+=7
        elif(total_cholesterol<239&age<=49):
            points+=5       
        elif(total_cholesterol<239&age<=59):
            points+=3                 
        elif(total_cholesterol<239&age<=69):
            points+=1     
        elif(total_cholesterol<239&age<=79):
            points+=0 
        ###################################
        elif(total_cholesterol<279&age<=39):
            points+=7
        elif(total_cholesterol<279&age<=49):
            points+=5       
        elif(total_cholesterol<279&age<=59):
            points+=3                 
        elif(total_cholesterol<279&age<=69):
            points+=1     
        elif(total_cholesterol<279&age<=79):
            points+=0 
        ###################################
        elif(total_cholesterol>280&age<=39):
            points+=11
        elif(total_cholesterol>280&age<=49):
            points+=8       
        elif(total_cholesterol>280&age<=59):
            points+=5                
        elif(total_cholesterol>280&age<=69):
            points+=3     
        elif(total_cholesterol>280&age<=79):
            points+=0 
        ####################################
        if(smoker):
            if(age<=39):
                points+=8
            elif(age<=49):
                points+=5       
            elif(age<=59):
                points+=3                 
            elif(age<=69):
                points+=1     
            elif(age<=79):
                points+=1
        ####################################
        if(medi_status):
            if(sys_BP<=120):
                points+=0
            elif(sys_BP<=129):
                points+=1
            elif(sys_BP<=139):
                points+=2
            elif(sys_BP<=159):
                points+=2 
            elif(sys_BP>=160):
                points+=3   
        else:
            if(sys_BP<=120):
                points+=0
            elif(sys_BP<=129):
                points+=0
            elif(sys_BP<=139):
                points+=1
            elif(sys_BP<=159):
                points+=1 
            elif(sys_BP>=160):
                points+=2
    if(points<1):
        out = "<1"
    elif(points<=4):
        out=1
    elif(points<=6):
        out=2     
    elif(points<=7):
        out=3       
    elif(points<=8):
        out=4
    elif(points<=9):
        out=5
    elif(points==10):
        out=6
    elif(points==11):
        out=8
    elif(points==12):
        out=10    
    elif(points==13):
        out=12      
    elif(points==14):
        out=16
    elif(points==15):
        out=20
    elif(points==16):
        out=25
    elif(points>=17):
        out=">30"
    
    if sex =="F":
        if(age<=34):
            points=-7
        elif(age<=39):
            points=-3
        elif(age<=44):
            points=0
        elif(age<=49):
            points=3   
        elif(age<=54):
            points=6
        elif(age<=59):
            points=8
        elif(age<=64):
            points=10        
        elif(age<=69):
            points=12
        elif(age<=74):
            points=14
        elif(age<=79):
            points=16
        ###############################
        if(total_cholesterol<160):
            points+=0
        elif(total_cholesterol<199&age<=39):
            points+=4
        elif(total_cholesterol<199&age<=49):
            points+= 3     
        elif(total_cholesterol<199&age<=59):
            points+=  2               
        elif(total_cholesterol<199&age<=69):
            points+= 1  
        elif(total_cholesterol<199&age<=79):
            points+=1
        ###################################
        elif(total_cholesterol<239&age<=39):
            points+=8
        elif(total_cholesterol<239&age<=49):
            points+=6       
        elif(total_cholesterol<239&age<=59):
            points+=4                
        elif(total_cholesterol<239&age<=69):
            points+=2     
        elif(total_cholesterol<239&age<=79):
            points+=1 
        ###################################
        elif(total_cholesterol<279&age<=39):
            points+=11
        elif(total_cholesterol<279&age<=49):
            points+=8       
        elif(total_cholesterol<279&age<=59):
            points+=5                 
        elif(total_cholesterol<279&age<=69):
            points+=3     
        elif(total_cholesterol<279&age<=79):
            points+=2 
        ###################################
        elif(total_cholesterol>280&age<=39):
            points+=11
        elif(total_cholesterol>280&age<=49):
            points+=8       
        elif(total_cholesterol>280&age<=59):
            points+=5                
        elif(total_cholesterol>280&age<=69):
            points+=3     
        elif(total_cholesterol>280&age<=79):
            points+=2 
        ####################################
        if(smoker):
            if(age<=39):
                points+=9
            elif(age<=49):
                points+=7       
            elif(age<=59):
                points+=4                 
            elif(age<=69):
                points+=2    
            elif(age<=79):
                points+=1
        ####################################
        if(medi_status):
            if(sys_BP<=120):
                points+=0
            elif(sys_BP<=129):
                points+=3
            elif(sys_BP<=139):
                points+=4
            elif(sys_BP<=159):
                points+=5
            elif(sys_BP>=160):
                points+=6   
        else:
            if(sys_BP<=120):
                points+=0
            elif(sys_BP<=129):
                points+=1
            elif(sys_BP<=139):
                points+=2
            elif(sys_BP<=159):
                points+=3 
            elif(sys_BP>=160):
                points+=4  
    if(points<=12):
        out=1
    elif(points<=14):
        out=2   
    elif(points<=15):
        out=3       
    elif(points<=16):
        out=4
    elif(points<=17):
        out=5
    elif(points==18):
        out=6
    elif(points==19):
        out=8
    elif(points==20):
        out=11    
    elif(points==21):
        out=14      
    elif(points==22):
        out=17
    elif(points==23):
        out=22
    elif(points==24):
        out=27
    elif(points>=25):
        out=">30"

    print(
        f"sex:{sex} age:{age} cho:{total_cholesterol} smo:{smoker} hdl:{hdl} sbp:{sys_BP} med: {medi_status} out:{out}",
        end="\n",
    )
    # if (age) <= 79:
    #     if sys_BP <= 160:
    #         sys_BP +=10
    #         return genTestCase(sex, age, total_cholesterol, smoker, hdl, sys_BP, medi_status)
    #     if(hdl<=60):
    #         sys_BP=119
    #         hdl+=10
    #         return genTestCase(sex, age, total_cholesterol, smoker, hdl, sys_BP, medi_status)

    #     if (smoker=="N"):
    #         smoker="Y"
    #         sys_BP=119
    #         hdl=39
    #         return genTestCase(sex, age, total_cholesterol, smoker, hdl, sys_BP, medi_status)

    #     if total_cholesterol<=280:
    #         smoker = "N"
    #         sys_BP=119
    #         hdl=39         
    #         total_cholesterol+=40  
    #         return genTestCase(sex, age, total_cholesterol, smoker, hdl, sys_BP, medi_status)

    #     if(medi_status=="N"):
    #         medi_status="Y"
    #         total_cholesterol=159
    #         smoker = "N"
    #         sys_BP=119
    #         hdl=39
    #         return genTestCase(sex, age, total_cholesterol, smoker, hdl, sys_BP, medi_status)

        
    #     medi_status="N"
    #     total_cholesterol=159
    #     smoker = "N"
    #     sys_BP=119
    #     hdl=39
    #     age += 5
    #     genTestCase(sex, age, total_cholesterol, smoker, hdl, sys_BP, medi_status)


genTestCase(sex, age, total_cholesterol, smoker, hdl, sys_BP, medi_status)
genTestCase(
    "F",
    20,
    159,
    "N",
    40,
    115,
    "N",
)
genTestCase(
    "M",
    1,
    159,
    "N",
    40,
    115,
    "N",
)
# genTestCase("M", 36, 170, "Y", 55, 125, "Y", ">30")

# genTestCase("M", 41, 220, "N", 42, 135, "Y", ">30")
# genTestCase("F", 37, 177, "N", 56, 127, "N", ">30")

# genTestCase("F", 41, 231, "N", 44, 136, "Y", ">30")
# genTestCase("M", 41, 231, "N", 44, 136, "Y", ">30")


# genTestCase("M", 45, 260, "Y", 38, 152, "N", ">30")
# genTestCase("F", 45, 260, "Y", 38, 152, "N", ">30")
