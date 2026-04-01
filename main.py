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


software_path = r"c:\Users\1\Desktop\usb\JHDSOWin20G.exe"
process = subprocess.Popen([software_path])
time.sleep(1)
button = pyautogui.locateCenterOnScreen('ok_button.png', confidence=0.8)
pyautogui.click(button)
while True:
    command = input("请输入指令: ")
    # if command == "close":
    #     if process:
    #         process.terminate()
    #         process.wait()  # 等待进程结束
    #         process = None
    #         print("软件已关闭")
    #     else:
    #         print("软件未运行")
    # elif command == "保存波形":
    #     do_action_with_osc("保存波形", 'ctrl', 's')
    # elif command == "读取波形到R1":
    #     do_action_with_osc("读取波形到R1", 'ctrl', 'o')
    # elif command == "保存环境配置":
    #     do_action_with_osc("保存环境配置", 'ctrl', 'shift', 's')
    # elif command == "读取环境配置":
    #     do_action_with_osc("读取环境配置", 'ctrl', 'shift', 'o')
    # elif command == "打印":
    #     do_action_with_osc("打印", 'ctrl', 'p')
    # elif command == "最小化":
    #     do_action_with_osc("最小化", 'ctrl', 'm')
    # elif command in ("解码通道1设置", "解码通道一设置"):
    #     do_sequence_click("解码通道1设置", ['tongdao.png', 'JMtongdao1.png'])
    # elif command in ("解码通道2设置", "解码通道二设置"):
    #     do_sequence_click("解码通道2设置", ['tongdao.png', 'JMtongdao2.png'])
    # elif command in ("模拟通道1设置", "模拟通道一设置"):
    #     do_action_with_osc("模拟通道1设置", 'ctrl', '1')
    # elif command in ("模拟通道2设置", "模拟通道二设置"):
    #     do_action_with_osc("模拟通道2设置", 'ctrl', '2')
    # elif command in ("扩展通道1设置", "扩展通道一设置"):
    #     do_action_with_osc("扩展通道1设置", 'ctrl', 'shift', '1')
    # elif command in ("扩展通道2设置", "扩展通道二设置"):
    #     do_action_with_osc("扩展通道2设置", 'ctrl', 'shift', '2')
    # elif command == "水平设置":
    #     do_action_with_osc("水平设置", 'ctrl', 't')
    # elif command == "实时采样":
    #     do_sequence_click("实时采样", ['shiji.png', 'sampling.png'])
    # elif command == "峰值检测":
    #     do_sequence_click("峰值检测", ['shiji.png', 'peak_detection.png'])
    # elif command == "平均":
    #     do_sequence_click("平均", ['shiji.png', 'average.png'])
    # elif command == "触发设置":
    #     do_action_with_osc("触发设置", 'ctrl', 'g')
    # elif command == "触发停止":
    #     do_sequence_click("触发停止", ['chufa.png', 'trigger_stop.png'])
    # elif command == "自动触发":
    #     do_sequence_click("自动触发", ['chufa.png', 'auto_trigger.png'])
    # elif command == "正常触发":
    #     do_sequence_click("正常触发", ['chufa.png', 'normal_trigger.png'])
    # elif command == "单次触发":
    #     do_sequence_click("单次触发", ['chufa.png', 'single_trigger.png'])
    # elif command == "边沿触发":
    #     do_sequence_click("边沿触发", ['chufa.png', 'edge_trigger.png'])
    # elif command == "脉宽触发":
    #     do_sequence_click("脉宽触发", ['chufa.png', 'pulse_width_trigger.png'])
    # elif command == "视频触发":
    #     do_sequence_click("视频触发", ['chufa.png', 'video_trigger.png'])
    # elif command == "显示设置":
    #     do_action_with_osc("显示设置", 'f7')
    # elif command == "YT栅格":
    #     do_sequence_click("YT栅格", ['xianshi', 'yt_grid.png'])
    # elif command == "XY栅格":
    #     do_sequence_click("XY栅格", ['xianshi', 'xy_grid.png'])
    # elif command == "测量设置":
    #     do_action_with_osc("测量设置", 'f9')
    # elif command == "退出":
    #     if process:
    #         if click_osc_button():
    #             pyautogui.hotkey('alt', 'f4')
    #             print("已发送 Alt+F4 (退出)")
    #         else:
    #             print("退出操作: 未找到 OSC 按钮")
    #         process = None
    #     else:
    #         print("软件未运行")
    # elif command == "over":
    #     if process:
    #         process.terminate()
    #         process.wait()
    #     break
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