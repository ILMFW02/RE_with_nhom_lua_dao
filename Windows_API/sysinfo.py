import platform
import os
import psutil
import socket

def get_os_manufacturer():
    try:
        # Sử dụng thông tin từ platform.uname() và các phương thức khác thay thế cho WMIC
        return platform.system() + " " + platform.release()
    except Exception as e:
        return f"Unable to retrieve OS manufacturer. Error: {e}"
    
def get_os_configuration():
    try:
        return platform.platform()
    except Exception as e:
        return f"Unable to retrieve OS configuration. Error: {e}"
    
def get_system_info():
    """Lấy thông tin hệ thống và in ra màn hình"""
    # Thông tin cơ bản về hệ điều hành
    print("Host Name:", socket.gethostname())
    print("OS Name:", platform.system())
    print("OS Version:", platform.release())
    print("OS Manufacturer: ", get_os_manufacturer())
    print("OS Configuration: ", get_os_configuration())
    
    # Thông tin về bộ xử lý
    print("Processor:", platform.processor())
    
    # Thông tin bộ nhớ vật lý (RAM)
    print(f"Total Physical Memory: {round(psutil.virtual_memory().total / (1024**2))} MB")
    print(f"Available Physical Memory: {round(psutil.virtual_memory().available / (1024**2))} MB")
    
    # Thông tin bộ nhớ ảo
    virtual_mem = psutil.virtual_memory()
    print(f"Virtual Memory: Max Size: {round(virtual_mem.total / (1024**2))} MB")
    print(f"Virtual Memory: Available: {round(virtual_mem.available / (1024**2))} MB")
    print(f"Virtual Memory: In Use: {round(virtual_mem.used / (1024**2))} MB")
    
    # Thông tin về thời gian khởi động hệ thống
    boot_time = psutil.boot_time()
    print(f"System Boot Time: {platform.uname().version}")
    
    # Thông tin về thư mục Windows
    print(f"Windows Directory: {os.environ.get('windir', 'N/A')}")
    
    # Thông tin BIOS và hệ thống phần cứng (giả lập)
    try:
        print(f"BIOS Version: {platform.uname().version}")
        print(f"System Manufacturer: {platform.uname().node}")
        print(f"System Model: {platform.machine()}")
        print(f"System Type: {platform.architecture()[0]}")
    except Exception as e:
        print(f"Unable to retrieve hardware information. Error: {e}")
    
    # Thông tin mạng
    try:
        network_cards = psutil.net_if_addrs()
        print(f"Network Card(s): {len(network_cards)} NIC(s) Installed.")
        for idx, (name, addr) in enumerate(network_cards.items(), start=1):
            print(f"   [{idx:02d}]: {name}")
    except Exception as e:
        print(f"Unable to retrieve network information. Error: {e}")

if __name__ == "__main__":
    get_system_info()
