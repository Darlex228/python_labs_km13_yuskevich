from exp_root.exponentation import exp2, exp3
from exp_root.root import root2, root3
from factorial.factorial import fact
from logarithm.logarithm import log, ln, lg



def main():
    while True:
        print('''
        Якщо ви бажаєте піднести до степені, напишіть "exp"
        Якщо ви бажаєте взяти корінь від числа, напишіть "root"
        Якщо ви бажаєте взяти факторіал від числа, напишіть "fact"
        Якщо ви бажаєте порахувати логарифм, напишіть "log"
        ''')
        a = input()
        if a in ["exp", "root", "fact", "log"]:
            break
        else:
            print("Ви ввели некоректні дані")
            continue
    while True:
        if a == "exp":
            while True:
                numb = input("Введіть ваше число: ")
                if numb.replace("-", "").replace(".", "").isdigit():
                    numb = float(numb)
                    while True:
                        ans = input("Якщо ви хочите піднести число до другою степені напишіть '2', якщо до третьої то '3': ")
                        if ans == "2" or "3":
                            ans = int(ans)
                            if ans == 2:
                                print(f'2 степінь від {numb} дорівнює: {exp2(numb)}')
                                break
                            elif ans == 3:
                                print(f'3 степінь від {numb} дорівнює: {exp3(numb)}')
                                break
                        else:
                            print("Ви ввели некоректну степінь")
                            continue
                    break
                else:
                    print("Ви ввели не число")
                    continue
            break
        elif a == "root":
            while True:
                numb = input("Введіть ваше число: ")
                if numb.replace("-", "").replace(".", "").isdigit():
                    numb = float(numb)
                    while True:
                        ans = input("Якщо ви хочите взяти квадратний корінь від числа, напишіть '2', якщо кубічний то '3': ")
                        if ans == "2" or "3":
                            ans = int(ans)
                            if ans == 2:
                                if numb >= 0:
                                    print(f'квадратний корінь від {numb} дорівнює: {root2(numb)}')
                                    break
                                else:
                                    print("від'ємне число не може бути під квадратним корнем")
                                    continue
                            elif ans == 3:
                                print(f'кубічний корінь від {numb} дорівнює: {root3(numb)}')
                                break
                        else:
                            print("Ви ввели некоректний корінь")
                            continue
                    break
                else:
                    print("Ви ввели не число")
                    continue
            break

        elif a == "fact":
            while True:
                numb = input("Введіть ваше число: ")
                if numb.isdigit():
                    numb = int(numb)
                    if numb > 0:
                        print(f'Лагорифм числа {numb} дорівнює: {fact(numb)}')
                        break
                    else:
                        print("Ви ввели некоректне число")
                        continue
                else:
                    print('Ви ввели некоректні дані')
                    continue
            break
        elif a == "log":
            while True:
                print('''Напишіть:
                            log - якщо хочите ввести свій логарифм
                            ln - якщо хочите отримати натуральний логарифм
                            lg - якщо хочите отримати десятковий логарифм
                            ''')
                l = input()
                if l == "log" or "ln" or "lg":
                    while True:
                        numb = input("Введіть значення логарифму: ")
                        if numb.replace(".", "").isdigit() and numb != "0":
                            numb = float(numb)
                            while True:
                                if l == "log":
                                    ans = input("Введіть основу логарифму: ")
                                    if ans.replace(".", "").isdigit():
                                        ans = float(ans)
                                        if ans > 0 and ans != 1:
                                            print(f'Логарифм з основою {ans} та значенням {numb} дорівнює: {log(ans, numb)}')
                                            break
                                        else:
                                            print("Ви ввели недоречне число")
                                            continue
                                    else:
                                        print("Ви ввели не число")
                                        continue

                                elif l == "ln":
                                    print(f'натуральний логарифм від {numb} дорівнює: {ln(numb)}')
                                    break
                                elif l == "lg":
                                    print(f'десятковий логарифм від {numb} дорівнює: {lg(numb)}')
                                    break
                        else:
                            print("Ви ввели щось недоречне")
                            continue
                        break
                    break
                else:
                    print("Ви ввели щось невідоме")
                    continue
        break
    q = input("Якщо хочите повторити натисніть '1', якщо ні то натисніть що завгодно: ")
    if q == '1':
        main()
    else:
        exit()


if __name__ == '__main__':
    main()

