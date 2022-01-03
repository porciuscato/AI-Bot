import sys
import pathlib
import subprocess


class SimulRun:
    def __init__(self):
        self.simul_reset = ...
        self.simul_reset = ...
        self.input_value()

    def input_value(self):
        file_path = pathlib.Path(__file__).parent.absolute() / 'Simulator_v2.py'
        print("file_path: ", file_path)
        print("sys.argv : ", sys.argv)

        if len(sys.argv) == 1:
            sys.argv += ['1', '15', 'n']
        if len(sys.argv) == 4:
            print(sys.argv)
            print("sys.argv1 : ", sys.argv[1])
            if sys.argv[3] == "y":
                self.simul_reset = 'reset'
            elif sys.argv[3] == 'n':
                self.simul_reset = 'continue'
            else:
                print("y or n (소문자) 만 입력 가능 합니다.")
                exit(1)
            for i in range(int(sys.argv[1]), int(sys.argv[2]) + 1):
                print("run: ", i)
                subprocess.Popen(["python", str(file_path), str(i), self.simul_reset])

        #  ex) python SimulRun.py 1 4 n 로 실행 했을 때
        #       위 for문을 돌리면 아래 4개 명령을 실행한 것과 같다.
        #       python Simulator_v2.py 1 continue
        #       python Simulator_v2.py 2 continue
        #       python Simulator_v2.py 3 continue
        #       python Simulator_v2.py 4 continue
        #
        # else:
        #     print("인자 3개를 입력 해주세요 ")


if __name__ == "__main__":
    SimulRun()
