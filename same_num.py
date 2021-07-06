List1 = ['aaa',111,(4,5),2.01]
List2 = ['bbb',333,3.14,(4,5)]
for l in List1:
    for x in List2:
        if l == x:
            print(str(l),'in List1 and List2')
    else:
        print(str(l),'only  in List1')