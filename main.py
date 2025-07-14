import pyautogui
import pygetwindow as gw
import time

pyautogui.useImageNotFoundException(False)

CONFIDENCE=0.9

def switch_window(title):
  uma = gw.getWindowsWithTitle(title)
  target_window = next((w for w in uma if w.title.strip() == "Umamusume"), None)
  if target_window:
    target_window.activate()
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

def register():
  print("\nREGISTER SECTION!\n")
  click("assets/logo.png")
  time.sleep(1)

  view_btn = list(pyautogui.locateAllOnScreen("assets/view_f_btn.png", confidence=CONFIDENCE))
  print(f"Ditemukan {len(view_btn)} tombol:")
  for _, btn in enumerate(view_btn):
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

  for _ in range(2):
    click("assets/close_btn.png")
    time.sleep(0.3)

def select_banner():
  current_banner = pyautogui.locateCenterOnScreen("assets/banner.png", confidence=CONFIDENCE)

  pyautogui.moveTo(current_banner.x + 255, current_banner.y, duration=1.5)
  pyautogui.click()

def gacha(pulls: int = 5):
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

  for _ in range(pulls):
    click("assets/scout_again_btn.png")
    click("assets/scout_btn.png")
    for _ in range(2):
      skip_icon_btn = pyautogui.locateCenterOnScreen("assets/skip_icon_btn.png", confidence=CONFIDENCE, minSearchTime=2)
      if skip_icon_btn:
        pyautogui.tripleClick(skip_icon_btn, interval=0.1)
        time.sleep(0.2)
    time.sleep(0.5)

  click("assets/back_btn.png")

  # Only happen when gacha character
  # time.sleep(1)

  # click("assets/close_btn.png")

  time.sleep(0.5)

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
  switch_window("Umamusume")

  while True:
    register()

    time.sleep(1.5)

    claim_mail()

    gacha(5)

    delete_data()

    time.sleep(5)


main()
