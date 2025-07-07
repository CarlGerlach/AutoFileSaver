import shutil


src_path = r"D:\Alles mögliche"
dst_path = r"\\MYCLOUDEX2ULTRA\Carl\Saves\saves-alles-mögliche\saveFile"





def copyDirecory():
    shutil.rmtree(dst_path)
    shutil.copytree(src_path, dst_path)


copyDirecory()
