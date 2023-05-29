'''
Copyright 2023 Kojima Shun

This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.
This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.
You should have received a copy of the GNU General Public License along with this program. If not, see <https://www.gnu.org/licenses/>.
'''

print("\">\"が表示されたら、数字を入力してください。Enterを押すごとに、次の数を入力できます。\nすべての数字を入力し終わったら、bと入力してください。\nそうすれば、[何番目の数を表示しますか？]というプロンプトが表示されます。\n任意の数Xを入力すれば、最初に入力した数の中でX番目に小さい数を表示します。")

numbers = []

while True:
    arg = input(">")
    if arg == "b":
        break
    else:
        if arg.isdecimal() == True:
            numbers.append(arg)
        else:
            print(arg,"は、数字でもコマンドでもありません。数字か、bを入力してください。")

banme = int( input("[何番目の数を表示しますか？]") )

x = len(numbers) - 1
i = 1
while i <= x:
    temporary = numbers[i]
    j = i - 1
    while (x > i >= 0) and (numbers[j] >= temporary):
        if numbers[j] == temporary :
            del numbers[j]
            x -= 1
            j -= 1
        else :
            numbers[j + 1] = numbers[j]
            j -= 1
    numbers[j + 1] = temporary
    i += 1

if 0 < banme <= len(numbers) :
    print (numbers[banme - 1])
else :
    print (banme,"番目の数は存在しません。大きすぎるか、0または負の数である可能性があります。")
