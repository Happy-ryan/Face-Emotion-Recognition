# command 일치를 위해서 폴더명 반드시 동일하게 생성
import os
def createFolder(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        print('Error:Creating directory.'+directory)

file_name = ['input','output']
for name in file_name:
    createFolder('C:/OpenFace/{}'.format(name))
    print('폴더가 생성 되었습니다.') # 코드 실행 체크 코드
