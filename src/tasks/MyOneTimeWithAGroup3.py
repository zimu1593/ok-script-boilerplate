from src.tasks.MyBaseTask import MyBaseTask


class MyOneTimeWithAGroup3(MyBaseTask):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name = "刷毒塔"
        self.description = "放在不同分组"
        self.group_name = "A分组"

    def run(self):
        # self.log_info('放在不同分组tab里的任务!', notify=True)
        while True:
            # self.log_info('放在不同分组tab里的任务2开始运行!', notify=True)
            self.sleep(1.5)
            self.send_key('1')
            self.sleep(2)
            self.send_key('e')
            self.send_key_down('space')
            self.sleep(1.5)
            self.send_key_up('space')
            self.sleep(0.5)
            self.send_key_down('space')
            self.sleep(0.5)
            self.send_key_up('space')
            self.sleep(0.5)
            self.send_key_down('space')
            self.sleep(0.5)
            self.send_key_up('space')
            self.sleep(3)
            self.send_key('q')
            try:
                guanbi_button = self.wait_feature("guanbi")
                if guanbi_button:
                    self.click(guanbi_button)
            except Exception as e:
                self.log_info(f'点击失败: {e}')
