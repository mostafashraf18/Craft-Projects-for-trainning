class Blockchain(object):
    def __init__(self):
        self.chain = []
        self.current_transaction = []

    def new_block(self, proof, previous_hash=None):
        #creates a new block and adds it ti the chain
        
        block = {
            'index': len(self.chain) + 1,
            'timestamp': time(),
            'transactions': self.current_transaction,
            'proof': proof,
            'previous_hash': previous_hash or self.hash(self.chain[-1])
        }

        self.current_transaction = []

        self.chain.append(block)
        return block
    
    def new_transactions(self, sender, recipient, amount):
        #Adds a new transaction to the list of transactons
        """
        Creates a new transaction to go into the next mined Block
        :param sender: <str> Address of the sender
        :param recipent: <str> Adress of the recipient
        "param amount: <int> Amount
        :return: <int> The index of the Block that will hold this transaction

        """

        self.current_transactions.append({
            'sender': sender,
            'recipient': recipient,
            'amount': amount,
        })

        return self.last_block['index']+1
    
    @property
    def last_block(self):
        return self.chain[-1]
    
    @staticmethod
    def hash(block):
        # Hashes a Block
        block_string = json.dumps(block, sort_keys=True).encode()
        return hashlib.sha256(block_string).hexadigest()

    @property
    def last_block(self):
        # Returns the last Block in the chain
        pass


        