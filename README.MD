CLI 기본문법
기초문법
 touch : 파일생성
mkdir : 새 디렉토리 생성
ls : 현재 작업 중인 디렉토리 내부의 폴더/파일 목록을 출력
cd : 현재 작업 중인 디렉토리를 변경(위치 이동)
start : 폴더/파일을 열기(Mac에서는 open을 사용)
rm : 파일 삭제(-r 옵션을 사용해 디렉토리 삭제)

Git : 분산버전관리시스템
git의 3가지 영역 : Working Directory / Staging Area / Repository
repository 저장하렴너 staging 단계에서 저장해줘야함.

순서                                                                       *github, repository 생성
1. 폴더 생성                                                                    url 복사
2. bash로 git init                -    Working Directory 단계
3. studio로 들어가서 파일생성. 
4. git add dlkf.txt              -  Staging Area 단계
5. git commit -m "기록"           - (Local) Repository 단계
6. git remote add ***  url            - 저장해야함!
7. git push -u *** master
8. 원격(github) 확인

원격에서 가져올때
git pull *** master        - 변경사항만
git clone url              - 전체
