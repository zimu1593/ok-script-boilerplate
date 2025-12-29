from src.tasks.MyBaseTask import MyBaseTask


class MyOneTimeWithBGroup(MyBaseTask):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name = "采集-F"
        self.description = "采集"
        self.group_name = "采集"

    def run(self):
        while True:
            # 调用 OCR 方法查找文字“关闭”
            close_boxes = self.ocr(match="关闭", threshold=0.8)
            if close_boxes:
                # 如果找到“关闭”文字，获取第一个匹配的 Box
                close_box = close_boxes[0]
                self.log_info(f"找到文字 '关闭'，位置: {close_box.center()}")
                # 可选操作：点击找到的“关闭”按钮
                self.send_key('space')
                # self.click(close_box)
                self.log_info("已点击 '关闭' 按钮。")
            else:
                self.log_info("未找到文字 '关闭'。")
                self.send_key('f')
                self.sleep(0.1)
                self.send_key('f')
                self.sleep(0.1)
                self.send_key('f')
                self.sleep(0.1)
            self.sleep(5)
