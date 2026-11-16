with open(r"E:\Darshan_Weneura\Task-4\wallpaper.png", "rb") as f:
    x = f.read()
    
with open(r"E:\Darshan_Weneura\Task-4\new_demo.txt", "wb") as y:
    y.write(x)

with open(r"E:\Darshan_Weneura\Task-4\new_demo.txt", "rb") as B:
    print(B.read())