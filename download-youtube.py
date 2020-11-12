import subprocess
import os
from concurrent.futures import ThreadPoolExecutor
import time
import shutil


class YoutubeDownload:
    def __init__(self, target_folder_path):
        self.download_command_template = 'youtube-dl -i --proxy socks5://127.0.0.1:10808 #ecode-video-placeholder# -o "{temp_folder}/%(title)s.%(ext)s" "{url}"'
        self.downloader = ThreadPoolExecutor(max_workers=2)
        self.target_folder_path = target_folder_path
        self.recode_video_sign = False

    def the_guide(self):
        self.prompt = '（当前Mp4转换状态：{recode_video_status}）（输入"mp4"切换状态）输入指令或Url：'
        self.prompt = self.prompt.format(recode_video_status=self.recode_video_sign)
        if self.recode_video_sign:
            self.download_command = self.download_command_template.replace('#ecode-video-placeholder#', '--recode-video mp4')
        else:
            self.download_command = self.download_command_template.replace('#ecode-video-placeholder#', '')

    def download_process(self, download_command):
        p = subprocess.Popen(download_command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, bufsize=1)
        for line in iter(p.stdout.readline, b''):
            line = line.decode().strip()
            print(line)
            if line.find('unable to extract') != -1:
                return False
        return True

    def download_dispatcher(self, url):
        print('开始下载：', url)
        temp_folder = str(time.time()).replace('.', '')
        download_command = self.download_command.format(temp_folder=temp_folder, url=url)
        print('下载指令：', download_command)
        retry_times = 5
        while retry_times >= 0:
            if self.download_process(download_command):
                success_sign = True
                break
            else:
                retry_times -= 1
        if success_sign:
            for file_ in os.listdir(temp_folder):
                shutil.move(os.path.join(temp_folder, file_), self.target_folder_path)
            shutil.rmtree(temp_folder)
            print('下载完成！', url)
        else:
            print('下载失败！', url)

    def run_local_loop(self):
        while True:
            self.the_guide()
            input_value = input(self.prompt).strip()
            if not input_value:
                continue
            if input_value == 'mp4':
                self.recode_video_sign = not self.recode_video_sign
            else:
                self.downloader.submit(self.download_dispatcher, input_value)


if __name__ == "__main__":
    api = YoutubeDownload(r'D:\syncthing-windows-amd64-v1.11.1\LOCAL_STORAGE\testout')
    api.run_local_loop()
