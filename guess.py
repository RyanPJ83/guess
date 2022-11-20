import random
start = input('請輸入開始值： ')
end = input('請輸入結束值： ')
start = int(start)
end = int(end)
ans = random.randint(start, end)
cnt = 0
while True:
	cnt += 1
	guess = input('plz input your ans: ')
	guess = int(guess)
	if guess == ans:
		print('congraduation!')
		print('您已猜過', cnt, '次')
		break
	elif guess > ans:
		print('你的回答比答案大')
	else:
		print('您的回答比答案小')
	print('您已猜過', cnt, '次')