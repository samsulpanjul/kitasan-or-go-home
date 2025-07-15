import pyautogui
import pygetwindow as gw
import time
import pymsgbox as msg

pyautogui.useImageNotFoundException(False)

CONFIDENCE=0.8
KITASAN_IMG="ss.png"

def switch_window(title):
  uma = gw.getWindowsWithTitle(title)
  target_window = next((w for w in uma if w.title.strip() == "Umamusume"), None)
  if target_window:
    target_window.activate()
    target_window.maximize()
    print("Umamusume found")
    time.sleep(0.5)
  else:
    print("Window 'Umamusume' tidak ditemukan.")

def click(img: str):
  click_btn = pyautogui.locateCenterOnScreen(img, confidence=CONFIDENCE, minSearchTime=5)
  if click_btn:
    print(f"{img} CLICKED")
    pyautogui.moveTo(click_btn, duration=0.15)
    pyautogui.click(click_btn)
    time.sleep(1.2)
    return
  else:
    print(f"{img} NOT FOUND")
  return

def locate_all_image(image_path: str, confidence=0.9, timeout=1, tolerance=15):
  start = time.time()
  filtered_img = []

  while time.time() - start < timeout:
    raw_img = list(pyautogui.locateAllOnScreen(image_path, confidence=confidence))

    temp_filtered = []
    for box in raw_img:
      is_duplicate = False
      for existing in temp_filtered:
        if abs(box.left - existing.left) < tolerance and abs(box.top - existing.top) < tolerance:
          is_duplicate = True
          break
      if not is_duplicate:
        temp_filtered.append(box)

    if temp_filtered:
      filtered_img = temp_filtered
      break

    time.sleep(0.2)

  return filtered_img

def register():
  print("\nREGISTER SECTION!\n")
  click("assets/logo.png")
  time.sleep(1)

  view_btn = locate_all_image("assets/view_f_btn.png")
  print(f"Ditemukan {len(view_btn)} tombol:")
  for i, btn in enumerate(view_btn):
    print("VIEW BTN CLICKED")
    pyautogui.click(btn)
    # print(f"{i+1}. {btn}")
  
  time.sleep(1)
  switch_window("Umamusume")
  time.sleep(1)

  click("assets/agree_f_btn.png")
  
  click("assets/change_btn.png")

  click("assets/ok_btn.png")

  click("assets/ok_btn.png")

  click("assets/input_birth.png")
  pyautogui.write("199001")
  click("assets/ok_btn.png")
  time.sleep(0.5)

  click("assets/skip_btn.png")

  click("assets/input_name.png")
  pyautogui.write("Elysia")
  click("assets/register_btn.png")

  click("assets/ok_btn.png")

  click("assets/ok_btn.png")

  for _ in range(10):
    skip_icon_btn = pyautogui.locateCenterOnScreen("assets/skip_icon_btn.png", confidence=CONFIDENCE, minSearchTime=1)
    if skip_icon_btn:
      pyautogui.tripleClick(skip_icon_btn, interval=0.1)
      time.sleep(0.5)

  for _ in range(2):
    click("assets/close_btn.png")
    time.sleep(0.3)

def claim_mail():
  print("\nCLAIM MAIL\n")
  click("assets/mail.png")

  click("assets/collect_all_btn.png")
  time.sleep(0.5)

  for _ in range(2):
    click("assets/close_btn.png")
    time.sleep(0.3)

def select_banner():
  print("\nSELECT BANNER!\n")
  current_banner = pyautogui.locateCenterOnScreen("assets/banner.png", confidence=CONFIDENCE, minSearchTime=2)

  if current_banner:
    pyautogui.moveTo(current_banner, duration=0.15)
    pyautogui.click()

def gacha(pulls: int = 5, kitasan_copy = 0, how_many_kitasan = 3):
  print("\nGACHA!\n")
  click("assets/gacha_menu.png")

  select_banner()

  click("assets/10_pull_btn.png")

  click("assets/scout_btn.png")

  for _ in range(2):
    skip_icon_btn = pyautogui.locateCenterOnScreen("assets/skip_icon_btn.png", confidence=CONFIDENCE, minSearchTime=2)
    if skip_icon_btn:
      pyautogui.tripleClick(skip_icon_btn, interval=0.1)
      time.sleep(0.2)

  time.sleep(0.5)
  kitasan_found = locate_all_image(KITASAN_IMG)
  if kitasan_found:
    kitasan_copy = kitasan_copy + len(kitasan_found)
    print(f"Got {kitasan_copy} Kitasan Black")

  if kitasan_copy >= how_many_kitasan:
    print(f"Done, already got {kitasan_copy} Kitasan.")
    return True

  for _ in range(pulls):
    click("assets/scout_again_btn.png")
    click("assets/scout_btn.png")
    for _ in range(2):
      skip_icon_btn = pyautogui.locateCenterOnScreen("assets/skip_icon_btn.png", confidence=CONFIDENCE, minSearchTime=2)
      if skip_icon_btn:
        pyautogui.tripleClick(skip_icon_btn, interval=0.1)
        time.sleep(0.2)
      
      kitasan_found = locate_all_image(KITASAN_IMG)
      if kitasan_found:
        kitasan_copy = kitasan_copy + len(kitasan_found)
        print(f"Got {kitasan_copy} Kitasan Black")
    
    time.sleep(0.5)
    if kitasan_copy >= how_many_kitasan:
      print(f"Done, already got {kitasan_copy} Kitasan.")
      return True

  # click("assets/back_btn.png")

  # Only happen when gacha character
  # time.sleep(1)

  # click("assets/close_btn.png")

  time.sleep(0.5)
  return False

def delete_data():
  print("\nREROLL\n")
  click("assets/to_title_screen.png")

  time.sleep(5)

  click("assets/acc_menu.png")

  click("assets/delete_data.png")

  click("assets/delete_data_btn.png")

  click("assets/delete_data_btn.png")
  
  click("assets/close_btn.png")

def main():
  how_many_kitasan = msg.prompt("How many kitasan do you want?")
  kitasan = 0

  if how_many_kitasan is not None:
    switch_window("Umamusume")
    
    while True:
      register()

      time.sleep(1.5)

      claim_mail()

      result = gacha(5, kitasan, int(how_many_kitasan))

      if result:
        msg.alert("Done, grats")
        break
      else:
        delete_data()

        time.sleep(5)

main()
