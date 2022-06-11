import matplotlib.pyplot as plt
import matplotlib.animation as animation
import random

fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)
SIZE = 100

nums = list(range(SIZE))
x = list(range(SIZE))

random.shuffle(nums)
ax1.bar(x, nums)

ans = [[]] * 100

for i in range(len(nums)):
    for j in range(len(nums)):
        if nums[i] < nums[j]:
            nums[i], nums[j] = nums[j], nums[i]
    ans[i] = nums.copy()


def animate(i):
    ax1.clear()
    try:
        ax1.bar(x, ans[i*5])
        ax1.axvline(x=i*5, color='r', linestyle='-')
    except:
        ax1.bar(x, list(range(SIZE)))
        ax1.axvline(x=SIZE-1, color='r', linestyle='-')

ani = animation.FuncAnimation(fig, animate, interval=200)
plt.show()