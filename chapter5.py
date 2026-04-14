import time
import datetime

# Tổng số giây từ Enpoch (01/01/1970)
total_second = time.time()

# Tính số ngày đã trôi qua 
day= int(total_second // (24*60*60) )

# Lấy thời gian hiện tại theo GMT 
current_time = datetime.datetime.utcfromtimestamp(total_second)

#in kết quả
print(f"tổng số giây từ Enpoch: {total_second}")
print(f"Số ngày đã trôi qua: {day} ngày")
print(f"Thời gian hiện tại (GMT): {current_time.strftime('%H:%M:%S')}")
