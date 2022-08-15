
import random
import math

limit = random.randint(-10, 10)
x = random.randint(-10, 10)
variable = random.choice(["f", "h", "g"])
question = f'''
        The function \\({variable}\\) is defined over the real numbers. This table gives a few values of \\({variable}\\).

        <table>
            <tr>
                <th>\\(x\\)</th>
                <th>{x - 0.1}</th>
                <th>{x - 0.01}</th>
                <th>{x - 0.001}</th>
                <th>{x + 0.001}</th>
                <th>{x + 0.01}</th>
                <th>{x + 0.1}</th>
            </tr>
            <tr>
                <td>\\({variable}(x)\\)</td>
                <td>{round(limit + (random.random()*2), 3)}  </td>
                <td>{round(limit + (random.random()/5), 3)} </td>
                <td>{round(limit + (random.random()/50), 3)}</td>
                <td>{round(limit - (random.random()/50), 3)}  </td>
                <td>{round(limit - (random.random()/5), 3)} </td>
                <td>{round(limit - (random.random()*2), 3)}</td>
            </tr>
        </table>

        What is a reasonable estimate for \\(\\lim_{{x \\to {x} }} {variable}(x)\\)?

'''

answer = None

if random.getrandbits(1):
    answer = limit
else:
    if limit < 0:
        l = list(range(-10, 1))
        l.remove(limit)
        answer = random.sample(l, 3)
    else:
        l = list(range(0, 11))
        l.remove(limit)
        answer = random.sample(l, 3)
    selection = random.randint(0, 3)
    answer.insert(selection, limit)
    
    answer = [answer, selection]
    
data = {
    "question": question,
    "answer": answer,
    "is_calc": False
}
