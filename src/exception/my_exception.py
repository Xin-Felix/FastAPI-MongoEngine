class MyError(Exception):
    def __init__(self, err_desc: str = "出现错误啦!", code: int = 400):
        self.err_desc = err_desc
        self.err_code = code
