# 載入內建的 Sys 模組並取得資訊
#import sys as system
#print(system.platform)
#print(system.maxsize)
# 建立 geometry 模組，載入使用
#import geometry
#result=geometry.distance(1,1,5,5)
#print(result)
#result=geometry.slope(1,2,5,6)
#print(result)


# 調整搜尋模組路徑
import sys
sys.path.append("modules")
print(sys.path)
print("----------------")
import geometry
print(geometry.distance(1,1,5,5))