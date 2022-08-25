# Face-Emotion-Recognition

## **💡프로젝트 요약**
인간의 감정을 구분하는 딥러닝 모델을 AU스코어를 추출하고 다중 로지스틱 회귀를 이용하여 설명함으써 분류의 근거를 얻는다.


## **💡프로젝트 개요**
 코로나가 발생으로 인해 실내외에서 마스크를 착용한 지 2년이 넘으며 방역 기조 전환으로 인해 실외 착용 의무가 해제됐지만 마스크는 여전히 실내나 실외 다중이용시설에서는 꼭 착용해야 한다.
 
 
이와 같은 마스크 착용 장기화는 어린이들의 얼굴 인식 능력에 부정적 영향을 미친다는 연구가 발표되고 있는 상황이다. 따라서 본 프로젝트는 차후 어린이들의 감정 이해 및 학습을 도울 수 있는 하나의 방안으로서 **인간의 감정을 판단할 수 있는 학습모델**을 만드는 것을 목표로 한다. 


우선 가장 대표적인 감정 6가지(angry, disgust, happy, neutral, sad, surprise)를 선정하여  [데이터 셋](#데이터셋)을 구성하였다. [오픈소스 ‘openface’](https://github.com/TadasBaltrusaitis/OpenFace/wiki/Action-Units)를 활용해 데이터셋을 분석하여 각 감정의 좌표 및 AU스코어 jpg파일, csv파일 데이터셋을 확보했다. 6가지 감정을 분류하는 방법은 **다중 로지스틱 회귀 방식**을 이용했으며 **속성은 AU_r, 클래스는 6가지 감정**으로 정했다. 


 마지막으로 AU스코어를 활용한 [다중로지스틱 회귀 방식의 모델](https://github.com/Happy-ryan/Face-Emotion-Recognition/blob/main/src/model.ipynb), 구글에서 제공하는 서비스인 [Teachable Machine 활용 모델](https://github.com/Happy-ryan/Face-Emotion-Recognition/blob/main/src/Teachable_machine_model.ipynb), [CNN 활용 모델](https://github.com/Happy-ryan/Face-Emotion-Recognition/blob/main/src/CNN_model.ipynb)(based [kaggle data_set](https://www.kaggle.com/datasets/msambare/fer2013))의 성능을 비교해본다.

## **💡버전**
```
TensorFlow 2.9.2 
Python 3.8.13 이상
matplotlib 3.5.2
keras 2.9.0
```
## **💡 1.오픈소스 환경 설정 및 데이터 추출 방법**
### 1) 오픈소스 환경 설정
1. Creat folder
- [creatFolder.py](https://github.com/Happy-ryan/Face-Emotion-Recognition/blob/main/src/creatFloder.py)으로 OpenFace > input, output 생성

2. Docker download 
- [docker download](https://docs.docker.com/get-docker/) 후 starting

3. Window powershell command 커널 설치
```
wslstorestorage.blob.core.windows.net/wslblob/wsl_update_x64.msi
```
### 2) 데이터셋 추출
방법1. window powershell command 입력
docker 실행 후 openface 
```
docker run -it --rm -d --name openface -v C:\OpenFace\input:/home/openface-build/build/bin/input -v C:\OpenFace\output:/home/openface-build/build/bin/processed -w /home/openface-build/build/bin algebr/openface:latest
```
input 하위 폴더의 데이터셋 분석
  > input의 하위 폴더에 분석하고자하는 데이터(jpg형식만 가능)저장 
```
docker exec openface ./FaceLandmarkImg -fdir input/[폴더명] -out_dir processed/[폴더명]
```
방법2. 파이썬 코드 입력
```
import os
# docker 실행 후 openface 실행 명렁어
os.system('docker run -it --rm -d --name openface -v C:\OpenFace\input:/home/openface-build/build/bin/input -v C:\OpenFace\output:/home/openface-build/build/bin/processed -w /home/openface-build/build/bin algebr/openface:latest')
# input 하위 폴더 분석 > output 하위 폴더 csv 파일 생성 명령어
os.system('docker exec openface ./FaceLandmarkImg -fdir input/[폴더명] -out_dir processed/[폴더명]')
```
- 실행결과 :  [command.ipynb](https://github.com/Happy-ryan/Face-Emotion-Recognition/blob/main/src/command.ipynb)
> <img width="304" alt="hahahah" src="https://user-images.githubusercontent.com/101412264/186561481-37dda9e5-13ea-486e-8301-206c37307ba9.PNG">


## **💡 2 .최종 학습 데이터 생성 및 모델 설계 방법**
### 1) csv파일 통합 후 au_r 스코어 추출 > 최종 학습데이터 생성
- 각 클래스별로 반복해서 csv파일 만들기 > 결과: [/data/csv/angry.csv](https://github.com/Happy-ryan/Face-Emotion-Recognition/blob/main/data/csv/angry.csv),[/data/csv/disgust.csv](https://github.com/Happy-ryan/Face-Emotion-Recognition/blob/main/data/csv/disgust.csv),[/data/csv/happy.csv](https://github.com/Happy-ryan/Face-Emotion-Recognition/blob/main/data/csv/happy.csv),[/data/csv/neutral.csv](https://github.com/Happy-ryan/Face-Emotion-Recognition/blob/main/data/csv/nutral.csv), [/data/csv/sad.csv](https://github.com/Happy-ryan/Face-Emotion-Recognition/blob/main/data/csv/sad.csv),[/data/csv/surprise.csv](https://github.com/Happy-ryan/Face-Emotion-Recognition/blob/main/data/csv/surprise.csv)
```
import os
import pandas as pd

file_csv = []
def print_files_in_dir(root_dir):
    files = os.listdir(root_dir)
    for file in files:
        path = os.path.join(root_dir, file)
        file_name = path
        if file_name[-4:] =='.csv':
            file_csv.append(file_name)
 
if __name__ == "__main__":
    root_dir = r"C:\OpenFace\output\[각 감정 폴더명]"
    print_files_in_dir(root_dir)

# csv 파일 > dataframe 읽고 통합하기
all_df = pd.DataFrame()
for path in file_csv:
    df = pd.read_csv(path)
    all_df = pd.concat([all_df,df],ignore_index=True)
```
**AU_r 스코어(속성) 추출 및 클래스(감정)추가 & csv저장**
```
all_df_X = all_df.iloc[:,-35:-18]
all_df['emotion'] = # 추출하는 감정 데이터에 맞춰서 숫자 넣기 - angry : 0 , disgust : 1, happy : 2, neutral : 3, sad : 4, surprise:5
all_df.to_csv('emotion.csv')
```
- 실행결과 
> 위의 과정 반복 후 각 클래스별csv 파일을 전부 합쳐서 **최종 학습데이터** [**emotion.csv**](https://github.com/Happy-ryan/Face-Emotion-Recognition/blob/main/data/csv/emotion.csv) 생성

### 2) 학습 진행 : 다중 로지스틱 회귀분석 > 모델 설계
학습할 데이터 불러오기 및 랜덤추출
```
df_pre = pd.read_csv('emotion.csv')

df_all = df_pre.sample(frac=1)
```
원-핫코딩
```
dataset = df_all.values

import tensorflow as tf
from sklearn.preprocessing import LabelEncoder

X = dataset[:,:-1].astype(float) # confidence 제외
Y = dataset[:,-1]
Y_encoded = tf.keras.utils.to_categorical(Y)
```
데이터셋(emotion.csv)에서 train,test 설정 
```
X_train,X_test,Y_train,Y_test = train_test_split(X,Y_encoded,
                                                 test_size = 0.25)
```
딥러닝 모델 결정하기 : relu 와 softmax 사용
```
model = Sequential()
model.add(Dense(300,input_dim=17,activation="relu"))
model.add(Dense(200,activation="relu"))
model.add(Dense(100,activation="relu"))
model.add(Dense(50,activation="relu"))
model.add(Dense(6,activation="softmax"))
model.compile(loss='categorical_crossentropy',
              optimizer='adam',
              metrics=['accuracy'])
```
자동 중단 설정 
```
early_stopping_callback = EarlyStopping(monitor='val_loss',patience=7)
```
모델 저장 폴더 생성 및  저장 조건 설정
```
MODEL_DIR = './model'
if not os.path.exists(MODEL_DIR):
  os.mkdir(MODEL_DIR)
# 모델 저장 조건 설정
modelpath = './model/{epoch:02d}-{val_loss:.4f}.hdf5'
checkpointer = ModelCheckpoint(filepath=modelpath,
                               monitor="val_loss",
                               verbose=1,
                               save_best_only=True)
```
모델 실행하기 및 저장
```
history = model.fit(X_train,Y_train,
                    validation_split=0.33,
                    epochs=5000,
                    batch_size=50,
                    callbacks=[early_stopping_callback,checkpointer])
```

## **💡모델 성능** 
- Model : [best_model.hdf5](https://github.com/Happy-ryan/Face-Emotion-Recognition/blob/main/models/best_model.hdf5)
- loss : 0.4320
- val_loss : 0.7306
- accuracy : 0.8518
- val_accuracy : 0.7353
- last update : 22/08/24
- 실험 결과 : [model.ipynb](https://github.com/Happy-ryan/Face-Emotion-Recognition/blob/main/src/model.ipynb)

## **💡모델 테스트** 
- 학습하지 않은 [test_data]()을 [best_model.hdf5](https://github.com/Happy-ryan/Face-Emotion-Recognition/blob/main/models/best_model.hdf5) 넣어 정답률 파악
- 실행결과
[exec_final.ipynb](https://github.com/Happy-ryan/Face-Emotion-Recognition/blob/main/src/exec_final.ipynb)

## **💡모델 성능 비교**
1. 데이터 수에 따른 각 감정별 정답률 판단
- model ( based [데이터 셋](#데이터셋) : 총 train_data 수 : 4474 / 총 test_data : 60 )
> <img width="378" alt="model" src="https://user-images.githubusercontent.com/101412264/186623603-38c37561-ec9b-4989-9e26-013ac503627f.png">


- CNN ( based [kaggle data_set](https://www.kaggle.com/datasets/msambare/fer2013) : 총 train_data 수 : 25538 / 총 test_data 수 7168 )
> <img width="376" alt="CNN" src="https://user-images.githubusercontent.com/101412264/186623588-4af2aa46-203b-4cc7-82cf-862cd8cadc49.png">


- Teachable machine ( based[데이터 셋](#데이터셋) : 총 train_data 수 : 4474 / 총 test_data : 60 )  
> <img width="421" alt="ㅇㅇ" src="https://user-images.githubusercontent.com/101412264/186637822-e5c234fe-ca69-481f-9e99-fce62be79658.png">


-정리
> Teachable machine 모델과 CNN 모델 모두 CNN을 기본으로 하는데 각 데이터를 학습하고 test_data에 대한 각 감정 판정률 및 전체 정답률 차이가 심하게난다. 이는 CNN기반으로
> 인간의 감정을 판단하기 위해서는 **kaggle 데이터만큼 아주 많은 수의 데이터가 있어야 유의미한 학습이 진행되어 판정을 할 수 있다는 결론**이 나온다.
> 
> 그에 반해 model은 CNN 모델 학습 데이터 수의 17%에 불과하지만 test_data에 대해서 CNN모델과 유사한 경향과 정답률을 보여준다. 
> 이를 통해서 **AU_r 스코어가 인간의 감정과 유의미한 상관관계가 있어 적은 수의 데이터로도 높은 확률로 인간의 감정을 판단할 수 있다는 결론**을 알 수 있다.

2. [test_data]()에 대한 두 가지 모델 전체 정답률 비교
- AU스코어를 활용한 다중로지스틱 회귀 방식의 모델 : **전체 정답률 : 0.80**
- Teachable Machine 활용 모델 : **전체 정답률 : 0.47**

- 정리
> 데이터의 수가 적을 때 그리고 분류해야할 클래스가 많을 때 Teachable Machine 모델은 제대로 감정 판정을 하기 어려운 것을 알 수 있다.


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
