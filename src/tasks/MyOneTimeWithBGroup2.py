from src.tasks.MyBaseTask import MyBaseTask


class MyOneTimeWithBGroup2(MyBaseTask):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name = "刷毒塔"
        self.description = "刷毒塔"
        self.group_name = "刷毒塔"

    def run(self):
        while True:
            # self.log_info('放在不同分组tab里的任务2开始运行!', notify=True)
            self.send_key('1')
            self.sleep(2)
            self.send_key('e')
            self.sleep(3)
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
            self.sleep(2)

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
            self.sleep(5)
