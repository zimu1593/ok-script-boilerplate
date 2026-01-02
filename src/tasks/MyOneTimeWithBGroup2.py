from src.tasks.MyBaseTask import MyBaseTask


class MyOneTimeWithBGroup2(MyBaseTask):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name = "采集-1"
        self.description = "采集"
        self.group_name = "采集"

    def run(self):
        while True:
            try:
                # self.wait_click_feature('caiji', time_out=5)
                # 查找关闭按钮
                guanbi_button = self.wait_feature("guanbi")
                if guanbi_button:
                    self.click(guanbi_button)
                # 查找采集按钮
                caiji_button = self.wait_feature("caiji", time_out=5)
                if caiji_button:
                    self.click(caiji_button)
            except Exception as e:
                self.log_info(f'点击失败: {e}')
