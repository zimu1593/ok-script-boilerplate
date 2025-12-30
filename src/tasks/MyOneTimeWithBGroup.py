from src.tasks.MyBaseTask import MyBaseTask


class MyOneTimeWithBGroup(MyBaseTask):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name = "暮光海岛"
        self.description = "暮光海岛金币点击"
        self.group_name = "暮光海岛"

    def run(self):
        self.log_info('查找金币并点击', notify=True)
        while True:
            try:
                self.wait_click_feature("jinbi", time_out=60)
            except Exception as e:
                self.log_info(f'点击金币失败: {e}')
