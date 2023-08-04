class BidirectNode:
    def __init__(self, x, prev_node: 'BidirectNode', next_node: 'BidirectNode'):
        self.item = x
        self.prev = prev_node
        self.next = next_node
