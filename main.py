import subprocess
import pyautogui
import time

process = None


def click_osc_button(retries=8, interval=0.5):
    """点击左上角的数字存储示波器按钮(OSC.png)。"""
    print("尝试定位数字存储示波器按钮 OSC.png...")
    for i in range(retries):
        button = pyautogui.locateCenterOnScreen('OSC.png', confidence=0.9)
        if button:
            print(f"找到 OSC 按钮: {button} (第{i+1}次尝试)")
            pyautogui.click(button)
            return True
        time.sleep(interval)
    print("未找到 OSC.png 按钮，请确保屏幕可见且截图正确")
    return False


def click_image(image_name, retries=8, interval=0.5):
    """使用截图定位并点击按钮。"""
    print(f"尝试定位按钮 {image_name}...")
    for i in range(retries):
        button = pyautogui.locateCenterOnScreen(image_name, confidence=0.9)
        if button:
            print(f"找到 {image_name} : {button} (第{i+1}次尝试)")
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
    print(f"已完成 {action_name} 的连续点击")


def do_action_with_osc(action_name, *keys):
    if not process:
        print("软件未运行")
        return
    if not click_osc_button():
        print(f"{action_name}：OSC 按钮未找到，已取消操作")
        return
    pyautogui.hotkey(*keys)
    print(f"已发送 {'+'.join(keys).upper()} ({action_name})")


while True:
    command = input("请输入指令: ")
    if command == "open":
        if process is None:
            software_path = r"c:\Users\1\Desktop\usb\JHDSOWin20G.exe"
            try:
                process = subprocess.Popen([software_path])
                print("软件已打开")
            except FileNotFoundError:
                print("软件文件未找到，请检查路径")
        else:
            print("软件已在运行")
    elif command == "close":
        if process:
            process.terminate()
            process.wait()  # 等待进程结束
            process = None
            print("软件已关闭")
        else:
            print("软件未运行")
    elif command == "ok":
        if process:
            # 方式2：使用按钮截图进行定位（推荐，可适应按钮位置变化）
            # 1) 先截取“确定”按钮为 ok_button.png，放到脚本同目录
            # 2) 运行前确保窗口可见且未被遮挡
            print("尝试定位确认按钮...")
            button = pyautogui.locateCenterOnScreen('ok_button.png', confidence=0.9)
            if button:
                print(f"找到按钮位置: {button}")
                pyautogui.click(button)
                print("已点击确认按钮")
            else:
                print("未找到按钮，可能是截图不匹配或窗口被遮挡")
                raise FileNotFoundError
        else:
            print("软件未运行")
    elif command == "保存波形":
        do_action_with_osc("保存波形", 'ctrl', 's')
    elif command == "读取波形到R1":
        do_action_with_osc("读取波形到R1", 'ctrl', 'o')
    elif command == "保存环境配置":
        do_action_with_osc("保存环境配置", 'ctrl', 'shift', 's')
    elif command == "读取环境配置":
        do_action_with_osc("读取环境配置", 'ctrl', 'shift', 'o')
    elif command == "打印":
        do_action_with_osc("打印", 'ctrl', 'p')
    elif command == "最小化":
        do_action_with_osc("最小化", 'ctrl', 'm')
    elif command in ("解码通道1设置", "解码通道一设置"):
        do_sequence_click("解码通道1设置", ['tongdao.png', 'JMtongdao1.png'])
    elif command in ("解码通道2设置", "解码通道二设置"):
        do_sequence_click("解码通道2设置", ['tongdao.png', 'JMtongdao2.png'])
    elif command in ("模拟通道1设置", "模拟通道一设置"):
        do_action_with_osc("模拟通道1设置", 'ctrl', '1')
    elif command in ("模拟通道2设置", "模拟通道二设置"):
        do_action_with_osc("模拟通道2设置", 'ctrl', '2')
    elif command in ("扩展通道1设置", "扩展通道一设置"):
        do_action_with_osc("扩展通道1设置", 'ctrl', 'shift', '1')
    elif command in ("扩展通道2设置", "扩展通道二设置"):
        do_action_with_osc("扩展通道2设置", 'ctrl', 'shift', '2')
    elif command == "水平设置":
        do_action_with_osc("水平设置", 'ctrl', 't')
    elif command == "实时采样":
        do_sequence_click("实时采样", ['shiji.png', 'sampling.png'])
    elif command == "峰值检测":
        do_sequence_click("峰值检测", ['shiji.png', 'peak_detection.png'])
    elif command == "平均":
        do_sequence_click("平均", ['shiji.png', 'average.png'])
    elif command == "触发设置":
        do_action_with_osc("触发设置", 'ctrl', 'g')
    elif command == "触发停止":
        do_sequence_click("触发停止", ['chufa.png', 'trigger_stop.png'])
    elif command == "自动触发":
        do_sequence_click("自动触发", ['chufa.png', 'auto_trigger.png'])
    elif command == "正常触发":
        do_sequence_click("正常触发", ['chufa.png', 'normal_trigger.png'])
    elif command == "单次触发":
        do_sequence_click("单次触发", ['chufa.png', 'single_trigger.png'])
    elif command == "边沿触发":
        do_sequence_click("边沿触发", ['chufa.png', 'edge_trigger.png'])
    elif command == "脉宽触发":
        do_sequence_click("脉宽触发", ['chufa.png', 'pulse_width_trigger.png'])
    elif command == "视频触发":
        do_sequence_click("视频触发", ['chufa.png', 'video_trigger.png'])
    elif command == "显示设置":
        do_action_with_osc("显示设置", 'f7')
    elif command == "YT栅格":
        do_sequence_click("YT栅格", ['xianshi', 'yt_grid.png'])
    elif command == "XY栅格":
        do_sequence_click("XY栅格", ['xianshi', 'xy_grid.png'])
    elif command == "测量设置":
        do_action_with_osc("测量设置", 'f9')
    elif command == "退出":
        if process:
            if click_osc_button():
                pyautogui.hotkey('alt', 'f4')
                print("已发送 Alt+F4 (退出)")
            else:
                print("退出操作: 未找到 OSC 按钮")
            process = None
        else:
            print("软件未运行")
    elif command == "over":
        if process:
            process.terminate()
            process.wait()
        break
    else:
        print("未知指令")