from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import requests
import cv2
import os
import uuid

alphabet = "abcdefghijklmnopqrstuvwxyz"

def create_directory_if_not_exists(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)

def generate_unique_filename(extension):
    unique_filename = str(uuid.uuid4())[:8]
    return f"{unique_filename}.{extension}"

def dataCollector1():
    alphabet = "abcdefghjklmnopqtuvwxyz"

    driver = webdriver.Chrome()

    for letter in alphabet:
        url = "https://www.signasl.org/"
        driver.get(url)
        count = 0

        time.sleep(0.5)
        searchInput = driver.find_elements(By.TAG_NAME, "input")[1]

        time.sleep(0.5)
        searchInput.send_keys(letter)

        time.sleep(0.5)
        searchInput.send_keys(Keys.ENTER)

        time.sleep(1)

        videos = driver.find_elements(By.TAG_NAME, "source")
        src = ["src1", "src2", "src3"]
        for i in range(len(videos)):
            if i == 3:
                break
            src[i] = videos[i].get_attribute("src")
            count = count + 1

        time.sleep(1)

        for i in range(count):
            response = requests.get(src[i])
            if response.status_code == 200:
                directory = f"Data\\{letter}\\"
                create_directory_if_not_exists(directory)

                video_filename = generate_unique_filename("mp4")
                with open(os.path.join(directory, video_filename), "wb") as video_file:
                    video_file.write(response.content)
                print("Video başarıyla indirildi.")

                cap = cv2.VideoCapture(os.path.join(directory, video_filename))

                total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
                fps = int(cap.get(cv2.CAP_PROP_FPS))

                target_time = total_frames / fps / 2

                cap.set(cv2.CAP_PROP_POS_MSEC, target_time * 1000)

                ret, frame = cap.read()

                cap.release()  # VideoCapture nesnesini serbest bırak

                if ret:
                    image_filename = generate_unique_filename("jpg")
                    cv2.imwrite(os.path.join(directory, image_filename), frame)
                    print(f"Kare başarıyla kaydedildi.")
                else:
                    print("Kare yakalanamadı.")

                # MP4 dosyasını sil
                os.remove(os.path.join(directory, video_filename))
            else:
                print("Video indirme hatası, HTTP kodu:", response.status_code)

def dataCollector2():
    driver = webdriver.Chrome()

    for index, letter in enumerate(alphabet):
        url = "https://alphabet.lingvano.com/glossary"
        driver.get(url)

        time.sleep(0.1)
        div = driver.find_element(By.XPATH, f"/html/body/div/div[1]/div/div/div/div/div/div[3]/div[{index+1}]/div/div")
        time.sleep(0.1)
        div.click()

        time.sleep(0.1)

        data = driver.find_element(By.XPATH, "/html/body/div/div[1]/div/div/div/div/div/div[2]/div/div[2]/video").get_attribute("src")
        response = requests.get(data)

        if response.status_code == 200:
            directory = os.path.join("Data", letter)
            create_directory_if_not_exists(directory)

            video_filename = generate_unique_filename("mp4")
            video_path = os.path.join(directory, video_filename)
            with open(video_path, "wb") as video_file:
                video_file.write(response.content)
            print("Video başarıyla indirildi.")

            cap = cv2.VideoCapture(video_path)

            total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
            fps = int(cap.get(cv2.CAP_PROP_FPS))

            target_time = total_frames / fps / 2

            cap.set(cv2.CAP_PROP_POS_MSEC, target_time * 1000)

            ret, frame = cap.read()

            cap.release()

            if ret:
                image_filename = generate_unique_filename("jpg")
                image_path = os.path.join(directory, image_filename)
                cv2.imwrite(image_path, frame)
                print(f"Kare başarıyla kaydedildi.")
            else:
                print("Kare yakalanamadı.")
            # MP4 dosyasını sil
            os.remove(os.path.join(directory, video_filename))
        else:
            print("Video indirme hatası, HTTP kodu:", response.status_code)

