import pyautogui
import time

time.sleep(2)

# PART 1 – Application Launch Automation
print("Launching Calculator...")
pyautogui.hotkey('win', 'r')
time.sleep(1)
pyautogui.write('calc')
pyautogui.press('enter')
time.sleep(2)
print("Calculator Opened Successfully")

# PART 2 – Automated Calculation
print("Performing Automated Calculation...")
pyautogui.write('1234+5678')
pyautogui.press('enter')
time.sleep(1)

screenshot = pyautogui.screenshot(region=(500, 300, 400, 300))
screenshot.save("calculator_result.png")

print("Result Captured Successfully")

# PART 3 – Mouse Control Simulation
print("Mouse Movement Started")

pyautogui.moveTo(300, 300, duration=1)
pyautogui.click()

pyautogui.doubleClick()

pyautogui.rightClick()

pyautogui.dragTo(600, 400, duration=1)

print("Click Actions Completed")
print("Drag Operation Completed")

# PART 4 – Typing & Keyboard Automation
print("Opening Notepad...")
pyautogui.hotkey('win', 'r')
time.sleep(1)
pyautogui.write('notepad')
pyautogui.press('enter')
time.sleep(2)

print("Typing Report...")
pyautogui.write("Daily Automation Report Generated")
pyautogui.press('enter')
pyautogui.write("Date: 03-03-2026")

pyautogui.hotkey('ctrl', 's')
time.sleep(1)
pyautogui.write('report.txt')
pyautogui.press('enter')

print("Report Saved Successfully")

# PART 5 – Screenshot Automation
full = pyautogui.screenshot()
full.save("full_screen.png")
print("Full Screen Captured")

partial = pyautogui.screenshot(region=(100, 100, 500, 400))
partial.save("partial_screen.png")
print("Partial Screen Captured")

print("Screenshots Saved Successfully")
