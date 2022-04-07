import hashlib
import datetime as dt

class Block:
    def __init__(self, index, timestamp, data, prev_hash):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.prev_hash = prev_hash
        self.hash = self.hash_block()

    def hash_block(self):
        sha = hashlib.sha256()
        sha.update(str(self.index).encode() + str(self.timestamp).encode() + str(self.data).encode() + str(self.prev_hash).encode())
        return sha.hexdigest()

def check_integrity(chain):
    for i, block in enumerate(chain):
        if i < len(chain) - 1:
            print("Checking integrity of block {}".format(i))
            if block.hash_block() != chain[i+1].prev_hash:
                return ("Chain has been modified at block index {}".format(i))
        else:
            return ("Chain has not been modified")

        
def create_genesis_block():
    return [Block(0, dt.datetime.now(), "Genesis Block", "0")]

def find_records(form, blockchain):
    for block in blockchain:
        print(block.data)
        condition = (block.data[0] == form.get("name") and
                    block.data[1] == form.get("date") and
                    block.data[2] == form.get("course") and
                    block.data[3] == form.get("year") and
                    len(block.data[4]) == int(form.get("number")))
        if condition:
            return block.data[4]
    return -1

def next_block(last_block, data):
    this_index = last_block.index + 1
    this_timestamp = dt.datetime.now()
    this_data = data[:]
    this_prev_hash = last_block.hash
    return Block(this_index, this_timestamp, this_data, this_prev_hash)

def add_block(form, data, blockchain):
    data.append([])
    i = 1
    while form.get("roll_no{}".format(i)):
        data[-1].append(form.get("roll_no{}".format(i)))
        i += 1
    previous_block = blockchain[-1]
    block_to_add = next_block(previous_block, data)
    blockchain.append(block_to_add)
    previous_block = block_to_add
    return "Block #{} has been added to the blockchain!".format(block_to_add.index)