def dataCollector3():
    driver = webdriver.Chrome()
    url = "https://www.wikihow.com/Fingerspell-the-Alphabet-in-American-Sign-Language"
    driver.get(url)

    time.sleep(0.1)
    imgs = driver.find_elements(By.TAG_NAME, "img")
    print(len(imgs))
    time.sleep(0.1)
    index = 0
    for img in imgs:
        if index == 26:
            break
        if img.get_attribute("data-width") == "460":
            data = img.get_attribute("src")
            response = requests.get(data)
            if response.status_code == 200:
                letter = alphabet[index]
                directory = os.path.join("Data", letter)
                create_directory_if_not_exists(directory)

                image_filename = generate_unique_filename("jpg")
                image_path = os.path.join(directory, image_filename)

                with open(image_path, "wb") as image_file:
                    image_file.write(response.content)
                print("Fotoğraf başarıyla indirildi.")
            else:
                print("Fotoğraf indirme hatası, HTTP kodu:", response.status_code)
            index = index+1

def dataCollector4():
    for letter in alphabet:
        driver = webdriver.Chrome()
        error = False
        url = "https://www.alamy.com/"
        driver.get(url)
        time.sleep(0.1)
        searchInput = driver.find_element(By.ID, "qt")

        time.sleep(0.1)
        searchInput.send_keys(f"Dramatic colour image of male hand demonstrating ASL American sign language letter {letter} with empty copy space for editors")

        time.sleep(0.1)
        searchInput.send_keys(Keys.ENTER)

        time.sleep(0.5)

        try:
            data = driver.find_element(By.XPATH, "/html/body/div[1]/div/div[5]/div/div[3]/div[1]/div/div/div[1]/div/img").get_attribute("src")
        except Exception as e:
            print(f'Hata: {e}')
            error = True
        finally:
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
            }

            if not error:
                letter_directory = os.path.join("Data", letter)
                create_directory_if_not_exists(letter_directory)

                image_filename = generate_unique_filename("jpg")
                image_path = os.path.join(letter_directory, image_filename)

                response = requests.get(data, headers=headers)
                if response.status_code == 200:
                    with open(image_path, "wb") as photo_file:
                        photo_file.write(response.content)
                    print("Fotoğraf başarıyla indirildi.")
                else:
                    print("Fotoğraf indirme hatası, HTTP kodu:", response.status_code)
            else:
                print("Hata oluştu: 'data' değişkeni tanımlanmamış.")
                continue
        driver.quit()

def dataCollector5():
    for letter in alphabet:
        driver = webdriver.Chrome()
        error = False
        url = "https://www.alamy.com/"
        driver.get(url)
        time.sleep(0.1)
        searchInput = driver.find_element(By.ID, "qt")

        time.sleep(0.1)
        searchInput.send_keys(f"Finger Spelling the Alphabet in American Sign Language (ASL). The Letter {letter}")

        time.sleep(0.1)
        searchInput.send_keys(Keys.ENTER)

        time.sleep(0.5)

        try:
            data = driver.find_element(By.XPATH, "/html/body/div[1]/div/div[5]/div/div[3]/div[1]/div/div/div[1]/div/img").get_attribute("src")
        except Exception as e:
            print(f'Hata: {e}')
            error = True
        finally:
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
            }

            if not error:
                letter_directory = os.path.join("Data", letter)
                create_directory_if_not_exists(letter_directory)

                image_filename = generate_unique_filename("jpg")
                image_path = os.path.join(letter_directory, image_filename)

                response = requests.get(data, headers=headers)
                if response.status_code == 200:
                    with open(image_path, "wb") as photo_file:
                        photo_file.write(response.content)
                    print("Fotoğraf başarıyla indirildi.")
                else:
                    print("Fotoğraf indirme hatası, HTTP kodu:", response.status_code)
            else:
                print("Hata oluştu: 'data' değişkeni tanımlanmamış.")
                continue
        driver.quit()

