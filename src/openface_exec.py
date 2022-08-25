import os
# docker 실행 후 openface 실행 명렁어
os.system('docker run -it --rm -d --name openface -v C:\OpenFace\input:/home/openface-build/build/bin/input -v C:\OpenFace\output:/home/openface-build/build/bin/processed -w /home/openface-build/build/bin algebr/openface:latest')
# input 하위 폴더 분석 > output 하위 폴더 csv 파일 생성 명령어
os.system('docker exec openface ./FaceLandmarkImg -fdir input/[폴더명] -out_dir processed/[폴더명]')
