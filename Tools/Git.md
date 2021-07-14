# Git

## 03월 19일

### 02. GIT UNDO

> 과거로 돌아가는 기능 구현해보기

`git status 찍어보고 거기서 나오는 명령어 사용하는 것이 BEST`

- add만 한 경우

```bash
$ git add a.txt
$ git rm --cached a.txt
> rm '파일이름'
	=> add한 것을 다시 remove해줌
```



- add 하고 commit까지 한 후, 다시 수정하고 add 한 경우

```bash
$ git restore --staged a.txt
```



- commit을 했는데, 그것을 취소하고 싶은 경우

  (가장 마지막에 한 commit만 취소 가능)

```bash
$ git add .
$ git commit -m "update my data"
$ git log
	=> commit 상태확인
$ git commit --amend
	=> 방금 한 commit 취소
>> i누르면 : 데이터 입력 모드
>> esc : 끼워넣기 모드 취소

	=> i 눌러서 commit 메세지 수정
	=> esc 눌러서 끼워넣기 모드 벗어나기
	=> :wq (콜론:wq) 입력 : 나가기
$ git log
	=> 상태 확인
```



- commit까지 했는데 업로드할 파일을 추가 못했을 경우

```bash
$ git add a.txt
$ git commit -m "update a,b"
	=>  b.txt도 업도르 했어야 했는데 add 못함

$ git add b.txt
$ git status
$ git commit --amend
>> :wq
	=> commit 메세지 수정할 거 없고 a,b다 업로드 됐으니까
	=> 나오면 됨
```



> commit을 쌓기

- hard

```bash
$ git log --oneline
	=> commit 쌓은 거 간략히 확인
$ git reset --hard 돌아가고자하는 commit의 id 이름
	=> 그 시점으로 돌아가게됨 (입력한 코드도)
	=> 그럼 다시 그 다음 코드를 입력하고 commit 하면 됨
```



- soft

```bash
$ git log --oneline
$ git reset --soft 돌아가고자하는 commit의 id 이름
	=> hard와는 다르게 그 시점으로 돌아가긴 하지만
	=> 파일에 입력했던 코드는 그대로!!
	=> Staging Area에 있게 됨
```



- mixed

```bash
$ git log --oneline
$ git reset 돌아가고자하는 commit의 id 이름
	=> mixed는 기본 default 값 (안적어도 됨)
	=> soft와 같이 commit은 돌아가지만
	=> 코드는 그대로
	=> 그리고!! add 전 단계 까지 남아있다.
$ git status
	=> Working Directory 로 가게 됨
```

