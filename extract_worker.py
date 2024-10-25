from PySide6.QtCore import QObject, Signal
# from SAM import extract_embedding 
from SAM_NEW import extract_embedding 

class ExtractWorker(QObject):
    finished = Signal(object)  # 定义一个信号，用于传递结果（例如 predictor）

    def __init__(self, image_path):
        super().__init__()
        self.image_path = image_path

    def run(self):
        # 在这里执行耗时的操作，例如提取 embedding
        predictor = extract_embedding(self.image_path)
        # 操作完成后发出信号，传递 predictor（提取结果）回主线程
        self.finished.emit(predictor)
