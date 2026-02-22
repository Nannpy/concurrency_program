# Concurrency Lab (Thread, Asyncio, Process Pool)

เพื่อศึกษาการทำงานของ Concurrency ใน Python  
โดยทดลองใช้งาน 3 รูปแบบ ได้แก่

1. Thread
2. Asyncio
3. Process Pool

# 1️⃣ Thread Example

## แนวคิด
Thread คือการสร้างเส้นการทำงานย่อยหลายเส้นภายในโปรแกรมเดียว  
เหมาะกับงานประเภท I/O-bound (งานที่ต้องรอ เช่น network, file, sleep)

## การทำงานของโค้ด
- สร้างฟังก์ชัน `task()` ให้พิมพ์ข้อความเริ่มต้น
- หน่วงเวลาด้วย `time.sleep()`
- พิมพ์ข้อความเมื่อทำงานเสร็จ
- สร้าง thread 3 ตัว (A, B, C)
- ใช้ `.start()` เพื่อเริ่มทำงาน
- ใช้ `.join()` เพื่อรอให้ทุก thread ทำเสร็จ

## สิ่งที่สังเกตได้
- งานทำงานพร้อมกัน
- ลำดับการเสร็จขึ้นอยู่กับเวลาที่ delay
- โปรแกรมจะรอจนทุก thread เสร็จก่อนพิมพ์ `All done`

# 2️⃣ Asyncio Example

## แนวคิด
Asyncio คือการทำงานแบบ Asynchronous โดยใช้ event loop  
เหมาะกับงาน I/O-bound จำนวนมาก

## การทำงานของโค้ด
- ใช้ `async def` เพื่อสร้าง async function
- ใช้ `await asyncio.sleep()` แทน `time.sleep()`
- ใช้ `asyncio.gather()` เพื่อรันหลาย task พร้อมกัน
- ใช้ `asyncio.run()` เพื่อเริ่ม event loop

## สิ่งที่สังเกตได้
- ทำงานพร้อมกันเหมือน thread
- ใช้เพียง thread เดียว
- ควบคุมการรอด้วย `await`

# 3️⃣ Process Pool Example

## แนวคิด
Process Pool คือการสร้างหลาย process แยกกันจริง ๆ  
เหมาะกับงาน CPU-bound (งานคำนวณหนัก)

## การทำงานของโค้ด
- สร้างฟังก์ชัน `square()` สำหรับคำนวณกำลังสอง
- ใช้ `multiprocessing.Pool()` เพื่อสร้างหลาย process
- ใช้ `pool.map()` แจกงานให้แต่ละ process
- รวมผลลัพธ์กลับมาเป็น list

## สิ่งที่สังเกตได้
- ใช้ CPU ได้หลาย core
- เหมาะกับงานคำนวณมากกว่า thread

# 🔎 เปรียบเทียบทั้ง 3 แบบ

| ประเภท | เหมาะกับงาน | ใช้หลาย CPU core | ใช้หน่วยความจำ |
|---------|--------------|------------------|-----------------|
| Thread | I/O-bound | ❌ | ต่ำ |
| Asyncio | I/O-bound จำนวนมาก | ❌ | ต่ำมาก |
| Process Pool | CPU-bound | ✅ | สูงกว่า |

# 🧠 สรุปผล

- Thread เหมาะกับงานที่ต้องรอ
- Asyncio เหมาะกับงาน I/O จำนวนมากใน thread เดียว
- Process Pool เหมาะกับงานคำนวณหนัก
- การเลือกใช้ขึ้นอยู่กับลักษณะของงาน (I/O-bound หรือ CPU-bound)
