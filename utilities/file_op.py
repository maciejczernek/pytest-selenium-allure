import os
import shutil
import platform

RESULTS_PATH = "../test_results"


def copy_allure_history():
    history_path = os.path.join(RESULTS_PATH, r"allure-report/history")
    target_path = os.path.join(RESULTS_PATH, r"allure-results/history")

    if not os.path.isdir(history_path):
        print("Folder doesn't exist")
        return

    shutil.copytree(history_path, target_path, dirs_exist_ok=True)


def create_environment_properties_file(driver, extra_info):
    target_path = os.path.join(RESULTS_PATH, r"allure-results")
    file_path = os.path.join(target_path, "environment.properties")
    info = [
        f"system = {platform.system()} {platform.release()}",
        f"browser = {driver.capabilities['browserName']}, {driver.capabilities['browserVersion']}",
        f"resolution = {extra_info['resolution']}",
        f"headless_mode = {extra_info['headless']}"
    ]
    with open(file_path, "w") as f_obj:
        for item in info:
            f_obj.write(f"{item}\n")


def generate_report():
    os.chdir(RESULTS_PATH)
    os.system("allure generate --clean")


def create_report_folder():
    path = os.path.join(RESULTS_PATH, r"allure-report")
    if not os.path.isdir(path):
        os.mkdir(path)
