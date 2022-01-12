from dataclasses import dataclass, field
from functools import reduce
import sys, os
from operator import mul
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from solution import Solution

class NoInstructionsException(Exception):
    pass

def stack(s:str) -> list:
    return  [c for c in s[::-1]]

def hexc_to_bin(hexc:str) -> str:
    return bin(int(hexc, base=16))[2:].zfill(4)

@dataclass
class TxPacket():
    version: int = -1
    pkt_type: int = -1
    length_id: int = -1
    length: int = -1
    children: list = field(default_factory=list)
    bit_length: int = 0
    
    def list_attributes(self) -> list:
        return [field for field in self.__dataclass_fields__]
    
    def is_literal(self) -> bool:
        return self.pkt_type == 4
    
    def add_child(self, obj) -> None:
        self.children.append(obj)
        
    def version_sum(self) -> int:
        if self.is_literal():
            return self.version
        else:
            children_vs = [child.version_sum() for child in self.children]
            return self.version + sum(children_vs)
        
    def total_length(self) -> int:
        if self.is_literal():
            return self.bit_length
        else:
            children_bl = [child.total_length() for child in self.children]
            return self.bit_length + sum(children_bl)
        
    def operation(self) -> int:
        if self.pkt_type == 4:
            # literal
            return self.children[0]
        else:
            cr = [c.operation() for c in self.children]
            match self.pkt_type:
                case 0:
                    # sum
                    return sum(cr)
                case 1:
                    # product
                    return reduce(mul, cr, 1)
                case 2:
                    # minimum
                    return min(cr)
                case 3:
                    # maximum
                    return max(cr)
                case 5:
                    # greater than
                    return int(cr[0] > cr[1])
                case 6:
                    # less than
                    return int(cr[0] < cr[1])
                case 7:
                    # equal
                    return int(cr[0] == cr[1])

@dataclass
class BitDispenser():
    '''
    Interface for continually retrieving the next bit from a
    transmission
    '''
    tx: str = field(default_factory=str)
    hex_stack: list = field(default_factory=list)
    buffer: list = field(default_factory=list)
    
    def __post_init__(self):
        self.hex_stack = stack(self.tx)
    
    def next_bit(self) -> str:
        if not self.buffer:
            self.load_buffer()
        return self.buffer.pop()

    def load_buffer(self) -> None:
        bits = hexc_to_bin(self.hex_stack.pop())
        self.buffer = stack(bits)

@dataclass
class TxPacketDecoder():
    '''
    Decodes a transmission and determines the undelying packet tree of
    the first-discovered packtet
    >>>d = TxPacketDecoder('(packet (sub_pkt1 sub_pkt2))')
    >>>d.pkt
    > (packet (sub_pkt1 sub_pkt2))
    
    >>>d = TxPacketDecoder('(packet1)(packet2)')
    >>>d.pkt
    > (packet1)
    '''
    bdisp: BitDispenser = field(default_factory=BitDispenser)
    pkt: TxPacket = field(default_factory=TxPacket)
    
    def __post_init__(self):
        for attr in self.pkt.list_attributes():
            self.fill_attr(attr)
        # finish up
            
    def fill_attr(self, attr) -> None:
        match attr:
            case 'version' | 'pkt_type':
                self.mungen(attr, 3)
            case 'length_id':
                if not self.pkt.is_literal():
                    self.mungen(attr, 1)
            case 'length':
                self.proc_length(attr)
            case 'children':
                if self.pkt.is_literal():
                    self.collect_literal()
                else:
                    self.collect_pkts()
                pass

    def mungen(self, attr, n) -> None:
        bit_value = self.get_bits(n)
        setattr(self.pkt, attr, int(bit_value, base=2))
    
    def get_bits(self, n) -> str:
        self.pkt.bit_length += n
        result = ''.join([self.bdisp.next_bit() for _ in range(n)])
        return result
    
    def proc_length(self, attr) -> None:
        if self.pkt.is_literal():
            pass
        elif self.pkt.length_id:
            self.mungen(attr, 11)
        elif not self.pkt.length_id:
            self.mungen(attr, 15)
    
    def collect_literal(self) -> None:
        bin_result = ''
        while True:
            leading_bit = int(self.get_bits(1))
            bin_result += str(self.get_bits(4))
            if not leading_bit:
                break
        self.pkt.add_child(int(bin_result, base=2))
    
    def collect_pkts(self) -> None:
        if self.pkt.length_id:
            self.collect_pkts_n()
        else:
            self.collect_pkts_bits()

    def collect_pkts_n(self) -> None:
        for _ in range(self.pkt.length):
            decode_next = TxPacketDecoder(bdisp=self.bdisp)
            self.pkt.add_child(decode_next.pkt)
    
    def collect_pkts_bits(self) -> None:
        bit_ctr = self.pkt.length
        while bit_ctr > 0:
            decode_next = TxPacketDecoder(bdisp=self.bdisp)
            pkt = decode_next.pkt
            bit_ctr -= pkt.total_length()
            self.pkt.add_child(pkt)
    
@dataclass  
class Day16Solution(Solution):
    txs: list = field(default_factory = list)
    packets: list = field(default_factory = list)
    pkt: TxPacket = field(default_factory=TxPacket)
    
    def __post_init__(self):
        self.packets = [self.extract_pkts(tx) for tx in self.raw_input()]
        pass
    
    def solve_part1(self) -> int:
        self.pkt = self.packets[0]
        return self.pkt.version_sum()

    def solve_part2(self, i=0) -> int:
        self.pkt = self.packets[i]
        return self.pkt.operation()
    
    def extract_pkts(self, tx) -> TxPacket:
        decode = TxPacketDecoder(bdisp=BitDispenser(tx))
        pkt = decode.pkt
        return pkt
    
def main():
    inp = 'day16/example.input'
    # p1 = Day16Solution(inp)
    # print(f'solve_part1: {p1.solve_part1()}')
    for i in range(8):
        p2 = Day16Solution(inp).solve_part2(i)
        print(f'#{i + 1} solve_part2: {p2}')

if __name__ == '__main__':
    main()