def dataCollector6():
    for letter in alphabet:
        driver = webdriver.Chrome()
        error = False
        url = "https://www.alamy.com/"
        driver.get(url)
        time.sleep(0.1)
        searchInput = driver.find_element(By.ID, "qt")

        time.sleep(0.1)
        searchInput.send_keys(f"ASL alphabet of signs for deaf, letter {letter}")

        time.sleep(0.1)
        searchInput.send_keys(Keys.ENTER)

        time.sleep(0.5)

        try:
            data = driver.find_element(By.XPATH, "/html/body/div[1]/div/div[5]/div/div[3]/div[1]/div/div/div[1]/div/img").get_attribute("src")
        except Exception as e:
            print(f'Hata: {e}')
            error = True
        finally:
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
            }

            if not error:
                letter_directory = os.path.join("Data", letter)
                create_directory_if_not_exists(letter_directory)

                image_filename = generate_unique_filename("jpg")
                image_path = os.path.join(letter_directory, image_filename)

                response = requests.get(data, headers=headers)
                if response.status_code == 200:
                    with open(image_path, "wb") as photo_file:
                        photo_file.write(response.content)
                    print("Fotoğraf başarıyla indirildi.")
                else:
                    print("Fotoğraf indirme hatası, HTTP kodu:", response.status_code)
            else:
                print("Hata oluştu: 'data' değişkeni tanımlanmamış.")
                continue
        driver.quit()

def dataCollector7():
    alphabet = "bcdefghjklmnopqrstuvwxyz"

    for letter in alphabet:
        driver = webdriver.Chrome()
        error = False
        url = "https://www.alamy.com/"
        driver.get(url)
        time.sleep(0.1)
        searchInput = driver.find_element(By.ID, "qt")

        time.sleep(0.1)
        searchInput.send_keys(f"Boy signing the letter '{letter}' in American Sign Language")

        time.sleep(0.1)
        searchInput.send_keys(Keys.ENTER)

        time.sleep(0.5)

        try:
            data = driver.find_element(By.XPATH, "/html/body/div[1]/div/div[5]/div/div[3]/div[1]/div/div/div[1]/div/img").get_attribute("src")
        except Exception as e:
            print(f'Hata: {e}')
            error = True
        finally:
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
            }

            if not error:
                letter_directory = os.path.join("Data", letter)
                create_directory_if_not_exists(letter_directory)

                image_filename = generate_unique_filename("jpg")
                image_path = os.path.join(letter_directory, image_filename)

                response = requests.get(data, headers=headers)
                if response.status_code == 200:
                    with open(image_path, "wb") as photo_file:
                        photo_file.write(response.content)
                    print("Fotoğraf başarıyla indirildi.")
                else:
                    print("Fotoğraf indirme hatası, HTTP kodu:", response.status_code)
            else:
                print("Hata oluştu: 'data' değişkeni tanımlanmamış.")
                continue
        driver.quit()

def dataCollector8():
    for letter in alphabet:
        driver = webdriver.Chrome()
        error = False
        url = "https://www.alamy.com/"
        driver.get(url)
        time.sleep(0.1)
        searchInput = driver.find_element(By.ID, "qt")

        time.sleep(0.1)
        searchInput.send_keys(f"Caucasian teenage boy doing American Sign Language on one hand showing the symbol for {letter}")

        time.sleep(0.1)
        searchInput.send_keys(Keys.ENTER)

        time.sleep(0.5)

        try:
            data = driver.find_element(By.XPATH, "/html/body/div[1]/div/div[5]/div/div[3]/div[1]/div/div/div[1]/div/img").get_attribute("src")
        except Exception as e:
            print(f'Hata: {e}')
            error = True
        finally:
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
            }

            if not error:
                letter_directory = os.path.join("Data", letter)
                create_directory_if_not_exists(letter_directory)

                image_filename = generate_unique_filename("jpg")
                image_path = os.path.join(letter_directory, image_filename)

                response = requests.get(data, headers=headers)
                if response.status_code == 200:
                    with open(image_path, "wb") as photo_file:
                        photo_file.write(response.content)
                    print("Fotoğraf başarıyla indirildi.")
                else:
                    print("Fotoğraf indirme hatası, HTTP kodu:", response.status_code)
            else:
                print("Hata oluştu: 'data' değişkeni tanımlanmamış.")
                continue
        driver.quit()

