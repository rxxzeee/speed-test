import speedtest
import time

def test_internet_speed():
    
    st = speedtest.Speedtest()
    
    print("Поиск лучших серверов...")
    st.get_best_server
    
    print("Измерение скорости загрузки...")
    download_speed = st.download()
    
    print("Измерение скорости выгрузки...")
    upload_speed = st.upload()
    
    print("Измерение пинга...")
    ping = st.results.ping
    
    print(f"Скорость загрузки: {download_speed / 1_000_000:.2f} Мбит/с")
    print(f"Скорость выгрузки: {upload_speed / 1_000_000:.2f} Мбит/с")
    print(f"Задержка: {ping} мс")

if __name__ == "__main__":
    test_internet_speed()
    while(True):
        time.sleep(1)