#Ｈｅｌｌｔａｋｅｒ ｃ３ｒｂ



import time
from DrissionPage import ChromiumPage, ChromiumOptions
from colorama import Fore, Style

def print_logo():
    logo = f"""
    {Fore.RED}******************************************************************************{Style.RESET_ALL}
    {Fore.GREEN}██╗  ██╗███████╗██╗     ██╗     ████████╗ █████╗ ██╗  ██╗███████╗██████╗     ██╗  ██╗{Style.RESET_ALL}
    {Fore.GREEN}██║  ██║██╔════╝██║     ██║     ╚══██╔══╝██╔══██╗██║  ██║██╔════╝██╔══██╗    ╚██╗██╔╝{Style.RESET_ALL}
    {Fore.GREEN}███████║█████╗  ██║     ██║        ██║   ███████║███████║█████╗  ██████╔╝     ╚███╔╝ {Style.RESET_ALL}
    {Fore.GREEN}██╔══██║██╔══╝  ██║     ██║        ██║   ██╔══██║██╔══██║██╔══╝  ██╔══██╗     ██╔██╗ {Style.RESET_ALL}
    {Fore.GREEN}██║  ██║███████╗███████╗███████╗   ██║   ██║  ██║██║  ██║███████╗██║  ██║    ██╔╝ ██╗{Style.RESET_ALL}
    {Fore.RED}╚═╝  ╚═╝╚══════╝╚══════╝╚══════╝   ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝    ╚═╝  ╚═╝{Style.RESET_ALL}
    {Fore.RED}******************************************************************************{Style.RESET_ALL}
    """
    print(logo)

def print_status(message, status_type='info'):
    if status_type == 'info':
        print(f"{Fore.BLUE}[INFO] {Style.RESET_ALL}{message}")
    elif status_type == 'success':
        print(f"{Fore.GREEN}[SUCCESS] {Style.RESET_ALL}{message}")
    elif status_type == 'warning':
        print(f"{Fore.YELLOW}[WARNING] {Style.RESET_ALL}{message}")
    elif status_type == 'error':
        print(f"{Fore.RED}[ERROR] {Style.RESET_ALL}{message}")

def pass_cycle(_driver: ChromiumPage):
    try:
        if _driver('xpath://div/iframe').s_ele(".ctp-checkbox-label") is not None:
            print_status("CAPTCHA found, attempting to bypass...", "warning")
            _driver('xpath://div/iframe').ele(".ctp-checkbox-label", timeout=0.1).click()
            print_status("CAPTCHA bypassed successfully!", "success")
    except:
        print_status("Failed to bypass CAPTCHA.", "error")
        pass


if __name__ == '__main__':
    print_logo()  

    browser_path = "/usr/bin/google-chrome"

    options = ChromiumOptions()
    options.set_paths(browser_path=browser_path) 

    arguments = [
        "-no-first-run",
        "-force-color-profile=srgb",
        "-metrics-recording-only",
        "-password-store=basic",
        "-use-mock-keychain",
        "-export-tagged-pdf",
        "-no-default-browser-check",
        "-disable-background-mode",
        "-enable-features=NetworkService,NetworkServiceInProcess,LoadCryptoTokenExtension,PermuteTLSExtensions",
        "-disable-features=FlashDeprecationWarning,EnablePasswordsAccountStorage",
        "-deny-permission-prompts",
        "-disable-gpu"
    ]

    for argument in arguments:
        options.set_argument(argument)

    driver = ChromiumPage(options=options)

    print_status("Launching the browser and opening the website...", "info")
    driver.get('https://nowsecure.nl')

    while True:
        pass_cycle(driver)
        try:
            ele = driver.s_ele('xpath://h3')
            if ele.text == "nowSecure.nl":
                print_status("Website loaded successfully!", "success")
                break
        except:
            time.sleep(.1)

    time.sleep(5)
    driver.quit()
    print_status("Process completed successfully! Goodbye!", "success")














#Ｈｅｌｌｔａｋｅｒ ｃ３ｒｂ
