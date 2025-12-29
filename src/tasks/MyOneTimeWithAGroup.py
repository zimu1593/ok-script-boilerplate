from qfluentwidgets import FluentIcon

from src.tasks.MyBaseTask import MyBaseTask


class MyOneTimeWithAGroup(MyBaseTask):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name = "采集-Z"
        self.description = "放在不同分组"
        self.group_name = "A分组"
        self.group_icon = FluentIcon.SYNC
        self.icon = FluentIcon.SYNC

    def run(self):
        # self.log_info('放在不同分组tab里的任务!', notify=True)
        while True:
            # self.log_info('采集-Z任务开始运行!', notify=True)
            # self.send_key('space',0.2)
            self.click(0.86, 0.85)
            self.click(0.5, 0.9)
            self.sleep(5)
