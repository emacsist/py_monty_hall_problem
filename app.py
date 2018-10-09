import random
N=100000000

# 所有可能的场景. 1表示有车
scene=['001', '010', '100']
debug=False


swap = 0


for _ in range(0, N):
    # 分别对应上面的场景. 0:001, 1:010, 2:100
    # 假设的实际场景
    sceneMap=[0, 1, 2]
    sceneV = random.choice(sceneMap)
    
    if debug:
        print("实际场景为 {}".format(scene[sceneV]))

    # 允许选择的第 N 扇门
    door = [0, 1, 2]

    # 选择的门
    doorV = random.choice(door)

    if debug:
        print("你选择了第 {} 扇门".format(doorV))

    # 主持人打开另一扇没有车的门
    # 这个是有车的. 删除后, 剩下的两个都是没有车的了.那就再删除一个
    sceneMap.remove(sceneV)

    # 主持人选择打开的门号
    presenter_opened_door = random.choice(sceneMap)

    if debug:
        print("主持人打开了第 {} 扇门".format(presenter_opened_door))

    # 剩下的选项
    sceneMap.remove(presenter_opened_door)

    if debug:
        print("剩下的门为 {}, 实际的场景为 {}".format(sceneMap, scene[sceneV]))

    # 每次都选择交换的话, 开始的时候, 如果不为车, 交换就赢了.
    if doorV != sceneV :
        swap += 1
        if debug:
            print("恭喜你, 交换时赢了~")

    if debug:
        print("-" * 80)        


print("进行 {} 次模拟中, 交换的话, 赢的概率为 {:.2f}%, 不交换的话, 赢的概率为 {:.2f}%".format(N, swap / N * 100, (1-swap/N)*100))
