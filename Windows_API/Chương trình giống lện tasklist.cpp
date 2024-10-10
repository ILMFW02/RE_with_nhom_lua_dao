#include <windows.h>
#include <tlhelp32.h>
#include <iostream>

int main() {
    // Tạo một snapshot của tất cả các process đang chạy
    HANDLE hProcessSnap = CreateToolhelp32Snapshot(TH32CS_SNAPPROCESS, 0);
    if (hProcessSnap == INVALID_HANDLE_VALUE) {
        std::cerr << "CreateToolhelp32Snapshot failed!" << std::endl;
        return 1;
    }

    // Cấu trúc để lưu thông tin về process
    PROCESSENTRY32 pe32;
    pe32.dwSize = sizeof(PROCESSENTRY32);

    // Lấy thông tin về process đầu tiên
    if (!Process32First(hProcessSnap, &pe32)) {
        std::cerr << "Process32First failed!" << std::endl;
        CloseHandle(hProcessSnap);
        return 1;
    }

    // In tiêu đề cột
    std::cout << "Image Name\t\tPID" << std::endl;
    std::cout << "----------------------------------------" << std::endl;

    // Duyệt qua tất cả các process và in thông tin
    do {
        std::wcout << pe32.szExeFile << "\t\t" << pe32.th32ProcessID << std::endl;
    } while (Process32Next(hProcessSnap, &pe32));

    // Đóng handle của snapshot
    CloseHandle(hProcessSnap);
    return 0;
}