def dataCollector9():
    alphabet = "bcdefghijklmnopqrstuvwxyz"
    driver = webdriver.Chrome()
    url = "https://www.alamy.com/"
    driver.get(url)
    time.sleep(0.1)
    searchInput = driver.find_element(By.ID, "qt")

    time.sleep(0.1)
    searchInput.send_keys(f"Hand showing letter a on color background. Sign language alphabet")

    time.sleep(0.1)
    searchInput.send_keys(Keys.ENTER)

    time.sleep(1)
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }

    data = driver.find_elements(By.TAG_NAME, "img")
    print(len(data))
    srcs = [data[1].get_attribute("src"), data[6].get_attribute("src")]

    for index, src in enumerate(srcs):
        response = requests.get(src, headers=headers)
        if response.status_code == 200:
            image_filename = generate_unique_filename("jpg")
            image_path = os.path.join("Data", "a", image_filename)
            create_directory_if_not_exists(os.path.dirname(image_path))
            with open(image_path, "wb") as photo_file:
                photo_file.write(response.content)
            print("Fotoğraf başarıyla indirildi.")
        else:
            print("Fotoğraf indirme hatası, HTTP kodu:", response.status_code)

    driver.quit()

    for letter in alphabet:
        driver = webdriver.Chrome()
        error = False
        url = "https://www.alamy.com/"
        driver.get(url)
        time.sleep(0.1)
        searchInput = driver.find_element(By.ID, "qt")

        time.sleep(0.1)
        searchInput.send_keys(f"Hand showing letter {letter} on color background. Sign language alphabet")

        time.sleep(0.1)
        searchInput.send_keys(Keys.ENTER)

        time.sleep(0.5)

        try:
            data = driver.find_elements(By.TAG_NAME, "img")
        except Exception as e:
            print(f'Hata: {e}')
            error = True
        finally:
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
            }

            for index, src in enumerate(data):
                if src.get_attribute("class") == "absolute object-cover bg-grey-light":
                    if not error:
                        response = requests.get(src.get_attribute("src"), headers=headers)
                        if response.status_code == 200:
                            image_filename = generate_unique_filename("jpg")
                            image_path = os.path.join("Data", letter, image_filename)
                            create_directory_if_not_exists(os.path.dirname(image_path))
                            with open(image_path, "wb") as photo_file:
                                photo_file.write(response.content)
                            print("Fotoğraf başarıyla indirildi.")
                        else:
                            print("Fotoğraf indirme hatası, HTTP kodu:", response.status_code)
                    else:
                        print("Hata oluştu: 'data' değişkeni tanımlanmamış.")
                        continue
        driver.quit()

