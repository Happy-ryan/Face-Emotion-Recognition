# Face-Emotion-Recognition

## **💡프로젝트 요약**
인간의 감정을 구분하는 딥러닝 모델을 AU스코어를 추출하고 다중 로지스틱 회귀를 이용하여 설명함으써 분류의 근거를 얻는다.


## **💡프로젝트 개요**

## **💡버전**
```
TensorFlow 2.5.1 이상
Python 3.8.10 이상
matplotlib 3.5.1
```
## **💡사용법**
1. 폴더 생성하기
- [creatFolder.py](https://github.com/Happy-ryan/Face-Emotion-Recognition/blob/main/src/creatFloder.py)으로 OpenFace > input, output 생성

2. docker 다운로드 및 실행 
- [docker download](https://docs.docker.com/get-docker/) 후 실행

3. 명렁어 실행
!커널 설치
wslstorestorage.blob.core.windows.net/wslblob/wsl_update_x64.msi
!openface 실행
docker run -it --rm -d --name openface -v C:\OpenFace\input:/home/openface-build/build/bin/input -v C:\OpenFace\output:/home/openface-build/build/bin/processed -w /home/openface-build/build/bin algebr/openface:latest
!input 하위 폴더의 데이터 분석 
docker exec openface ./FaceLandmarkImg -fdir input/[폴더명] -out_dir processed/[폴더명]
!실행결과
<img width="340" alt="happyhappy" src="https://user-images.githubusercontent.com/101412264/186548779-5e1f45e0-39b4-47cc-86de-8a5c20250f05.PNG">

4. 

## **💡모델 성능** 
- Model : [best_model.hdf5](https://github.com/Happy-ryan/Face-Emotion-Recognition/blob/main/models/best_model.hdf5)
- loss : 0.4320
- val_loss : 0.7306
- accuracy : 0.8518
- val_accuracy : 0.7353
- last update : 22/08/24
- 실험 결과 :

## **데이터셋** 
총 6종 선정
1. train_data
- angry 713장
- disgust 220장
- happy 766장
- neutral 700장
- sad 1039장
- surprise 1041장
2. test_data
- 각 감정별 10장씩 60장
