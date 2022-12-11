from functools import reduce
import re
# import numpy

monkey_list = []
common_div = 0


class Monkey:

    def __init__(self, data) -> None:
        nums = re.compile(r"\d+")

        lines = str(data).splitlines()

        self.items = [int(s) for s in re.findall(nums, lines[1])]

        self.operation = lines[2][19:]
        self.divider = int(nums.search(lines[3]).group(0))
        self.true_pass = int(nums.search(lines[4]).group(0))
        self.false_pass = int(nums.search(lines[5]).group(0))
        self.inspect = 0

    def add_item(self, item):
        self.items.append(item)

    def _throw_all_items(self, part1):
        throwable = 0
        for item in self.items:
            self.inspect += 1
            throwable = eval(self.operation, {}, {'old': item})

            if part1:
                throwable = throwable//3

            if throwable % self.divider == 0:
                monkey_list[self.true_pass].add_item(throwable % common_div)
            else:
                monkey_list[self.false_pass].add_item(throwable % common_div)
        self.items.clear()

    def throw_all_items_p1(self):
        self._throw_all_items(True)

    def throw_all_items_p2(self):
        self._throw_all_items(False)


def compute_business():
    business_list = []
    for monkey in monkey_list:
        business_list.append(monkey.inspect)
    business_list.sort()
    ret = (business_list.pop() * business_list.pop())
    return ret


if __name__ == '__main__':
    with open('input') as f:
        monkeys = f.read().split('\n\n')

        for monkey in monkeys:
            monkey_list.append(Monkey(monkey))

        common_div = reduce(lambda a, b: a*b, (monkey.divider for monkey in monkey_list))
        # div_list = []
        # for monkey in monkey_list:
        #     div_list.append(monkey.divider)
        # common_div = numpy.prod(div_list)

        for i in range(20):
            for monkey in monkey_list:
                monkey.throw_all_items_p1()
        print('Part 1:', compute_business())

        monkey_list.clear()
        for monkey in monkeys:
            monkey_list.append(Monkey(monkey))

        for i in range(10000):
            for monkey in monkey_list:
                monkey.throw_all_items_p2()
        print('Part 2:', compute_business())