def dataCollector10():
    driver = webdriver.Chrome()

    for i in range(26):
        url = f"https://www.ava.me/asl/letter-{alphabet[i]}"
        driver.get(url)

        
        time.sleep(1)
        data = driver.find_element(By.XPATH, "/html/body/div[3]/section/div[2]/img").get_attribute("src")
        time.sleep(1)
        response = requests.get(data)
        if response.status_code == 200:
            letter = alphabet[i]
            directory = os.path.join("Data", letter)
            create_directory_if_not_exists(directory)

            gif_filename = generate_unique_filename("gif")
            gif_path = os.path.join(directory, gif_filename)

            with open(gif_path, "wb") as gif_file:
                gif_file.write(response.content)
            print("Video başarıyla indirildi.")

            cap = cv2.VideoCapture(gif_path)

            total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
            fps = int(cap.get(cv2.CAP_PROP_FPS))

            target_time = total_frames / fps / 2

            cap.set(cv2.CAP_PROP_POS_MSEC, target_time * 1000)

            ret, frame = cap.read()

            cap.release()

            if ret:
                jpg_filename = generate_unique_filename("jpg")
                jpg_path = os.path.join(directory, jpg_filename)
                cv2.imwrite(jpg_path, frame)
                print(f"Kare başarıyla kaydedildi.")
            else:
                print("Kare yakalanamadı.")
            
            # MP4 dosyasını sil
            os.remove(gif_path)
        else:
            print("Video indirme hatası, HTTP kodu:", response.status_code)

    driver.quit()

def dataCollector11():
    driver = webdriver.Chrome()

    for letter in alphabet:
        url = f"https://www.signingsavvy.com/sign/{letter}/0/fingerspell"
        driver.get(url)

        time.sleep(1)
        video_source = driver.find_element(By.TAG_NAME, "source").get_attribute("src")
        response = requests.get(video_source)
        
        if response.status_code == 200:
            letter_directory = os.path.join("Data", letter)
            create_directory_if_not_exists(letter_directory)

            video_filename = generate_unique_filename("mp4")
            video_path = os.path.join(letter_directory, video_filename)

            with open(video_path, "wb") as video_file:
                video_file.write(response.content)
            print("Video başarıyla indirildi.")

            cap = cv2.VideoCapture(video_path)

            total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
            fps = int(cap.get(cv2.CAP_PROP_FPS))

            target_time = total_frames / fps / 2

            cap.set(cv2.CAP_PROP_POS_MSEC, target_time * 1000)

            ret, frame = cap.read()

            cap.release()

            if ret:
                image_filename = generate_unique_filename("jpg")
                image_path = os.path.join(letter_directory, image_filename)
                cv2.imwrite(image_path, frame)
                print(f"Kare başarıyla kaydedildi.")
            else:
                print("Kare yakalanamadı.")
            
            # MP4 dosyasını sil
            os.remove(video_path)
        else:
            print("Video indirme hatası, HTTP kodu:", response.status_code)

    driver.quit()

def dataCollector12():
    driver = webdriver.Chrome()
    url = "https://www.signingsavvy.com/wordlist/fingerspelling"
    driver.get(url)

    time.sleep(1)
    images = driver.find_elements(By.TAG_NAME, "img")
    
    for i, img in enumerate(images[3:29], start=0):
        src = img.get_attribute("src")
        response = requests.get(src)
        
        if response.status_code == 200:
            letter_directory = os.path.join("Data", alphabet[i])
            create_directory_if_not_exists(letter_directory)

            image_filename = generate_unique_filename("jpg")
            image_path = os.path.join(letter_directory, image_filename)

            with open(image_path, "wb") as image_file:
                image_file.write(response.content)
            print("Fotoğraf başarıyla indirildi.")
        else:
            print(f"Fotoğraf indirme hatası, HTTP kodu ({alphabet[i]}):", response.status_code)

    driver.quit()

def dataCollector13():
    driver = webdriver.Chrome()
    url = "https://www.spreadthesign.com/en.us/alphabet/21/"
    driver.get(url)
    time.sleep(0.1)

    for i in range(26):
        letter = driver.find_elements(By.TAG_NAME, "a")[i + 8]

        time.sleep(0.5)
        letter.click()

        time.sleep(0.5)

        data = driver.find_elements(By.TAG_NAME, "img")[1].get_attribute("src")
        time.sleep(0.2)
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }

        response = requests.get(data, headers=headers)
        if response.status_code == 200:
            letter_directory = os.path.join("Data", alphabet[i])
            create_directory_if_not_exists(letter_directory)

            image_filename = generate_unique_filename("jpg")
            image_path = os.path.join(letter_directory, image_filename)

            with open(image_path, "wb") as photo_file:
                photo_file.write(response.content)
            print(f"{i + 1}. Fotoğraf başarıyla indirildi.")
        else:
            print(f"{i + 1}. Fotoğraf indirme hatası, HTTP kodu:", response.status_code)

    driver.quit()

