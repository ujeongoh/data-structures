class HashTable:   
    def __init__(self, size=5) -> None:
        '''
        해시 테이블 크기를 설정하고
        설정한 크기의 길이를 가진 해시 테이블을 생성한다.
        '''
        self.size = size
        self.hash_table = [[] for _ in range(self.size)]
        
    def get_hashcode(self, key) -> int:
        '''
        키를 문자열로 바꿔서 각 문자의 유니코드 정수를 더한 해시코드를 반환한다.
        '''
        return sum([ord(s) for s in key])
    
    def convert_to_index(self, hash_code) -> int:
        '''
        주어진 해시코드를 해시 테이블의 크기로 나눈 나머지 값을 반환한다.
        '''
        return hash_code % self.size
    
    def hash(self, key) -> int:
        '''
        주어진 키를 해싱한다.
        '''
        return self.convert_to_index(self.get_hashcode(key))
        
    def set(self, key, val):
        '''
        해시 테이블에 key, value 쌍의 데이터를 넣는다.
        '''
        index = self.hash(key)
        self.hash_table[index].append((key, val))
    
    def get(self, key):
        '''
        해시 테이블에서 key에 해당하는 value를 찾는다.
        key에 해당하는 값이 없으면 None을 반환한다.
        '''
        index = self.hash(key)
        vals = self.hash_table[index]
        if not vals:
            return None
        for val in vals:
            k, v = val
            if k == key:
                return v
        return None
    
        
if __name__ == "__main__":
    capital = HashTable()
    country = ["Korea", "America", "China", "England", "Türkiye"]
    city = ["Seoul", "Washington", "Beijing", "London", "Ankara"]
    
    for co, ci in zip(country, city):
        capital.set(co, ci)
        
    print("해시 테이블의 상태")
    print("===============")
    for i, v in enumerate(capital.hash_table):
        print(i, v)
        
    print()
    print("해시 테이블의 검색 결과")
    print("====================")
    print(f"Captial of America = {capital.get('America')}")
    print(f"Captial of Korea = {capital.get('Korea')}")
    print(f"Captial of England = {capital.get('England')}")
    print(f"Captial of China = {capital.get('China')}")
    print(f"Captial of Japan = {capital.get('Japan')}")
    print(f"Captial of Türkiye = {capital.get('Türkiye')}")
    
