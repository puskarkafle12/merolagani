import json
# Opening JSON file 
f = open('data.json','r') 
  
# returns JSON object as  
# a dictionary 
data = json.load(f) 
  
# Iterating through the json 
# list 
print(f)
for i in data:
        try:
            if(sector=='')
            if float(float(i['pe_ratio'])<15 and float(i['pe_ratio'])>5):
                    print(str(i['eps'])+"  "+i['company_name']+"pe : "+i['pe_ratio'])
        except:
            print("failed company name ::"+ i['company_name'])

f.close()