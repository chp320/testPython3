# testPython3

## 목적
- 이 프로젝트는 파이썬을 통해 다양한 기능을 테스트함에 목적이 있다.

## 오류 기록
- urllib3 관련 오류 (test1.py)
  - 오류 상세: "urllib3 v2.0 only supports OpenSSL 1.1.1+, currently "
    ImportError: urllib3 v2.0 only supports OpenSSL 1.1.1+, currently the 'ssl' module is compiled with 'OpenSSL 1.1.0j  20 Nov 2018'. See: https://github.chttps://github.com/urllib3/urllib3/issues/2168
  - 위 오류는 파이썬의 ssl 모듈과 urllib 의 openssl 의 버전간 충돌(?)로 발생하는 것으로 urllib3 의 버전을 호환 가능 버전으로 변경하여 해결
``` python
pip3 install "urllib3 <=1.26.15"
```

## 사용법
- python test3.py sequence_number output_dir
- sh getData.sh     /* 스크립트 내 start, end, n 값을 변경 */

