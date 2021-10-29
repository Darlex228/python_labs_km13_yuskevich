import re

pose_estimation = "[BodyPart:0-(0.55, 0.17) score=0.81 BodyPart:1-(0.49, 0.27) score=0.85 BodyPart:2-(0.41, 0.26) score=0.67 BodyPart:3-(0.33, 0.37) score=0.72 BodyPart:4-(0.36, 0.48) score=0.78 BodyPart:5-(0.58, 0.27) score=0.81 BodyPart:6-(0.65, 0.38) score=0.88 BodyPart:7-(0.62, 0.48) score=0.86 BodyPart:8-(0.43, 0.48) score=0.60 BodyPart:9-(0.43, 0.66) score=0.67 BodyPart:10-(0.53, 0.79) score=0.56 BodyPart:11-(0.53, 0.48) score=0.56 BodyPart:12-(0.59, 0.66) score=0.75 BodyPart:13-(0.49, 0.80) score=0.50 BodyPart:14-(0.54, 0.15) score=0.73 BodyPart:15-(0.56, 0.15) score=0.85 BodyPart:16-(0.48, 0.16) score=0.81 BodyPart:17-(0.83, 0.18) score=0.79]"

patern1 = re.compile(r'\d.\d{2},\s\d.\d{2}')
patern2 = re.compile(r'=\d.\d{2}')
list_1 = re.findall(patern1, pose_estimation)
list_2 = re.findall(patern2, pose_estimation)

list_out = list()
for i in range(len(list_1)):
    list_1_temp = list(map(str, list_1[i].split()))
    list_1_temp[0] = float(list_1_temp[0][:-1])
    list_1_temp[1] = float(list_1_temp[1])
    list_out.append(list_1_temp[0])
    list_out.append(list_1_temp[1])
    list_2[i] = float(list_2[i][1:])
print('points =', *list_out)
print('scores =', *list_2)