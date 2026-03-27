cidade = [
    [1, 0, 2, 0, 1],  
    [0, 9, 2, 1, 3],  
    [1, 0, 1, 9, 2],  
    [9, 3, 0, 2, 1],  
    [0, 1, 2, 0, 9]
    ]
ruavazia=0
csresidencial=0
hospital=0
geradordeemergencia=0
areadestruida=0
for i in list(range(len(cidade))):
    for n in range(len(cidade[i])):
       # print(cidade[i][n]) 
       
        if cidade [i][n]==0:
            ruavazia+=1
        if cidade [i][n]==1:
            csresidencial+=1
        if cidade [i][n]==2:
            hospital+=1
        if cidade [i][n]==3:
            geradordeemergencia+=1
        if cidade [i][n]==9:
            areadestruida+=1
            
print (f"Casas: {csresidencial}  |  Hospitais: {hospital}  |  Geradores: {geradordeemergencia}  |  Áreas destruídas: {areadestruida}") 
