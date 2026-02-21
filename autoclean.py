import os
import shutil
import ctypes

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

def clean_folder(folder_path):
    print(f"กำลังตรวจสอบ: {folder_path}")
    if not os.path.exists(folder_path):
        print(f"ไม่พบโฟลเดอร์: {folder_path}")
        return

    files_deleted = 0
    errors = 0

    for item in os.listdir(folder_path):
        item_path = os.path.join(folder_path, item)
        try:
            if os.path.isfile(item_path) or os.path.islink(item_path):
                os.unlink(item_path) # ลบไฟล์หรือลิงก์
                files_deleted += 1
            elif os.path.isdir(item_path):
                shutil.rmtree(item_path) # ลบโฟลเดอร์
                files_deleted += 1
        except Exception as e:
            # ไฟล์บางไฟล์อาจถูกใช้งานอยู่ จะข้ามไปโดยไม่หยุดการทำงาน
            errors += 1

    print(f"เสร็จสิ้น! ลบไปได้ {files_deleted} รายการ (ข้าม {errors} รายการที่กำลังถูกใช้งาน)")

if __name__ == "__main__":
    if not is_admin():
        print("⚠️ แนะนำให้รันด้วยสิทธิ์ Administrator เพื่อการทำความสะอาดที่หมดจด")
    
    # รายการโฟลเดอร์ขยะ
    folders_to_clean = [
        os.environ.get('TEMP'),                  # User Temp
        r'C:\Windows\Temp',                      # System Temp
        r'C:\Windows\Prefetch'                   # Prefetch
    ]

    for folder in folders_to_clean:
        if folder:
            clean_folder(folder)
            print("-" * 30)

    print("✨ ทำความสะอาดเรียบร้อยแล้ว!")