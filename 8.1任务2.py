# 读写json文件
import json
file = open("test2.json","w",encoding="utf-8")
message = {"name":"fang","age":12,"sex":"male"}
json.dump(message,file,ensure_ascii=False)
file.close()
file = open("test2.json","r",encoding="utf-8")