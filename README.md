# Face-Emotion-Recognition

## **💡프로젝트 요약**
인간의 감정을 구분하는 딥러닝 모델을 AU스코어를 추출하고 다중 로지스틱 회귀를 이용하여 설명함으써 분류의 근거를 얻는다.


## **💡프로젝트 개요**
 코로나가 발생으로 인해 실내외에서 마스크를 착용한 지 2년이 넘으며 방역 기조 전환으로 인해 실외 착용 의무가 해제됐지만 마스크는 여전히 실내나 실외 다중이용시설에서는 꼭 착용해야 한다.
 
 
이와 같은 마스크 착용 장기화는 어린이들의 얼굴 인식 능력에 부정적 영향을 미친다는 연구가 발표되고 있는 상황이다. 따라서 본 프로젝트는 차후 어린이들의 감정 이해 및 학습을 도울 수 있는 하나의 방안으로서 “인간의 감정을 판단할 수 있는 학습모델”을 만드는 것을 목표로 한다. 


우선 가장 대표적인 감정 6가지(angry, disgust, happy, neutral, sad, surprise)를 선정하여  [데이터 셋](#데이터셋)을 구성하였다. 오픈소스 ‘openface’를 활용해 데이터셋을 분석하여 각 감정의 좌표 및 AU스코어 jpg파일, csv파일 데이터셋을 확보했다. 6가지 감정을 분류하는 방법은 다중 로지스틱 회귀 방식을 이용했으며 속성은 AU_r, 클래스는 6가지 감정으로 정했다. 


 마지막으로 AU스코어를 활용한 다중로지스틱 회귀 방식의 모델, 구글에서 제공하는 서비스인 Teachable Machine 활용 모델, CNN 활용 모델(based [kaggle](https://www.kaggle.com/datasets/msambare/fer2013)을 비교해볼 예정이다.

## **💡버전**
```
TensorFlow 2.9.2 
Python 3.8.13 이상
matplotlib 3.5.2
keras 2.9.0
```
## **💡사용법**
1. Creat folder
- [creatFolder.py](https://github.com/Happy-ryan/Face-Emotion-Recognition/blob/main/src/creatFloder.py)으로 OpenFace > input, output 생성

2. Docker download 
- [docker download](https://docs.docker.com/get-docker/) 후 실행

3. Window powershell command
- 커널 설치
  > wslstorestorage.blob.core.windows.net/wslblob/wsl_update_x64.msi
- openface 실행
  > docker run -it --rm -d --name openface -v C:\OpenFace\input:/home/openface-build/build/bin/input -v C:\OpenFace\output:/home/openface-build/build/bin/processed -w /home/openface-build/build/bin algebr/openface:latest
- input 하위 폴더의 데이터셋 분석 
  > docker exec openface ./FaceLandmarkImg -fdir input/[폴더명] -out_dir processed/[폴더명]

4. Execution result
- [command.ipynb](https://github.com/Happy-ryan/Face-Emotion-Recognition/blob/main/src/command.ipynb)
> <img width="304" alt="hahahah" src="https://user-images.githubusercontent.com/101412264/186561481-37dda9e5-13ea-486e-8301-206c37307ba9.PNG">

## **💡모델 성능** 
- Model : [best_model.hdf5](https://github.com/Happy-ryan/Face-Emotion-Recognition/blob/main/models/best_model.hdf5)
- loss : 0.4320
- val_loss : 0.7306
- accuracy : 0.8518
- val_accuracy : 0.7353
- last update : 22/08/24
- 실험 결과 : [exec_final.ipynb](https://github.com/Happy-ryan/Face-Emotion-Recognition/blob/main/src/exec_final.ipynb)

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
