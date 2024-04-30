# selenium基本的配置
from selenium.webdriver.common.by import By  # html 路径获取方法
from selenium import webdriver  # driver
from selenium.webdriver.common.by import By
from selenium.webdriver import Chrome  # 谷歌浏览器 参数
import pyautogui

import pyperclip  # Python操作剪切板：pyperclip库的使用
from time import sleep

port = 8057
pyautogui.PAUSE = 0.5  # 意味着所有pyautogui的指令都要暂停0.5
# 默认这项功能为True, 这项功能意味着：当鼠标的指针在屏幕的最坐上方，程序会报错；目的是为了防止程序无法停止
pyautogui.FAILSAFE = False

import socket

def check_port(address, port):
    # 创建套接字对象
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 检查端口是否占用
    result = sock.connect_ex((address, port))
    # 关闭套接字
    sock.close()
    # 返回结果
    print(result,result == 0)
    return result == 0


check_port('127.0.0.1',port)


def create_chrome_driver():
    option = webdriver.ChromeOptions()

    # 以本地打开的 特点端口浏览器为目标
    option.add_experimental_option(
        "debuggerAddress",
        "127.0.0.1:{}".format(port))
    chrome_driver = Chrome(options=option) # 端口占用会报错
    # 第四步，等待文件 设置 通用安全设置
    chrome_driver.implicitly_wait(5)
    with open('stealthFile/stealth.min.js') as f:  # 打开文件
        js = f.read()  # 文件值
    chrome_driver.execute_cdp_cmd(
        "Page.addScriptToEvaluateOnNewDocument", {
            "source": js})  # 批量设置
    chrome_driver.execute_cdp_cmd(
        "Page.addScriptToEvaluateOnNewDocument", {
            "source": """
                                    Object.defineProperty(navigator, 'webdriver', {
                                      get: () => undefined
                                    })
                                  """})

    # 第五步，返回加工好的浏览器对象
    return chrome_driver


def open_local_browser():
    chrome_path = 'cd C:/Program Files/Google/Chrome/Application'
    debugger = 'chrome.exe --remote-debugging-port={}'.format(port)
    print('运行：open_local_browser')
    pyautogui.hotkey('win', 'r')
    pyautogui.hotkey('enter')
    # set_clipboard(chrome_path)
    pyperclip.copy(chrome_path)
    pyautogui.hotkey('ctrl', 'v')
    pyautogui.hotkey('enter')

    # set_clipboard(debugger)  # 使用复制
    pyperclip.copy(debugger)

    pyautogui.hotkey('ctrl', 'v')
    pyautogui.hotkey('enter')


open_local_browser()
sleep(4)
driver = create_chrome_driver()
driver.get('https://www.google.com')

sleep(10)
print('关闭浏览器')
driver.close()
driver.quit()



# input = driver.find_element(By.XPATH, '//input[@id="su"]')
#
# print(input, 'xxx')
