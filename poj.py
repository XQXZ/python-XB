#coding=utf-8
import urllib

class User():

    def __init__(self, *args):
        self.problems = []
        self.count = 0
        self.username = ""
        self.iter = 0
        if len(args):
            self.username = args[0]
            self.load(self.username)

    def load(self, username):
        '''读取用户数据'''
        page = urllib.urlopen('http://poj.org/userstatus?user_id=' + username)
        page_lines = page.readlines()
        self.count = len(page_lines) - 26
        for p in page_lines[16:-10]:
            self.problems.append(p[2:-2])
        self.problems.sort()

    def __add__(self, o):
        '''两个用户提交的题目相加'''
        n = User()
        n.username = ' '.join(['(', self.username, '+', o.username, ')'])
        n.problems = list(set(self.problems + o.problems))
        n.problems.sort()
        n.count = len(n.problems)
        return n

    def __sub__(self, o):
        '''用户相减的结果为前面的AC而后面没有通过的'''
        n = User()
        n.username = ' '.join(['(', self.username, '-', o.username, ')'])
        n.problems = self.problems[:] #[:]深拷贝
        n.count = self.count
        for i in o.problems:
            if i in n.problems:
                n.problems.remove(i)
                n.count -= 1
        return n

    def __mul__(self, o):
        '''相乘的结果为两人同时通过的'''
        n = User()
        n.username = ' '.join(['(', self.username, '*', o.username, ')'])
        for i in self.problems:
            if i in o.problems:
                n.problems.append(i)
                n.count += 1
        return n

    def next(self):
        '''迭代'''
        if self.iter < self.count:
            self.iter += 1
            return self.problems[self.iter - 1]
        raise StopIteration
    
    def __iter__(self):
        return self

    def __str__(self):
        return self.username

    __repr__ = __str__


#if __name__ == '__main__':
    
a = User('MeiK')
b = User('15110572028')
    