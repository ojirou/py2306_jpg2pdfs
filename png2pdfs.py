import os
import img2pdf
import glob
from PIL import Image
def main():
    BaseFolder = input('複数の対象フォルダが入っているベースフォルダ名を入力　>> ')
    folders=os.listdir(BaseFolder)
    for folder_name in folders:
        img_Folder=BaseFolder+'//'+folder_name+'//'
        pdf_FileName = BaseFolder + '//' + folder_name + '.pdf'
        extension  = ".png"
        print('img_Folder', img_Folder)
        print('pdf_FileName', pdf_FileName)
        if glob.glob(img_Folder+'*'+extension)!=[]:
            with open(pdf_FileName,"wb") as f:
                f.write(img2pdf.convert([Image.open(img_Folder+j).filename for j in os.listdir(img_Folder)if j.endswith(extension)]))
        else:
            print(extension+'ファイルは、存在しません')
if __name__ == "__main__":
    main()