def dataCollector14():
    driver = webdriver.Chrome()
    url = "https://www.spreadthesign.com/en.us/alphabet/21/"
    driver.get(url)
    time.sleep(0.1)

    for i in range(26):
        letter = driver.find_elements(By.TAG_NAME, "a")[i + 8]

        time.sleep(0.5)
        letter.click()

        time.sleep(0.5)

        video_data = driver.find_element(By.TAG_NAME, "video").get_attribute("src")
        time.sleep(0.2)
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }

        # Video indirme
        video_response = requests.get(video_data, headers=headers)
        if video_response.status_code == 200:
            video_filename = generate_unique_filename("mp4")
            video_path = os.path.join("Data", alphabet[i], video_filename)

            with open(video_path, "wb") as video_file:
                video_file.write(video_response.content)
            print(f"{i + 1}. Video başarıyla indirildi.")
        else:
            print(f"{i + 1}. Video indirme hatası, HTTP kodu:", video_response.status_code)
            continue

        # Video'dan kare yakalama
        cap = cv2.VideoCapture(video_path)
        total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
        fps = int(cap.get(cv2.CAP_PROP_FPS))
        target_time = total_frames / fps / 2
        cap.set(cv2.CAP_PROP_POS_MSEC, target_time * 1000)
        ret, frame = cap.read()
        cap.release()

        # Video dosyasını silme
        os.remove(video_path)

        if ret:
            image_filename = generate_unique_filename("jpg")
            image_path = os.path.join("Data", alphabet[i], image_filename)

            with open(image_path, "wb") as photo_file:
                cv2.imwrite(image_path, frame)
            print(f"{i + 1}. Kare başarıyla kaydedildi.")
        else:
            print(f"{i + 1}. Kare yakalanamadı.")

    driver.quit()

def dataCollector15():
    driver = webdriver.Chrome()

    for i in range(26):
        url = f"https://www.handspeak.com/word/{2460 + i}/"
        driver.get(url)
        time.sleep(0.1)

        video_data = driver.find_element(By.XPATH, "/html/body/div[3]/article/video").get_attribute("src")

        time.sleep(0.5)
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }

        # Video indirme
        video_response = requests.get(video_data, headers=headers)
        if video_response.status_code == 200:
            video_filename = generate_unique_filename("mp4")
            video_path = os.path.join("Data", f"{alphabet[i]}", video_filename)

            with open(video_path, "wb") as video_file:
                video_file.write(video_response.content)
            print(f"{i + 1}. Video başarıyla indirildi.")
        else:
            print(f"{i + 1}. Video indirme hatası, HTTP kodu:", video_response.status_code)
            continue

        # Video'dan kare yakalama
        cap = cv2.VideoCapture(video_path)
        total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
        fps = int(cap.get(cv2.CAP_PROP_FPS))
        target_time = total_frames / fps / 2
        cap.set(cv2.CAP_PROP_POS_MSEC, target_time * 1000)
        ret, frame = cap.read()
        cap.release()

        # Video dosyasını silme
        os.remove(video_path)

        if ret:
            image_filename = generate_unique_filename("jpg")
            image_path = os.path.join("Data", f"{alphabet[i]}", image_filename)

            with open(image_path, "wb") as photo_file:
                cv2.imwrite(image_path, frame)
            print(f"{i + 1}. Kare başarıyla kaydedildi.")
        else:
            print(f"{i + 1}. Kare yakalanamadı.")

    driver.quit()



dataCollector15()
