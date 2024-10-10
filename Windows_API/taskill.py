import ctypes
import psutil
from ctypes import wintypes

# Load kernel32.dll
kernel32 = ctypes.WinDLL('kernel32', use_last_error=True)

# Khai báo các hàm Windows API
OpenProcess = kernel32.OpenProcess
TerminateProcess = kernel32.TerminateProcess
CloseHandle = kernel32.CloseHandle

# Các quyền truy cập process
PROCESS_TERMINATE = 0x0001

# Hàm để kết thúc process bằng PID
def terminate_process_by_pid(pid):
    hProcess = OpenProcess(PROCESS_TERMINATE, False, pid)
    if not hProcess:
        raise ctypes.WinError(ctypes.get_last_error())
    
    if not TerminateProcess(hProcess, 1):
        raise ctypes.WinError(ctypes.get_last_error())
    
    CloseHandle(hProcess)
    print(f"Process with PID {pid} has been terminated.")

# Hàm để kết thúc process bằng image name
def terminate_process_by_imagename(image_name):
    for proc in psutil.process_iter(['pid', 'name']):
        if proc.info['name'].lower() == image_name.lower():
            terminate_process_by_pid(proc.info['pid'])

print("Bạn muốn taskill process bằng 1.PID hay 2. image name? \n Nhập lựa chọn 1 hoặc 2: ");
x = input();
if x == 1:
    y = input("Nhập PID của process: ");
    terminate_process_by_pid(int(y));
else: 
    y = input("Nhập image_name của process: ");
    terminate_process_by_imagename(y);
