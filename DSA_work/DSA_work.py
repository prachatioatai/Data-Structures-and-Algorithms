class Node:
    def __init__(box, number, name):
        box.number = number
        box.name = name
        box.next = None

head = None # คนเเรก
last = None # คนสุดท้าย

while True: # ลูปเพื่อรับข้อมูล เเล้วก็สั่งให้มันหยุด เเล้วมันก็จะเเสดงoutputออกมาทั้งหมด
    name = input("ป้อนชื่อ (หรือพิมพ์ 'stop' เพื่อหยุด): ")
    if name == "stop":
        break  
        
    num = input("ป้อนตัวเลข: ") #รับค่าตัวเลข
    
    new_node = Node(num, name)

    if head is None: #อันนี้กรณี ถ้ายังไม่มีใครในลิสต์
        head = new_node  # ถ้ายังไม่มีใคร คนนี้จะเป็นคนเเรก
        last = new_node  # เเล้วก็คนท้าย เพราะในเเถวมีคนเดียว
    else: #กรณี ถ้ามีคนในลิสต์เเล้ว
        last.next = new_node # เอาคนใหม่ไปต่อหลัง
        last = new_node      # ตั้งคนใหม่นี้เป็นคนท้าย

print("--- รายชื่อทั้งหมด ---") #อันนี้คือส่วนที่ต้องเเสดงผล เวลาoutputออกมา
current = head
while current: # สมมติ current คือโหนดปัจจุบัน
    print(f"เลข: {current.number} -> ชื่อ: {current.name}") #เลขปัจจุบัน กับชื่อปัจจุบัน       
    current = current.next # เลื่อนไปคนถัดไป
