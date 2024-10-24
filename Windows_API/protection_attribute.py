import ctypes
from ctypes import wintypes

# Định nghĩa các hằng số và cấu trúc cần thiết
MEM_COMMIT = 0x1000
PAGE_EXECUTE_READ_WRITE = 0x40

class MEMORY_BASIC_INFORMATION(ctypes.Structure):
    _fields_ = [
        ("BaseAddress", wintypes.LPVOID),
        ("AllocationBase", wintypes.LPVOID),
        ("AllocationProtect", wintypes.DWORD),
        ("RegionSize", ctypes.c_size_t),
        ("State", wintypes.DWORD),
        ("Protect", wintypes.DWORD),
        ("Type", wintypes.DWORD)
    ]

def list_memory_regions(process_id):
    """Liệt kê các vùng nhớ có thuộc tính PAGE_EXECUTE_READ_WRITE của tiến trình."""
    # Mở tiến trình
    hProcess = ctypes.windll.kernel32.OpenProcess(0x0010 | 0x0400, False, process_id)
    if not hProcess:
        print(f"Error: Unable to open process. Error code: {ctypes.GetLastError()}")
        return

    mbi = MEMORY_BASIC_INFORMATION()
    address = 0

    print("Memory regions with PAGE_EXECUTE_READ_WRITE:")

    # Duyệt qua tất cả các vùng nhớ
    while ctypes.windll.kernel32.VirtualQueryEx(hProcess, ctypes.c_void_p(address), ctypes.byref(mbi), ctypes.sizeof(mbi)):
        # Kiểm tra trạng thái và thuộc tính bảo vệ
        if mbi.State == MEM_COMMIT and mbi.Protect == PAGE_EXECUTE_READ_WRITE:
            print(f"Base Address: {hex(mbi.BaseAddress)}, Region Size: {mbi.RegionSize}, Protect: {mbi.Protect}")
        address += mbi.RegionSize  # Di chuyển đến địa chỉ vùng nhớ tiếp theo

    # Đóng handle của tiến trình
    ctypes.windll.kernel32.CloseHandle(hProcess)

def main():
    """Chương trình chính để nhận ID tiến trình từ người dùng và liệt kê vùng nhớ."""
    try:
        process_id = int(input("Enter Process ID: "))  # Nhập ID của tiến trình
        list_memory_regions(process_id)  # Gọi hàm để liệt kê vùng nhớ
    except ValueError:
        print("Please enter a valid integer for Process ID.")

if __name__ == "__main__":
    main()  
