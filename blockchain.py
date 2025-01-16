import hashlib
import time

# Класс для блока
class Block:
    def __init__(self, data, previous_hash):
        self.data = data  # Данные в блоке
        self.previous_hash = previous_hash  # Хэш предыдущего блока
        self.timestamp = time.time()  # Время создания блока
        self.hash = self.calculate_hash()  # Хэш текущего блока

    def calculate_hash(self):
        # Создаём хэш на основе данных, времени и хэша предыдущего блока
        hash_string = str(self.data) + str(self.previous_hash) + str(self.timestamp)
        return hashlib.sha256(hash_string.encode()).hexdigest()


# Класс для блокчейна
class Blockchain:
    def __init__(self):
        # Создаём первый блок (genesis block)
        genesis_block = Block("Genesis Block", "0")
        self.chain = [genesis_block]  # Цепочка блоков

    def add_block(self, data):
        # Получаем последний блок в цепочке
        previous_block = self.chain[-1]
        # Создаём новый блок
        new_block = Block(data, previous_block.hash)
        # Добавляем новый блок в цепочку
        self.chain.append(new_block)
        print("Block added to the chain!")

    def is_chain_valid(self):
        # Проверяем, не была ли изменена цепочка
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i - 1]

            # Проверяем, совпадает ли хэш текущего блока
            if current_block.hash != current_block.calculate_hash():
                print("Blockchain is invalid: Current block hash is incorrect.")
                return False

            # Проверяем, ссылается ли текущий блок на предыдущий
            if current_block.previous_hash != previous_block.hash:
                print("Blockchain is invalid: Previous block hash is incorrect.")
                return False

        print("Blockchain is valid.")
        return True


# Основная программа
if __name__ == "__main__":
    # Создаём блокчейн
    my_blockchain = Blockchain()

    # Добавляем блоки
    print("Adding block 1...")
    my_blockchain.add_block("First Block")
    print("Adding block 2...")
    my_blockchain.add_block("Second Block")
    print("Adding block 3...")
    my_blockchain.add_block("Third Block")

    # Выводим информацию о каждом блоке
    print("\nBlockchain:")
    for block in my_blockchain.chain:
        print(f"Data: {block.data}")
        print(f"Hash: {block.hash}")
        print(f"Previous Hash: {block.previous_hash}")
        print("------")

    # Проверяем целостность блокчейна
    print("\nChecking blockchain validity...")
    my_blockchain.is_chain_valid()

    # Попробуем изменить данные в блоке и проверить целостность
    print("\nTampering with the blockchain...")
    my_blockchain.chain[1].data = "Hacked Block"
    my_blockchain.is_chain_valid()