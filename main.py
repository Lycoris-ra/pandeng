import subprocess
import pyautogui
import time

process = None

def locate_center_safe(image, confidence=None):
    try:
        if confidence is not None:
            return pyautogui.locateCenterOnScreen(image, confidence=confidence)
        else:
            return pyautogui.locateCenterOnScreen(image)
    except pyautogui.ImageNotFoundException:
        return None

def click_osc_button(retries=8, interval=0.5):
    """点击左上角的数字存储示波器按钮(OSC.png)。"""
    for i in range(retries):
        button = locate_center_safe('OSC.png', confidence=0.6)
        if button:
            pyautogui.click(button)
            return True
        time.sleep(interval)
    print("未找到 OSC.png 按钮，请确保屏幕可见且截图正确")
    return False


def click_image(image_name, retries=8, interval=0.5):
    """使用截图定位并点击按钮。"""
    for i in range(retries):
        button = locate_center_safe(image_name, confidence=0.9)
        if button:
            pyautogui.click(button)
            return True
        time.sleep(interval)
    print(f"未找到 {image_name}，请确保屏幕可见且截图正确")
    return False


def do_sequence_click(action_name, image_list):
    if not process:
        print("软件未运行")
        return
    if not click_osc_button():
        print(f"{action_name}：OSC 按钮未找到，已取消操作")
        return
    for image in image_list:
        if not click_image(image):
            print(f"{action_name}：未找到 {image}，已取消")
            return


def do_action_with_osc(action_name, *keys):
    if not process:
        print("软件未运行")
        return
    if not click_osc_button():
        print(f"{action_name}：OSC 按钮未找到，已取消操作")
        return
    pyautogui.hotkey(*keys)

def read_commands_from_file(path, last_line_index):
    try:
        with open(path, 'r', encoding='utf-8') as f:
            lines = f.readlines()
    except FileNotFoundError:
        return [], last_line_index

    cleaned = [line.strip() for line in lines if line.strip() and not line.strip().startswith('#')]
    if last_line_index < len(cleaned):
        return cleaned[last_line_index:], len(cleaned)
    return [], last_line_index


if locate_center_safe('OSC.png', confidence=0.9) is None:
    software_path = r"c:\Users\1\Desktop\usb\JHDSOWin20G.exe"
    process = subprocess.Popen([software_path])
    time.sleep(1)
    if locate_center_safe('open.png', confidence=0.9):
        pyautogui.click(pyautogui.locateCenterOnScreen('open.png', confidence=0.9))
    button = pyautogui.locateCenterOnScreen('ok_button.png', confidence=0.8)
    pyautogui.click(button)
command_file_path = 'commands.txt'
processed_lines = 0
while True:
    if locate_center_safe('OSC.png', confidence=0.9):
        print("软件已打开，进入指令监听...")
        break
while True:
    command = input("请输入指令: ")
    if command == ":AUTO":
        do_action_with_osc("自动设置", 'f4')
    elif command == ":CHANnel1:COUPLing":
        do_action_with_osc("模拟通道1设置", 'ctrl', '1')
    elif command == ":CHANnel2:COUPLing":
        do_action_with_osc("模拟通道2设置", 'ctrl', '2')
    elif command == ":STOP":
        click_osc_button()
        time.sleep(0.6)
        if locate_center_safe('stop.png', confidence=0.9):
            print("当前状态: 停止")
        else:
            do_sequence_click("停止", ['run.png', 'run.png'])
    elif command == ":RUN":
        click_osc_button()
        time.sleep(0.6)
        if locate_center_safe('run.png', confidence=0.9):
            print("当前状态: 运行")
        else:
            do_sequence_click("运行", ['stop.png', 'stop.png'])
    elif command == "over":
        if process:
            process.terminate()
            process.wait()
        break
    elif ':CHAN1:COUP' in command:
        do_action_with_osc("模拟通道1设置", 'ctrl', '1')
        if 'DC' in command:
            do_sequence_click("直流耦合", ['DC_1M.png'])
        elif 'AC' in command:
            do_sequence_click("交流耦合", ['AC_1M.png'])
        elif 'GND' in command:
            do_sequence_click("接地", ['GND.png'])
        else:
            print("未知通道1耦合类型")
    elif ':CHAN2:COUP' in command:
        do_action_with_osc("模拟通道2设置", 'ctrl', '2')
        if 'DC' in command:
            do_sequence_click("直流耦合", ['DC_1M.png'])
        elif 'AC' in command:
            do_sequence_click("交流耦合", ['AC_1M.png'])
        elif 'GND' in command:
            do_sequence_click("接地", ['GND.png'])
        else:
            print("未知通道2耦合类型")
    elif ':CHAN1:DISP' in command:
        do_action_with_osc("模拟通道1设置", 'ctrl', '1')
        time.sleep(0.6)
        if 'ON' in command:
            if locate_center_safe('display_on.png', confidence=0.9):
                do_sequence_click("显示", ['display_on.png'])
        elif 'OFF' in command:
            if locate_center_safe('display_off.png', confidence=0.9):
                do_sequence_click("隐藏", ['display_off.png'])
        else:
            print("未知通道1显示状态")
    elif ':CHAN2:DISP' in command:
        do_action_with_osc("模拟通道2设置", 'ctrl', '2')
        time.sleep(0.6)
        if 'ON' in command:
            if locate_center_safe('display_on.png', confidence=0.9):
                do_sequence_click("显示", ['display_on.png'])
        elif 'OFF' in command:
            if locate_center_safe('display_off.png', confidence=0.9):
                do_sequence_click("隐藏", ['display_off.png'])
        else:
            print("未知通道2显示状态")
    else:
        print("未知指令")