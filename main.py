'''
Copyright 2023 Kojima Shun
This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or any later version.
This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.
You should have received a copy of the GNU General Public License along with this program. If not, see <https://www.gnu.org/licenses/>.
'''

print("\">\"が表示されたら、数字を入力してください。Enterを押すごとに、次の数を入力できます。\nすべての数字を入力し終わったら、bと入力してください。\nそうすれば、[何番目の数を表示しますか？]というプロンプトが表示されます。\n任意の数Xを入力すれば、最初に入力した数の中でX番目に小さい数を表示します。")

list = []

while True:
    arg = input(">")
    if arg == "b":
        break
    else:
        if arg.isdecimal() == True:
            list.append(arg)
        else:
            print(arg,"は、数字でもコマンドでもありません。数字か、bを入力してください。")

banme = int( input("[何番目の数を表示しますか？]") )

x = len(list) - 1

i = 1

while i <= x :
    how_many_deleted = 0
    j = i - 1
    tmp = list[i]
    
    while 0 <= j < x and i <= x:
        if list[j] < tmp :
            i = i + 1 - how_many_deleted
            break
        elif list[j] == tmp :
            del list[j + 1]
            j = j - 1
            x = x - 1
            how_many_deleted = how_many_deleted + 1
        else :
            list[j + 1] = list[j]
            list[j] = tmp
            j = j - 1

if 0 < banme <= len(list) :
    print ("結果：", list[banme - 1])
else :
    print (banme,"番目の数は存在しません。大きすぎるか、0または負の数である可能性があります。")
