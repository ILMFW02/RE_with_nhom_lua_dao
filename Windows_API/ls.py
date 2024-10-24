import os

def list_files(directory):
    try:
        # Duyệt qua tất cả các file và thư mục trong thư mục chỉ định
        for filename in os.listdir(directory):
            # Kiểm tra nếu đó là file
            if os.path.isfile(os.path.join(directory, filename)):
                print(filename)
    except Exception as e:
        print(f"Error: {e}")

# Sử dụng hàm
directory_path = input("Nhập thư mục cần list: ")  
list_files(directory_path)
