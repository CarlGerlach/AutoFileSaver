import schedule as schedule
import shutil


src_path = r"D:\testdict\\"
dst_path = r"D:\test saves folder\test"


def copyDirecory():
    shutil.rmtree(dst_path)
    shutil.copytree(src_path, dst_path)


copyDirecory()
