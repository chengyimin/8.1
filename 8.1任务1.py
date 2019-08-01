# 读写csv文件
import csv
datas = [
["   姓名""   年龄""   性别"],
["  程伊旻""   21""    男"],
["   许景""    1""     男"],
["  马雪迪""   2""     男"],
["  尤赛赛""   3""     男"],
["   蔡婧""    4""     女"]
] 
with open("F:\\python project\\test1.csv", "w", encoding="utf-8") as csvfile:    
    writer  = csv.writer(csvfile)    
    for row in datas:        
        writer.writerow(row)

