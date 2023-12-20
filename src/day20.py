#!/usr/bin/env pypy

"""
Modules and Pulses.

Timing:
python3: 238 ms
pypy: 165 ms
"""

from dataclasses import dataclass, field
from aoc import lcm, read_input

# ------------------------------------------------------------------------------


@dataclass
class Module:
    name: str
    tech: str
    outputs: list

    state: bool = False
    inputs: dict = field(default_factory=dict)

    def process(self, src: str, pulse: bool) -> bool:
        if self.tech == "%":
            return self._flip(pulse)
        elif self.tech == "&":
            return self._conj(src, pulse)
        else:
            return True

    def _flip(self, pulse: bool) -> bool:
        """
        Flip-Flop Module

        pulse high -> nothing
        pulse low  -> toggle
        """
        if pulse:
            return False
        else:
            self.state = not self.state
            return True

    def _conj(self, src: str, pulse: bool) -> bool:
        """
        Conjunction Module

        all input high -> low
        else           -> high
        """
        self.inputs[src] = pulse
        self.state = not all(x for x in self.inputs.values())
        return True


def solve(day: int = 20, test: bool = False) -> tuple[int, int]:
    """
    Part1: count low and high pulses
    Part2: when will 'rx' module receive low pulse
    """
    txt = read_input(day, test).splitlines()

    BT = "button"
    BC = "broadcaster"
    RX = "rx"

    MODULES = {}

    for line in txt:
        src, dest = line.split(" -> ")
        dest = dest.split(", ")

        if src == BC:
            MODULES[BC] = Module(BC, BC, dest)
            continue

        tech = src[0]
        name = src[1:]
        MODULES[name] = Module(name, tech, dest)

        if RX in dest:
            rx_in = name

    CYCLE = {}
    COUNTER = {}
    for name, module in MODULES.items():
        for out in module.outputs:
            if out not in MODULES:
                continue

            if out == rx_in:
                COUNTER[name] = 0

            MODULES[out].inputs[name] = False

    part1 = part2 = 0

    lo = hi = 0

    for t in range(1, 10**6):
        if part1 and part2:
            break

        if t == 1000 + 1:
            part1 = lo * hi

        Q = [(BT, BC, False)]

        while Q:
            src, dest, pulse = Q.pop(0)

            hi += 1 if pulse else 0
            lo += 0 if pulse else 1

            if dest not in MODULES:
                continue

            module = MODULES[dest]
            if module.process(src, pulse):
                Q.extend((module.name, x, module.state) for x in module.outputs)

            if not pulse and dest in COUNTER:
                COUNTER[dest] += 1

                if dest not in CYCLE:
                    CYCLE[dest] = t
                else:
                    assert t == COUNTER[dest] * CYCLE[dest]

                # print(f"{t=} cycle={cycle[dest]} {src=} {dest=}")

                if all(COUNTER.values()):
                    part2 = lcm(CYCLE.values())

    return part1, part2


# ------------------------------------------------------------------------------

res = solve()
print(*res)
assert res == (841_763_884, 246_006_621_493_687)

# ------------------------------------------------------------------------------
