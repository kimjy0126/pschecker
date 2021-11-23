# pschecker

맞았는데 왜 틀려요?

틀리니까 틀렸지!

## usage

`python.exe pschecker.py <your execution> <solution execution> <num of input files>`

### execution

코드를 실행할 방법을 쓰면 된다. `"A.exe"`, `"python.exe B.py"` 등등...

### input

input 파일은 다음과 같은 형식을 따라야 한다:  
`input[0-9][0-9][0-9].txt`

`input000.txt`에서 `input999.txt`까지 인식이 된다. 숫자 세자리를 꼭 맞춰야 한다.

`<num of input files>`는 최대 1000이다.

input file generator는 알아서 짜도록 하자.

### example

`python.exe pschecker.py "A.exe" "python.exe B.py" 500`