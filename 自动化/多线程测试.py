import threading

def edge(index):

    print("index",index)
    index+=1
    print("index", index)


class myThead(threading.Thread):
    def __init__(self,page):
        threading.Thread.__init__(self)
        self.page = page

    def run(self):
        print(self.page,"selfpage")
        edge(1)


f1 = myThead(1)
f1.start()
f1.join()

print("数量",threading.active_count(),"sd")