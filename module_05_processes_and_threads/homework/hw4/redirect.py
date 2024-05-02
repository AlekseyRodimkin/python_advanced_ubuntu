"""
Иногда возникает необходимость перенаправить вывод в нужное нам место внутри программы по ходу её выполнения.
Реализуйте контекстный менеджер, который принимает два IO-объекта (например, открытые файлы)
и перенаправляет туда стандартные потоки stdout и stderr.

Аргументы контекстного менеджера должны быть непозиционными,
чтобы можно было ещё перенаправить только stdout или только stderr.
"""
import traceback
from types import TracebackType
from typing import Type, Literal, IO
import sys


class Redirect:
    def __init__(self, stdout: IO = None, stderr: IO = None) -> None:
        self.stdout, self.stderr = stdout, stderr
        self.orig_stdout, self.orig_stderr = sys.stdout, sys.stderr

    def __enter__(self):
        if self.stdout:
            sys.stdout = self.stdout
        if self.stderr:
            sys.stderr = self.stderr

    def __exit__(
            self,
            exc_type: Type[BaseException] | None,
            exc_val: BaseException | None,
            exc_tb: TracebackType | None
    ) -> Literal[True] | None:
        try:
            if self.stderr and exc_type:
                sys.stderr.write(traceback.format_exc())
                return True
            elif exc_type:
                raise exc_val
        finally:
            if self.stdout:
                sys.stdout = self.orig_stdout
            if self.stderr:
                sys.stderr = self.orig_stderr
        sys.stdout, sys.stderr = self.orig_stdout, self.orig_stderr

        return True


if __name__ == '__main__':
    print('Hello stdout 1')
    stdout_file = open('stdout.txt', 'w')
    stderr_file = open('stderr.txt', 'w')

    with Redirect(stdout=stdout_file, stderr=stderr_file):
        print('Hello stdout.txt 2')
        raise Exception('Hello stderr.txt 1')
    stdout_file.close()
    stderr_file.close()
    print('Hello stdout 3')
    raise Exception('Hello stderr.txt 2')
